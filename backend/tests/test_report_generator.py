from unittest.mock import MagicMock, patch

import pytest

from app.schemas.assessment import Question, QuestionOption
from app.services.report_generator import (
    calculate_assessment_scores,
    calculate_confidence_level,
    calculate_question_score,
    generate_ai_insights,
    generate_prioritized_remediation,
    generate_section_summaries,
    get_maturity_tier,
    normalize_answer_display,
)


def test_calculate_question_score_yes():
    from app.models.assessment import AssessmentResponse

    response = MagicMock(spec=AssessmentResponse)
    response.answer_value = "yes"

    question = MagicMock(spec=Question)
    question.type = "yes_no"
    question.weight = 5

    score = calculate_question_score(response, question)
    assert score == 5


def test_calculate_question_score_no():
    from app.models.assessment import AssessmentResponse

    response = MagicMock(spec=AssessmentResponse)
    response.answer_value = "no"

    question = MagicMock(spec=Question)
    question.type = "yes_no"
    question.weight = 5

    score = calculate_question_score(response, question)
    assert score == 0


def test_calculate_question_score_multiple_choice():
    from app.models.assessment import AssessmentResponse

    response = MagicMock(spec=AssessmentResponse)
    response.answer_value = "option1"

    question = MagicMock(spec=Question)
    question.type = "multiple_choice"
    question.weight = 3

    score = calculate_question_score(response, question)
    assert score == 3


def test_calculate_question_score_na():
    from app.models.assessment import AssessmentResponse

    response = MagicMock(spec=AssessmentResponse)
    response.answer_value = "n/a"

    question = MagicMock(spec=Question)
    question.type = "yes_no"
    question.weight = 5

    score = calculate_question_score(response, question)
    assert score == 0


def test_calculate_assessment_scores(test_assessment_response):
    from app.services.question_parser import load_assessment_structure

    structure = load_assessment_structure()
    responses = [test_assessment_response]

    scores = calculate_assessment_scores(responses, structure)

    assert scores is not None
    assert "overall" in scores
    assert scores["overall"]["score"] >= 0
    assert scores["overall"]["max_score"] > 0


def test_calculate_assessment_scores_empty():
    from app.services.question_parser import load_assessment_structure

    structure = load_assessment_structure()
    responses = []

    scores = calculate_assessment_scores(responses, structure)

    assert scores["overall"]["score"] == 0
    assert scores["overall"]["max_score"] > 0


@pytest.mark.asyncio
async def test_generate_ai_insights():
    from app.services.question_parser import create_sample_assessment_structure

    structure = create_sample_assessment_structure()
    responses = []

    with patch("openai.ChatCompletion.acreate") as mock_openai:
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Test insight"
        mock_openai.return_value = mock_response

        insights = await generate_ai_insights(responses, structure)

        assert insights is not None
        assert isinstance(insights, dict)


def test_generate_standard_report(
    db_session, test_report, completed_assessment, test_assessment_response
):
    from app.services.report_generator import generate_standard_report

    with patch("app.services.report_generator.HTML") as mock_html_class:
        mock_html_instance = MagicMock()
        mock_html_class.return_value = mock_html_instance
        mock_html_instance.write_pdf = MagicMock(return_value=b"pdf-bytes")

        with patch(
            "app.services.report_generator.get_storage_service"
        ) as mock_storage_factory:
            mock_storage = MagicMock()
            mock_storage.save.return_value = "/tmp/report.pdf"
            mock_storage.exists.return_value = True
            mock_storage_factory.return_value = mock_storage

            generate_standard_report(str(test_report.id))

            mock_storage.save.assert_called_once()

    db_session.refresh(test_report)


