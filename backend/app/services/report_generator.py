import logging
import uuid
from datetime import datetime
from typing import Any

import openai
from jinja2 import Environment
from weasyprint import HTML

from app.core.config import settings
from app.core.database import SessionLocal
from app.models.assessment import Assessment, AssessmentResponse, Report
from app.services.question_parser import load_assessment_structure
from app.services.storage import get_storage_service

logger = logging.getLogger(__name__)

jinja_env = Environment(autoescape=True)

if settings.OPENAI_API_KEY:
    openai.api_key = settings.OPENAI_API_KEY


async def generate_standard_report(report_id: str):
    """Generate a standard PDF report"""

    db = SessionLocal()
    report = None
    try:
        logger.info(f"Starting standard report generation for report_id: {report_id}")

        report = db.query(Report).filter(Report.id == report_id).first()
        if not report:
            logger.error(f"Report not found: {report_id}")
            return

        assessment = (
            db.query(Assessment).filter(Assessment.id == report.assessment_id).first()
        )
        if not assessment:
            logger.error(f"Assessment not found for report: {report_id}")
            report.status = "failed"
            db.commit()
            return

        logger.info(f"Loading responses for assessment: {assessment.id}")
        responses = (
            db.query(AssessmentResponse)
            .filter(AssessmentResponse.assessment_id == assessment.id)
            .all()
        )
        logger.info(f"Found {len(responses)} responses")

        logger.info("Loading assessment structure")
        structure = load_assessment_structure()

        logger.info("Calculating scores")
        scores = calculate_assessment_scores(responses, structure)

        logger.info("Generating HTML content")
        html_content = generate_report_html(assessment, responses, scores, structure)
        logger.info(f"HTML content generated successfully ({len(html_content)} bytes)")

        filename = f"report_{report_id}_{uuid.uuid4().hex[:8]}.pdf"
        storage_service = get_storage_service()

        logger.info("REPORTS_DIR configured as: %s", settings.REPORTS_DIR)
        logger.info("Generating PDF bytes for storage")
        try:
            pdf_bytes = HTML(string=html_content).write_pdf()
            logger.info("WeasyPrint PDF byte generation completed")
        except Exception as pdf_error:
            logger.error(
                "WeasyPrint PDF generation failed: %s", str(pdf_error), exc_info=True
            )
            raise

        logger.info("Saving report to configured storage backend")
        storage_location = storage_service.save(pdf_bytes, filename)

        if not storage_service.exists(storage_location):
            raise Exception(
                f"PDF file was not persisted at storage location {storage_location}"
            )

        logger.info("PDF generated and stored successfully: %s", storage_location)
        report.file_path = storage_location
        report.status = "completed"
        report.completed_at = datetime.now(datetime.UTC)
        db.commit()

        logger.info(
            f"Report generation completed successfully for report_id: {report_id}"
        )

    except Exception as e:
        error_msg = f"Error generating standard report {report_id}: {str(e)}"
        logger.error(error_msg, exc_info=True)
        if report:
            report.status = "failed"
            db.commit()
    finally:
        db.close()


