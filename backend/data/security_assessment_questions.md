# Security Posture Assessment - Complete Question Database

*Comprehensive documentation of all assessment questions with detailed option explanations*

## Overview

- **Total Sections:** 19
- **Total Subsections:** 63
- **Total Questions:** 409
- **Documentation Level:** Enhanced with detailed option explanations, market benchmarks, and actionable recommendations

## Table of Contents

- [Section 1: Governance & Strategy](#section-1-governance-and-strategy)
  - [1.1: Security Vision & Objectives](#subsection-11-security-vision-and-objectives)
  - [1.2: Policies & Standards Lifecycle](#subsection-12-policies-and-standards-lifecycle)
  - [1.3: Budget & Resource Allocation](#subsection-13-budget-and-resource-allocation)
  - [1.4: Metrics / KPIs / Board Reporting](#subsection-14-metrics-/-kpis-/-board-reporting)
- [Section 4: Identity & Access Management (IAM)](#section-4-identity-and-access-management-(iam))
  - [4.1: Directory Architecture (AD/AAD/IDaaS)](#subsection-41-directory-architecture-(ad/aad/idaas))
  - [4.2: Access Control & Authorization](#subsection-42-access-control-and-authorization)
  - [4.3: User Lifecycle Management](#subsection-43-user-lifecycle-management)
  - [4.4: Multi-Factor Authentication](#subsection-44-multi-factor-authentication)
- [Section 2: Risk Management](#section-2-risk-management)
  - [2.1: Risk Assessment & Analysis](#subsection-21-risk-assessment-and-analysis)
  - [2.2: Risk Treatment & Mitigation](#subsection-22-risk-treatment-and-mitigation)
  - [2.3: Business Impact Analysis](#subsection-23-business-impact-analysis)
- [Section 3: Asset Management](#section-3-asset-management)
  - [3.1: Asset Inventory & Classification](#subsection-31-asset-inventory-and-classification)
  - [3.2: Asset Lifecycle Management](#subsection-32-asset-lifecycle-management)
  - [3.3: Data Classification & Handling](#subsection-33-data-classification-and-handling)
- [Section 5: Network Security](#section-5-network-security)
  - [5.1: Network Architecture & Segmentation](#subsection-51-network-architecture-and-segmentation)
  - [5.2: Firewall & Perimeter Security](#subsection-52-firewall-and-perimeter-security)
  - [5.3: Network Monitoring & Detection](#subsection-53-network-monitoring-and-detection)
  - [5.4: Remote Access & VPN](#subsection-54-remote-access-and-vpn)
- [Section 6: Endpoint Security](#section-6-endpoint-security)
  - [6.1: Endpoint Protection & Management](#subsection-61-endpoint-protection-and-management)
  - [6.2: Mobile Device Security](#subsection-62-mobile-device-security)
  - [6.3: Endpoint Configuration Management](#subsection-63-endpoint-configuration-management)
- [Section 7: Data Protection & Privacy](#section-7-data-protection-and-privacy)
  - [7.1: Data Encryption & Protection](#subsection-71-data-encryption-and-protection)
  - [7.2: Privacy & Compliance](#subsection-72-privacy-and-compliance)
  - [7.3: Data Backup & Recovery](#subsection-73-data-backup-and-recovery)
  - [7.4: Data Governance & Subject Rights](#subsection-74-data-governance-and-subject-rights)
- [Section 8: Application Security](#section-8-application-security)
  - [8.1: Secure Development Lifecycle](#subsection-81-secure-development-lifecycle)
  - [8.2: Web Application Security](#subsection-82-web-application-security)
  - [8.3: API Security](#subsection-83-api-security)
  - [8.4: DevSecOps & CI/CD Security](#subsection-84-devsecops-and-ci/cd-security)
- [Section 9: Cloud & Container Security](#section-9-cloud-and-container-security)
  - [9.1: Cloud Infrastructure Security](#subsection-91-cloud-infrastructure-security)
  - [9.2: Cloud Identity & Access Management](#subsection-92-cloud-identity-and-access-management)
  - [9.3: Container & Serverless Security](#subsection-93-container-and-serverless-security)
- [Section 10: Incident Response & Resilience](#section-10-incident-response-and-resilience)
  - [10.1: Incident Response Planning](#subsection-101-incident-response-planning)
  - [10.2: Incident Detection & Response](#subsection-102-incident-detection-and-response)
  - [10.3: Incident Recovery & Lessons Learned](#subsection-103-incident-recovery-and-lessons-learned)
- [Section 11: Business Continuity](#section-11-business-continuity)
  - [11.1: Business Continuity Planning](#subsection-111-business-continuity-planning)
  - [11.2: Disaster Recovery](#subsection-112-disaster-recovery)
  - [11.3: Crisis Management](#subsection-113-crisis-management)
  - [11.4: Recovery Operations](#subsection-114-recovery-operations)
- [Section 12: Vendor Management](#section-12-vendor-management)
  - [12.1: Vendor Risk Assessment](#subsection-121-vendor-risk-assessment)
  - [12.2: Contract Management](#subsection-122-contract-management)
  - [12.3: Vendor Monitoring & Oversight](#subsection-123-vendor-monitoring-and-oversight)
  - [12.4: Supply Chain Security](#subsection-124-supply-chain-security)
- [Section 13: Security Awareness & Training](#section-13-security-awareness-and-training)
  - [13.1: Security Awareness Program](#subsection-131-security-awareness-program)
  - [13.2: Phishing & Social Engineering](#subsection-132-phishing-and-social-engineering)
  - [13.3: Role-Based Training](#subsection-133-role-based-training)
  - [13.4: Training Management & Compliance](#subsection-134-training-management-and-compliance)
- [Section 14: Physical Security](#section-14-physical-security)
  - [14.1: Facility Security](#subsection-141-facility-security)
  - [14.2: Environmental Controls](#subsection-142-environmental-controls)
  - [14.3: Equipment Security](#subsection-143-equipment-security)
- [Section 15: Monitoring & Detection](#section-15-monitoring-and-detection)
  - [15.1: Security Monitoring](#subsection-151-security-monitoring)
  - [15.2: Threat Detection](#subsection-152-threat-detection)
  - [15.3: Log Management](#subsection-153-log-management)
- [Section 16: Vulnerability Management](#section-16-vulnerability-management)
  - [16.1: Vulnerability Assessment](#subsection-161-vulnerability-assessment)
  - [16.2: Vulnerability Management Process](#subsection-162-vulnerability-management-process)
  - [16.3: Patch Management](#subsection-163-patch-management)
- [Section 17: Compliance & Audit](#section-17-compliance-and-audit)
  - [17.1: Regulatory Compliance](#subsection-171-regulatory-compliance)
  - [17.2: Internal Audits](#subsection-172-internal-audits)
  - [17.3: External Audits & Certifications](#subsection-173-external-audits-and-certifications)
- [Section 18: OT/ICS & IoT Security](#section-18-ot/ics-and-iot-security)
  - [18.1: Operational Technology Security](#subsection-181-operational-technology-security)
  - [18.2: IoT Device Security](#subsection-182-iot-device-security)
- [Section 19: AI/ML & Machine Learning Security](#section-19-ai/ml-and-machine-learning-security)
  - [19.1: Model Security & Governance](#subsection-191-model-security-and-governance)
  - [19.2: ML Pipeline Security](#subsection-192-ml-pipeline-security)

---

## Section 1: Governance & Strategy

**Suggested Respondents:** CISO, CIO, Risk Officer

### Subsection 1.1: Security Vision & Objectives

#### Question 1.1.1

**Question:** Does your organization have a formally documented cybersecurity strategy?

**Type:** yes_no

**Weight:** 5

**Explanation:** A documented cybersecurity strategy provides clear direction and alignment with business objectives.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 1.1.2

**Question:** How often is your cybersecurity strategy reviewed and updated?

**Type:** multiple_choice

**Explanation:** Regular strategy reviews ensure alignment with evolving threats and business changes.

**Answer Options:**

**Option 1: Annually**
*Basic Description:* Once per year review cycle

**📋 What This Option Means:**
- **Definition:** Cybersecurity strategy is formally reviewed and updated once every 12 months, typically aligned with annual business planning cycles.
- **Why It Matters:** Annual reviews ensure strategy remains aligned with evolving business objectives and threat landscape. However, may miss rapid changes in threat environment or business priorities.

**📊 Market Context & Benchmarks:**
- **Industry Adoption Rate:** 65% of organizations review annually
- **Industry Benchmark:** Standard for stable, low-risk industries
- **Compliance Frameworks:** ISO 27001 requires annual management review, NIST CSF suggests regular strategy updates

**🎯 Recommendations & Next Steps:**
- **If You Select This Option:** Consider supplementing with quarterly threat landscape reviews and ad-hoc reviews after major business changes or security incidents.
- **Path to Improvement:** Move to bi-annual reviews for more dynamic threat response, especially in high-risk industries.

**Option 2: Bi-annually**
*Basic Description:* Twice per year review cycle

**📋 What This Option Means:**
- **Definition:** Cybersecurity strategy is formally reviewed and updated twice per year, providing more frequent alignment checks with business objectives and threat landscape changes.
- **Why It Matters:** Bi-annual reviews strike a balance between staying current with threats and avoiding review fatigue. Allows for mid-year course corrections based on emerging threats or business changes.

**📊 Market Context & Benchmarks:**
- **Industry Adoption Rate:** 25% of organizations review bi-annually
- **Industry Benchmark:** Best practice for medium-risk industries and growing organizations
- **Compliance Frameworks:** Exceeds most regulatory requirements, Aligns with NIST CSF continuous improvement principles

**🎯 Recommendations & Next Steps:**
- **If You Select This Option:** Ensure reviews are substantive and not just administrative exercises. Focus one review on strategic alignment and another on tactical effectiveness.
- **Path to Improvement:** Consider quarterly reviews for high-risk industries or during periods of rapid business change.

**Option 3: As needed**
*Basic Description:* Reactive reviews based on events

**📋 What This Option Means:**
- **Definition:** Cybersecurity strategy reviews are triggered by specific events such as security incidents, major business changes, regulatory updates, or significant threat landscape shifts.
- **Why It Matters:** Event-driven reviews can be highly relevant and timely, but may result in inconsistent review frequency and potential gaps during quiet periods. Risk of reactive rather than proactive strategy management.

**📊 Market Context & Benchmarks:**
- **Industry Adoption Rate:** 15% of organizations use purely event-driven reviews
- **Industry Benchmark:** Common in resource-constrained organizations but not considered best practice
- **Compliance Frameworks:** May not meet regulatory requirements for regular reviews, Could satisfy requirements if events trigger sufficient review frequency

**🎯 Recommendations & Next Steps:**
- **If You Select This Option:** Establish clear criteria for what events trigger reviews and ensure minimum annual review regardless of events. Document review triggers and maintain review schedule visibility.
- **Path to Improvement:** Transition to scheduled reviews (at least annually) supplemented by event-driven reviews for major changes.

**Option 4: Never**
*Basic Description:* No formal review process

**📋 What This Option Means:**
- **Definition:** The organization does not have a formal process for reviewing and updating its cybersecurity strategy, meaning the strategy remains static after initial creation.
- **Why It Matters:** Lack of strategy reviews creates significant risk of strategy becoming outdated, misaligned with business objectives, and ineffective against evolving threats. This is a critical governance gap.

**📊 Market Context & Benchmarks:**
- **Industry Adoption Rate:** Less than 5% of mature organizations have no review process
- **Industry Benchmark:** Considered a significant security governance failure
- **Compliance Frameworks:** Fails most regulatory requirements, Does not meet ISO 27001, SOX, or other major frameworks

**🎯 Recommendations & Next Steps:**
- **If You Select This Option:** Immediately establish at minimum an annual strategy review process. Assign clear ownership, define review scope, and document review outcomes. This is a high-priority remediation item.
- **Path to Improvement:** Start with annual reviews and evolve to bi-annual or quarterly based on organizational risk profile and industry requirements.


#### Question 1.1.3

**Question:** Are cybersecurity objectives aligned with business objectives?

**Type:** multiple_choice

**Explanation:** Alignment ensures cybersecurity investments support business goals and priorities.

**Answer Options:**

**Option 1: Fully aligned**
*Basic Description:* Complete integration with business goals

**Option 2: Partially aligned**
*Basic Description:* Some alignment but gaps exist

**Option 3: Not aligned**
*Basic Description:* Security operates independently

**Option 4: Unknown**
*Basic Description:* Alignment status unclear


#### Question 1.1.4

**Question:** Who is accountable for cybersecurity strategy execution?

**Type:** multiple_choice

**Explanation:** Clear accountability ensures cybersecurity strategy has executive ownership and support.

**Answer Options:**

**Option 1: CISO**
*Basic Description:* Chief Information Security Officer

**📋 What This Option Means:**
- **Definition:** The Chief Information Security Officer has primary accountability for cybersecurity strategy execution, including resource allocation, program oversight, and performance measurement.
- **Why It Matters:** CISO accountability ensures dedicated security leadership with appropriate expertise and authority. Provides clear escalation path and executive-level security advocacy.

**📊 Market Context & Benchmarks:**
- **Industry Adoption Rate:** 78% of large organizations assign CISO accountability
- **Industry Benchmark:** Standard practice for organizations with dedicated security teams
- **Compliance Frameworks:** Aligns with NIST CSF governance requirements, Supports SOX internal control frameworks

**🎯 Recommendations & Next Steps:**
- **If You Select This Option:** Ensure CISO has sufficient authority, budget, and board access to execute strategy effectively. Define clear success metrics and reporting relationships.
- **Path to Improvement:** Consider dual accountability with business executives for strategic alignment while maintaining CISO operational accountability.

**Option 2: CIO**
*Basic Description:* Chief Information Officer

**📋 What This Option Means:**
- **Definition:** The Chief Information Officer has primary accountability for cybersecurity strategy execution, typically as part of broader IT governance responsibilities.
- **Why It Matters:** CIO accountability can provide good IT integration but may lack dedicated security focus. Risk of security being subordinated to IT operational priorities.

**📊 Market Context & Benchmarks:**
- **Industry Adoption Rate:** 35% of mid-size organizations assign CIO accountability
- **Industry Benchmark:** Common in organizations without dedicated CISO role
- **Compliance Frameworks:** May meet basic governance requirements, Could create conflicts between IT efficiency and security priorities

**🎯 Recommendations & Next Steps:**
- **If You Select This Option:** Ensure CIO has adequate security expertise or dedicated security leadership reporting to them. Define clear security performance metrics separate from IT operational metrics.
- **Path to Improvement:** Consider establishing dedicated CISO role as organization grows, or appointing Deputy CISO under CIO leadership.

**Option 3: CEO**
*Basic Description:* Chief Executive Officer

**📋 What This Option Means:**
- **Definition:** The Chief Executive Officer has direct accountability for cybersecurity strategy execution, demonstrating highest level of organizational commitment to security.
- **Why It Matters:** CEO accountability ensures maximum organizational priority and resource allocation for security. However, may lack technical expertise and day-to-day operational focus needed for effective execution.

**📊 Market Context & Benchmarks:**
- **Industry Adoption Rate:** 12% of organizations assign direct CEO accountability
- **Industry Benchmark:** More common in small organizations or highly regulated industries
- **Compliance Frameworks:** Demonstrates strong tone at the top, May exceed regulatory expectations for executive accountability

**🎯 Recommendations & Next Steps:**
- **If You Select This Option:** Ensure CEO has strong security advisory support and delegates operational execution to qualified security professionals. Maintain CEO strategic oversight while building dedicated security capabilities.
- **Path to Improvement:** Transition to dedicated CISO accountability as organization scales, while maintaining CEO strategic oversight and support.

**Option 4: Board**
*Basic Description:* Board of Directors oversight

**📋 What This Option Means:**
- **Definition:** The Board of Directors maintains direct oversight and accountability for cybersecurity strategy execution, typically through a dedicated committee or full board governance.
- **Why It Matters:** Board accountability demonstrates highest governance commitment but may lack operational effectiveness due to meeting frequency and technical expertise limitations.

**📊 Market Context & Benchmarks:**
- **Industry Adoption Rate:** 8% of organizations assign direct board accountability
- **Industry Benchmark:** Rare except in highly regulated industries or after major incidents
- **Compliance Frameworks:** Exceeds most governance requirements, May indicate response to regulatory pressure or incident

**🎯 Recommendations & Next Steps:**
- **If You Select This Option:** Establish clear delegation to executive leadership for day-to-day execution while maintaining board strategic oversight. Ensure board has adequate security expertise or advisory support.
- **Path to Improvement:** Transition to executive accountability (CEO/CISO) with regular board reporting and oversight rather than direct board execution responsibility.

**Option 5: Other**
*Basic Description:* Different role or shared responsibility

**📋 What This Option Means:**
- **Definition:** Cybersecurity strategy execution accountability is assigned to a different role (such as COO, CRO) or distributed across multiple executives without clear primary accountability.
- **Why It Matters:** Alternative accountability structures may work in specific contexts but risk unclear ownership, coordination challenges, and potential gaps in execution oversight.

**📊 Market Context & Benchmarks:**
- **Industry Adoption Rate:** 15% of organizations use alternative accountability models
- **Industry Benchmark:** Varies by industry and organizational structure
- **Compliance Frameworks:** May meet requirements if clearly defined, Risk of regulatory questions about accountability clarity

**🎯 Recommendations & Next Steps:**
- **If You Select This Option:** Clearly document accountability structure, define roles and responsibilities, and establish coordination mechanisms. Ensure primary accountability is clearly identified even in shared models.
- **Path to Improvement:** Consider consolidating accountability under single executive (CISO/CIO/CEO) for clearer ownership and more effective execution.


#### Question 1.1.5

**Question:** What is your organization's risk appetite for cybersecurity?

**Type:** multiple_choice

**Explanation:** Risk appetite defines how much cybersecurity risk the organization is willing to accept.

**Answer Options:**

**Option 1: Very low**
*Basic Description:* Minimal risk tolerance, maximum security

**Option 2: Low**
*Basic Description:* Conservative approach to risk

**Option 3: Medium**
*Basic Description:* Balanced risk and business needs

**Option 4: High**
*Basic Description:* Accept higher risk for agility

**Option 5: Very high**
*Basic Description:* Maximum risk tolerance


#### Question 1.1.6

**Question:** Are cybersecurity metrics regularly reported to executive leadership?

**Type:** yes_no

**Explanation:** Regular reporting ensures leadership visibility into cybersecurity posture and performance.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 1.1.7

**Question:** How mature is your cybersecurity governance framework?

**Type:** multiple_choice

**Explanation:** Maturity levels indicate the sophistication and effectiveness of governance processes.

**Answer Options:**

**Option 1: Ad-hoc**
*Basic Description:* Informal, reactive processes

**Option 2: Defined**
*Basic Description:* Documented processes and procedures

**Option 3: Managed**
*Basic Description:* Measured and controlled processes

**Option 4: Optimized**
*Basic Description:* Continuously improving processes



### Subsection 1.2: Policies & Standards Lifecycle

#### Question 1.2.1

**Question:** How many cybersecurity policies does your organization maintain?

**Type:** multiple_choice

**Explanation:** Policy count indicates coverage breadth - too few may miss areas, too many may be unmanageable.

**Answer Options:**

**Option 1: 0-5**
*Basic Description:* Minimal policy coverage

**Option 2: 6-15**
*Basic Description:* Basic policy framework

**Option 3: 16-30**
*Basic Description:* Comprehensive policy set

**Option 4: 30+**
*Basic Description:* Extensive policy library


#### Question 1.2.2

**Question:** How frequently are security policies reviewed?

**Type:** multiple_choice

**Explanation:** Regular reviews ensure policies remain current with threats, regulations, and business changes.

**Answer Options:**

**Option 1: Quarterly**
*Basic Description:* Every three months review cycle

**Option 2: Annually**
*Basic Description:* Once per year review

**Option 3: Bi-annually**
*Basic Description:* Twice per year review

**Option 4: As needed**
*Basic Description:* Event-driven reviews only

**Option 5: Never**
*Basic Description:* No formal review process


#### Question 1.2.3

**Question:** What is the average age of your current security policies?

**Type:** multiple_choice

**Explanation:** Older policies may not address current threats or reflect modern security practices.

**Answer Options:**

**Option 1: <1 year**
*Basic Description:* Recently created or updated

**Option 2: 1-2 years**
*Basic Description:* Moderately current policies

**Option 3: 2-3 years**
*Basic Description:* Aging policies needing review

**Option 4: 3+ years**
*Basic Description:* Outdated policies requiring updates


#### Question 1.2.4

**Question:** Do you have a formal policy approval process?

**Type:** yes_no

**Explanation:** Formal approval ensures policies have proper authority and stakeholder buy-in.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 1.2.5

**Question:** Are policies regularly communicated to all employees?

**Type:** yes_no

**Explanation:** Communication ensures employees understand their security responsibilities and requirements.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 1.2.6

**Question:** How do you track policy compliance?

**Type:** multiple_choice

**Explanation:** Compliance tracking ensures policies are being followed and identifies gaps.

**Answer Options:**

**Option 1: Automated tools**
*Basic Description:* Software-based compliance monitoring

**Option 2: Manual tracking**
*Basic Description:* Human-driven compliance checks

**Option 3: No tracking**
*Basic Description:* No compliance monitoring in place


#### Question 1.2.7

**Question:** Do you maintain policy exception processes?

**Type:** yes_no

**Explanation:** Exception processes allow controlled deviations while maintaining security oversight.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 1.3: Budget & Resource Allocation

#### Question 1.3.1

**Question:** What percentage of IT budget is allocated to cybersecurity?

**Type:** multiple_choice

**Explanation:** Industry benchmarks suggest 10-15% of IT budget should be allocated to cybersecurity.

**Answer Options:**

**Option 1: 0-4.9%**
*Basic Description:* Below industry minimum

**Option 2: 5.0-9.9%**
*Basic Description:* Basic security investment

**Option 3: 10.0-14.9%**
*Basic Description:* Industry standard allocation

**Option 4: 15.0%+**
*Basic Description:* Above average investment


#### Question 1.3.2

**Question:** How has your cybersecurity budget changed in the last year?

**Type:** multiple_choice

**Explanation:** Budget trends indicate organizational commitment to cybersecurity improvement.

**Answer Options:**

**Option 1: Increased significantly**
*Basic Description:* Major budget growth (>20%)

**Option 2: Increased slightly**
*Basic Description:* Modest budget growth (<20%)

**Option 3: Remained same**
*Basic Description:* No budget change

**Option 4: Decreased**
*Basic Description:* Budget reduction


#### Question 1.3.3

**Question:** Do you have dedicated cybersecurity staff?

**Type:** yes_no

**Explanation:** Dedicated staff ensures focused expertise and accountability for security functions.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 1.3.4

**Question:** How many FTE cybersecurity professionals do you employ?

**Type:** multiple_choice

**Explanation:** Staffing levels should align with organization size, complexity, and risk profile.

**Answer Options:**

**Option 1: 0**
*Basic Description:* No dedicated security staff

**Option 2: 1-5**
*Basic Description:* Small security team

**Option 3: 6-15**
*Basic Description:* Medium security team

**Option 4: 16-30**
*Basic Description:* Large security team

**Option 5: 30+**
*Basic Description:* Enterprise security organization


#### Question 1.3.5

**Question:** Do you use external cybersecurity services?

**Type:** yes_no

**Explanation:** External services can supplement internal capabilities and provide specialized expertise.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 1.3.6

**Question:** How do you justify cybersecurity investments?

**Type:** multiple_choice

**Explanation:** Risk-based justification ensures investments address the most critical security needs.

**Answer Options:**

**Option 1: Risk-based**
*Basic Description:* Investments based on risk analysis

**Option 2: Compliance-driven**
*Basic Description:* Investments for regulatory compliance

**Option 3: Industry benchmarks**
*Basic Description:* Investments based on peer comparison

**Option 4: Ad-hoc**
*Basic Description:* No systematic justification process



### Subsection 1.4: Metrics / KPIs / Board Reporting

#### Question 1.4.1

**Question:** Do you have established cybersecurity KPIs?

**Type:** yes_no

**Explanation:** KPIs provide measurable indicators of cybersecurity program effectiveness.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 1.4.2

**Question:** How often do you report cybersecurity metrics to the board?

**Type:** multiple_choice

**Explanation:** Regular board reporting ensures governance oversight and strategic alignment.

**Answer Options:**

**Option 1: Monthly**
*Basic Description:* Every month board reporting

**Option 2: Quarterly**
*Basic Description:* Every three months reporting

**Option 3: Annually**
*Basic Description:* Once per year reporting

**Option 4: Never**
*Basic Description:* No board reporting


#### Question 1.4.3

**Question:** Which metrics do you track?

**Type:** multiple_select

**Explanation:** Comprehensive metrics provide visibility into different aspects of security posture.

**Answer Options:**
**Option 1: Security incidents count**
*Basic Description:* Number of security incidents per period

**Option 2: Mean time to detect (MTTD)**
*Basic Description:* Average time to detect security incidents

**Option 3: Mean time to respond (MTTR)**
*Basic Description:* Average time to respond to incidents

**Option 4: Vulnerability remediation time**
*Basic Description:* Time taken to remediate vulnerabilities

**Option 5: Patch compliance rate**
*Basic Description:* Percentage of systems with current patches

**Option 6: User awareness training completion**
*Basic Description:* Training completion rates

**Option 7: Security audit findings**
*Basic Description:* Number and severity of audit findings

**Option 8: Risk assessment scores**
*Basic Description:* Overall risk posture scores



#### Question 1.4.4

**Question:** Do you benchmark your security posture against industry peers?

**Type:** yes_no

**Explanation:** Benchmarking helps identify gaps and improvement opportunities relative to industry standards.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 1.4.5

**Question:** How do you measure cybersecurity program effectiveness?

**Type:** multiple_choice

**Explanation:** Effectiveness measurement demonstrates program value and identifies improvement areas.

**Answer Options:**

**Option 1: Quantitative metrics**
*Basic Description:* Numerical data and measurements

**Option 2: Qualitative assessments**
*Basic Description:* Subjective evaluations and reviews

**Option 3: Both**
*Basic Description:* Combined quantitative and qualitative

**Option 4: Not measured**
*Basic Description:* No effectiveness measurement


#### Question 1.4.6

**Question:** Do you maintain security Key Performance Indicators (KPIs)?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Security KPIs provide measurable insights into security program effectiveness.

**Answer Options:**
**Option 1: Incident response time**
*Basic Description:* Time to detect and respond to incidents

**Option 2: Vulnerability remediation rate**
*Basic Description:* Speed of vulnerability patching

**Option 3: Security awareness metrics**
*Basic Description:* Training completion and phishing test results

**Option 4: Compliance status**
*Basic Description:* Adherence to regulatory requirements

**Option 5: Access control effectiveness**
*Basic Description:* Proper access provisioning and reviews

**Option 6: Security tool coverage**
*Basic Description:* Percentage of assets protected

**Option 7: No KPIs maintained**
*Basic Description:* KPIs not currently tracked



#### Question 1.4.7

**Question:** Do you have defined security Objectives and Key Results (OKRs)?

**Type:** yes_no

**Weight:** 1

**Explanation:** Security OKRs align security initiatives with business objectives and drive measurable outcomes.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 1.4.8

**Question:** How do you measure security program maturity?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Maturity measurement guides security program improvement and investment decisions.

**Answer Options:**
**Option 1: Maturity model framework**
*Basic Description:* Using CMMI, NIST CSF, or similar

**Option 2: Capability assessments**
*Basic Description:* Regular capability evaluations

**Option 3: Benchmark comparisons**
*Basic Description:* Comparing against industry standards

**Option 4: Audit results**
*Basic Description:* Based on internal/external audit findings

**Option 5: Self-assessment**
*Basic Description:* Internal maturity evaluations

**Option 6: Not measured**
*Basic Description:* Maturity not currently assessed



#### Question 1.4.9

**Question:** Which security metrics are reported to the board?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Board-level security metrics ensure executive visibility into security program performance.

**Answer Options:**
**Option 1: Incident statistics**
*Basic Description:* Number and severity of security incidents

**Option 2: Risk posture**
*Basic Description:* Overall organizational risk levels

**Option 3: Compliance status**
*Basic Description:* Regulatory compliance metrics

**Option 4: Security investments**
*Basic Description:* Budget and resource allocation

**Option 5: Program maturity**
*Basic Description:* Security program maturity scores

**Option 6: Vulnerability metrics**
*Basic Description:* Critical vulnerability counts and trends

**Option 7: Third-party risk**
*Basic Description:* Vendor security risk metrics

**Option 8: No board reporting**
*Basic Description:* Security metrics not reported to board




---

## Section 4: Identity & Access Management (IAM)

**Suggested Respondents:** Directory/IAM Architect

### Subsection 4.1: Directory Architecture (AD/AAD/IDaaS)

#### Question 4.1.1

**Question:** What is your primary identity provider?

**Type:** multiple_choice

**Explanation:** Identity providers centralize authentication and user management across systems.

**Answer Options:**

**Option 1: Active Directory**
*Basic Description:* Microsoft on-premises directory

**Option 2: Azure AD**
*Basic Description:* Microsoft cloud identity service

**Option 3: Okta**
*Basic Description:* Third-party identity provider

**Option 4: Auth0**
*Basic Description:* Developer-focused identity platform

**Option 5: Google Workspace**
*Basic Description:* Google cloud identity service

**Option 6: Other**
*Basic Description:* Different identity provider


#### Question 4.1.2

**Question:** How many separate identity stores do you maintain?

**Type:** multiple_choice

**Explanation:** Multiple identity stores increase complexity and security risks - consolidation is preferred.

**Answer Options:**

**Option 1: 1**
*Basic Description:* Single identity store

**Option 2: 2-3**
*Basic Description:* Few identity stores

**Option 3: 4-5**
*Basic Description:* Multiple identity stores

**Option 4: 6+**
*Basic Description:* Many identity stores


#### Question 4.1.3

**Question:** Do you have identity federation implemented?

**Type:** yes_no

**Explanation:** Federation allows secure sharing of identity information across different systems and organizations.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 4.1.4

**Question:** What percentage of applications use centralized authentication?

**Type:** multiple_choice

**Explanation:** Centralized authentication improves security and user experience while reducing management overhead.

**Answer Options:**

**Option 1: 0-25%**
*Basic Description:* Minimal centralized authentication

**Option 2: 26-50%**
*Basic Description:* Some centralized authentication

**Option 3: 51-75%**
*Basic Description:* Most applications centralized

**Option 4: 76-100%**
*Basic Description:* Nearly all applications centralized


#### Question 4.1.5

**Question:** Do you have a single sign-on (SSO) solution?

**Type:** yes_no

**Explanation:** SSO improves user experience and security by reducing password fatigue and enabling centralized access control.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 4.1.6

**Question:** How do you synchronize identities across systems?

**Type:** multiple_choice

**Explanation:** Automated synchronization ensures consistency and reduces administrative overhead and errors.

**Answer Options:**

**Option 1: Automated**
*Basic Description:* System-driven synchronization

**Option 2: Manual**
*Basic Description:* Human-driven synchronization

**Option 3: Not synchronized**
*Basic Description:* No identity synchronization


#### Question 4.1.7

**Question:** Do you have directory service redundancy?

**Type:** yes_no

**Explanation:** Directory redundancy ensures authentication availability during outages.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 4.1.8

**Question:** How do you monitor directory service health?

**Type:** multiple_select

**Explanation:** Directory monitoring ensures reliable identity services and detects security issues.

**Answer Options:**
**Option 1: Automated monitoring tools**
*Basic Description:* Using SIEM, monitoring platforms, or similar

**Option 2: Manual reviews**
*Basic Description:* Regular manual checks and reviews

**Option 3: Combination approach**
*Basic Description:* Mix of automated and manual monitoring

**Option 4: Third-party service**
*Basic Description:* Outsourced monitoring

**Option 5: Not monitored**
*Basic Description:* Not currently monitored




### Subsection 4.2: Access Control & Authorization

#### Question 4.2.1

**Question:** What access control model do you use?

**Type:** multiple_choice

**Explanation:** Access control models define how permissions are granted and managed.

**Answer Options:**

**Option 1: Role-based (RBAC)**
*Basic Description:* Permissions based on user roles

**Option 2: Attribute-based (ABAC)**
*Basic Description:* Permissions based on attributes

**Option 3: Discretionary (DAC)**
*Basic Description:* Owner-controlled permissions

**Option 4: Mandatory (MAC)**
*Basic Description:* System-enforced permissions

**Option 5: Mixed approach**
*Basic Description:* Combination of access models


#### Question 4.2.2

**Question:** Do you implement least privilege access?

**Type:** yes_no

**Explanation:** Least privilege reduces security risk by granting minimal necessary access.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 4.2.3

**Question:** How do you manage privileged accounts?

**Type:** multiple_select

**Explanation:** Privileged account management protects high-risk administrative access.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 4.2.4

**Question:** Do you use dynamic authorization?

**Type:** yes_no

**Explanation:** Dynamic authorization adapts access decisions based on context and risk.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 4.2.5

**Question:** How do you handle emergency access?

**Type:** multiple_select

**Explanation:** Emergency access procedures balance security with operational needs during crises.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 4.2.6

**Question:** Do you implement segregation of duties?

**Type:** yes_no

**Explanation:** Segregation of duties prevents single individuals from having excessive control.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 4.3: User Lifecycle Management

#### Question 4.3.1

**Question:** Do you have automated user provisioning?

**Type:** yes_no

**Explanation:** Automated provisioning ensures consistent and timely account creation.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 4.3.2

**Question:** How do you handle user onboarding?

**Type:** multiple_select

**Explanation:** Structured onboarding ensures users receive appropriate access from day one.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 4.3.3

**Question:** Do you conduct regular access reviews?

**Type:** multiple_choice

**Explanation:** Regular access reviews identify and remove unnecessary permissions.

**Answer Options:**

**Option 1: Monthly**
*Basic Description:* Every month review cycle

**Option 2: Quarterly**
*Basic Description:* Every three months review

**Option 3: Annually**
*Basic Description:* Once per year review

**Option 4: As needed**
*Basic Description:* Event-driven reviews only

**Option 5: Never**
*Basic Description:* No formal reviews


#### Question 4.3.4

**Question:** How do you handle user role changes?

**Type:** multiple_select

**Explanation:** Role change processes ensure access remains appropriate as responsibilities change.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 4.3.5

**Question:** Do you have automated user deprovisioning?

**Type:** yes_no

**Explanation:** Automated deprovisioning ensures timely access removal when users leave.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 4.3.6

**Question:** How quickly do you disable accounts for terminated users?

**Type:** multiple_choice

**Explanation:** Rapid account disabling prevents unauthorized access by former employees.

**Answer Options:**

**Option 1: Immediately**
*Basic Description:* Instant account disabling

**Option 2: Within 1 hour**
*Basic Description:* Disabled within one hour

**Option 3: Within 24 hours**
*Basic Description:* Disabled within one day

**Option 4: Within 1 week**
*Basic Description:* Disabled within one week

**Option 5: No defined timeframe**
*Basic Description:* No specific timeline


#### Question 4.3.7

**Question:** Do you track orphaned accounts?

**Type:** yes_no

**Explanation:** Orphaned account tracking identifies accounts that should be disabled or removed.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 4.4: Multi-Factor Authentication

#### Question 4.4.1

**Question:** Do you require multi-factor authentication (MFA)?

**Type:** yes_no

**Explanation:** MFA significantly reduces the risk of account compromise from stolen credentials.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 4.4.2

**Question:** What MFA methods do you support?

**Type:** multiple_select

**Explanation:** Multiple MFA methods provide flexibility while maintaining security.

**Answer Options:**
**Option 1: SMS/Text message**
*Basic Description:* One-time codes via SMS

**Option 2: Authenticator app**
*Basic Description:* TOTP-based authenticator apps

**Option 3: Hardware token**
*Basic Description:* Physical security keys like YubiKey

**Option 4: Biometric**
*Basic Description:* Fingerprint or facial recognition

**Option 5: Push notification**
*Basic Description:* Mobile app push approvals

**Option 6: Not implemented**
*Basic Description:* MFA not currently implemented



#### Question 4.4.3

**Question:** What percentage of users have MFA enabled?

**Type:** multiple_choice

**Explanation:** High MFA adoption rates improve overall security posture.

**Answer Options:**

**Option 1: 0-25%**
*Basic Description:* Minimal MFA adoption

**Option 2: 26-50%**
*Basic Description:* Some MFA adoption

**Option 3: 51-75%**
*Basic Description:* Most users have MFA

**Option 4: 76-100%**
*Basic Description:* Nearly all users have MFA


#### Question 4.4.4

**Question:** Do you have conditional access policies?

**Type:** yes_no

**Explanation:** Conditional access adapts authentication requirements based on risk factors.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 4.4.5

**Question:** How do you handle MFA bypass requests?

**Type:** multiple_select

**Explanation:** MFA bypass procedures should balance security with operational needs.

**Answer Options:**
**Option 1: SMS/Text message**
*Basic Description:* One-time codes via SMS

**Option 2: Authenticator app**
*Basic Description:* TOTP-based authenticator apps

**Option 3: Hardware token**
*Basic Description:* Physical security keys like YubiKey

**Option 4: Biometric**
*Basic Description:* Fingerprint or facial recognition

**Option 5: Push notification**
*Basic Description:* Mobile app push approvals

**Option 6: Not implemented**
*Basic Description:* MFA not currently implemented




---

## Section 2: Risk Management

**Suggested Respondents:** Enterprise Risk Manager, Compliance Lead

### Subsection 2.1: Risk Assessment & Analysis

#### Question 2.1.1

**Question:** How frequently does your organization conduct cybersecurity risk assessments?

**Type:** multiple_choice

**Explanation:** Regular risk assessments help identify and prioritize cybersecurity threats and vulnerabilities.

**Answer Options:**

**Option 1:** Monthly

**Option 2:** Quarterly

**Option 3:** Annually

**Option 4:** Bi-annually

**Option 5:** As needed

**Option 6:** Never


#### Question 2.1.2

**Question:** Do you have a formal risk management framework in place?

**Type:** yes_no

**Explanation:** A formal framework provides structure and consistency for risk management activities.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 2.1.3

**Question:** What methodology do you use for risk assessment?

**Type:** multiple_choice

**Explanation:** Standardized methodologies ensure comprehensive and consistent risk assessments.

**Answer Options:**

**Option 1: NIST**
*Basic Description:* NIST Risk Management Framework

**Option 2: ISO 27001**
*Basic Description:* ISO 27001 risk management

**Option 3: FAIR**
*Basic Description:* Factor Analysis of Information Risk

**Option 4: Custom**
*Basic Description:* Organization-specific methodology

**Option 5: None**
*Basic Description:* No formal methodology


#### Question 2.1.4

**Question:** Do you maintain a risk register or inventory?

**Type:** yes_no

**Explanation:** A risk register provides centralized tracking and management of identified risks.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 2.1.5

**Question:** How do you prioritize cybersecurity risks?

**Type:** multiple_choice

**Explanation:** Risk prioritization ensures resources are allocated to the most critical threats first.

**Answer Options:**

**Option 1: Impact x Likelihood**
*Basic Description:* Risk matrix approach

**Option 2: Business criticality**
*Basic Description:* Based on business importance

**Option 3: Regulatory requirements**
*Basic Description:* Compliance-driven prioritization

**Option 4: Ad-hoc**
*Basic Description:* No systematic approach

**Option 5: Not prioritized**
*Basic Description:* No risk prioritization


#### Question 2.1.6

**Question:** Do you conduct threat modeling exercises?

**Type:** yes_no

**Explanation:** Threat modeling helps identify potential attack vectors and security weaknesses.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 2.1.7

**Question:** How often do you update your risk assessments?

**Type:** multiple_choice

**Explanation:** Regular updates ensure risk assessments reflect current threat landscape and business changes.

**Answer Options:**

**Option 1: Continuously**
*Basic Description:* Ongoing risk assessment updates

**Option 2: Quarterly**
*Basic Description:* Every three months updates

**Option 3: Annually**
*Basic Description:* Once per year updates

**Option 4: When incidents occur**
*Basic Description:* Event-driven updates only

**Option 5: Never**
*Basic Description:* No risk assessment updates



### Subsection 2.2: Risk Treatment & Mitigation

#### Question 2.2.1

**Question:** What risk treatment strategies does your organization employ?

**Type:** multiple_select

**Explanation:** Multiple treatment strategies provide flexibility in addressing different types of risks.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 2.2.2

**Question:** Do you have defined risk tolerance levels?

**Type:** yes_no

**Explanation:** Risk tolerance levels guide decision-making about which risks to accept or mitigate.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 2.2.3

**Question:** How do you track risk mitigation progress?

**Type:** multiple_choice

**Explanation:** Progress tracking ensures risk mitigation efforts are effective and timely.

**Answer Options:**

**Option 1: Automated tools**
*Basic Description:* Software-based progress tracking

**Option 2: Manual tracking**
*Basic Description:* Human-driven progress monitoring

**Option 3: Periodic reviews**
*Basic Description:* Regular review meetings

**Option 4: Not tracked**
*Basic Description:* No progress tracking


#### Question 2.2.4

**Question:** Do you have cybersecurity insurance?

**Type:** yes_no

**Explanation:** Cybersecurity insurance provides financial protection against cyber incidents.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 2.2.5

**Question:** What is your organization's risk appetite statement?

**Type:** multiple_choice

**Explanation:** A clear risk appetite statement guides consistent risk decision-making across the organization.

**Answer Options:**

**Option 1: Formally documented**
*Basic Description:* Written risk appetite statement

**Option 2: Informally understood**
*Basic Description:* Unwritten but understood

**Option 3: Under development**
*Basic Description:* Currently being created

**Option 4: Not defined**
*Basic Description:* No risk appetite defined


#### Question 2.2.6

**Question:** How do you communicate risks to stakeholders?

**Type:** multiple_choice

**Explanation:** Effective risk communication ensures stakeholders can make informed decisions.

**Answer Options:**

**Option 1: Regular reports**
*Basic Description:* Scheduled risk reporting

**Option 2: Dashboard/metrics**
*Basic Description:* Visual risk dashboards

**Option 3: Ad-hoc briefings**
*Basic Description:* As-needed risk communication

**Option 4: Not communicated**
*Basic Description:* No risk communication



### Subsection 2.3: Business Impact Analysis

#### Question 2.3.1

**Question:** Have you conducted a business impact analysis (BIA)?

**Type:** yes_no

**Explanation:** BIA identifies critical business processes and their dependencies for risk prioritization.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 2.3.2

**Question:** How do you classify business processes by criticality?

**Type:** multiple_choice

**Explanation:** Process classification helps prioritize protection efforts and resource allocation.

**Answer Options:**

**Option 1: Critical/High/Medium/Low**
*Basic Description:* Four-tier criticality levels

**Option 2: Tier 1/2/3**
*Basic Description:* Three-tier classification system

**Option 3: Custom classification**
*Basic Description:* Organization-specific classification

**Option 4: Not classified**
*Basic Description:* No process classification


#### Question 2.3.3

**Question:** Do you have defined Recovery Time Objectives (RTO)?

**Type:** yes_no

**Explanation:** RTOs define acceptable downtime for business processes and guide recovery planning.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 2.3.4

**Question:** Do you have defined Recovery Point Objectives (RPO)?

**Type:** yes_no

**Explanation:** RPOs define acceptable data loss and guide backup and recovery strategies.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 2.3.5

**Question:** How often do you update your business impact analysis?

**Type:** multiple_choice

**Explanation:** Regular updates ensure BIA reflects current business operations and dependencies.

**Answer Options:**

**Option 1: Annually**
*Basic Description:* Once per year updates

**Option 2: Bi-annually**
*Basic Description:* Twice per year updates

**Option 3: When business changes**
*Basic Description:* Event-driven updates only

**Option 4: Never updated**
*Basic Description:* No BIA updates


#### Question 2.3.6

**Question:** Do you quantify financial impact of potential cyber incidents?

**Type:** yes_no

**Explanation:** Financial quantification helps justify security investments and insurance decisions.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



---

## Section 3: Asset Management

**Suggested Respondents:** ITAM Lead, Infrastructure Manager

### Subsection 3.1: Asset Inventory & Classification

#### Question 3.1.1

**Question:** Do you maintain a comprehensive IT asset inventory?

**Type:** yes_no

**Explanation:** Asset inventory is fundamental for security management and risk assessment.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 3.1.2

**Question:** What percentage of your IT assets are inventoried?

**Type:** multiple_choice

**Explanation:** High inventory coverage is essential for effective security management.

**Answer Options:**

**Option 1:** 90-100%

**Option 2:** 75-89%

**Option 3:** 50-74%

**Option 4:** 25-49%

**Option 5:** 0-24%


#### Question 3.1.3

**Question:** How do you discover and track new assets?

**Type:** multiple_choice

**Explanation:** Automated discovery helps maintain accurate and up-to-date asset inventories.

**Answer Options:**

**Option 1:** Automated discovery

**Option 2:** Manual registration

**Option 3:** Network scanning

**Option 4:** Combination

**Option 5:** No process


#### Question 3.1.4

**Question:** Do you classify assets by criticality or sensitivity?

**Type:** yes_no

**Explanation:** Asset classification enables risk-based security controls and resource allocation.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 3.1.5

**Question:** What asset types do you track?

**Type:** multiple_select

**Explanation:** Comprehensive asset tracking covers all technology components that could pose security risks.

**Answer Options:**
**Option 1: Type A**
*Basic Description:* Primary implementation type

**Option 2: Type B**
*Basic Description:* Secondary implementation type

**Option 3: Type C**
*Basic Description:* Alternative implementation type

**Option 4: Hybrid**
*Basic Description:* Combination of multiple types

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 3.1.6

**Question:** How often do you update your asset inventory?

**Type:** multiple_choice

**Explanation:** Frequent updates ensure inventory accuracy in dynamic IT environments.

**Answer Options:**

**Option 1:** Real-time

**Option 2:** Daily

**Option 3:** Weekly

**Option 4:** Monthly

**Option 5:** Quarterly

**Option 6:** Annually


#### Question 3.1.7

**Question:** Do you track asset ownership and accountability?

**Type:** yes_no

**Explanation:** Clear ownership ensures accountability for asset security and maintenance.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 3.2: Asset Lifecycle Management

#### Question 3.2.1

**Question:** Do you have formal asset lifecycle management processes?

**Type:** yes_no

**Explanation:** Lifecycle management ensures security controls are maintained throughout asset lifespan.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 3.2.2

**Question:** How do you handle asset procurement security requirements?

**Type:** multiple_choice

**Explanation:** Security requirements during procurement prevent introduction of vulnerable assets.

**Answer Options:**

**Option 1: Security review required**
*Basic Description:* Mandatory security review process

**Option 2: Standard security specs**
*Basic Description:* Predefined security specifications

**Option 3: Vendor security assessment**
*Basic Description:* Vendor security evaluation

**Option 4: No requirements**
*Basic Description:* No security requirements


#### Question 3.2.3

**Question:** Do you have secure asset disposal procedures?

**Type:** yes_no

**Explanation:** Secure disposal prevents data breaches and ensures compliance with data protection regulations.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 3.2.4

**Question:** How do you handle end-of-life assets?

**Type:** multiple_choice

**Explanation:** Proper end-of-life handling prevents data exposure and ensures regulatory compliance.

**Answer Options:**

**Option 1:** Data wiping

**Option 2:** Physical destruction

**Option 3:** Certified disposal

**Option 4:** Return to vendor

**Option 5:** No formal process


#### Question 3.2.5

**Question:** Do you track asset warranty and support status?

**Type:** yes_no

**Explanation:** Tracking support status helps identify assets that may lack security updates.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 3.2.6

**Question:** How do you manage asset configuration changes?

**Type:** multiple_choice

**Explanation:** Configuration management prevents unauthorized changes that could introduce vulnerabilities.

**Answer Options:**

**Option 1: Change management process**
*Basic Description:* Formal change control procedures

**Option 2: Automated configuration**
*Basic Description:* System-driven configuration management

**Option 3: Manual tracking**
*Basic Description:* Human-driven change tracking

**Option 4: No formal process**
*Basic Description:* No configuration management



### Subsection 3.3: Data Classification & Handling

#### Question 3.3.1

**Question:** Do you have a data classification scheme?

**Type:** yes_no

**Explanation:** Data classification enables appropriate protection controls based on sensitivity.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 3.3.2

**Question:** What data classification levels do you use?

**Type:** multiple_choice

**Explanation:** Clear classification levels help users understand appropriate handling requirements.

**Answer Options:**

**Option 1: Public/Internal/Confidential/Restricted**
*Basic Description:* Four-tier data classification

**Option 2: High/Medium/Low**
*Basic Description:* Three-tier classification system

**Option 3: Custom scheme**
*Basic Description:* Organization-specific classification

**Option 4: No classification**
*Basic Description:* No data classification


#### Question 3.3.3

**Question:** Do you label data according to its classification?

**Type:** yes_no

**Explanation:** Data labeling helps users identify and apply appropriate protection measures.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 3.3.4

**Question:** How do you enforce data handling requirements?

**Type:** multiple_choice

**Explanation:** Enforcement mechanisms ensure data classification translates to actual protection.

**Answer Options:**

**Option 1:** Technical controls

**Option 2:** Policy enforcement

**Option 3:** Training

**Option 4:** Combination

**Option 5:** Not enforced


#### Question 3.3.5

**Question:** Do you track data location and movement?

**Type:** yes_no

**Explanation:** Data tracking helps ensure compliance with regulations and internal policies.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 3.3.6

**Question:** How do you handle data retention and disposal?

**Type:** multiple_choice

**Explanation:** Proper retention and disposal reduce data exposure risks and ensure compliance.

**Answer Options:**

**Option 1: Automated policies**
*Basic Description:* System-driven retention and disposal

**Option 2: Manual processes**
*Basic Description:* Human-driven data management

**Option 3: Legal hold procedures**
*Basic Description:* Legal compliance procedures

**Option 4: No formal process**
*Basic Description:* No retention/disposal process



---

## Section 5: Network Security

**Suggested Respondents:** Network Security Engineer

### Subsection 5.1: Network Architecture & Segmentation

#### Question 5.1.1

**Question:** Do you implement network segmentation?

**Type:** yes_no

**Explanation:** Network segmentation limits the spread of attacks and reduces blast radius.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 5.1.2

**Question:** What type of network segmentation do you use?

**Type:** multiple_select

**Explanation:** Multiple segmentation techniques provide defense in depth.

**Answer Options:**
**Option 1: Physical segmentation**
*Basic Description:* Separate physical networks

**Option 2: Virtual segmentation (VLANs)**
*Basic Description:* Virtual LANs

**Option 3: Software-defined networking (SDN)**
*Basic Description:* SDN-based segmentation

**Option 4: Micro-segmentation**
*Basic Description:* Granular workload-level segmentation

**Option 5: No segmentation**
*Basic Description:* No network segmentation implemented



#### Question 5.1.3

**Question:** Do you have a DMZ (demilitarized zone)?

**Type:** yes_no

**Explanation:** DMZ provides additional protection for public-facing services.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 5.1.4

**Question:** How do you control network access between segments?

**Type:** multiple_choice

**Explanation:** Access controls between segments prevent lateral movement of attackers.

**Answer Options:**

**Option 1: Firewalls**
*Basic Description:* Firewall-based access control

**Option 2: Access control lists**
*Basic Description:* ACL-based access control

**Option 3: Zero trust model**
*Basic Description:* Zero trust network architecture

**Option 4: No controls**
*Basic Description:* No network access controls


#### Question 5.1.5

**Question:** Do you implement zero trust network principles?

**Type:** multiple_choice

**Explanation:** Zero trust assumes no implicit trust and verifies every transaction.

**Answer Options:**

**Option 1: Fully implemented**
*Basic Description:* Complete zero trust implementation

**Option 2: Partially implemented**
*Basic Description:* Some zero trust principles

**Option 3: Planning**
*Basic Description:* Zero trust implementation planned

**Option 4: Not implemented**
*Basic Description:* No zero trust implementation


#### Question 5.1.6

**Question:** How do you secure wireless networks?

**Type:** multiple_select

**Explanation:** Wireless security prevents unauthorized network access and data interception.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 5.1.7

**Question:** Do you have network documentation and diagrams?

**Type:** yes_no

**Explanation:** Network documentation is essential for security planning and incident response.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 5.2: Firewall & Perimeter Security

#### Question 5.2.1

**Question:** What types of firewalls do you deploy?

**Type:** multiple_select

**Explanation:** Multiple firewall types provide layered protection at different network levels.

**Answer Options:**
**Option 1: Next-generation firewall (NGFW)**
*Basic Description:* Advanced firewall with IPS/IDS

**Option 2: Traditional firewall**
*Basic Description:* Standard packet filtering firewall

**Option 3: Web application firewall (WAF)**
*Basic Description:* Application-layer firewall

**Option 4: Cloud firewall**
*Basic Description:* Cloud-native firewall service

**Option 5: Not deployed**
*Basic Description:* No firewall deployed



#### Question 5.2.2

**Question:** How often do you review firewall rules?

**Type:** multiple_choice

**Explanation:** Regular rule reviews prevent rule creep and maintain security effectiveness.

**Answer Options:**

**Option 1: Weekly**
*Basic Description:* Every week review cycle

**Option 2: Monthly**
*Basic Description:* Every month review cycle

**Option 3: Quarterly**
*Basic Description:* Every three months review

**Option 4: Annually**
*Basic Description:* Once per year review

**Option 5: As needed**
*Basic Description:* Event-driven reviews only

**Option 6: Never**
*Basic Description:* No formal reviews


#### Question 5.2.3

**Question:** Do you implement default deny policies?

**Type:** yes_no

**Explanation:** Default deny ensures only explicitly allowed traffic is permitted.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 5.2.4

**Question:** Do you have intrusion detection/prevention systems (IDS/IPS)?

**Type:** multiple_choice

**Explanation:** IDS/IPS systems detect and prevent malicious network activity.

**Answer Options:**

**Option 1:** Both IDS and IPS

**Option 2:** IDS only

**Option 3:** IPS only

**Option 4:** Neither


#### Question 5.2.5

**Question:** How do you handle firewall change management?

**Type:** multiple_choice

**Explanation:** Change management prevents unauthorized modifications and maintains security.

**Answer Options:**

**Option 1:** Formal change process

**Option 2:** Automated deployment

**Option 3:** Manual changes

**Option 4:** No process


#### Question 5.2.6

**Question:** Do you monitor firewall logs?

**Type:** yes_no

**Explanation:** Log monitoring helps detect attacks and troubleshoot connectivity issues.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 5.2.7

**Question:** Do you perform firewall penetration testing?

**Type:** multiple_choice

**Explanation:** Penetration testing validates firewall effectiveness against real-world attacks.

**Answer Options:**

**Option 1:** Annually

**Option 2:** Bi-annually

**Option 3:** After major changes

**Option 4:** Never



### Subsection 5.3: Network Monitoring & Detection

#### Question 5.3.1

**Question:** Do you have network traffic monitoring capabilities?

**Type:** yes_no

**Explanation:** Traffic monitoring helps detect anomalies and potential security incidents.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 5.3.2

**Question:** What network monitoring tools do you use?

**Type:** multiple_select

**Explanation:** Multiple monitoring tools provide comprehensive visibility into network activity.

**Answer Options:**
**Option 1: Commercial solution**
*Basic Description:* Vendor-provided commercial product

**Option 2: Open-source solution**
*Basic Description:* Open-source tools and platforms

**Option 3: Custom-built solution**
*Basic Description:* Internally developed solution

**Option 4: Managed service**
*Basic Description:* Third-party managed service

**Option 5: Not deployed**
*Basic Description:* Not currently deployed



#### Question 5.3.3

**Question:** Do you monitor for lateral movement?

**Type:** yes_no

**Explanation:** Lateral movement detection helps identify compromised systems spreading through the network.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 5.3.4

**Question:** How do you detect network anomalies?

**Type:** multiple_choice

**Explanation:** Anomaly detection helps identify previously unknown threats and attack patterns.

**Answer Options:**

**Option 1:** Machine learning

**Option 2:** Signature-based

**Option 3:** Behavioral analysis

**Option 4:** Manual review

**Option 5:** No detection


#### Question 5.3.5

**Question:** Do you have network forensics capabilities?

**Type:** yes_no

**Explanation:** Network forensics enables investigation of security incidents and attack reconstruction.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 5.3.6

**Question:** How long do you retain network logs?

**Type:** multiple_choice

**Explanation:** Log retention enables historical analysis and compliance with regulatory requirements.

**Answer Options:**

**Option 1:** 30 days

**Option 2:** 90 days

**Option 3:** 6 months

**Option 4:** 1 year

**Option 5:** > 1 year

**Option 6:** Not retained



### Subsection 5.4: Remote Access & VPN

#### Question 5.4.1

**Question:** What remote access solutions do you provide?

**Type:** multiple_select

**Explanation:** Secure remote access is essential for modern distributed workforces.

**Answer Options:**
**Option 1: Commercial solution**
*Basic Description:* Vendor-provided commercial product

**Option 2: Open-source solution**
*Basic Description:* Open-source tools and platforms

**Option 3: Custom-built solution**
*Basic Description:* Internally developed solution

**Option 4: Managed service**
*Basic Description:* Third-party managed service

**Option 5: Not deployed**
*Basic Description:* Not currently deployed



#### Question 5.4.2

**Question:** Do you require multi-factor authentication for remote access?

**Type:** yes_no

**Explanation:** MFA significantly reduces the risk of unauthorized remote access.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 5.4.3

**Question:** What VPN protocols do you support?

**Type:** multiple_select

**Explanation:** Modern VPN protocols provide better security and performance than legacy options.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 5.4.4

**Question:** Do you implement split tunneling policies?

**Type:** multiple_choice

**Explanation:** Split tunneling policies balance security with performance and user experience.

**Answer Options:**

**Option 1:** Prohibited

**Option 2:** Allowed with restrictions

**Option 3:** Fully allowed

**Option 4:** Not configured


#### Question 5.4.5

**Question:** How do you monitor remote access sessions?

**Type:** multiple_choice

**Explanation:** Remote access monitoring helps detect unauthorized usage and security incidents.

**Answer Options:**

**Option 1:** Real-time monitoring

**Option 2:** Log analysis

**Option 3:** Periodic reviews

**Option 4:** Not monitored


#### Question 5.4.6

**Question:** Do you have device compliance requirements for remote access?

**Type:** yes_no

**Explanation:** Device compliance ensures remote devices meet security standards before network access.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



---

## Section 6: Endpoint Security

**Suggested Respondents:** Endpoint Engineering Lead

### Subsection 6.1: Endpoint Protection & Management

#### Question 6.1.1

**Question:** What endpoint protection solutions do you deploy?

**Type:** multiple_select

**Explanation:** Multiple endpoint protection layers provide comprehensive defense against various threats.

**Answer Options:**
**Option 1: Commercial solution**
*Basic Description:* Vendor-provided commercial product

**Option 2: Open-source solution**
*Basic Description:* Open-source tools and platforms

**Option 3: Custom-built solution**
*Basic Description:* Internally developed solution

**Option 4: Managed service**
*Basic Description:* Third-party managed service

**Option 5: Not deployed**
*Basic Description:* Not currently deployed



#### Question 6.1.2

**Question:** Do you have centralized endpoint management?

**Type:** yes_no

**Explanation:** Centralized management enables consistent policy enforcement and monitoring across all endpoints.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 6.1.3

**Question:** How do you manage endpoint configurations?

**Type:** multiple_choice

**Explanation:** Automated configuration management ensures consistent security settings across endpoints.

**Answer Options:**

**Option 1: Group Policy**
*Basic Description:* Microsoft Active Directory centralized configuration management

**Option 2: MDM/EMM**
*Basic Description:* Mobile Device Management/Enterprise Mobility Management

**Option 3: Configuration management tools**
*Basic Description:* Automated tools like Ansible, Puppet, Chef

**Option 4:** Manual configuration

**Option 5:** No management


#### Question 6.1.4

**Question:** Do you implement application whitelisting/allowlisting?

**Type:** yes_no

**Explanation:** Application control prevents execution of unauthorized or malicious software.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 6.1.5

**Question:** How often do you update endpoint protection signatures?

**Type:** multiple_choice

**Explanation:** Frequent signature updates ensure protection against the latest threats.

**Answer Options:**

**Option 1:** Real-time

**Option 2:** Hourly

**Option 3:** Daily

**Option 4:** Weekly

**Option 5:** Manual updates


#### Question 6.1.6

**Question:** Do you monitor endpoint security events?

**Type:** yes_no

**Explanation:** Event monitoring enables rapid detection and response to security incidents.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 6.1.7

**Question:** What percentage of endpoints have security agents installed?

**Type:** multiple_choice

**Explanation:** High coverage ensures comprehensive endpoint protection across the organization.

**Answer Options:**

**Option 1:** 90-100%

**Option 2:** 75-89%

**Option 3:** 50-74%

**Option 4:** 25-49%

**Option 5:** 0-24%



### Subsection 6.2: Mobile Device Security

#### Question 6.2.1

**Question:** Do you have a mobile device management (MDM) solution?

**Type:** yes_no

**Explanation:** MDM solutions provide centralized management and security for mobile devices.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 6.2.2

**Question:** What mobile device policies do you enforce?

**Type:** multiple_select

**Explanation:** Mobile policies protect corporate data on personal and company devices.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 6.2.3

**Question:** How do you handle BYOD (Bring Your Own Device)?

**Type:** multiple_choice

**Explanation:** BYOD policies balance user convenience with security requirements.

**Answer Options:**

**Option 1:** Full MDM enrollment

**Option 2:** App wrapping/containerization

**Option 3:** VPN-only access

**Option 4:** Not allowed

**Option 5:** No controls


#### Question 6.2.4

**Question:** Do you separate personal and corporate data on mobile devices?

**Type:** yes_no

**Explanation:** Data separation protects corporate information while preserving user privacy.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 6.2.5

**Question:** How do you manage mobile app installations?

**Type:** multiple_choice

**Explanation:** App management prevents installation of malicious or unauthorized applications.

**Answer Options:**

**Option 1:** App store restrictions

**Option 2:** Corporate app catalog

**Option 3:** Sideloading blocked

**Option 4:** No restrictions


#### Question 6.2.6

**Question:** Do you monitor mobile device compliance?

**Type:** yes_no

**Explanation:** Compliance monitoring ensures devices meet security requirements before accessing corporate resources.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 6.3: Endpoint Configuration Management

#### Question 6.3.1

**Question:** Do you have standardized endpoint configurations?

**Type:** yes_no

**Weight:** 3

**Explanation:** Standardized configurations reduce security risks and improve management efficiency.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 6.3.2

**Question:** How do you enforce endpoint configuration compliance?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** Configuration enforcement ensures endpoints maintain security standards.

**Answer Options:**

**Option 1: Group Policy**
*Basic Description:* Microsoft Active Directory centralized configuration management

**Option 2: Configuration management tools**
*Basic Description:* Automated tools like Ansible, Puppet, Chef

**Option 3:** Manual checks

**Option 4:** No enforcement


#### Question 6.3.3

**Question:** Do you monitor endpoint configuration drift?

**Type:** yes_no

**Weight:** 3

**Explanation:** Configuration drift monitoring helps maintain security baselines over time.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 6.3.4

**Question:** How often do you review endpoint security configurations?

**Type:** multiple_choice

**Weight:** 1

**Explanation:** Regular configuration reviews ensure ongoing security effectiveness.

**Answer Options:**

**Option 1:** Weekly

**Option 2:** Monthly

**Option 3:** Quarterly

**Option 4:** Annually

**Option 5:** As needed

**Option 6:** Never



---

## Section 7: Data Protection & Privacy

**Suggested Respondents:** DLP Owner, Data Protection Officer

### Subsection 7.1: Data Encryption & Protection

#### Question 7.1.1

**Question:** Do you encrypt data at rest?

**Type:** yes_no

**Explanation:** Data encryption at rest protects against unauthorized access to stored information.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 7.1.2

**Question:** Do you encrypt data in transit?

**Type:** yes_no

**Explanation:** Data encryption in transit protects against interception during transmission.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 7.1.3

**Question:** What encryption standards do you use?

**Type:** multiple_select

**Explanation:** Strong encryption standards provide robust protection for sensitive data.

**Answer Options:**
**Option 1: AES-256**
*Basic Description:* Advanced Encryption Standard 256-bit

**Option 2: AES-128**
*Basic Description:* Advanced Encryption Standard 128-bit

**Option 3: RSA**
*Basic Description:* RSA encryption

**Option 4: Other encryption**
*Basic Description:* Other encryption methods

**Option 5: Not encrypted**
*Basic Description:* Data not encrypted



#### Question 7.1.4

**Question:** How do you manage encryption keys?

**Type:** multiple_choice

**Explanation:** Proper key management is essential for maintaining encryption security.

**Answer Options:**

**Option 1:** Hardware Security Module (HSM)

**Option 2:** Key Management Service (KMS)

**Option 3:** Software-based

**Option 4:** Manual management

**Option 5:** No key management


#### Question 7.1.5

**Question:** Do you implement data loss prevention (DLP) controls?

**Type:** yes_no

**Explanation:** DLP controls prevent unauthorized data exfiltration and ensure compliance.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 7.1.6

**Question:** How do you protect data on mobile devices?

**Type:** multiple_select

**Explanation:** Mobile data protection prevents loss of sensitive information on portable devices.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 7.1.7

**Question:** Do you use database encryption?

**Type:** multiple_choice

**Explanation:** Database encryption protects sensitive information stored in database systems.

**Answer Options:**

**Option 1:** Transparent Data Encryption (TDE)

**Option 2:** Column-level encryption

**Option 3:** Application-level encryption

**Option 4:** No database encryption



### Subsection 7.2: Privacy & Compliance

#### Question 7.2.1

**Question:** Which privacy regulations apply to your organization?

**Type:** multiple_select

**Explanation:** Understanding applicable regulations is essential for compliance planning.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Option 5**
*Basic Description:* Fifth option

**Option 6: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 7.2.2

**Question:** Do you have a privacy policy?

**Type:** yes_no

**Explanation:** Privacy policies inform users about data collection and processing practices.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 7.2.3

**Question:** Do you conduct privacy impact assessments (PIAs)?

**Type:** yes_no

**Explanation:** PIAs help identify and mitigate privacy risks in new projects and systems.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 7.2.4

**Question:** How do you handle data subject requests?

**Type:** multiple_choice

**Explanation:** Efficient handling of data subject requests ensures compliance with privacy regulations.

**Answer Options:**

**Option 1:** Automated system

**Option 2:** Manual process

**Option 3:** Third-party service

**Option 4:** No formal process


#### Question 7.2.5

**Question:** Do you have a Data Protection Officer (DPO)?

**Type:** yes_no

**Explanation:** DPOs provide expertise and oversight for privacy compliance programs.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 7.2.6

**Question:** How do you obtain consent for data processing?

**Type:** multiple_choice

**Explanation:** Proper consent mechanisms ensure lawful processing of personal data.

**Answer Options:**

**Option 1:** Explicit consent

**Option 2:** Opt-in

**Option 3:** Opt-out

**Option 4:** Implied consent

**Option 5:** No consent mechanism



### Subsection 7.3: Data Backup & Recovery

#### Question 7.3.1

**Question:** Do you have a data backup strategy?

**Type:** yes_no

**Explanation:** Backup strategies ensure data availability and business continuity.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 7.3.2

**Question:** How frequently do you backup critical data?

**Type:** multiple_choice

**Explanation:** Frequent backups minimize data loss in case of incidents.

**Answer Options:**

**Option 1:** Real-time

**Option 2:** Hourly

**Option 3:** Daily

**Option 4:** Weekly

**Option 5:** Monthly


#### Question 7.3.3

**Question:** Where do you store backup data?

**Type:** multiple_select

**Explanation:** Multiple backup locations protect against site-specific disasters.

**Answer Options:**
**Option 1: Daily**
*Basic Description:* Daily backup schedule

**Option 2: Weekly**
*Basic Description:* Weekly backup schedule

**Option 3: Monthly**
*Basic Description:* Monthly backup schedule

**Option 4: Real-time/Continuous**
*Basic Description:* Continuous data protection

**Option 5: No regular backups**
*Basic Description:* Backups not performed regularly



#### Question 7.3.4

**Question:** Do you test backup restoration procedures?

**Type:** multiple_choice

**Explanation:** Regular testing ensures backups can be successfully restored when needed.

**Answer Options:**

**Option 1:** Monthly

**Option 2:** Quarterly

**Option 3:** Annually

**Option 4:** Never


#### Question 7.3.5

**Question:** Are your backups encrypted?

**Type:** yes_no

**Explanation:** Backup encryption protects data confidentiality during storage and transmission.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 7.3.6

**Question:** What is your target Recovery Point Objective (RPO)?

**Type:** multiple_choice

**Explanation:** RPO defines acceptable data loss and guides backup frequency decisions.

**Answer Options:**

**Option 1:** < 1 hour

**Option 2:** 1-4 hours

**Option 3:** 4-24 hours

**Option 4:** > 24 hours

**Option 5:** Not defined



### Subsection 7.4: Data Governance & Subject Rights

#### Question 7.4.1

**Question:** Do you have data discovery and lineage capabilities?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** Data discovery and lineage support compliance and risk management.

**Answer Options:**

**Option 1:** Automated discovery

**Option 2:** Manual mapping

**Option 3:** Partial capabilities

**Option 4:** No capabilities


#### Question 7.4.2

**Question:** How do you handle data subject access requests (DSAR)?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Efficient DSAR handling ensures compliance with privacy regulations.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 7.4.3

**Question:** Do you conduct Data Protection Impact Assessments (DPIA)?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** DPIAs identify and mitigate privacy risks in data processing activities.

**Answer Options:**

**Option 1:** For all high-risk processing

**Option 2:** For new systems only

**Option 3:** Occasionally

**Option 4:** Never


#### Question 7.4.4

**Question:** How do you manage cross-border data transfers?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Proper transfer mechanisms ensure lawful international data transfers.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 7.4.5

**Question:** Do you maintain consent management capabilities?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Consent management ensures lawful processing and user control over personal data.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization




---

## Section 8: Application Security

**Suggested Respondents:** DevSecOps Lead, Application Security Architect

### Subsection 8.1: Secure Development Lifecycle

#### Question 8.1.1

**Question:** Do you have a secure software development lifecycle (SDLC)?

**Type:** yes_no

**Explanation:** Secure SDLC integrates security practices throughout the development process.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.1.2

**Question:** Do you conduct security code reviews?

**Type:** multiple_choice

**Explanation:** Code reviews help identify security vulnerabilities before deployment.

**Answer Options:**

**Option 1:** Always

**Option 2:** For critical applications

**Option 3:** Occasionally

**Option 4:** Never


#### Question 8.1.3

**Question:** What static application security testing (SAST) tools do you use?

**Type:** multiple_select

**Explanation:** SAST tools automatically identify security vulnerabilities in source code.

**Answer Options:**
**Option 1: Commercial SAST tool**
*Basic Description:* Vendor SAST solution

**Option 2: Open-source SAST tool**
*Basic Description:* Open-source static analysis

**Option 3: IDE-integrated analysis**
*Basic Description:* Built into development environment

**Option 4: Manual code review**
*Basic Description:* Manual security code review

**Option 5: Not performed**
*Basic Description:* SAST not performed



#### Question 8.1.4

**Question:** Do you perform dynamic application security testing (DAST)?

**Type:** yes_no

**Explanation:** DAST identifies vulnerabilities in running applications through external testing.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.1.5

**Question:** Do you use interactive application security testing (IAST)?

**Type:** yes_no

**Explanation:** IAST combines SAST and DAST approaches for comprehensive testing.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.1.6

**Question:** How do you manage third-party libraries and dependencies?

**Type:** multiple_choice

**Explanation:** Dependency management prevents introduction of vulnerable third-party components.

**Answer Options:**

**Option 1:** Automated scanning

**Option 2:** Manual review

**Option 3:** Dependency management tools

**Option 4:** No management


#### Question 8.1.7

**Question:** Do you have secure coding standards?

**Type:** yes_no

**Explanation:** Coding standards provide guidelines for writing secure code.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 8.2: Web Application Security

#### Question 8.2.1

**Question:** Do you protect against OWASP Top 10 vulnerabilities?

**Type:** yes_no

**Explanation:** OWASP Top 10 represents the most critical web application security risks.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.2.2

**Question:** Do you implement input validation and sanitization?

**Type:** yes_no

**Explanation:** Input validation prevents injection attacks and data corruption.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.2.3

**Question:** How do you handle authentication in web applications?

**Type:** multiple_select

**Explanation:** Proper authentication mechanisms protect against unauthorized access.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 8.2.4

**Question:** Do you implement proper session management?

**Type:** yes_no

**Explanation:** Session management prevents session hijacking and fixation attacks.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.2.5

**Question:** Do you use Content Security Policy (CSP)?

**Type:** yes_no

**Explanation:** CSP helps prevent cross-site scripting (XSS) attacks.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.2.6

**Question:** How do you protect against cross-site request forgery (CSRF)?

**Type:** multiple_choice

**Explanation:** CSRF protection prevents unauthorized actions on behalf of authenticated users.

**Answer Options:**

**Option 1:** CSRF tokens

**Option 2:** SameSite cookies

**Option 3:** Referrer validation

**Option 4:** No protection



### Subsection 8.3: API Security

#### Question 8.3.1

**Question:** How do you secure your APIs?

**Type:** multiple_select

**Explanation:** API security prevents unauthorized access and abuse of application interfaces.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 8.3.2

**Question:** Do you implement API rate limiting?

**Type:** yes_no

**Explanation:** Rate limiting prevents API abuse and denial of service attacks.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.3.3

**Question:** Do you log and monitor API usage?

**Type:** yes_no

**Explanation:** API monitoring helps detect suspicious activity and security incidents.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.3.4

**Question:** How do you handle API versioning?

**Type:** multiple_choice

**Explanation:** Proper API versioning ensures backward compatibility and security updates.

**Answer Options:**

**Option 1:** URL versioning

**Option 2:** Header versioning

**Option 3:** Parameter versioning

**Option 4:** No versioning


#### Question 8.3.5

**Question:** Do you validate API inputs and outputs?

**Type:** yes_no

**Explanation:** Input/output validation prevents injection attacks and data leakage.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 8.3.6

**Question:** Do you use API gateways?

**Type:** yes_no

**Explanation:** API gateways provide centralized security, monitoring, and management.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 8.4: DevSecOps & CI/CD Security

#### Question 8.4.1

**Question:** Do you integrate security testing in your CI/CD pipeline?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Automated security testing in CI/CD enables early detection of vulnerabilities.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 8.4.2

**Question:** Do you implement merge gate policies for security?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Merge gates prevent vulnerable code from reaching production.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 8.4.3

**Question:** How do you scan for secrets in code repositories?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Secret scanning prevents credential exposure in source code.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 8.4.4

**Question:** Do you perform Infrastructure as Code (IaC) security scanning?

**Type:** multiple_select

**Weight:** 3

**Explanation:** IaC scanning identifies misconfigurations before deployment.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 8.4.5

**Question:** How do you handle security findings in CI/CD?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Structured handling ensures security findings are addressed promptly.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 8.4.6

**Question:** Do you enforce SBOM generation and attestation in your release pipeline?

**Type:** multiple_select

**Weight:** 5

**Explanation:** SBOM enforcement provides supply chain transparency and enables vulnerability tracking.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 8.4.7

**Question:** Do you implement mandatory Infrastructure as Code (IaC) policy enforcement?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Mandatory IaC policies prevent misconfigurations and enforce security standards.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization




---

## Section 9: Cloud & Container Security

**Suggested Respondents:** Cloud Security Architect

### Subsection 9.1: Cloud Infrastructure Security

#### Question 9.1.1

**Question:** Which cloud service models do you use?

**Type:** multiple_select

**Explanation:** Different service models require different security approaches and responsibilities.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Option 5**
*Basic Description:* Fifth option

**Option 6: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 9.1.2

**Question:** Do you have a cloud security strategy?

**Type:** yes_no

**Explanation:** A cloud security strategy ensures consistent protection across cloud environments.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 9.1.3

**Question:** How do you secure cloud configurations?

**Type:** multiple_select

**Explanation:** Secure configurations prevent common cloud misconfigurations and vulnerabilities.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 9.1.4

**Question:** Do you implement network security in the cloud?

**Type:** multiple_select

**Explanation:** Cloud network security controls protect against unauthorized access and attacks.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 9.1.5

**Question:** How do you monitor cloud security?

**Type:** multiple_select

**Explanation:** Cloud security monitoring provides visibility into threats and compliance issues.

**Answer Options:**
**Option 1: Automated monitoring tools**
*Basic Description:* Using SIEM, monitoring platforms, or similar

**Option 2: Manual reviews**
*Basic Description:* Regular manual checks and reviews

**Option 3: Combination approach**
*Basic Description:* Mix of automated and manual monitoring

**Option 4: Third-party service**
*Basic Description:* Outsourced monitoring

**Option 5: Not monitored**
*Basic Description:* Not currently monitored



#### Question 9.1.6

**Question:** Do you encrypt data in cloud storage?

**Type:** yes_no

**Explanation:** Cloud data encryption protects against unauthorized access to stored information.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 9.1.7

**Question:** How do you manage cloud costs and security trade-offs?

**Type:** multiple_choice

**Explanation:** Balancing cost and security ensures adequate protection within budget constraints.

**Answer Options:**

**Option 1:** Security-first approach

**Option 2:** Cost-optimized with security

**Option 3:** Balanced approach

**Option 4:** Cost-first approach



### Subsection 9.2: Cloud Identity & Access Management

#### Question 9.2.1

**Question:** How do you manage cloud identities?

**Type:** multiple_select

**Explanation:** Proper cloud identity management ensures secure access to cloud resources.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 9.2.2

**Question:** Do you implement least privilege in cloud environments?

**Type:** yes_no

**Explanation:** Least privilege reduces the risk of unauthorized access and privilege escalation.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 9.2.3

**Question:** How do you secure cloud API access?

**Type:** multiple_select

**Explanation:** API security prevents unauthorized access to cloud management interfaces.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 9.2.4

**Question:** Do you rotate cloud access credentials?

**Type:** multiple_choice

**Explanation:** Credential rotation reduces the risk of compromised access keys.

**Answer Options:**

**Option 1:** Automatically

**Option 2:** Regularly

**Option 3:** Occasionally

**Option 4:** Never


#### Question 9.2.5

**Question:** How do you manage privileged access to cloud resources?

**Type:** multiple_choice

**Explanation:** Privileged access management prevents unauthorized administrative actions.

**Answer Options:**

**Option 1:** PAM solution

**Option 2:** Break-glass procedures

**Option 3:** Shared accounts

**Option 4:** No special controls


#### Question 9.2.6

**Question:** Do you monitor cloud access and activities?

**Type:** yes_no

**Explanation:** Activity monitoring helps detect unauthorized access and suspicious behavior.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 9.3: Container & Serverless Security

#### Question 9.3.1

**Question:** Do you use containers in your cloud environment?

**Type:** yes_no

**Explanation:** Container usage requires specific security considerations and controls.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 9.3.2

**Question:** How do you secure container images?

**Type:** multiple_select

**Explanation:** Container image security prevents deployment of vulnerable or malicious containers.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 9.3.3

**Question:** Do you implement container runtime security?

**Type:** multiple_select

**Explanation:** Runtime security protects containers during execution from various threats.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 9.3.4

**Question:** How do you secure serverless functions?

**Type:** multiple_select

**Explanation:** Serverless security addresses unique risks in function-as-a-service environments.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 9.3.5

**Question:** Do you scan for vulnerabilities in cloud workloads?

**Type:** yes_no

**Explanation:** Vulnerability scanning identifies security weaknesses in cloud-deployed applications.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 9.3.6

**Question:** How do you manage secrets in cloud environments?

**Type:** multiple_choice

**Explanation:** Proper secret management prevents exposure of sensitive credentials and keys.

**Answer Options:**

**Option 1:** Cloud secret managers

**Option 2:** Environment variables

**Option 3:** Configuration files

**Option 4:** Hardcoded

**Option 5:** External vault



---

## Section 10: Incident Response & Resilience

**Suggested Respondents:** CISO, Incident Response Manager

### Subsection 10.1: Incident Response Planning

#### Question 10.1.1

**Question:** Do you have a formal incident response plan?

**Type:** yes_no

**Explanation:** A formal incident response plan ensures coordinated and effective response to security incidents.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 10.1.2

**Question:** How often do you update your incident response plan?

**Type:** multiple_choice

**Explanation:** Regular updates ensure the plan remains current with threats and organizational changes.

**Answer Options:**

**Option 1:** Quarterly

**Option 2:** Annually

**Option 3:** After incidents

**Option 4:** As needed

**Option 5:** Never updated


#### Question 10.1.3

**Question:** Do you have an incident response team (IRT)?

**Type:** yes_no

**Explanation:** A dedicated incident response team provides specialized expertise for handling security incidents.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 10.1.4

**Question:** What roles are defined in your incident response team?

**Type:** multiple_select

**Explanation:** Clear roles ensure effective coordination and decision-making during incidents.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 10.1.5

**Question:** Do you conduct incident response training?

**Type:** multiple_choice

**Explanation:** Training ensures team members are prepared to execute the incident response plan effectively.

**Answer Options:**

**Option 1:** Regularly

**Option 2:** Annually

**Option 3:** Occasionally

**Option 4:** Never


#### Question 10.1.6

**Question:** Do you perform incident response exercises or tabletops?

**Type:** multiple_choice

**Explanation:** Exercises test the incident response plan and identify areas for improvement.

**Answer Options:**

**Option 1:** Quarterly

**Option 2:** Annually

**Option 3:** Occasionally

**Option 4:** Never


#### Question 10.1.7

**Question:** Do you have predefined incident severity levels?

**Type:** yes_no

**Explanation:** Severity levels help prioritize response efforts and determine escalation procedures.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 10.2: Incident Detection & Response

#### Question 10.2.1

**Question:** How do you detect security incidents?

**Type:** multiple_select

**Explanation:** Multiple detection methods improve the likelihood of identifying security incidents quickly.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 10.2.2

**Question:** What is your target time for incident detection?

**Type:** multiple_choice

**Explanation:** Rapid detection minimizes the impact and spread of security incidents.

**Answer Options:**

**Option 1:** < 1 hour

**Option 2:** 1-4 hours

**Option 3:** 4-24 hours

**Option 4:** > 24 hours

**Option 5:** No target


#### Question 10.2.3

**Question:** Do you have 24/7 incident response capabilities?

**Type:** yes_no

**Explanation:** Round-the-clock capabilities ensure incidents can be addressed regardless of when they occur.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 10.2.4

**Question:** How do you contain security incidents?

**Type:** multiple_select

**Explanation:** Containment prevents incidents from spreading and causing additional damage.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 10.2.5

**Question:** Do you have incident escalation procedures?

**Type:** yes_no

**Explanation:** Escalation procedures ensure appropriate stakeholders are notified based on incident severity.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 10.2.6

**Question:** How do you communicate during incidents?

**Type:** multiple_select

**Explanation:** Effective communication keeps stakeholders informed and coordinates response efforts.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented




### Subsection 10.3: Incident Recovery & Lessons Learned

#### Question 10.3.1

**Question:** Do you have incident recovery procedures?

**Type:** yes_no

**Explanation:** Recovery procedures ensure systems and operations are restored safely after incidents.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 10.3.2

**Question:** How do you validate system integrity after incidents?

**Type:** multiple_choice

**Explanation:** Integrity validation ensures systems are clean before returning to normal operations.

**Answer Options:**

**Option 1:** Automated scanning

**Option 2:** Manual verification

**Option 3:** Third-party assessment

**Option 4:** No validation


#### Question 10.3.3

**Question:** Do you conduct post-incident reviews?

**Type:** yes_no

**Explanation:** Post-incident reviews identify lessons learned and opportunities for improvement.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 10.3.4

**Question:** Do you document incident details and response actions?

**Type:** yes_no

**Explanation:** Documentation provides valuable information for future incidents and compliance requirements.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 10.3.5

**Question:** How do you track incident metrics?

**Type:** multiple_select

**Explanation:** Metrics help measure incident response effectiveness and identify improvement areas.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 10.3.6

**Question:** Do you update security controls based on incident findings?

**Type:** yes_no

**Explanation:** Control updates help prevent similar incidents from occurring in the future.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



---

## Section 11: Business Continuity

**Suggested Respondents:** BCP Coordinator, Risk Manager

### Subsection 11.1: Business Continuity Planning

#### Question 11.1.1

**Question:** Do you have a business continuity plan (BCP)?

**Type:** yes_no

**Explanation:** A BCP ensures critical business functions can continue during and after disruptions.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 11.1.2

**Question:** How often do you update your business continuity plan?

**Type:** multiple_choice

**Explanation:** Regular updates ensure the plan remains current with business changes and lessons learned.

**Answer Options:**

**Option 1:** Quarterly

**Option 2:** Annually

**Option 3:** After incidents

**Option 4:** As needed

**Option 5:** Never updated


#### Question 11.1.3

**Question:** Do you conduct business impact assessments (BIA)?

**Type:** yes_no

**Explanation:** BIAs identify critical business processes and their recovery requirements.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 11.1.4

**Question:** What is your target Recovery Time Objective (RTO) for critical systems?

**Type:** multiple_choice

**Explanation:** RTO defines acceptable downtime and guides recovery planning decisions.

**Answer Options:**

**Option 1:** < 1 hour

**Option 2:** 1-4 hours

**Option 3:** 4-24 hours

**Option 4:** > 24 hours

**Option 5:** Not defined


#### Question 11.1.5

**Question:** Do you have alternate work locations identified?

**Type:** yes_no

**Explanation:** Alternate locations ensure business operations can continue if primary facilities are unavailable.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 11.1.6

**Question:** Do you test your business continuity plan?

**Type:** multiple_choice

**Explanation:** Regular testing validates the plan's effectiveness and identifies improvement areas.

**Answer Options:**

**Option 1:** Quarterly

**Option 2:** Annually

**Option 3:** Occasionally

**Option 4:** Never



### Subsection 11.2: Disaster Recovery

#### Question 11.2.1

**Question:** Do you have a disaster recovery plan (DRP)?

**Type:** yes_no

**Explanation:** A DRP provides procedures for recovering IT systems and data after disasters.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 11.2.2

**Question:** Where do you maintain disaster recovery capabilities?

**Type:** multiple_select

**Explanation:** Multiple recovery options provide flexibility and resilience against different disaster scenarios.

**Answer Options:**
**Option 1: Commercial SAST tool**
*Basic Description:* Vendor SAST solution

**Option 2: Open-source SAST tool**
*Basic Description:* Open-source static analysis

**Option 3: IDE-integrated analysis**
*Basic Description:* Built into development environment

**Option 4: Manual code review**
*Basic Description:* Manual security code review

**Option 5: Not performed**
*Basic Description:* SAST not performed



#### Question 11.2.3

**Question:** How do you replicate critical data for disaster recovery?

**Type:** multiple_choice

**Explanation:** Data replication ensures critical information is available for recovery operations.

**Answer Options:**

**Option 1:** Real-time replication

**Option 2:** Near real-time

**Option 3:** Scheduled backups

**Option 4:** Manual copying

**Option 5:** No replication


#### Question 11.2.4

**Question:** Do you conduct disaster recovery exercises?

**Type:** multiple_choice

**Explanation:** DR exercises validate recovery procedures and team readiness.

**Answer Options:**

**Option 1:** Quarterly

**Option 2:** Annually

**Option 3:** Occasionally

**Option 4:** Never


#### Question 11.2.5

**Question:** How do you communicate during disaster recovery?

**Type:** multiple_select

**Explanation:** Effective communication keeps stakeholders informed during recovery operations.

**Answer Options:**
**Option 1: Commercial SAST tool**
*Basic Description:* Vendor SAST solution

**Option 2: Open-source SAST tool**
*Basic Description:* Open-source static analysis

**Option 3: IDE-integrated analysis**
*Basic Description:* Built into development environment

**Option 4: Manual code review**
*Basic Description:* Manual security code review

**Option 5: Not performed**
*Basic Description:* SAST not performed




### Subsection 11.3: Crisis Management

#### Question 11.3.1

**Question:** Do you have a crisis management team?

**Type:** yes_no

**Explanation:** A crisis management team provides leadership and coordination during major disruptions.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 11.3.2

**Question:** Do you have crisis communication procedures?

**Type:** yes_no

**Explanation:** Communication procedures ensure consistent and timely information sharing during crises.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 11.3.3

**Question:** How do you coordinate with external stakeholders during crises?

**Type:** multiple_select

**Explanation:** External coordination ensures comprehensive crisis response and stakeholder management.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 11.3.4

**Question:** Do you conduct crisis management training?

**Type:** multiple_choice

**Explanation:** Training ensures team members are prepared to manage crises effectively.

**Answer Options:**

**Option 1:** Regularly

**Option 2:** Annually

**Option 3:** Occasionally

**Option 4:** Never


#### Question 11.3.5

**Question:** How do you manage crisis decision-making authority?

**Type:** multiple_select

**Explanation:** Clear decision-making authority enables rapid crisis response.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 11.3.6

**Question:** Do you have crisis resource allocation procedures?

**Type:** yes_no

**Explanation:** Resource allocation procedures ensure critical needs are met during crises.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 11.4: Recovery Operations

#### Question 11.4.1

**Question:** Do you have documented recovery procedures?

**Type:** yes_no

**Explanation:** Recovery procedures provide step-by-step guidance for restoring operations.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 11.4.2

**Question:** How do you prioritize recovery activities?

**Type:** multiple_select

**Explanation:** Recovery prioritization ensures critical functions are restored first.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 11.4.3

**Question:** Do you have recovery time objectives (RTO) defined?

**Type:** yes_no

**Explanation:** RTOs establish target timeframes for restoring business functions.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 11.4.4

**Question:** Do you have recovery point objectives (RPO) defined?

**Type:** yes_no

**Explanation:** RPOs define acceptable data loss limits during recovery.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 11.4.5

**Question:** How do you coordinate recovery activities?

**Type:** multiple_select

**Explanation:** Coordinated recovery ensures efficient restoration of operations.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 11.4.6

**Question:** Do you conduct post-incident reviews?

**Type:** yes_no

**Explanation:** Post-incident reviews identify lessons learned and improvement opportunities.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



---

## Section 12: Vendor Management

**Suggested Respondents:** Vendor Risk Manager, Procurement

### Subsection 12.1: Vendor Risk Assessment

#### Question 12.1.1

**Question:** Do you conduct security assessments of vendors?

**Type:** yes_no

**Explanation:** Vendor security assessments help identify and mitigate third-party risks.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 12.1.2

**Question:** What criteria do you use for vendor security evaluation?

**Type:** multiple_select

**Explanation:** Multiple evaluation criteria provide comprehensive vendor risk assessment.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 12.1.3

**Question:** How do you classify vendor risk levels?

**Type:** multiple_choice

**Explanation:** Risk classification helps prioritize vendor management efforts and controls.

**Answer Options:**

**Option 1:** High/Medium/Low

**Option 2:** Critical/Important/Standard

**Option 3:** Tiered approach

**Option 4:** No classification


#### Question 12.1.4

**Question:** Do you require security certifications from vendors?

**Type:** multiple_select

**Explanation:** Security certifications provide assurance of vendor security practices.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 12.1.5

**Question:** How often do you reassess vendor security?

**Type:** multiple_choice

**Explanation:** Regular reassessment ensures ongoing vendor security compliance.

**Answer Options:**

**Option 1:** Annually

**Option 2:** Bi-annually

**Option 3:** Contract renewal

**Option 4:** As needed

**Option 5:** Never


#### Question 12.1.6

**Question:** Do you maintain a vendor risk register?

**Type:** yes_no

**Explanation:** A risk register provides centralized tracking of vendor security risks.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 12.1.7

**Question:** How do you handle high-risk vendors?

**Type:** multiple_select

**Explanation:** High-risk vendors require additional security measures and oversight.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed




### Subsection 12.2: Contract Management

#### Question 12.2.1

**Question:** Do you include security requirements in vendor contracts?

**Type:** yes_no

**Explanation:** Contractual security requirements establish legal obligations for vendor security.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 12.2.2

**Question:** What security clauses do you include in contracts?

**Type:** multiple_select

**Explanation:** Comprehensive security clauses protect organizational interests and data.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 12.2.3

**Question:** Do you require vendor insurance coverage?

**Type:** multiple_choice

**Explanation:** Insurance coverage provides financial protection against vendor-related incidents.

**Answer Options:**

**Option 1:** Cyber liability

**Option 2:** Professional liability

**Option 3:** General liability

**Option 4:** All of the above

**Option 5:** None required


#### Question 12.2.4

**Question:** How do you handle data processing agreements?

**Type:** multiple_choice

**Explanation:** Data processing agreements ensure compliance with privacy regulations.

**Answer Options:**

**Option 1:** Standard DPA

**Option 2:** Custom agreements

**Option 3:** Vendor templates

**Option 4:** No formal agreements


#### Question 12.2.5

**Question:** Do you include right-to-audit clauses?

**Type:** yes_no

**Explanation:** Audit rights enable verification of vendor security compliance.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 12.2.6

**Question:** How do you handle contract termination security requirements?

**Type:** multiple_select

**Explanation:** Termination requirements ensure secure end-of-relationship procedures.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed




### Subsection 12.3: Vendor Monitoring & Oversight

#### Question 12.3.1

**Question:** How do you monitor vendor security performance?

**Type:** multiple_select

**Explanation:** Ongoing monitoring ensures vendors maintain security standards.

**Answer Options:**
**Option 1: Automated monitoring tools**
*Basic Description:* Using SIEM, monitoring platforms, or similar

**Option 2: Manual reviews**
*Basic Description:* Regular manual checks and reviews

**Option 3: Combination approach**
*Basic Description:* Mix of automated and manual monitoring

**Option 4: Third-party service**
*Basic Description:* Outsourced monitoring

**Option 5: Not monitored**
*Basic Description:* Not currently monitored



#### Question 12.3.2

**Question:** Do you require incident notification from vendors?

**Type:** yes_no

**Explanation:** Incident notification enables rapid response to vendor security events.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 12.3.3

**Question:** What is your required timeframe for vendor incident notification?

**Type:** multiple_choice

**Explanation:** Timely notification enables effective incident response and risk mitigation.

**Answer Options:**

**Option 1:** Immediately

**Option 2:** 24 hours

**Option 3:** 72 hours

**Option 4:** 1 week

**Option 5:** No requirement


#### Question 12.3.4

**Question:** Do you conduct vendor security audits?

**Type:** multiple_choice

**Explanation:** Security audits verify vendor compliance with security requirements.

**Answer Options:**

**Option 1:** Regularly

**Option 2:** Risk-based

**Option 3:** Contract-driven

**Option 4:** Never


#### Question 12.3.5

**Question:** How do you handle vendor security incidents?

**Type:** multiple_select

**Explanation:** Structured incident handling ensures effective response to vendor security events.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 12.3.6

**Question:** Do you maintain vendor contact information for security issues?

**Type:** yes_no

**Explanation:** Current contact information enables rapid communication during security incidents.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 12.4: Supply Chain Security

#### Question 12.4.1

**Question:** Do you maintain Software Bill of Materials (SBOM) for your applications?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** SBOM provides visibility into software components and dependencies.

**Answer Options:**

**Option 1:** Comprehensive SBOM

**Option 2:** Partial SBOM

**Option 3:** Planning to implement

**Option 4:** No SBOM


#### Question 12.4.2

**Question:** How do you verify software integrity?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Software integrity verification prevents tampering and ensures authenticity.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 12.4.3

**Question:** Do you assess open source component risks?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Open source risk assessment identifies potential security and compliance issues.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 12.4.4

**Question:** How do you handle SaaS application security?

**Type:** multiple_select

**Weight:** 3

**Explanation:** SaaS security assessment ensures third-party services meet security standards.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 12.4.5

**Question:** Do you monitor supply chain security threats?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Supply chain monitoring enables rapid response to emerging threats.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization




---

## Section 13: Security Awareness & Training

**Suggested Respondents:** Security Awareness Lead, HR Learning & Development

### Subsection 13.1: Security Awareness Program

#### Question 13.1.1

**Question:** Do you have a formal security awareness program?

**Type:** yes_no

**Explanation:** A formal program ensures consistent and comprehensive security awareness across the organization.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.1.2

**Question:** How often do you conduct security awareness training?

**Type:** multiple_choice

**Explanation:** Regular training keeps security awareness current with evolving threats.

**Answer Options:**

**Option 1: Monthly**
*Basic Description:* Every month review cycle

**Option 2: Quarterly**
*Basic Description:* Every three months review

**Option 3: Annually**
*Basic Description:* Once per year review

**Option 4: As needed**
*Basic Description:* Event-driven reviews only

**Option 5: Never**
*Basic Description:* No formal reviews


#### Question 13.1.3

**Question:** What topics are covered in your security awareness training?

**Type:** multiple_select

**Explanation:** Comprehensive topics ensure broad security awareness coverage.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 13.1.4

**Question:** How do you deliver security awareness training?

**Type:** multiple_select

**Explanation:** Multiple delivery methods accommodate different learning preferences and reinforce messages.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 13.1.5

**Question:** Do you track security awareness training completion?

**Type:** yes_no

**Explanation:** Tracking ensures all employees receive required security awareness training.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.1.6

**Question:** What is your target completion rate for security training?

**Type:** multiple_choice

**Explanation:** High completion rates ensure comprehensive security awareness across the organization.

**Answer Options:**

**Option 1:** 100%

**Option 2:** 95-99%

**Option 3:** 90-94%

**Option 4:** 80-89%

**Option 5:** No target


#### Question 13.1.7

**Question:** Do you customize training content for different roles?

**Type:** yes_no

**Explanation:** Customized training addresses specific organizational risks and improves relevance.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.1.8

**Question:** How often do you conduct phishing simulations?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** Regular phishing simulations test and improve user awareness of social engineering attacks.

**Answer Options:**

**Option 1:** Monthly

**Option 2:** Quarterly

**Option 3:** Bi-annually

**Option 4:** Annually

**Option 5:** Never


#### Question 13.1.9

**Question:** Do you conduct executive tabletop exercises?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** Executive tabletop exercises prepare leadership for security incident response.

**Answer Options:**

**Option 1:** Quarterly

**Option 2:** Annually

**Option 3:** Bi-annually

**Option 4:** As needed

**Option 5:** Never


#### Question 13.1.10

**Question:** How do you measure security culture maturity?

**Type:** multiple_select

**Weight:** 1

**Explanation:** Security culture measurement identifies areas for improvement in human security factors.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented




### Subsection 13.2: Phishing & Social Engineering

#### Question 13.2.1

**Question:** Do you conduct phishing simulation exercises?

**Type:** yes_no

**Explanation:** Phishing simulations test and improve employee ability to identify malicious emails.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.2.2

**Question:** How often do you run phishing simulations?

**Type:** multiple_choice

**Explanation:** Regular simulations maintain awareness and improve detection capabilities.

**Answer Options:**

**Option 1:** Monthly

**Option 2:** Quarterly

**Option 3:** Bi-annually

**Option 4:** Annually

**Option 5:** Never


#### Question 13.2.3

**Question:** How do you handle employees who fail phishing tests?

**Type:** multiple_select

**Explanation:** Appropriate responses help improve individual security awareness without being punitive.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 13.2.4

**Question:** Do you provide social engineering awareness training?

**Type:** yes_no

**Explanation:** Social engineering training helps employees recognize and respond to manipulation attempts.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.2.5

**Question:** What is your current phishing simulation click rate?

**Type:** multiple_choice

**Explanation:** Low click rates indicate effective security awareness and training programs.

**Answer Options:**

**Option 1:** 0-4.9%

**Option 2:** 5.0-9.9%

**Option 3:** 10-20%

**Option 4:** >20%

**Option 5:** Not measured



### Subsection 13.3: Role-Based Training

#### Question 13.3.1

**Question:** Do you provide role-specific security training?

**Type:** yes_no

**Explanation:** Role-specific training addresses unique security responsibilities and risks for different positions.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.3.2

**Question:** What roles receive specialized security training?

**Type:** multiple_select

**Explanation:** Different roles face different security risks and require tailored training.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 13.3.3

**Question:** Do you provide security training for new employees?

**Type:** yes_no

**Explanation:** New employee training ensures security awareness from the start of employment.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.3.4

**Question:** How do you measure training effectiveness?

**Type:** multiple_select

**Explanation:** Effectiveness measurement helps improve training programs and demonstrate value.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 13.3.5

**Question:** Do you provide security training for contractors and vendors?

**Type:** yes_no

**Explanation:** Third-party training ensures consistent security practices across all personnel.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.3.6

**Question:** How do you handle security training for remote workers?

**Type:** multiple_select

**Explanation:** Remote workers face unique security challenges requiring tailored training approaches.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed




### Subsection 13.4: Training Management & Compliance

#### Question 13.4.1

**Question:** Do you maintain training records and certificates?

**Type:** yes_no

**Explanation:** Training records provide compliance evidence and track individual progress.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.4.2

**Question:** How do you handle training compliance requirements?

**Type:** multiple_select

**Explanation:** Compliance requirements drive training content and frequency decisions.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 13.4.3

**Question:** Do you have training renewal or refresher requirements?

**Type:** multiple_choice

**Explanation:** Regular refresher training maintains current security awareness.

**Answer Options:**

**Option 1:** Annual

**Option 2:** Bi-annual

**Option 3:** Based on role changes

**Option 4:** As needed

**Option 5:** No renewals


#### Question 13.4.4

**Question:** How do you budget for security training?

**Type:** multiple_choice

**Explanation:** Dedicated budgeting ensures consistent investment in security awareness.

**Answer Options:**

**Option 1:** Dedicated budget

**Option 2:** Part of IT budget

**Option 3:** HR budget

**Option 4:** Ad-hoc funding

**Option 5:** No specific budget


#### Question 13.4.5

**Question:** Do you use external training providers?

**Type:** multiple_select

**Explanation:** External providers can offer specialized expertise and current threat intelligence.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 13.4.6

**Question:** How do you customize training for different audiences?

**Type:** multiple_select

**Explanation:** Customized training improves relevance and effectiveness for different user groups.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 13.4.7

**Question:** Do you integrate security training with onboarding?

**Type:** yes_no

**Explanation:** Onboarding integration ensures new employees receive security training from day one.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 13.4.8

**Question:** How do you communicate training requirements to employees?

**Type:** multiple_select

**Explanation:** Clear communication ensures employees understand training expectations and deadlines.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented




---

## Section 14: Physical Security

**Suggested Respondents:** Facilities Manager, Corporate Security

### Subsection 14.1: Facility Security

#### Question 14.1.1

**Question:** Do you have physical access controls for your facilities?

**Type:** yes_no

**Explanation:** Physical access controls prevent unauthorized entry to facilities and sensitive areas.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 14.1.2

**Question:** What types of physical access controls do you use?

**Type:** multiple_select

**Explanation:** Multiple access control methods provide layered physical security protection.

**Answer Options:**
**Option 1: Biometric**
*Basic Description:* Fingerprint, facial recognition, etc.

**Option 2: Card/badge access**
*Basic Description:* RFID or magnetic stripe cards

**Option 3: PIN/password**
*Basic Description:* Numeric or alphanumeric codes

**Option 4: Multi-factor**
*Basic Description:* Combination of multiple methods

**Option 5: Security personnel**
*Basic Description:* Manned security checkpoints

**Option 6: No formal controls**
*Basic Description:* No formal access control system



#### Question 14.1.3

**Question:** Do you have surveillance systems in place?

**Type:** multiple_select

**Explanation:** Surveillance systems provide detection and deterrence for physical security threats.

**Answer Options:**
**Option 1: 24/7 monitoring**
*Basic Description:* Continuous surveillance monitoring

**Option 2: Recording only**
*Basic Description:* Cameras record but not actively monitored

**Option 3: Motion-activated**
*Basic Description:* Cameras activate on motion detection

**Option 4: Limited coverage**
*Basic Description:* Partial surveillance coverage

**Option 5: No surveillance**
*Basic Description:* No surveillance system



#### Question 14.1.4

**Question:** How do you manage visitor access?

**Type:** multiple_select

**Explanation:** Visitor management ensures unauthorized individuals cannot access sensitive areas.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 14.1.5

**Question:** Do you have secure areas for sensitive equipment?

**Type:** yes_no

**Explanation:** Secure areas protect critical infrastructure and sensitive equipment from unauthorized access.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 14.1.6

**Question:** How often do you review physical access logs?

**Type:** multiple_choice

**Explanation:** Regular log reviews help detect unauthorized access attempts and security incidents.

**Answer Options:**

**Option 1:** Daily

**Option 2:** Weekly

**Option 3:** Monthly

**Option 4:** As needed

**Option 5:** Never



### Subsection 14.2: Environmental Controls

#### Question 14.2.1

**Question:** Do you have environmental monitoring systems?

**Type:** multiple_select

**Explanation:** Environmental monitoring protects equipment and data from environmental threats.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 14.2.2

**Question:** Do you have backup power systems?

**Type:** multiple_choice

**Explanation:** Backup power ensures continued operations during power outages.

**Answer Options:**

**Option 1:** UPS systems

**Option 2:** Generators

**Option 3:** Battery backup

**Option 4:** Multiple power sources

**Option 5:** None


#### Question 14.2.3

**Question:** How do you protect against fire hazards?

**Type:** multiple_select

**Explanation:** Fire protection systems prevent damage to equipment and data from fire incidents.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 14.2.4

**Question:** Do you have climate control systems?

**Type:** yes_no

**Explanation:** Climate control maintains optimal environmental conditions for equipment operation.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 14.3: Equipment Security

#### Question 14.3.1

**Question:** How do you secure workstations and laptops?

**Type:** multiple_select

**Explanation:** Equipment security prevents theft and unauthorized access to devices.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 14.3.2

**Question:** Do you have policies for equipment disposal?

**Type:** yes_no

**Explanation:** Secure disposal policies ensure sensitive data is properly destroyed when equipment is retired.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 14.3.3

**Question:** How do you handle mobile device security?

**Type:** multiple_select

**Explanation:** Mobile device security protects against data loss and unauthorized access.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 14.3.4

**Question:** Do you maintain an asset inventory?

**Type:** yes_no

**Explanation:** Asset inventory helps track and manage physical security of equipment and devices.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 14.3.5

**Question:** How do you secure server rooms and data centers?

**Type:** multiple_select

**Explanation:** Server room security protects critical infrastructure from physical threats.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 14.3.6

**Question:** Do you have equipment maintenance security procedures?

**Type:** yes_no

**Explanation:** Maintenance security procedures ensure equipment servicing doesn't compromise security.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 14.3.7

**Question:** How do you handle equipment loans and temporary access?

**Type:** multiple_select

**Explanation:** Equipment loan procedures prevent unauthorized use and ensure accountability.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 14.3.8

**Question:** Do you conduct physical security audits?

**Type:** multiple_choice

**Explanation:** Regular audits identify physical security gaps and improvement opportunities.

**Answer Options:**

**Option 1:** Annually

**Option 2:** Bi-annually

**Option 3:** As needed

**Option 4:** Never


#### Question 14.3.9

**Question:** How do you secure network equipment and cables?

**Type:** multiple_select

**Explanation:** Network infrastructure security prevents unauthorized access and tampering.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 14.3.10

**Question:** Do you have procedures for emergency equipment access?

**Type:** yes_no

**Explanation:** Emergency procedures ensure critical equipment remains accessible during crises.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 14.3.11

**Question:** How do you protect against electromagnetic interference?

**Type:** multiple_select

**Explanation:** EMI protection ensures equipment operates reliably and data remains secure.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 14.3.12

**Question:** Do you have clean desk and clear screen policies?

**Type:** yes_no

**Explanation:** Clean desk policies prevent unauthorized access to sensitive information.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 14.3.13

**Question:** How do you secure backup media and storage?

**Type:** multiple_select

**Explanation:** Backup media security ensures data recovery capabilities are protected.

**Answer Options:**
**Option 1: Daily**
*Basic Description:* Daily backup schedule

**Option 2: Weekly**
*Basic Description:* Weekly backup schedule

**Option 3: Monthly**
*Basic Description:* Monthly backup schedule

**Option 4: Real-time/Continuous**
*Basic Description:* Continuous data protection

**Option 5: No regular backups**
*Basic Description:* Backups not performed regularly



#### Question 14.3.14

**Question:** Do you have physical security incident response procedures?

**Type:** yes_no

**Explanation:** Physical incident procedures ensure appropriate response to security breaches.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 14.3.15

**Question:** How do you manage physical security during construction or renovation?

**Type:** multiple_select

**Explanation:** Construction security prevents unauthorized access during facility changes.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 14.3.16

**Question:** Do you conduct physical penetration testing?

**Type:** multiple_choice

**Explanation:** Physical penetration testing validates the effectiveness of physical security controls.

**Answer Options:**

**Option 1:** Annually

**Option 2:** Bi-annually

**Option 3:** As needed

**Option 4:** Never



---

## Section 15: Monitoring & Detection

**Suggested Respondents:** SOC Lead, Security Analyst

### Subsection 15.1: Security Monitoring

#### Question 15.1.1

**Question:** Do you have a Security Operations Center (SOC)?

**Type:** yes_no

**Explanation:** A SOC provides centralized security monitoring and incident response capabilities.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 15.1.2

**Question:** What security monitoring tools do you use?

**Type:** multiple_select

**Explanation:** Multiple monitoring tools provide comprehensive visibility into security events.

**Answer Options:**
**Option 1: Commercial solution**
*Basic Description:* Vendor-provided commercial product

**Option 2: Open-source solution**
*Basic Description:* Open-source tools and platforms

**Option 3: Custom-built solution**
*Basic Description:* Internally developed solution

**Option 4: Managed service**
*Basic Description:* Third-party managed service

**Option 5: Not deployed**
*Basic Description:* Not currently deployed



#### Question 15.1.3

**Question:** Do you have 24/7 security monitoring?

**Type:** yes_no

**Explanation:** Continuous monitoring ensures threats are detected regardless of when they occur.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 15.1.4

**Question:** How do you correlate security events?

**Type:** multiple_choice

**Explanation:** Event correlation helps identify complex attack patterns and reduce false positives.

**Answer Options:**

**Option 1:** Automated correlation

**Option 2:** Manual analysis

**Option 3:** Hybrid approach

**Option 4:** No correlation


#### Question 15.1.5

**Question:** What is your mean time to detect (MTTD) security incidents?

**Type:** multiple_choice

**Explanation:** Faster detection reduces the impact and spread of security incidents.

**Answer Options:**

**Option 1:** < 1 hour

**Option 2:** 1-4 hours

**Option 3:** 4-24 hours

**Option 4:** > 24 hours

**Option 5:** Not measured


#### Question 15.1.6

**Question:** Do you monitor user behavior for anomalies?

**Type:** yes_no

**Explanation:** User behavior analytics help detect insider threats and compromised accounts.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 15.1.7

**Question:** How do you handle security alerts?

**Type:** multiple_select

**Explanation:** Effective alert handling ensures timely response to genuine security threats.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed




### Subsection 15.2: Threat Detection

#### Question 15.2.1

**Question:** Do you use threat intelligence feeds?

**Type:** yes_no

**Explanation:** Threat intelligence helps identify known threats and attack patterns.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 15.2.2

**Question:** What types of threat detection do you implement?

**Type:** multiple_select

**Explanation:** Multiple detection methods improve coverage against different types of threats.

**Answer Options:**
**Option 1: Type A**
*Basic Description:* Primary implementation type

**Option 2: Type B**
*Basic Description:* Secondary implementation type

**Option 3: Type C**
*Basic Description:* Alternative implementation type

**Option 4: Hybrid**
*Basic Description:* Combination of multiple types

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 15.2.3

**Question:** Do you conduct proactive threat hunting?

**Type:** multiple_choice

**Explanation:** Threat hunting proactively identifies threats that may have evaded automated detection.

**Answer Options:**

**Option 1:** Regularly

**Option 2:** Occasionally

**Option 3:** After incidents

**Option 4:** Never


#### Question 15.2.4

**Question:** How do you detect advanced persistent threats (APTs)?

**Type:** multiple_select

**Explanation:** APT detection requires sophisticated monitoring and analysis capabilities.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 15.2.5

**Question:** Do you monitor for insider threats?

**Type:** yes_no

**Explanation:** Insider threat monitoring helps detect malicious or negligent employee activities.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 15.2.6

**Question:** How do you validate threat detection effectiveness?

**Type:** multiple_select

**Explanation:** Validation ensures detection capabilities are working effectively against real threats.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented




### Subsection 15.3: Log Management

#### Question 15.3.1

**Question:** Do you have centralized log management?

**Type:** yes_no

**Explanation:** Centralized logging provides comprehensive visibility and easier analysis of security events.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 15.3.2

**Question:** What types of logs do you collect?

**Type:** multiple_select

**Explanation:** Comprehensive log collection provides better visibility into security events.

**Answer Options:**
**Option 1: Type A**
*Basic Description:* Primary implementation type

**Option 2: Type B**
*Basic Description:* Secondary implementation type

**Option 3: Type C**
*Basic Description:* Alternative implementation type

**Option 4: Hybrid**
*Basic Description:* Combination of multiple types

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 15.3.3

**Question:** How long do you retain security logs?

**Type:** multiple_choice

**Explanation:** Adequate log retention supports incident investigation and compliance requirements.

**Answer Options:**

**Option 1:** 30 days

**Option 2:** 90 days

**Option 3:** 6 months

**Option 4:** 1 year

**Option 5:** > 1 year

**Option 6:** Varies by log type


#### Question 15.3.4

**Question:** Do you protect log integrity?

**Type:** multiple_select

**Explanation:** Log integrity protection ensures logs cannot be tampered with by attackers.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 15.3.5

**Question:** How do you analyze security logs?

**Type:** multiple_select

**Explanation:** Effective log analysis helps identify security incidents and trends.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 15.3.6

**Question:** Do you have log monitoring alerts?

**Type:** yes_no

**Explanation:** Log monitoring alerts provide real-time notification of security events.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



---

## Section 16: Vulnerability Management

**Suggested Respondents:** Vulnerability Management Lead, Patch Coordinator

### Subsection 16.1: Vulnerability Assessment

#### Question 16.1.1

**Question:** Do you conduct regular vulnerability assessments?

**Type:** yes_no

**Explanation:** Regular vulnerability assessments help identify security weaknesses before they can be exploited.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 16.1.2

**Question:** How often do you perform vulnerability scans?

**Type:** multiple_choice

**Explanation:** Frequent scanning ensures vulnerabilities are identified quickly as they emerge.

**Answer Options:**

**Option 1:** Daily

**Option 2:** Weekly

**Option 3:** Monthly

**Option 4:** Quarterly

**Option 5:** Annually

**Option 6:** Never


#### Question 16.1.3

**Question:** What types of vulnerability assessments do you perform?

**Type:** multiple_select

**Explanation:** Comprehensive assessments cover all potential attack vectors and system types.

**Answer Options:**
**Option 1: Type A**
*Basic Description:* Primary implementation type

**Option 2: Type B**
*Basic Description:* Secondary implementation type

**Option 3: Type C**
*Basic Description:* Alternative implementation type

**Option 4: Hybrid**
*Basic Description:* Combination of multiple types

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 16.1.4

**Question:** Do you use automated vulnerability scanning tools?

**Type:** yes_no

**Explanation:** Automated tools provide consistent and scalable vulnerability detection capabilities.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 16.1.5

**Question:** Do you conduct manual penetration testing?

**Type:** multiple_choice

**Explanation:** Manual testing identifies complex vulnerabilities that automated tools might miss.

**Answer Options:**

**Option 1:** Regularly

**Option 2:** Annually

**Option 3:** Occasionally

**Option 4:** Never


#### Question 16.1.6

**Question:** How do you validate vulnerability scan results?

**Type:** multiple_select

**Explanation:** Validation ensures scan results are accurate and actionable.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 16.1.7

**Question:** Do you scan for vulnerabilities in third-party components?

**Type:** yes_no

**Explanation:** Third-party component scanning identifies vulnerabilities in dependencies and libraries.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 16.2: Vulnerability Management Process

#### Question 16.2.1

**Question:** Do you have a formal vulnerability management process?

**Type:** yes_no

**Explanation:** A formal process ensures consistent and effective vulnerability handling.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 16.2.2

**Question:** How do you prioritize vulnerabilities for remediation?

**Type:** multiple_select

**Explanation:** Effective prioritization ensures critical vulnerabilities are addressed first.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 16.2.3

**Question:** What are your target remediation timeframes?

**Type:** multiple_choice

**Explanation:** Defined timeframes ensure timely vulnerability remediation based on risk levels.

**Answer Options:**

**Option 1:** Critical: 24h, High: 7d, Medium: 30d

**Option 2:** Critical: 72h, High: 14d, Medium: 60d

**Option 3:** Critical: 7d, High: 30d, Medium: 90d

**Option 4:** No defined timeframes


#### Question 16.2.4

**Question:** How do you track vulnerability remediation progress?

**Type:** multiple_select

**Explanation:** Progress tracking ensures vulnerabilities are remediated within target timeframes.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 16.2.5

**Question:** Do you have a vulnerability disclosure process?

**Type:** yes_no

**Explanation:** A disclosure process provides a channel for external researchers to report vulnerabilities.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 16.2.6

**Question:** How do you handle zero-day vulnerabilities?

**Type:** multiple_select

**Explanation:** Zero-day handling requires rapid response and alternative protection measures.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed




### Subsection 16.3: Patch Management

#### Question 16.3.1

**Question:** Do you have a formal patch management process?

**Type:** yes_no

**Weight:** 5

**Explanation:** Formal patch management ensures systematic and timely application of security updates.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 16.3.2

**Question:** How do you prioritize security patches?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Patch prioritization ensures critical vulnerabilities are addressed first.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 16.3.3

**Question:** What is your target timeframe for critical patches?

**Type:** multiple_choice

**Weight:** 5

**Explanation:** Rapid patching of critical vulnerabilities reduces exposure to attacks.

**Answer Options:**

**Option 1:** Within 24 hours

**Option 2:** Within 72 hours

**Option 3:** Within 1 week

**Option 4:** Within 1 month

**Option 5:** No defined timeline


#### Question 16.3.4

**Question:** How do you test patches before deployment?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Patch testing prevents deployment issues while maintaining security.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 16.3.5

**Question:** Do you have automated patch deployment capabilities?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** Automation enables faster and more consistent patch deployment.

**Answer Options:**

**Option 1:** Fully automated

**Option 2:** Semi-automated

**Option 3:** Manual only

**Option 4:** Varies by system type


#### Question 16.3.6

**Question:** How do you track patch deployment status?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Deployment tracking ensures patches are successfully applied across all systems.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 16.3.7

**Question:** How do you handle patch rollback procedures?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Rollback procedures enable quick recovery from problematic patches.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 16.3.8

**Question:** Do you have an emergency patching process?

**Type:** yes_no

**Weight:** 5

**Explanation:** Emergency processes enable rapid response to zero-day vulnerabilities and active exploits.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 16.3.9

**Question:** Do you maintain patch compliance reporting?

**Type:** yes_no

**Weight:** 1

**Explanation:** Compliance reporting provides visibility into patch status across the environment.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 16.3.10

**Question:** How do you handle end-of-life systems that cannot be patched?

**Type:** multiple_select

**Weight:** 3

**Explanation:** End-of-life systems require alternative security measures when patching is not possible.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed




---

## Section 17: Compliance & Audit

**Suggested Respondents:** Compliance Lead, Internal Audit

### Subsection 17.1: Regulatory Compliance

#### Question 17.1.1

**Question:** Which regulatory frameworks apply to your organization?

**Type:** multiple_select

**Explanation:** Understanding applicable regulations is essential for compliance planning and implementation.

**Answer Options:**
**Option 1: GDPR**
*Basic Description:* General Data Protection Regulation

**Option 2: HIPAA**
*Basic Description:* Health Insurance Portability and Accountability Act

**Option 3: PCI DSS**
*Basic Description:* Payment Card Industry Data Security Standard

**Option 4: SOC 2**
*Basic Description:* Service Organization Control 2

**Option 5: ISO 27001**
*Basic Description:* International Organization for Standardization 27001

**Option 6: NIST CSF**
*Basic Description:* NIST Cybersecurity Framework

**Option 7: Not applicable**
*Basic Description:* No specific compliance requirements



#### Question 17.1.2

**Question:** Do you have a compliance management program?

**Type:** yes_no

**Explanation:** A formal compliance program ensures systematic adherence to regulatory requirements.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 17.1.3

**Question:** How do you track compliance status?

**Type:** multiple_select

**Explanation:** Effective tracking ensures ongoing compliance and identifies gaps before they become violations.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 17.1.4

**Question:** Do you conduct regular compliance assessments?

**Type:** multiple_choice

**Explanation:** Regular assessments help maintain compliance and identify areas for improvement.

**Answer Options:**

**Option 1:** Monthly

**Option 2:** Quarterly

**Option 3:** Annually

**Option 4:** Bi-annually

**Option 5:** As required

**Option 6:** Never


#### Question 17.1.5

**Question:** How do you handle compliance violations?

**Type:** multiple_select

**Explanation:** Structured violation handling ensures proper response and prevents recurrence.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 17.1.6

**Question:** Do you maintain compliance documentation?

**Type:** yes_no

**Explanation:** Proper documentation demonstrates compliance efforts and supports audit activities.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 17.1.7

**Question:** How do you stay updated on regulatory changes?

**Type:** multiple_select

**Explanation:** Staying current with regulatory changes ensures ongoing compliance as requirements evolve.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented




### Subsection 17.2: Internal Audits

#### Question 17.2.1

**Question:** Do you conduct internal security audits?

**Type:** yes_no

**Explanation:** Internal audits provide independent assessment of security controls and compliance.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 17.2.2

**Question:** How often do you perform internal security audits?

**Type:** multiple_choice

**Explanation:** Regular internal audits help identify issues before external audits or incidents occur.

**Answer Options:**

**Option 1:** Quarterly

**Option 2:** Annually

**Option 3:** Bi-annually

**Option 4:** As needed

**Option 5:** Never


#### Question 17.2.3

**Question:** What areas do your internal audits cover?

**Type:** multiple_select

**Explanation:** Comprehensive audit coverage ensures all critical security areas are evaluated.

**Answer Options:**
**Option 1: Option 1**
*Basic Description:* First option

**Option 2: Option 2**
*Basic Description:* Second option

**Option 3: Option 3**
*Basic Description:* Third option

**Option 4: Option 4**
*Basic Description:* Fourth option

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 17.2.4

**Question:** Who conducts your internal security audits?

**Type:** multiple_choice

**Explanation:** Independent audit teams provide objective assessment of security controls.

**Answer Options:**

**Option 1:** Internal audit team

**Option 2:** IT security team

**Option 3:** External consultants

**Option 4:** Mixed approach

**Option 5:** No audits conducted


#### Question 17.2.5

**Question:** How do you track audit findings and remediation?

**Type:** multiple_select

**Explanation:** Systematic tracking ensures audit findings are properly addressed and resolved.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 17.2.6

**Question:** Do you have audit finding escalation procedures?

**Type:** yes_no

**Explanation:** Escalation procedures ensure critical findings receive appropriate management attention.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 17.3: External Audits & Certifications

#### Question 17.3.1

**Question:** Do you undergo external security audits?

**Type:** yes_no

**Explanation:** External audits provide independent validation of security controls and compliance.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 17.3.2

**Question:** What types of external audits do you participate in?

**Type:** multiple_select

**Explanation:** Different audit types serve various compliance and business requirements.

**Answer Options:**
**Option 1: Type A**
*Basic Description:* Primary implementation type

**Option 2: Type B**
*Basic Description:* Secondary implementation type

**Option 3: Type C**
*Basic Description:* Alternative implementation type

**Option 4: Hybrid**
*Basic Description:* Combination of multiple types

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 17.3.3

**Question:** How do you prepare for external audits?

**Type:** multiple_select

**Explanation:** Proper preparation increases audit success and reduces findings.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 17.3.4

**Question:** Do you maintain security certifications?

**Type:** multiple_select

**Explanation:** Security certifications demonstrate commitment to security best practices.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 17.3.5

**Question:** How do you manage audit evidence collection?

**Type:** multiple_select

**Explanation:** Efficient evidence collection streamlines audit processes and reduces burden.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 17.3.6

**Question:** Do you conduct management reviews of audit results?

**Type:** yes_no

**Explanation:** Management review ensures audit findings receive appropriate attention and resources for remediation.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 17.3.7

**Question:** How do you communicate audit results to stakeholders?

**Type:** multiple_select

**Explanation:** Effective communication ensures stakeholders understand audit outcomes and required actions.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented




---

## Section 18: OT/ICS & IoT Security

**Suggested Respondents:** OT Security Lead, Industrial Control Systems Engineer

### Subsection 18.1: Operational Technology Security

#### Question 18.1.1

**Question:** Do you have operational technology (OT) or industrial control systems (ICS)?

**Type:** yes_no

**Weight:** 1

**Explanation:** OT/ICS systems require specialized security approaches due to safety and availability requirements.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 18.1.2

**Question:** How do you segment OT networks from IT networks?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Network segmentation protects critical OT systems from IT-based attacks.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 18.1.3

**Question:** Do you conduct safety impact analysis for security changes?

**Type:** yes_no

**Weight:** 5

**Explanation:** Safety impact analysis ensures security measures don't compromise operational safety.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 18.1.4

**Question:** How do you handle OT system patching?

**Type:** multiple_select

**Weight:** 3

**Explanation:** OT patching requires careful coordination to maintain system availability and safety.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 18.1.5

**Question:** Do you monitor OT network traffic?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** OT network monitoring helps detect anomalies and potential security incidents.

**Answer Options:**

**Option 1:** Continuous monitoring

**Option 2:** Periodic monitoring

**Option 3:** Passive monitoring only

**Option 4:** No monitoring


#### Question 18.1.6

**Question:** Do you have OT-specific incident response procedures?

**Type:** yes_no

**Weight:** 3

**Explanation:** OT incident response requires specialized procedures considering safety and operational impact.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*



### Subsection 18.2: IoT Device Security

#### Question 18.2.1

**Question:** Do you have IoT devices in your environment?

**Type:** yes_no

**Weight:** 1

**Explanation:** IoT devices introduce unique security challenges requiring specialized management.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 18.2.2

**Question:** How do you secure IoT device communications?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Secure communications protect IoT data and prevent unauthorized access.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 18.2.3

**Question:** Do you maintain an inventory of IoT devices?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** IoT device inventory enables proper security management and risk assessment.

**Answer Options:**

**Option 1:** Comprehensive inventory

**Option 2:** Partial inventory

**Option 3:** Manual tracking

**Option 4:** No inventory


#### Question 18.2.4

**Question:** How do you manage IoT device firmware updates?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Regular firmware updates address security vulnerabilities in IoT devices.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Third-party managed**
*Basic Description:* Outsourced to service provider

**Option 5: Informal process**
*Basic Description:* Ad-hoc handling without formal procedures

**Option 6: Not currently managed**
*Basic Description:* Not currently managed



#### Question 18.2.5

**Question:** Do you monitor IoT device behavior?

**Type:** multiple_choice

**Weight:** 3

**Explanation:** IoT monitoring helps detect compromised devices and unusual behavior.

**Answer Options:**

**Option 1:** Continuous monitoring

**Option 2:** Periodic monitoring

**Option 3:** Anomaly detection

**Option 4:** No monitoring



---

## Section 19: AI/ML & Machine Learning Security

**Suggested Respondents:** AI/ML Security Lead, Data Science Lead

### Subsection 19.1: Model Security & Governance

#### Question 19.1.1

**Question:** Do you have AI/ML models in production?

**Type:** yes_no

**Weight:** 1

**Explanation:** AI/ML models in production require specialized security controls and governance.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*


#### Question 19.1.2

**Question:** Do you maintain a model registry with security controls?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Model registries provide centralized governance and security for ML artifacts.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 19.1.3

**Question:** How do you ensure model provenance and lineage?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Model provenance ensures traceability and helps identify security risks in the ML pipeline.

**Answer Options:**
**Option 1: Formal documented process**
*Basic Description:* Documented procedures and workflows

**Option 2: Automated system**
*Basic Description:* Using automation tools or platforms

**Option 3: Manual process**
*Basic Description:* Manual handling and tracking

**Option 4: Not currently implemented**
*Basic Description:* Not currently implemented



#### Question 19.1.4

**Question:** Do you conduct adversarial testing on ML models?

**Type:** multiple_choice

**Weight:** 5

**Explanation:** Adversarial testing identifies vulnerabilities to malicious inputs and model attacks.

**Answer Options:**

**Option 1:** Regular testing

**Option 2:** Occasional testing

**Option 3:** Only for critical models

**Option 4:** No testing


#### Question 19.1.5

**Question:** How do you protect against data poisoning attacks?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Data poisoning protection prevents malicious manipulation of training data.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 19.1.6

**Question:** Do you implement model explainability and bias detection?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Explainability and bias detection ensure responsible and secure AI deployment.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization




### Subsection 19.2: ML Pipeline Security

#### Question 19.2.1

**Question:** How do you secure your ML training pipeline?

**Type:** multiple_select

**Weight:** 5

**Explanation:** ML pipeline security prevents unauthorized access and resource abuse.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 19.2.2

**Question:** Do you protect feature stores and data privacy?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Feature store security protects sensitive data used in ML model training and inference.

**Answer Options:**
**Option 1: Fully implemented**
*Basic Description:* Fully implemented and operational

**Option 2: Partially implemented**
*Basic Description:* Partially implemented or in progress

**Option 3: Planned**
*Basic Description:* Planned but not yet implemented

**Option 4: Not implemented**
*Basic Description:* Not currently implemented

**Option 5: Not applicable**
*Basic Description:* Not applicable to our organization



#### Question 19.2.3

**Question:** How do you secure model inference endpoints?

**Type:** multiple_select

**Weight:** 5

**Explanation:** Inference endpoint security prevents abuse and protects model intellectual property.

**Answer Options:**
**Option 1: Encryption**
*Basic Description:* Data encryption at rest and in transit

**Option 2: Access controls**
*Basic Description:* Role-based access control and authentication

**Option 3: Network segmentation**
*Basic Description:* Isolated network zones

**Option 4: Monitoring and logging**
*Basic Description:* Continuous monitoring and audit logs

**Option 5: Security policies**
*Basic Description:* Documented security policies and procedures

**Option 6: Not currently secured**
*Basic Description:* No specific security measures



#### Question 19.2.4

**Question:** Do you monitor for model drift and anomalies?

**Type:** multiple_select

**Weight:** 3

**Explanation:** Model monitoring detects degradation and potential security issues in production.

**Answer Options:**
**Option 1: Yes** - This security control/practice is implemented in your organization
**Option 2: No** - This security control/practice is not currently implemented
*Note: If you select 'No', consider this an opportunity for security improvement.*

---
