import re

from app.schemas.assessment import (
    AssessmentStructure,
    Question,
    QuestionOption,
    Section,
)


def parse_assessment_questions(md_content: str) -> AssessmentStructure:
    """Parse the markdown file to extract all assessment questions and structure"""

    sections = []
    current_section = None
    current_question = None

    lines = md_content.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if line.startswith("## Section"):
            if current_section:
                sections.append(current_section)

            section_match = re.match(r"## Section (\d+): (.+)", line)
            if section_match:
                section_id = f"section_{section_match.group(1)}"
                section_title = section_match.group(2)
                current_section = {
                    "id": section_id,
                    "title": section_title,
                    "description": "",
                    "questions": [],
                }

        elif line.startswith("### Subsection"):
            pass

        elif line.startswith("#### Question"):
            if current_question and current_section:
                current_section["questions"].append(current_question)

            question_match = re.match(r"#### Question (.+)", line)
            if question_match:
                question_id = question_match.group(1).replace(".", "_")
                current_question = {
                    "id": question_id,
                    "section_id": current_section["id"]
                    if current_section
                    else "unknown",
                    "text": "",
                    "type": "multiple_choice",
                    "weight": 1,
                    "explanation": "",
                    "options": [],
                }

        elif line.startswith("**Question:**") and current_question:
            current_question["text"] = line.replace("**Question:**", "").strip()

        elif line.startswith("**Type:**") and current_question:
            type_text = line.replace("**Type:**", "").strip()
            current_question["type"] = type_text

        elif line.startswith("**Weight:**") and current_question:
            weight_text = line.replace("**Weight:**", "").strip()
            try:
                current_question["weight"] = int(weight_text)
            except ValueError:
                current_question["weight"] = 1

        elif line.startswith("**Explanation:**") and current_question:
            current_question["explanation"] = line.replace(
                "**Explanation:**", ""
            ).strip()

        elif line.startswith("**Option") and current_question:
            option_match = re.match(r"\*\*Option (\d+): (.+?)\*\*", line)
            if not option_match:
                option_match = re.match(r"\*\*Option (\d+):\*\* (.+)", line)

            if option_match:
                option_value = option_match.group(1)
                option_label = option_match.group(2)

                description = ""
                j = i + 1
                while (
                    j < len(lines)
                    and not lines[j].strip().startswith("**")
                    and not lines[j].strip().startswith("####")
                ):
                    desc_line = lines[j].strip()
                    if desc_line and not desc_line.startswith("*Note:"):
                        if desc_line.startswith("*Basic Description:"):
                            description = desc_line.replace(
                                "*Basic Description:", ""
                            ).strip()
                        elif not desc_line.startswith("*") and description == "":
                            description = desc_line
                        elif (
                            desc_line.startswith("-")
                            and "This security control" in desc_line
                        ):
                            description = desc_line.replace("- ", "").strip()
                    j += 1

                current_question["options"].append(
                    {
                        "value": option_value,
                        "label": option_label,
                        "description": description.strip(),
                    }
                )

        i += 1

    if current_question and current_section:
        current_section["questions"].append(current_question)
    if current_section:
        sections.append(current_section)

    structured_sections = []
    total_questions = 0

    for section_data in sections:
        questions = []
        for q_data in section_data["questions"]:
            options = [
                QuestionOption(
                    value=opt["value"],
                    label=opt["label"],
                    description=opt["description"],
                )
                for opt in q_data["options"]
            ]

            question = Question(
                id=q_data["id"],
                section_id=q_data["section_id"],
                text=q_data["text"],
                type=q_data["type"],
                weight=q_data["weight"],
                explanation=q_data["explanation"],
                options=options,
            )
            questions.append(question)
            total_questions += 1

        section = Section(
            id=section_data["id"],
            title=section_data["title"],
            description=section_data["description"],
            questions=questions,
        )
        structured_sections.append(section)

    return AssessmentStructure(
        sections=structured_sections, total_questions=total_questions
    )


