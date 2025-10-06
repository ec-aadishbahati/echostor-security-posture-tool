from app.services.question_parser import (
    create_sample_assessment_structure,
    load_assessment_structure,
)


def test_load_assessment_structure():
    structure = load_assessment_structure()

    assert structure is not None
    assert hasattr(structure, "sections")
    assert hasattr(structure, "total_questions")
    assert structure.total_questions > 0
    assert len(structure.sections) > 0


def test_assessment_structure_has_required_fields():
    structure = load_assessment_structure()

    assert hasattr(structure, "sections")
    assert hasattr(structure, "total_questions")

    for section in structure.sections:
        assert hasattr(section, "id")
        assert hasattr(section, "title")
        assert hasattr(section, "questions")


def test_question_types_are_valid():
    structure = load_assessment_structure()

    valid_types = ["yes_no", "multiple_choice", "multiple_select", "text"]

    for section in structure.sections:
        for question in section.questions:
            assert question.type in valid_types


def test_total_questions_count():
    structure = load_assessment_structure()

    actual_count = sum(len(section.questions) for section in structure.sections)

    assert structure.total_questions == actual_count
    assert structure.total_questions > 0


def test_create_sample_assessment_structure():
    structure = create_sample_assessment_structure()

    assert structure is not None
    assert hasattr(structure, "sections")
    assert structure.total_questions > 0
    assert len(structure.sections) == 2
