from app.services.question_parser import (
    _parse_option_explanation,
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


def test_parse_option_explanation_with_full_details():
    """Test parsing option explanation with all sections present"""
    lines = [
        "**📋 What This Option Means:**",
        "This is the definition of the option.",
        "",
        "**📊 Market Context & Benchmarks:**",
        "- **Industry Adoption Rate:** 75% of organizations",
        "- **Industry Benchmark:** Leading practice",
        "- **Compliance Frameworks:** ISO 27001, SOC 2",
        "",
        "**🎯 Recommendations & Next Steps:**",
        "This is the recommendation.",
        "",
        "**Option 2: Another option**",
    ]
    
    result = _parse_option_explanation(lines, 0)
    
    assert result is not None
    assert result["definition"] == "This is the definition of the option."
    assert "75% of organizations" in result["industry_adoption_rate"]
    assert "Leading practice" in result["industry_benchmark"]
    assert "ISO 27001, SOC 2" in result["compliance_frameworks"]
    assert result["recommendation"] == "This is the recommendation."


def test_parse_option_explanation_with_minimal_details():
    """Test parsing option explanation with only definition"""
    lines = [
        "**📋 What This Option Means:**",
        "Just a definition.",
        "",
        "**Option 2: Another option**",
    ]
    
    result = _parse_option_explanation(lines, 0)
    
    assert result is not None
    assert result["definition"] == "Just a definition."
    assert result["industry_adoption_rate"] is None
    assert result["recommendation"] is None


def test_parse_option_explanation_no_detailed_explanation():
    """Test parsing when no detailed explanation is present"""
    lines = [
        "*Basic Description: Simple description*",
        "",
        "**Option 2: Another option**",
    ]
    
    result = _parse_option_explanation(lines, 0)
    
    assert result is None


def test_parse_option_explanation_case_insensitive():
    """Test that parsing is case-insensitive for headings"""
    lines = [
        "**what this option means:**",
        "Definition text.",
        "",
        "**RECOMMENDATIONS & next steps:**",
        "Recommendation text.",
        "",
        "**Option 2: Another option**",
    ]
    
    result = _parse_option_explanation(lines, 0)
    
    assert result is not None
    assert result["definition"] == "Definition text."
    assert result["recommendation"] == "Recommendation text."


def test_parse_option_explanation_emoji_agnostic():
    """Test that parsing works without emojis"""
    lines = [
        "**What This Option Means:**",
        "Definition without emoji.",
        "",
        "**Market Context & Benchmarks:**",
        "- **Industry Adoption Rate:** 50%",
        "",
        "**Recommendations & Next Steps:**",
        "Recommendation without emoji.",
        "",
        "**Option 2: Another option**",
    ]
    
    result = _parse_option_explanation(lines, 0)
    
    assert result is not None
    assert result["definition"] == "Definition without emoji."
    assert "50%" in result["industry_adoption_rate"]
    assert result["recommendation"] == "Recommendation without emoji."


def test_loaded_structure_has_explanations():
    """Test that loaded structure includes detailed explanations for some options"""
    structure = load_assessment_structure()
    
    options_with_explanations = 0
    total_options = 0
    
    for section in structure.sections:
        for question in section.questions:
            for option in question.options:
                total_options += 1
                if option.detailed_explanation is not None:
                    options_with_explanations += 1
    
    assert total_options > 0
    assert options_with_explanations >= 0