@pytest.mark.asyncio
async def test_generate_ai_report(
    db_session, completed_assessment, test_assessment_response
):
    from app.models.assessment import Report
    from app.services import report_generator as report_generator_module
    from app.services.report_generator import generate_ai_report

    ai_report = Report(
        assessment_id=completed_assessment.id,
        report_type="ai_enhanced",
        status="pending",
    )
    db_session.add(ai_report)
    db_session.commit()
    db_session.refresh(ai_report)

    with patch.object(report_generator_module.settings, "OPENAI_API_KEY", "test-key"):
        with patch("openai.ChatCompletion.acreate") as mock_openai:
            mock_response = MagicMock()
            mock_response.choices = [MagicMock()]
            mock_response.choices[0].message.content = "AI insights"
            mock_openai.return_value = mock_response

            with patch("app.services.report_generator.HTML") as mock_html_class:
                mock_html_instance = MagicMock()
                mock_html_class.return_value = mock_html_instance
                mock_html_instance.write_pdf = MagicMock(return_value=b"pdf-bytes")

                with patch(
                    "app.services.report_generator.get_storage_service"
                ) as mock_storage_factory:
                    mock_storage = MagicMock()
                    mock_storage.save.return_value = "/tmp/ai-report.pdf"
                    mock_storage.exists.return_value = True
                    mock_storage_factory.return_value = mock_storage

                    await generate_ai_report(str(ai_report.id))

                    mock_storage.save.assert_called_once()

            db_session.refresh(ai_report)


def test_format_responses_for_ai():
    from app.services.report_generator import format_responses_for_ai

    responses = [
        {"question": "Test question 1?", "answer": "yes", "weight": 5},
        {"question": "Test question 2?", "answer": "no", "weight": 3},
    ]

    result = format_responses_for_ai(responses)

    assert "Test question 1?" in result
    assert "yes" in result
    assert "Weight: 5" in result
    assert "Test question 2?" in result
    assert "no" in result
    assert "Weight: 3" in result


def test_generate_recommendations():
    from app.services.question_parser import create_sample_assessment_structure
    from app.services.report_generator import generate_recommendations

    structure = create_sample_assessment_structure()

    scores = {
        "overall": {"percentage": 50.0},
        "section_1": {"percentage": 40.0},
        "section_2": {"percentage": 60.0},
    }

    recommendations = generate_recommendations(scores, structure)

    assert isinstance(recommendations, list)
    assert len(recommendations) > 0


def test_generate_recommendations_high_score():
    from app.services.question_parser import create_sample_assessment_structure
    from app.services.report_generator import generate_recommendations

    structure = create_sample_assessment_structure()

    scores = {
        "overall": {"percentage": 85.0},
        "section_1": {"percentage": 90.0},
        "section_2": {"percentage": 85.0},
    }

    recommendations = generate_recommendations(scores, structure)

    assert isinstance(recommendations, list)


def test_generate_report_html(completed_assessment, test_assessment_response):
    from app.services.question_parser import create_sample_assessment_structure
    from app.services.report_generator import generate_report_html

    structure = create_sample_assessment_structure()
    responses = [test_assessment_response]
    scores = {
        "overall": {"percentage": 75.0, "score": 75, "max_score": 100},
        "section_1": {
            "percentage": 70.0,
            "score": 70,
            "max_score": 100,
            "completion_rate": 80.0,
            "responses_count": 4,
            "total_questions": 5,
        },
        "section_2": {
            "percentage": 80.0,
            "score": 80,
            "max_score": 100,
            "completion_rate": 90.0,
            "responses_count": 9,
            "total_questions": 10,
        },
    }

    html = generate_report_html(completed_assessment, responses, scores, structure)

    assert isinstance(html, str)
    assert "Security Posture Assessment Report" in html
    assert "75.0%" in html
    assert len(html) > 100


def test_generate_ai_report_html(completed_assessment, test_assessment_response):
    from app.services.question_parser import create_sample_assessment_structure
    from app.services.report_generator import generate_ai_report_html

    structure = create_sample_assessment_structure()
    responses = [test_assessment_response]
    scores = {
        "overall": {"percentage": 75.0, "score": 75, "max_score": 100},
        "section_1": {
            "percentage": 70.0,
            "score": 70,
            "max_score": 100,
            "completion_rate": 80.0,
            "responses_count": 4,
            "total_questions": 5,
        },
        "section_2": {
            "percentage": 80.0,
            "score": 80,
            "max_score": 100,
            "completion_rate": 90.0,
            "responses_count": 9,
            "total_questions": 10,
        },
    }
    ai_insights = {
        "section_1": "Good progress in this area",
        "section_2": "Excellent security practices",
    }

    html = generate_ai_report_html(
        completed_assessment, responses, scores, structure, ai_insights
    )

    assert isinstance(html, str)
    assert "AI-Enhanced Security Posture Assessment Report" in html
    assert "75.0%" in html
    assert "Good progress" in html
    assert len(html) > 100


