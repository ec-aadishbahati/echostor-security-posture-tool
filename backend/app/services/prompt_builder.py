"""Prompt builder service for AI report generation"""


def build_section_prompt_v2(section, section_responses: list[dict], curated_context: str = "") -> str:
    """Build JSON-mode prompt for section analysis"""
    
    signals = []
    for i, resp in enumerate(section_responses, 1):
        answer_str = str(resp['answer'])
        signals.append(f"Q{i}: {answer_str} (weight:{resp['weight']})")
    
    prompt = f"""Analyze this cybersecurity assessment section and provide structured insights.

Section: {section.title}
Description: {section.description}

Signals:
{chr(10).join(signals)}

{curated_context}

Provide your analysis as JSON matching this schema:
{{
  "risk_level": "Low|Medium|Medium-High|High|Critical",
  "risk_explanation": "Detailed explanation (50-1000 chars)",
  "strengths": ["strength1", "strength2", "strength3"],
  "gaps": [
    {{
      "gap": "description",
      "linked_signals": ["Q1", "Q7"],
      "severity": "Low|Medium|High|Critical"
    }}
  ],
  "recommendations": [
    {{
      "action": "specific action",
      "rationale": "why this matters",
      "linked_signals": ["Q3"],
      "effort": "Low|Medium|High",
      "impact": "Low|Medium|High|Critical",
      "timeline": "30-day|60-day|90-day",
      "references": ["NIST CSF PR.AC-1"]
    }}
  ],
  "benchmarks": [
    {{
      "control": "Multi-Factor Authentication",
      "status": "Implemented|Partial|Missing|Not Applicable",
      "framework": "NIST|ISO|OWASP|CIS",
      "reference": "NIST CSF PR.AC-7"
    }}
  ],
  "confidence_score": 0.85
}}

STRICT REQUIREMENTS:
1. Every gap MUST reference at least one signal (Q1, Q2, etc.) that supports it
2. Every recommendation MUST reference the signals it addresses
3. Use exact signal IDs from the list above (Q1-Q{len(section_responses)})
4. Severity levels must match: Critical (score <40%), High (40-60%), Medium (60-80%), Low (>80%)
5. Effort estimates: Low (<1 week), Medium (1-4 weeks), High (>1 month)
6. Timeline: 30-day for Critical/High, 60-day for Medium, 90-day for Low
7. Benchmark status must be based on signals: Missing if answer=No, Partial if answer=Partial, Implemented if answer=Yes

Example gap with proper signal reference:
{{
  "gap": "No multi-factor authentication for admin accounts",
  "linked_signals": ["Q7", "Q12"],
  "severity": "High"
}}

Example recommendation with proper signal reference:
{{
  "action": "Implement MFA for all administrative accounts",
  "rationale": "Current lack of MFA (Q7: No) creates high risk of account compromise",
  "linked_signals": ["Q7"],
  "effort": "Medium",
  "impact": "High",
  "timeline": "30-day",
  "references": ["NIST CSF PR.AC-7", "ISO 27001 A.9.4.2"]
}}

Keep the response professional and actionable. Total response ~400-600 words equivalent.
"""
    return prompt
