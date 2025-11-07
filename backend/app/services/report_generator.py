import logging
import uuid
from datetime import UTC, datetime
from typing import Any

from jinja2 import Environment
from openai import OpenAI
from weasyprint import HTML

from app.core.config import settings
from app.core.database import SessionLocal
from app.models.assessment import Assessment, AssessmentResponse, Report
from app.schemas.assessment import Question
from app.services.openai_key_manager import OpenAIKeyManager
from app.services.question_parser import (
    filter_structure_by_sections,
    load_assessment_structure,
)
from app.services.storage import get_storage_service

logger = logging.getLogger(__name__)

jinja_env = Environment(autoescape=True)


def generate_standard_report(report_id: str):
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

        if assessment.selected_section_ids:
            logger.info(
                f"Filtering structure to {len(assessment.selected_section_ids)} selected sections"
            )
            structure = filter_structure_by_sections(
                structure, assessment.selected_section_ids
            )

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
        report.completed_at = datetime.now(UTC)
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


def generate_ai_report(report_id: str):
    """Generate an AI-enhanced report using ChatGPT"""

    db = SessionLocal()
    report = None
    key_manager = None
    try:
        logger.info(f"Starting AI report generation for report_id: {report_id}")

        report = db.query(Report).filter(Report.id == report_id).first()
        if not report:
            logger.error(f"Report not found: {report_id}")
            return

        key_manager = OpenAIKeyManager(db)

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

        if assessment.selected_section_ids:
            logger.info(
                f"Filtering structure to {len(assessment.selected_section_ids)} selected sections"
            )
            structure = filter_structure_by_sections(
                structure, assessment.selected_section_ids
            )

        logger.info("Generating AI insights")
        ai_insights = generate_ai_insights(responses, structure, key_manager)

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
                f"AI PDF file was not persisted at storage location {storage_location}"
            )

        import os

        fly_region = os.getenv("FLY_REGION", "unknown")
        fly_primary = os.getenv("FLY_PRIMARY_REGION", "unknown")
        storage_backend = getattr(settings, "STORAGE_BACKEND", "local")

        logger.info(
            f"AI PDF generated successfully: {storage_location} "
            f"(region={fly_region}, primary={fly_primary}, backend={storage_backend})"
        )
        report.file_path = storage_location
        report.status = "completed"
        report.completed_at = datetime.now(UTC)
        db.commit()

        logger.info(
            f"AI report generation completed successfully for report_id: {report_id} "
            f"with file_path: {storage_location}"
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


def generate_ai_insights(
    responses: list[AssessmentResponse], structure, key_manager: OpenAIKeyManager
) -> dict[str, str]:
    """Generate AI insights for each section using round-robin key rotation"""

    insights = {}
    response_dict = {r.question_id: r for r in responses}

    try:
        key_id, api_key = key_manager.get_next_key()
        client = OpenAI(api_key=api_key, timeout=settings.OPENAI_TIMEOUT)
        logger.info(f"Using API key {key_id} for AI report generation")
    except ValueError as e:
        logger.error(f"Failed to get OpenAI API key: {e}")
        raise

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

                response = client.chat.completions.create(
                    model=settings.OPENAI_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=settings.OPENAI_MAX_TOKENS,
                    temperature=settings.OPENAI_TEMPERATURE,
                )

                insights[section.id] = response.choices[0].message.content

                if len(insights) == 1:
                    key_manager.record_success(key_id)

            except Exception as e:
                logger.error(
                    f"Error generating AI insight for section {section.id}: {e}"
                )
                key_manager.record_failure(key_id, e)
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
            body { font-family: 'Aptos (Body)', Arial, sans-serif; font-size: 12px; margin: 0; padding: 40px; line-height: 1.6; color: #333; }
            .container { max-width: 85%; margin: 0 auto; }
            .header { text-align: center; margin-bottom: 40px; border-bottom: 3px solid #2c3e50; padding-bottom: 20px; }
            .section { margin-bottom: 30px; page-break-inside: avoid; }
            .score-box { background: #f5f5f5; padding: 15px; border-radius: 5px; margin: 10px 0; }
            .high-score { background: #d4edda; border-left: 4px solid #28a745; }
            .medium-score { background: #fff3cd; border-left: 4px solid #ffc107; }
            .low-score { background: #f8d7da; border-left: 4px solid #dc3545; }
            table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 0.9em; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #2c3e50; color: white; font-weight: bold; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            .toc { background: #f8f9fa; padding: 20px; border-radius: 5px; margin-bottom: 30px; }
            .toc ul { list-style-type: none; padding-left: 0; }
            .toc li { margin: 8px 0; }
            .toc a { color: #2c3e50; text-decoration: none; }
            .toc a:hover { text-decoration: underline; }
            .metadata-box { background: #e9ecef; padding: 15px; border-radius: 5px; margin: 15px 0; }
            .confidence-box { padding: 10px; border-radius: 5px; margin: 10px 0; font-weight: bold; }
            .heatmap { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; margin: 20px 0; }
            .heatmap-item { padding: 15px; border-radius: 5px; text-align: center; }
            .remediation-table td { vertical-align: top; }
            .priority-p1 { color: #dc3545; font-weight: bold; }
            .priority-p2 { color: #fd7e14; font-weight: bold; }
            .priority-p3 { color: #28a745; font-weight: bold; }
            .question-row { page-break-inside: avoid; }
            .question-text { font-weight: bold; color: #2c3e50; }
            .answer-text { color: #495057; }
            .comment-text { font-style: italic; color: #6c757d; background: #f8f9fa; padding: 5px; border-radius: 3px; }
            .weight-badge { background: #6c757d; color: white; padding: 2px 8px; border-radius: 3px; font-size: 0.85em; }
            h1 { font-family: 'Aptos (Body)', Arial, sans-serif; font-size: 16px; color: #2c3e50; }
            h2 { font-family: 'Aptos (Body)', Arial, sans-serif; font-size: 16px; color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; margin-top: 30px; }
            h3 { font-family: 'Aptos (Body)', Arial, sans-serif; font-size: 14px; color: #495057; margin-top: 20px; }
            .summary-box { background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0; border-left: 4px solid #6c757d; }
            .strength-item { color: #28a745; }
            .gap-item { color: #dc3545; }
        </style>
    </head>
    <body>
        <div class="container">
        <div class="header">
            <h1>Security Posture Assessment Report</h1>
            <p><strong>Generated on:</strong> {{ report_date }}</p>
            <p><strong>Assessment Period:</strong> {{ assessment.started_at.strftime('%Y-%m-%d') }} to {{ assessment.completed_at.strftime('%Y-%m-%d') }}</p>
        </div>
        
        <div class="section toc">
            <h2>Table of Contents</h2>
            <ul>
                <li><a href="#executive-summary">1. Executive Summary</a></li>
                <li><a href="#assessment-overview">2. Assessment Overview and Metadata</a></li>
                <li><a href="#methodology">3. Methodology and Scoring</a></li>
                <li><a href="#data-quality">4. Data Quality and Confidence Level</a></li>
                <li><a href="#domain-heatmap">5. Domain Heatmap and Maturity Tiers</a></li>
                <li><a href="#section-scores">6. Section Scores</a></li>
                <li><a href="#remediation-plan">7. Prioritized Remediation Plan</a></li>
                <li><a href="#section-summaries">8. Section Summaries</a></li>
                <li><a href="#recommendations">9. Overall Recommendations</a></li>
                <li><a href="#detailed-responses">10. Detailed Responses (All Questions and Answers)</a></li>
                <li><a href="#comments-digest">11. Comments Digest</a></li>
                {% if assessment.consultation_interest %}
                <li><a href="#consultation">12. Consultation Request</a></li>
                {% endif %}
                <li><a href="#disclaimer">Disclaimer</a></li>
            </ul>
        </div>
        
        <div class="section" id="executive-summary">
            <h2>1. Executive Summary</h2>
            <div class="score-box {{ overall_score_class }}">
                <h3>Overall Security Score: {{ "%.1f"|format(scores.overall.percentage) }}%</h3>
                <p>{{ overall_assessment }}</p>
            </div>
        </div>
        
        <div class="section" id="assessment-overview">
            <h2>2. Assessment Overview and Metadata</h2>
            <div class="metadata-box">
                <p><strong>Assessment ID:</strong> {{ assessment.id }}</p>
                <p><strong>Started:</strong> {{ assessment.started_at.strftime('%Y-%m-%d %H:%M UTC') }}</p>
                <p><strong>Completed:</strong> {{ assessment.completed_at.strftime('%Y-%m-%d %H:%M UTC') }}</p>
                <p><strong>Total Questions:</strong> {{ structure.total_questions }}</p>
                <p><strong>Questions Answered:</strong> {{ responses|length }}</p>
                <p><strong>Overall Progress:</strong> {{ "%.1f"|format(assessment.progress_percentage) }}%</p>
                <p><strong>Report Version:</strong> Standard Report v1.0</p>
            </div>
            <p>This assessment evaluates your organization's cybersecurity posture across {{ structure.sections|length }} key security domains. 
            The evaluation is based on industry best practices and provides actionable insights for improving your security program.</p>
        </div>
        
        <div class="section" id="methodology">
            <h2>3. Methodology and Scoring</h2>
            <p>This assessment uses a weighted scoring methodology to evaluate your security posture:</p>
            <ul>
                <li><strong>Question Types:</strong>
                    <ul>
                        <li><em>Yes/No Questions:</em> Full weight awarded for "Yes" answers, zero for "No"</li>
                        <li><em>Multiple Choice:</em> Weight awarded for selecting an answer</li>
                        <li><em>Multiple Select:</em> Weight awarded for selecting one or more answers</li>
                        <li><em>Text Questions:</em> Not scored, used for context and planning</li>
                    </ul>
                </li>
                <li><strong>Question Weights:</strong> Questions are weighted 1-5 based on their importance to security posture</li>
                <li><strong>Section Scores:</strong> Calculated as (total points earned / total possible points) × 100%</li>
                <li><strong>Overall Score:</strong> Aggregate of all section scores weighted equally</li>
                <li><strong>Maturity Tiers:</strong>
                    <ul>
                        <li><em>Strong (≥80%):</em> Robust security practices in place</li>
                        <li><em>Moderate (60-79%):</em> Foundational practices with room for improvement</li>
                        <li><em>Needs Improvement (<60%):</em> Significant gaps requiring attention</li>
                    </ul>
                </li>
            </ul>
        </div>
        
        <div class="section" id="data-quality">
            <h2>4. Data Quality and Confidence Level</h2>
            <div class="confidence-box {{ confidence_class }}">
                <p><strong>Confidence Level:</strong> {{ confidence_level }}</p>
                <p>{{ confidence_description }}</p>
            </div>
            <table>
                <tr>
                    <th>Metric</th>
                    <th>Value</th>
                </tr>
                <tr>
                    <td>Total Questions</td>
                    <td>{{ structure.total_questions }}</td>
                </tr>
                <tr>
                    <td>Questions Answered</td>
                    <td>{{ responses|length }}</td>
                </tr>
                <tr>
                    <td>Questions Unanswered</td>
                    <td>{{ structure.total_questions - responses|length }}</td>
                </tr>
                <tr>
                    <td>Overall Completion Rate</td>
                    <td>{{ "%.1f"|format(assessment.progress_percentage) }}%</td>
                </tr>
                <tr>
                    <td>Comments Provided</td>
                    <td>{{ comments_count }}</td>
                </tr>
            </table>
        </div>
        
        <div class="section" id="domain-heatmap">
            <h2>5. Domain Heatmap and Maturity Tiers</h2>
            <p>Visual overview of security maturity across all domains:</p>
            <div class="heatmap">
                {% for section in structure.sections %}
                <div class="heatmap-item {{ maturity_tiers[section.id].css_class }}">
                    <strong>{{ section.title }}</strong><br>
                    {{ "%.1f"|format(scores[section.id].percentage) }}%<br>
                    <small>{{ maturity_tiers[section.id].tier }}</small>
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div class="section" id="section-scores">
            <h2>6. Section Scores</h2>
            <table>
                <tr>
                    <th>Section</th>
                    <th>Score</th>
                    <th>Completion</th>
                    <th>Maturity Tier</th>
                </tr>
                {% for section in structure.sections %}
                <tr>
                    <td>{{ section.title }}</td>
                    <td>{{ "%.1f"|format(scores[section.id].percentage) }}%</td>
                    <td>{{ "%.1f"|format(scores[section.id].completion_rate) }}%</td>
                    <td>{{ maturity_tiers[section.id].tier }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
        
        <div class="section" id="remediation-plan">
            <h2>7. Prioritized Remediation Plan</h2>
            <p>Recommended actions prioritized by impact and urgency:</p>
            {% if remediation_items %}
            <table class="remediation-table">
                <tr>
                    <th>Priority</th>
                    <th>Domain</th>
                    <th>Current Score</th>
                    <th>Effort</th>
                    <th>Timeframe</th>
                </tr>
                {% for item in remediation_items %}
                <tr>
                    <td class="priority-{{ item.priority|lower }}">{{ item.priority }}</td>
                    <td>{{ item.domain }}</td>
                    <td>{{ item.current_score }}</td>
                    <td>{{ item.effort }}</td>
                    <td>{{ item.timeframe }}</td>
                </tr>
                {% endfor %}
            </table>
            <p><strong>Priority Levels:</strong></p>
            <ul>
                <li><span class="priority-p1">P1 (Critical):</span> Address immediately - significant security gaps</li>
                <li><span class="priority-p2">P2 (High):</span> Address within 30-90 days - important improvements</li>
                <li><span class="priority-p3">P3 (Medium):</span> Quick wins - low effort, visible improvements</li>
            </ul>
            {% else %}
            <p>No critical remediation items identified. Continue maintaining current security practices.</p>
            {% endif %}
        </div>
        
        <div class="section" id="section-summaries">
            <h2>8. Section Summaries</h2>
            <p>Detailed analysis of each security domain:</p>
            {% for summary in section_summaries %}
            <div class="summary-box">
                <h3>{{ summary.section.title }}</h3>
                <p><strong>Score:</strong> {{ "%.1f"|format(summary.score) }}% | 
                   <strong>Completion:</strong> {{ "%.1f"|format(summary.completion) }}%</p>
                
                {% if summary.strengths %}
                <p><strong>Key Strengths:</strong></p>
                <ul>
                    {% for strength in summary.strengths %}
                    <li class="strength-item">{{ strength }}</li>
                    {% endfor %}
                </ul>
                {% endif %}
                
                {% if summary.gaps %}
                <p><strong>Critical Gaps:</strong></p>
                <ul>
                    {% for gap in summary.gaps %}
                    <li class="gap-item">{{ gap }}</li>
                    {% endfor %}
                </ul>
                {% endif %}
                
                {% if summary.recommendations %}
                <p><strong>Recommendations:</strong></p>
                <ul>
                    {% for rec in summary.recommendations %}
                    <li>{{ rec }}</li>
                    {% endfor %}
                </ul>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        
        <div class="section" id="recommendations">
            <h2>9. Overall Recommendations</h2>
            <ul>
                {% for recommendation in recommendations %}
                <li>{{ recommendation }}</li>
                {% endfor %}
            </ul>
        </div>
        
        <div class="section" id="detailed-responses">
            <h2>10. Detailed Responses (All Questions and Answers)</h2>
            <p>Complete record of all assessment questions with your submitted answers and comments:</p>
            {% for section in structure.sections %}
            <div class="section">
                <h3>{{ section.title }}</h3>
                <table>
                    <tr>
                        <th style="width: 50%;">Question</th>
                        <th style="width: 25%;">Answer</th>
                        <th style="width: 15%;">Comment</th>
                        <th style="width: 10%;">Weight</th>
                    </tr>
                    {% for question in section.questions %}
                    <tr class="question-row">
                        <td class="question-text">{{ question.text }}</td>
                        <td class="answer-text">{{ question_answers[question.id] }}</td>
                        <td class="comment-text">{{ question_comments[question.id] }}</td>
                        <td><span class="weight-badge">{{ question.weight }}</span></td>
                    </tr>
                    {% endfor %}
                </table>
            </div>
            {% endfor %}
        </div>
        
        <div class="section" id="comments-digest">
            <h2>11. Comments Digest</h2>
            <p>All comments provided during the assessment, grouped by domain:</p>
            {% if all_comments %}
            {% for section in structure.sections %}
                {% if section_comments[section.id] %}
                <div class="summary-box">
                    <h3>{{ section.title }}</h3>
                    {% for comment_item in section_comments[section.id] %}
                    <p><strong>Q:</strong> {{ comment_item.question }}<br>
                       <strong>Comment:</strong> <em>{{ comment_item.comment }}</em></p>
                    {% endfor %}
                </div>
                {% endif %}
            {% endfor %}
            {% else %}
            <p>No comments were provided during this assessment.</p>
            {% endif %}
        </div>
        
        {% if assessment.consultation_interest %}
        <div class="section" id="consultation">
            <h2>12. Consultation Request</h2>
            <div class="score-box medium-score">
                <p><strong>Consultation Interest:</strong> Yes</p>
                {% if assessment.consultation_details %}
                <p><strong>Details:</strong></p>
                <p>{{ assessment.consultation_details }}</p>
                {% endif %}
                <p><em>An EchoStor security consultant will contact you to discuss your specific needs and how we can help improve your security posture.</em></p>
            </div>
        </div>
        {% endif %}
        
        <div class="section" id="disclaimer">
            <h2>Disclaimer</h2>
            <p>This assessment provides general guidance based on industry best practices and your self-reported responses. 
            The scores and recommendations are indicative and should be validated through comprehensive security audits. 
            For detailed security architecture planning, penetration testing, or compliance assessments, 
            please contact EchoStor's security team for a professional evaluation tailored to your organization's specific needs.</p>
        </div>
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

    confidence_level, confidence_description = calculate_confidence_level(scores)
    if confidence_level == "High":
        confidence_class = "high-score"
    elif confidence_level == "Medium":
        confidence_class = "medium-score"
    else:
        confidence_class = "low-score"

    maturity_tiers = {}
    for section in structure.sections:
        tier, css_class = get_maturity_tier(scores[section.id]["percentage"])
        maturity_tiers[section.id] = {"tier": tier, "css_class": css_class}

    remediation_items = generate_prioritized_remediation(scores, structure)
    section_summaries = generate_section_summaries(scores, structure, responses)

    response_dict = {r.question_id: r for r in responses}
    question_answers = {}
    question_comments = {}

    for section in structure.sections:
        for question in section.questions:
            response = response_dict.get(question.id)
            if response:
                question_answers[question.id] = normalize_answer_display(
                    response.answer_value, question
                )
                question_comments[question.id] = (
                    response.comment if response.comment else "—"
                )
            else:
                question_answers[question.id] = "Not answered"
                question_comments[question.id] = "—"

    all_comments = []
    section_comments: dict[str, list] = {}
    comments_count = 0

    for section in structure.sections:
        section_comments[section.id] = []
        for question in section.questions:
            response = response_dict.get(question.id)
            if response and response.comment:
                comments_count += 1
                all_comments.append(
                    {
                        "section": section.title,
                        "question": question.text,
                        "comment": response.comment,
                    }
                )
                section_comments[section.id].append(
                    {"question": question.text, "comment": response.comment}
                )

    return template.render(
        assessment=assessment,
        scores=scores,
        structure=structure,
        responses=responses,
        report_date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        overall_score_class=overall_score_class,
        overall_assessment=overall_assessment,
        recommendations=recommendations,
        confidence_level=confidence_level,
        confidence_description=confidence_description,
        confidence_class=confidence_class,
        maturity_tiers=maturity_tiers,
        remediation_items=remediation_items,
        section_summaries=section_summaries,
        question_answers=question_answers,
        question_comments=question_comments,
        all_comments=all_comments,
        section_comments=section_comments,
        comments_count=comments_count,
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
            body { font-family: 'Aptos (Body)', Arial, sans-serif; font-size: 12px; margin: 0; padding: 40px; line-height: 1.6; color: #333; }
            .container { max-width: 85%; margin: 0 auto; }
            .header { text-align: center; margin-bottom: 40px; border-bottom: 3px solid #2c3e50; padding-bottom: 20px; }
            .section { margin-bottom: 30px; page-break-inside: avoid; }
            .score-box { background: #f5f5f5; padding: 15px; border-radius: 5px; margin: 10px 0; }
            .ai-insight { background: #e3f2fd; padding: 15px; border-left: 4px solid #2196f3; margin: 15px 0; }
            .high-score { background: #d4edda; border-left: 4px solid #28a745; }
            .medium-score { background: #fff3cd; border-left: 4px solid #ffc107; }
            .low-score { background: #f8d7da; border-left: 4px solid #dc3545; }
            table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 0.9em; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #2c3e50; color: white; font-weight: bold; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            h1 { font-family: 'Aptos (Body)', Arial, sans-serif; font-size: 16px; color: #2c3e50; }
            h2 { font-family: 'Aptos (Body)', Arial, sans-serif; font-size: 16px; color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; margin-top: 30px; }
            h3 { font-family: 'Aptos (Body)', Arial, sans-serif; font-size: 14px; color: #495057; margin-top: 20px; }
            h4 { font-family: 'Aptos (Body)', Arial, sans-serif; font-size: 12px; color: #2196f3; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
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


def normalize_answer_display(answer_value: Any, question: Question) -> str:
    """Convert answer value to human-readable display format"""

    if answer_value is None:
        return "Not answered"

    if question.type == "yes_no":
        if isinstance(answer_value, bool):
            return "Yes" if answer_value else "No"
        if isinstance(answer_value, str):
            return "Yes" if answer_value.lower() in ["yes", "true", "1"] else "No"
        return "Yes" if answer_value else "No"

    elif question.type == "multiple_choice":
        if isinstance(answer_value, str):
            for option in question.options:
                if option.value == answer_value:
                    return option.label
        return str(answer_value) if answer_value else "Not answered"

    elif question.type == "multiple_select":
        if isinstance(answer_value, list) and answer_value:
            labels = []
            for val in answer_value:
                for option in question.options:
                    if option.value == val:
                        labels.append(option.label)
                        break
                else:
                    labels.append(str(val))
            return ", ".join(labels) if labels else "Not answered"
        return "Not answered"

    elif question.type == "text":
        if isinstance(answer_value, str) and answer_value.strip():
            return answer_value.replace("\n", "<br>")
        return "Not answered"

    return str(answer_value) if answer_value else "Not answered"


def get_maturity_tier(percentage: float) -> tuple[str, str]:
    """Get maturity tier and CSS class for a score percentage"""
    if percentage >= 80:
        return ("Strong", "high-score")
    elif percentage >= 60:
        return ("Moderate", "medium-score")
    else:
        return ("Needs Improvement", "low-score")


def calculate_confidence_level(scores: dict) -> tuple[str, str]:
    """Calculate overall confidence level based on completion rates"""

    total_completion = 0
    section_count = 0

    for key, value in scores.items():
        if key != "overall" and "completion_rate" in value:
            total_completion += value["completion_rate"]
            section_count += 1

    avg_completion = total_completion / section_count if section_count > 0 else 0

    if avg_completion >= 80:
        return ("High", "All sections substantially completed with reliable results")
    elif avg_completion >= 60:
        return ("Medium", "Most sections completed, results generally reliable")
    else:
        return ("Low", "Significant gaps in completion may affect result reliability")


def generate_prioritized_remediation(scores: dict, structure: Any) -> list[dict]:
    """Generate prioritized remediation plan with effort and timeframe"""

    remediation_items = []

    section_scores = [
        (section, scores[section.id]["percentage"]) for section in structure.sections
    ]
    section_scores.sort(key=lambda x: x[1])

    for section, percentage in section_scores[:5]:
        if percentage < 70:
            priority = "P1" if percentage < 50 else "P2"
            effort = "High" if percentage < 40 else "Medium"
            timeframe = "90-180 days" if percentage < 40 else "30-90 days"

            remediation_items.append(
                {
                    "domain": section.title,
                    "priority": priority,
                    "effort": effort,
                    "timeframe": timeframe,
                    "current_score": f"{percentage:.1f}%",
                }
            )

    for section, percentage in section_scores:
        if 60 <= percentage < 80:
            remediation_items.append(
                {
                    "domain": section.title,
                    "priority": "P3",
                    "effort": "Low",
                    "timeframe": "0-30 days",
                    "current_score": f"{percentage:.1f}%",
                }
            )
            if len(remediation_items) >= 10:
                break

    return remediation_items


def generate_section_summaries(
    scores: dict, structure: Any, responses: list
) -> list[dict]:
    """Generate summary for each section with strengths and gaps"""

    response_dict = {r.question_id: r for r in responses}
    summaries = []

    for section in structure.sections:
        section_score = scores[section.id]

        answered_questions = []
        for question in section.questions:
            response = response_dict.get(question.id)
            if response:
                answered_questions.append((question, response))

        strengths = []
        gaps = []

        for question, response in answered_questions:
            if question.type == "yes_no":
                answer_str = str(response.answer_value).lower()
                if answer_str in ["yes", "true", "1"]:
                    if question.weight >= 4:
                        strengths.append(
                            question.text[:80] + "..."
                            if len(question.text) > 80
                            else question.text
                        )
                else:
                    if question.weight >= 4:
                        gaps.append(
                            question.text[:80] + "..."
                            if len(question.text) > 80
                            else question.text
                        )

        # Generate recommendations
        recommendations = []
        if section_score["percentage"] < 70:
            recommendations.append(
                f"Focus on improving {section.title} - current score below target"
            )
        if section_score["completion_rate"] < 100:
            recommendations.append(
                f"Complete remaining {section_score['total_questions'] - section_score['responses_count']} questions"
            )
        if section_score["percentage"] >= 80:
            recommendations.append(
                "Maintain current strong practices and review periodically"
            )

        summaries.append(
            {
                "section": section,
                "score": section_score["percentage"],
                "completion": section_score["completion_rate"],
                "strengths": strengths[:3],  # Top 3
                "gaps": gaps[:3],  # Top 3
                "recommendations": recommendations[:3],  # Top 3
            }
        )

    return summaries