def test_normalize_answer_display_yes_no():
    question = MagicMock(spec=Question)
    question.type = "yes_no"

    assert normalize_answer_display(True, question) == "Yes"
    assert normalize_answer_display(False, question) == "No"
    assert normalize_answer_display("yes", question) == "Yes"
    assert normalize_answer_display("no", question) == "No"
    assert normalize_answer_display("YES", question) == "Yes"
    assert normalize_answer_display(None, question) == "Not answered"


def test_normalize_answer_display_multiple_choice():
    option1 = QuestionOption(
        value="opt1", label="Option One", description="First option"
    )
    option2 = QuestionOption(
        value="opt2", label="Option Two", description="Second option"
    )

    question = MagicMock(spec=Question)
    question.type = "multiple_choice"
    question.options = [option1, option2]

    assert normalize_answer_display("opt1", question) == "Option One"
    assert normalize_answer_display("opt2", question) == "Option Two"
    assert normalize_answer_display("unknown", question) == "unknown"
    assert normalize_answer_display(None, question) == "Not answered"


def test_normalize_answer_display_multiple_select():
    option1 = QuestionOption(
        value="opt1", label="Option One", description="First option"
    )
    option2 = QuestionOption(
        value="opt2", label="Option Two", description="Second option"
    )

    question = MagicMock(spec=Question)
    question.type = "multiple_select"
    question.options = [option1, option2]

    assert (
        normalize_answer_display(["opt1", "opt2"], question) == "Option One, Option Two"
    )
    assert normalize_answer_display(["opt1"], question) == "Option One"
    assert normalize_answer_display([], question) == "Not answered"
    assert normalize_answer_display(None, question) == "Not answered"


def test_normalize_answer_display_text():
    question = MagicMock(spec=Question)
    question.type = "text"

    assert normalize_answer_display("Some text", question) == "Some text"
    assert normalize_answer_display("Line 1\nLine 2", question) == "Line 1<br>Line 2"
    assert normalize_answer_display("", question) == "Not answered"
    assert normalize_answer_display("   ", question) == "Not answered"
    assert normalize_answer_display(None, question) == "Not answered"


def test_get_maturity_tier():
    tier, css = get_maturity_tier(80.0)
    assert tier == "Strong"
    assert css == "high-score"

    tier, css = get_maturity_tier(60.0)
    assert tier == "Moderate"
    assert css == "medium-score"

    tier, css = get_maturity_tier(59.9)
    assert tier == "Needs Improvement"
    assert css == "low-score"

    tier, css = get_maturity_tier(100.0)
    assert tier == "Strong"

    tier, css = get_maturity_tier(0.0)
    assert tier == "Needs Improvement"


def test_calculate_confidence_level_high():
    scores = {
        "overall": {"percentage": 85.0},
        "section_1": {"percentage": 80.0, "completion_rate": 85.0},
        "section_2": {"percentage": 90.0, "completion_rate": 90.0},
    }

    level, description = calculate_confidence_level(scores)
    assert level == "High"
    assert "substantially completed" in description


def test_calculate_confidence_level_medium():
    scores = {
        "overall": {"percentage": 70.0},
        "section_1": {"percentage": 65.0, "completion_rate": 65.0},
        "section_2": {"percentage": 75.0, "completion_rate": 70.0},
    }

    level, description = calculate_confidence_level(scores)
    assert level == "Medium"
    assert "generally reliable" in description