async def generate_ai_report(report_id: str):
    """Generate an AI-enhanced report using ChatGPT"""

    db = SessionLocal()
    report = None
    try:
        logger.info(f"Starting AI report generation for report_id: {report_id}")

        report = db.query(Report).filter(Report.id == report_id).first()
        if not report:
            logger.error(f"Report not found: {report_id}")
            return

        if not settings.OPENAI_API_KEY:
            logger.error("OPENAI_API_KEY not configured - cannot generate AI report")
            report.status = "failed"
            db.commit()
            return

        assessment = (
            db.query(Assessment).filter(Assessment.id == report.assessment_id).first()
        )
        if not assessment:
            logger.error(f"Assessment not found for report: {report_id}")
            report.status = "failed"
            db.commit()
            return

        logger.info(f"Loading responses for assessment: {assessment.id}")
        responses = (
            db.query(AssessmentResponse)
            .filter(AssessmentResponse.assessment_id == assessment.id)
            .all()
        )
        logger.info(f"Found {len(responses)} responses")

        logger.info("Loading assessment structure")
        structure = load_assessment_structure()

        logger.info("Generating AI insights")
        ai_insights = await generate_ai_insights(responses, structure)

        logger.info("Calculating scores")
        scores = calculate_assessment_scores(responses, structure)

        logger.info("Generating AI report HTML")
        html_content = generate_ai_report_html(
            assessment, responses, scores, structure, ai_insights
        )

        filename = f"ai_report_{report_id}_{uuid.uuid4().hex[:8]}.pdf"
        storage_service = get_storage_service()

        logger.info("Generating AI PDF bytes")
        pdf_bytes = HTML(string=html_content).write_pdf()

        logger.info("Saving AI report to configured storage backend")
        storage_location = storage_service.save(pdf_bytes, filename)

        if not storage_service.exists(storage_location):
            raise Exception(
                "AI PDF file was not persisted at storage location "
                f"{storage_location}"
            )

        logger.info(f"AI PDF generated successfully: {storage_location}")
        report.file_path = storage_location
        report.status = "completed"
        report.completed_at = datetime.now(datetime.UTC)
        db.commit()

        logger.info(
            f"AI report generation completed successfully for report_id: {report_id}"
        )

    except Exception as e:
        error_msg = f"Error generating AI report {report_id}: {str(e)}"
        logger.error(error_msg, exc_info=True)
        if report:
            report.status = "failed"
            db.commit()
    finally:
        db.close()


def calculate_assessment_scores(
    responses: list[AssessmentResponse], structure
) -> dict[str, Any]:
    """Calculate assessment scores by section"""

    scores = {}
    response_dict = {r.question_id: r for r in responses}

    for section in structure.sections:
        section_score = 0
        section_max_score = 0
        section_responses = 0

        for question in section.questions:
            response = response_dict.get(question.id)
            if response:
                section_responses += 1
                question_score = calculate_question_score(response, question)
                section_score += question_score

            section_max_score += question.weight

        completion_rate = (
            (section_responses / len(section.questions)) * 100
            if section.questions
            else 0
        )
        score_percentage = (
            (section_score / section_max_score) * 100 if section_max_score > 0 else 0
        )

        scores[section.id] = {
            "score": section_score,
            "max_score": section_max_score,
            "percentage": score_percentage,
            "completion_rate": completion_rate,
            "responses_count": section_responses,
            "total_questions": len(section.questions),
        }

    total_score = sum(s["score"] for s in scores.values())
    total_max_score = sum(s["max_score"] for s in scores.values())
    overall_percentage = (
        (total_score / total_max_score) * 100 if total_max_score > 0 else 0
    )

    scores["overall"] = {
        "score": total_score,
        "max_score": total_max_score,
        "percentage": overall_percentage,
    }

    return scores


def calculate_question_score(response: AssessmentResponse, question) -> int:
    """Calculate score for a single question response"""

    if question.type == "yes_no":
        if response.answer_value == "yes":
            return question.weight
        else:
            return 0

    elif question.type == "multiple_choice":
        return question.weight if response.answer_value else 0

    elif question.type == "multiple_select":
        if isinstance(response.answer_value, list):
            return question.weight if response.answer_value else 0
        return question.weight if response.answer_value else 0

    return 0


async def generate_ai_insights(
    responses: list[AssessmentResponse], structure
) -> dict[str, str]:
    """Generate AI insights for each section"""

    insights = {}
    response_dict = {r.question_id: r for r in responses}

    for section in structure.sections:
        section_responses = []
        for question in section.questions:
            response = response_dict.get(question.id)
            if response:
                section_responses.append(
                    {
                        "question": question.text,
                        "answer": response.answer_value,
                        "weight": question.weight,
                    }
                )

        if section_responses:
            try:
                prompt = f"""
                Analyze this cybersecurity assessment section and provide insights:
                
                Section: {section.title}
                Description: {section.description}
                
                Responses:
                {format_responses_for_ai(section_responses)}
                
                Please provide:
                1. Risk Assessment (High/Medium/Low with explanation)
                2. Key Strengths identified
                3. Critical Gaps or Weaknesses
                4. Top 3 Priority Recommendations
                5. Industry Benchmark Comparison
                
                Keep the response professional and actionable, around 300-400 words.
                """

                response = await openai.ChatCompletion.acreate(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=500,
                    temperature=0.7,
                )

                insights[section.id] = response.choices[0].message.content

            except Exception as e:
                print(f"Error generating AI insight for section {section.id}: {e}")
                insights[section.id] = (
                    "AI analysis temporarily unavailable for this section."
                )

    return insights