def load_assessment_structure() -> AssessmentStructure:
    """Load and parse the assessment questions from the markdown file"""
    try:
        import os

        from fastapi import HTTPException, status

        current_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        md_file_path = os.path.join(
            current_dir, "data", "security_assessment_questions.md"
        )

        if not os.path.exists(md_file_path):
            raise FileNotFoundError(
                f"Assessment questions file not found at {md_file_path}"
            )

        with open(md_file_path, encoding="utf-8") as file:
            md_content = file.read()

        if not md_content.strip():
            raise ValueError("Assessment questions file is empty")

        structure = parse_assessment_questions(md_content)
        if structure.total_questions == 0:
            raise ValueError("No questions found in assessment structure")

        return structure
    except Exception as e:
        print(f"Critical error loading assessment structure: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Assessment questions are not available. Please contact support.",
        )


def load_assessment_structure_cached() -> AssessmentStructure:
    from app.services.cache import cache_service

    CACHE_KEY = "assessment:structure"

    if cache_service.has_questions_file_changed():
        cache_service.delete(CACHE_KEY)

    cached_data = cache_service.get(CACHE_KEY)
    if cached_data:
        return AssessmentStructure(**cached_data)

    structure = load_assessment_structure()

    cache_service.set(CACHE_KEY, structure.model_dump())

    return structure


def filter_structure_by_sections(
    structure: AssessmentStructure, section_ids: list[str]
) -> AssessmentStructure:
    """Filter assessment structure to only include specified sections"""
    if not section_ids:
        return structure

    filtered_sections = [
        section for section in structure.sections if section.id in section_ids
    ]

    total_questions = sum(len(section.questions) for section in filtered_sections)

    return AssessmentStructure(
        sections=filtered_sections, total_questions=total_questions
    )


def create_sample_assessment_structure() -> AssessmentStructure:
    """Create a sample assessment structure for testing"""

    sections = [
        Section(
            id="section_1",
            title="Governance & Strategy",
            description="Cybersecurity governance, strategy, and organizational structure",
            questions=[
                Question(
                    id="1_1_1",
                    section_id="section_1",
                    text="Does your organization have a formally documented cybersecurity strategy?",
                    type="yes_no",
                    weight=5,
                    explanation="A documented cybersecurity strategy provides clear direction and alignment with business objectives.",
                    options=[
                        QuestionOption(
                            value="yes",
                            label="Yes",
                            description="This security control/practice is implemented in your organization",
                        ),
                        QuestionOption(
                            value="no",
                            label="No",
                            description="This security control/practice is not currently implemented",
                        ),
                    ],
                ),
                Question(
                    id="1_1_2",
                    section_id="section_1",
                    text="How often is your cybersecurity strategy reviewed and updated?",
                    type="multiple_choice",
                    weight=3,
                    explanation="Regular strategy reviews ensure alignment with evolving threats and business changes.",
                    options=[
                        QuestionOption(
                            value="annually",
                            label="Annually",
                            description="Once per year review cycle",
                        ),
                        QuestionOption(
                            value="bi_annually",
                            label="Bi-annually",
                            description="Twice per year review cycle",
                        ),
                        QuestionOption(
                            value="as_needed",
                            label="As needed",
                            description="Reactive reviews based on events",
                        ),
                        QuestionOption(
                            value="never",
                            label="Never",
                            description="No formal review process",
                        ),
                    ],
                ),
            ],
        ),
        Section(
            id="section_2",
            title="Risk Management",
            description="Risk assessment, management, and mitigation strategies",
            questions=[
                Question(
                    id="2_1_1",
                    section_id="section_2",
                    text="Do you conduct regular cybersecurity risk assessments?",
                    type="yes_no",
                    weight=5,
                    explanation="Regular risk assessments help identify and prioritize security threats.",
                    options=[
                        QuestionOption(
                            value="yes",
                            label="Yes",
                            description="Regular risk assessments are conducted",
                        ),
                        QuestionOption(
                            value="no",
                            label="No",
                            description="No regular risk assessment process",
                        ),
                    ],
                )
            ],
        ),
    ]

    total_questions = sum(len(section.questions) for section in sections)

    return AssessmentStructure(sections=sections, total_questions=total_questions)
