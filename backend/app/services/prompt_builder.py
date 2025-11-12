"""Prompt builder service for AI report generation"""


def build_section_prompt_v2(
    section, section_responses: list[dict], curated_context: str = ""
) -> str:
    """Build JSON-mode prompt for section analysis"""

    signals = []
    for i, resp in enumerate(section_responses, 1):
        answer_str = str(resp["answer"])
        signals.append(f"Q{i}: {answer_str} (weight:{resp['weight']})")

    prompt = f"""Analyze this cybersecurity assessment section and provide comprehensive, structured insights.

Section: {section.title}
Description: {section.description}

Signals:
{chr(10).join(signals)}

{curated_context}

Provide your analysis as JSON matching this schema:
{{
  "risk_level": "Low|Medium|Medium-High|High|Critical",
  "risk_explanation": "Detailed explanation (120-180 words)",
  "strengths": ["strength1", "strength2", "strength3"],
  "gaps": [
    {{
      "gap": "description (25-40 words)",
      "linked_signals": ["Q1", "Q7"],
      "severity": "Low|Medium|High|Critical"
    }}
  ],
  "recommendations": [
    {{
      "action": "specific action (15-25 words)",
      "rationale": "why this matters (30-50 words)",
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

WORD COUNT REQUIREMENTS (TOTAL: 300-400 WORDS):
- risk_explanation: 120-180 words - Provide a comprehensive analysis of the current security posture, specific risks identified, and their potential business impact
- strengths: 3-5 items, each 20-30 words - Highlight specific positive security practices with context
- gaps: 3-5 items, each gap description 25-40 words - Identify specific security weaknesses with clear explanations
- recommendations: 3-5 items, each rationale 30-50 words - Provide actionable guidance with detailed justification

STRICT REQUIREMENTS:
1. Every gap MUST reference at least one signal (Q1, Q2, etc.) that supports it
2. Every recommendation MUST reference the signals it addresses
3. Use exact signal IDs from the list above (Q1-Q{len(section_responses)})
4. Severity levels must match: Critical (score <40%), High (40-60%), Medium (60-80%), Low (>80%)
5. Effort estimates: Low (<1 week), Medium (1-4 weeks), High (>1 month)
6. Timeline: 30-day for Critical/High, 60-day for Medium, 90-day for Low
7. Benchmark status must be based on signals: Missing if answer=No, Partial if answer=Partial, Implemented if answer=Yes
8. If any gap has severity "Critical", risk_level MUST be "High" or "Critical"

COMPREHENSIVE EXAMPLE:
{{
  "risk_level": "Medium-High",
  "risk_explanation": "The organization demonstrates a foundational understanding of access control principles with basic authentication mechanisms in place. However, critical gaps exist in multi-factor authentication deployment and privileged access management. The current reliance on password-only authentication for administrative accounts creates significant vulnerability to credential-based attacks, which represent over 80% of security breaches according to industry data. Without MFA, a single compromised password could grant attackers full system access. The lack of regular access reviews and automated deprovisioning processes further compounds this risk, as dormant accounts with elevated privileges remain active indefinitely. These vulnerabilities are particularly concerning given the organization's handling of sensitive customer data and regulatory compliance requirements under frameworks like SOC 2 and ISO 27001.",
  "strengths": [
    "Password complexity requirements are enforced across all user accounts, requiring minimum 12 characters with mixed case, numbers, and special characters, reducing brute-force attack susceptibility",
    "Role-based access control (RBAC) framework is implemented for application-level permissions, ensuring users only access resources necessary for their job functions",
    "Annual security awareness training is provided to all employees, covering phishing recognition, password hygiene, and social engineering tactics"
  ],
  "gaps": [
    {{
      "gap": "Multi-factor authentication is not implemented for administrative accounts, leaving critical systems vulnerable to credential theft and unauthorized access despite strong password policies",
      "linked_signals": ["Q7", "Q12"],
      "severity": "High"
    }},
    {{
      "gap": "No automated user access review process exists, resulting in accumulation of orphaned accounts and excessive permissions that violate least-privilege principles",
      "linked_signals": ["Q15", "Q18"],
      "severity": "Medium"
    }},
    {{
      "gap": "Privileged access management solution is absent, preventing secure storage and rotation of administrative credentials and lacking session recording for audit purposes",
      "linked_signals": ["Q9", "Q14"],
      "severity": "High"
    }}
  ],
  "recommendations": [
    {{
      "action": "Deploy multi-factor authentication for all administrative and privileged accounts using hardware tokens or authenticator apps",
      "rationale": "Current password-only authentication (Q7: No, Q12: No) exposes critical systems to credential-based attacks. MFA reduces account compromise risk by 99.9% according to Microsoft research. This control is required by SOC 2, ISO 27001, and most cyber insurance policies. Implementation should prioritize admin accounts first, then expand to all users within 90 days.",
      "linked_signals": ["Q7", "Q12"],
      "effort": "Medium",
      "impact": "Critical",
      "timeline": "30-day",
      "references": ["NIST CSF PR.AC-7", "ISO 27001 A.9.4.2", "CIS Control 6.3"]
    }},
    {{
      "action": "Implement quarterly access reviews with automated workflows for approval and deprovisioning of unnecessary permissions",
      "rationale": "Without regular reviews (Q15: No, Q18: Partial), access rights accumulate over time leading to excessive privileges and compliance violations. Automated quarterly reviews ensure timely removal of access for terminated employees and role changes. This addresses audit findings and reduces insider threat risk by limiting the attack surface available to compromised accounts.",
      "linked_signals": ["Q15", "Q18"],
      "effort": "Medium",
      "impact": "High",
      "timeline": "60-day",
      "references": ["NIST CSF PR.AC-4", "ISO 27001 A.9.2.5", "SOC 2 CC6.2"]
    }},
    {{
      "action": "Deploy privileged access management (PAM) solution to secure, rotate, and monitor all administrative credentials and sessions",
      "rationale": "Lack of PAM (Q9: No, Q14: No) means administrative passwords are stored insecurely and rarely rotated, creating persistent attack vectors. PAM solutions provide secure vaults, automatic credential rotation, session recording for forensics, and just-in-time access provisioning. This is critical for compliance with PCI-DSS, HIPAA, and SOX requirements for organizations handling sensitive data.",
      "linked_signals": ["Q9", "Q14"],
      "effort": "High",
      "impact": "High",
      "timeline": "60-day",
      "references": ["NIST CSF PR.AC-6", "ISO 27001 A.9.4.3", "CIS Control 5.4"]
    }}
  ],
  "benchmarks": [
    {{
      "control": "Multi-Factor Authentication",
      "status": "Missing",
      "framework": "NIST",
      "reference": "NIST CSF PR.AC-7"
    }},
    {{
      "control": "Access Review Process",
      "status": "Partial",
      "framework": "ISO",
      "reference": "ISO 27001 A.9.2.5"
    }},
    {{
      "control": "Privileged Access Management",
      "status": "Missing",
      "framework": "CIS",
      "reference": "CIS Control 5.4"
    }}
  ],
  "confidence_score": 0.85
}}

Provide detailed, actionable insights that help the organization understand their security posture and prioritize improvements. Be specific and reference industry standards.
"""
    return prompt