def format_responses_for_ai(responses: list[dict]) -> str:
    """Format responses for AI analysis"""

    formatted = []
    for resp in responses:
        formatted.append(f"Q: {resp['question']}")
        formatted.append(f"A: {resp['answer']} (Weight: {resp['weight']})")
        formatted.append("")

    return "\n".join(formatted)


def generate_report_html(assessment, responses, scores, structure) -> str:
    """Generate HTML content for standard report"""

    template = jinja_env.from_string(
        """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Security Posture Assessment Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .header { text-align: center; margin-bottom: 40px; }
            .section { margin-bottom: 30px; page-break-inside: avoid; }
            .score-box { background: #f5f5f5; padding: 15px; border-radius: 5px; margin: 10px 0; }
            .high-score { background: #d4edda; }
            .medium-score { background: #fff3cd; }
            .low-score { background: #f8d7da; }
            table { width: 100%; border-collapse: collapse; margin: 10px 0; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Security Posture Assessment Report</h1>
            <p>Generated on: {{ report_date }}</p>
            <p>Assessment Period: {{ assessment.started_at.strftime('%Y-%m-%d') }} to {{ assessment.completed_at.strftime('%Y-%m-%d') }}</p>
        </div>
        
        <div class="section">
            <h2>Executive Summary</h2>
            <div class="score-box {{ overall_score_class }}">
                <h3>Overall Security Score: {{ "%.1f"|format(scores.overall.percentage) }}%</h3>
                <p>{{ overall_assessment }}</p>
            </div>
        </div>
        
        <div class="section">
            <h2>Section Scores</h2>
            <table>
                <tr>
                    <th>Section</th>
                    <th>Score</th>
                    <th>Completion</th>
                    <th>Status</th>
                </tr>
                {% for section in structure.sections %}
                <tr>
                    <td>{{ section.title }}</td>
                    <td>{{ "%.1f"|format(scores[section.id].percentage) }}%</td>
                    <td>{{ "%.1f"|format(scores[section.id].completion_rate) }}%</td>
                    <td>{{ get_score_status(scores[section.id].percentage) }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
        
        <div class="section">
            <h2>Recommendations</h2>
            <ul>
                {% for recommendation in recommendations %}
                <li>{{ recommendation }}</li>
                {% endfor %}
            </ul>
        </div>
        
        <div class="section">
            <h2>Disclaimer</h2>
            <p>This assessment provides general guidance based on industry best practices. 
            For comprehensive security architecture planning, please contact EchoStor's security team 
            for a detailed professional assessment.</p>
        </div>
    </body>
    </html>
    """
    )

    overall_percentage = scores["overall"]["percentage"]
    if overall_percentage >= 80:
        overall_score_class = "high-score"
        overall_assessment = (
            "Strong security posture with good coverage across most areas."
        )
    elif overall_percentage >= 60:
        overall_score_class = "medium-score"
        overall_assessment = (
            "Moderate security posture with room for improvement in several areas."
        )
    else:
        overall_score_class = "low-score"
        overall_assessment = (
            "Security posture needs significant improvement across multiple areas."
        )

    recommendations = generate_recommendations(scores, structure)

    def get_score_status(percentage):
        if percentage >= 80:
            return "Strong"
        elif percentage >= 60:
            return "Moderate"
        else:
            return "Needs Improvement"

    return template.render(
        assessment=assessment,
        scores=scores,
        structure=structure,
        report_date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        overall_score_class=overall_score_class,
        overall_assessment=overall_assessment,
        recommendations=recommendations,
        get_score_status=get_score_status,
    )