def test_calculate_confidence_level_low():
    scores = {
        "overall": {"percentage": 50.0},
        "section_1": {"percentage": 40.0, "completion_rate": 50.0},
        "section_2": {"percentage": 60.0, "completion_rate": 55.0},
    }

    level, description = calculate_confidence_level(scores)
    assert level == "Low"
    assert "gaps" in description


def test_generate_prioritized_remediation():
    from app.services.question_parser import create_sample_assessment_structure

    structure = create_sample_assessment_structure()
    scores = {
        "section_1": {"percentage": 45.0},
        "section_2": {"percentage": 65.0},
    }

    items = generate_prioritized_remediation(scores, structure)

    assert isinstance(items, list)
    assert len(items) > 0

    p1_item = items[0]
    assert p1_item["priority"] == "P1"
    assert p1_item["effort"] == "Medium"
    assert p1_item["timeframe"] == "30-90 days"
    assert "45.0%" in p1_item["current_score"]

    p2_item = items[1]
    assert p2_item["priority"] == "P2"
    assert p2_item["effort"] == "Medium"
    assert p2_item["timeframe"] == "30-90 days"


def test_generate_section_summaries():
    from app.models.assessment import AssessmentResponse
    from app.services.question_parser import create_sample_assessment_structure

    structure = create_sample_assessment_structure()

    response1 = MagicMock(spec=AssessmentResponse)
    response1.question_id = "1_1_1"
    response1.answer_value = "yes"
    response1.comment = None

    response2 = MagicMock(spec=AssessmentResponse)
    response2.question_id = "1_1_2"
    response2.answer_value = "annually"
    response2.comment = "We review annually"

    responses = [response1, response2]

    scores = {
        "section_1": {
            "percentage": 85.0,
            "completion_rate": 100.0,
            "responses_count": 2,
            "total_questions": 2,
        },
        "section_2": {
            "percentage": 60.0,
            "completion_rate": 50.0,
            "responses_count": 1,
            "total_questions": 2,
        },
    }

    summaries = generate_section_summaries(scores, structure, responses)

    assert isinstance(summaries, list)
    assert len(summaries) == 2

    summary1 = summaries[0]
    assert summary1["score"] == 85.0
    assert summary1["completion"] == 100.0
    assert len(summary1["strengths"]) >= 0
    assert len(summary1["recommendations"]) > 0


def test_generate_report_html_enhanced(completed_assessment, test_assessment_response):
    from app.models.assessment import AssessmentResponse
    from app.services.question_parser import create_sample_assessment_structure
    from app.services.report_generator import generate_report_html

    structure = create_sample_assessment_structure()

    completed_assessment.consultation_interest = True
    completed_assessment.consultation_details = (
        "We need help with security improvements"
    )
    completed_assessment.progress_percentage = 65.0

    response_with_comment = MagicMock(spec=AssessmentResponse)
    response_with_comment.question_id = "1_1_1"
    response_with_comment.answer_value = "yes"
    response_with_comment.comment = "This is a test comment"

    responses = [test_assessment_response, response_with_comment]

    scores = {
        "overall": {"percentage": 65.0, "score": 65, "max_score": 100},
        "section_1": {
            "percentage": 60.0,
            "score": 60,
            "max_score": 100,
            "completion_rate": 75.0,
            "responses_count": 3,
            "total_questions": 4,
        },
        "section_2": {
            "percentage": 70.0,
            "score": 70,
            "max_score": 100,
            "completion_rate": 80.0,
            "responses_count": 4,
            "total_questions": 5,
        },
    }

    html = generate_report_html(completed_assessment, responses, scores, structure)

    assert isinstance(html, str)
    assert "Table of Contents" in html
    assert "Methodology and Scoring" in html
    assert "Data Quality and Confidence Level" in html
    assert "Domain Heatmap and Maturity Tiers" in html
    assert "Prioritized Remediation Plan" in html
    assert "Section Summaries" in html
    assert "Detailed Responses (All Questions and Answers)" in html
    assert "Comments Digest" in html
    assert "Consultation Interest:" in html
    assert "We need help with security improvements" in html
    assert "Not answered" in html
    assert "Disclaimer" in html