def generate_ai_report_html(
    assessment, responses, scores, structure, ai_insights
) -> str:
    """Generate HTML content for AI-enhanced report"""

    template = jinja_env.from_string(
        """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>AI-Enhanced Security Posture Assessment Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .header { text-align: center; margin-bottom: 40px; }
            .section { margin-bottom: 30px; page-break-inside: avoid; }
            .score-box { background: #f5f5f5; padding: 15px; border-radius: 5px; margin: 10px 0; }
            .ai-insight { background: #e3f2fd; padding: 15px; border-left: 4px solid #2196f3; margin: 15px 0; }
            .high-score { background: #d4edda; }
            .medium-score { background: #fff3cd; }
            .low-score { background: #f8d7da; }
            table { width: 100%; border-collapse: collapse; margin: 10px 0; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>AI-Enhanced Security Posture Assessment Report</h1>
            <p>Generated on: {{ report_date }}</p>
            <p>Assessment Period: {{ assessment.started_at.strftime('%Y-%m-%d') }} to {{ assessment.completed_at.strftime('%Y-%m-%d') }}</p>
            <p><em>Enhanced with AI-powered analysis and recommendations</em></p>
        </div>
        
        <div class="section">
            <h2>Executive Summary</h2>
            <div class="score-box {{ overall_score_class }}">
                <h3>Overall Security Score: {{ "%.1f"|format(scores.overall.percentage) }}%</h3>
                <p>{{ overall_assessment }}</p>
            </div>
        </div>
        
        <div class="section">
            <h2>Section Analysis with AI Insights</h2>
            {% for section in structure.sections %}
            <div class="section">
                <h3>{{ section.title }}</h3>
                <div class="score-box">
                    <strong>Score: {{ "%.1f"|format(scores[section.id].percentage) }}%</strong>
                    ({{ scores[section.id].responses_count }}/{{ scores[section.id].total_questions }} questions completed)
                </div>
                {% if ai_insights[section.id] %}
                <div class="ai-insight">
                    <h4>🤖 AI Analysis</h4>
                    <p>{{ ai_insights[section.id] | replace('\n', '<br>') }}</p>
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        
        <div class="section">
            <h2>Overall Recommendations</h2>
            <ul>
                {% for recommendation in recommendations %}
                <li>{{ recommendation }}</li>
                {% endfor %}
            </ul>
        </div>
        
        <div class="section">
            <h2>Disclaimer</h2>
            <p>This AI-enhanced assessment provides advanced analysis based on industry best practices and AI-powered insights. 
            The AI analysis is provided for informational purposes and should be validated by security professionals. 
            For comprehensive security architecture planning, please contact EchoStor's security team 
            for a detailed professional assessment.</p>
        </div>
    </body>
    </html>
    """
    )

    overall_percentage = scores["overall"]["percentage"]
    if overall_percentage >= 80:
        overall_score_class = "high-score"
        overall_assessment = (
            "Strong security posture with good coverage across most areas."
        )
    elif overall_percentage >= 60:
        overall_score_class = "medium-score"
        overall_assessment = (
            "Moderate security posture with room for improvement in several areas."
        )
    else:
        overall_score_class = "low-score"
        overall_assessment = (
            "Security posture needs significant improvement across multiple areas."
        )

    recommendations = generate_recommendations(scores, structure)

    return template.render(
        assessment=assessment,
        scores=scores,
        structure=structure,
        ai_insights=ai_insights,
        report_date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        overall_score_class=overall_score_class,
        overall_assessment=overall_assessment,
        recommendations=recommendations,
    )


def generate_recommendations(scores, structure) -> list[str]:
    """Generate recommendations based on scores"""

    recommendations = []

    section_scores = [
        (section.title, scores[section.id]["percentage"])
        for section in structure.sections
    ]
    section_scores.sort(key=lambda x: x[1])

    for title, percentage in section_scores[:3]:
        if percentage < 70:
            recommendations.append(
                f"Prioritize improvements in {title} (current score: {percentage:.1f}%)"
            )

    overall_percentage = scores["overall"]["percentage"]
    if overall_percentage < 60:
        recommendations.append(
            "Consider engaging a cybersecurity consultant for comprehensive security program development"
        )

    if overall_percentage < 80:
        recommendations.append(
            "Implement regular security awareness training for all employees"
        )
        recommendations.append(
            "Establish a formal incident response plan and test it regularly"
        )

    return recommendations
