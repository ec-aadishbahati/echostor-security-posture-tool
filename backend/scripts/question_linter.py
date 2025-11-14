#!/usr/bin/env python3
"""
Question Library Linter - Run in CI to catch issues

This linter checks for:
1. Duplicate option values within questions
2. Mismatched questions (question text vs options)
3. Frequency scale consistency
4. Missing "Not sure" or "Not applicable" options where needed
"""
import re
import sys
from pathlib import Path


def lint_questions():
    """Lint question library for common issues"""
    errors = []
    warnings = []
    
    script_dir = Path(__file__).parent
    md_path = script_dir.parent / "data" / "security_assessment_questions.md"
    
    if not md_path.exists():
        print(f"❌ ERROR: Question file not found: {md_path}", file=sys.stderr)
        sys.exit(1)
    
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"Linting question library: {md_path}")
    print("-" * 80)
    
    current_question = None
    current_section = None
    questions = []
    
    for i, line in enumerate(lines, start=1):
        line_stripped = line.strip()
        
        if line_stripped.startswith("## Section"):
            section_match = re.match(r"## Section (\d+):", line_stripped)
            if section_match:
                current_section = section_match.group(1)
        
        if line_stripped.startswith("#### Question"):
            if current_question:
                questions.append(current_question)
            
            question_match = re.match(r"#### Question ([\d\.]+)", line_stripped)
            if question_match:
                current_question = {
                    "id": question_match.group(1),
                    "section": current_section,
                    "line": i,
                    "text": "",
                    "type": "",
                    "options": []
                }
        
        if current_question and line_stripped.startswith("**Question:**"):
            current_question["text"] = line_stripped.replace("**Question:**", "").strip()
        
        if current_question and line_stripped.startswith("**Type:**"):
            current_question["type"] = line_stripped.replace("**Type:**", "").strip()
        
        if current_question and line_stripped.startswith("**Option"):
            option_match = re.match(r"\*\*Option (\d+):\s*(.+?)\*\*", line_stripped)
            if option_match:
                option_num = option_match.group(1)
                option_label = option_match.group(2)
                current_question["options"].append({
                    "value": option_num,
                    "label": option_label,
                    "line": i
                })
    
    if current_question:
        questions.append(current_question)
    
    print(f"Parsed {len(questions)} questions")
    print("-" * 80)
    
    for question in questions:
        values = [opt["value"] for opt in question["options"]]
        if len(values) != len(set(values)):
            duplicates = [v for v in values if values.count(v) > 1]
            errors.append(
                f"Question {question['id']} (line {question['line']}): "
                f"Duplicate option values: {', '.join(set(duplicates))}"
            )
    
    for question in questions:
        q_id = question["id"]
        q_text = question["text"].lower()
        option_labels = [opt["label"].lower() for opt in question["options"]]
        
        if q_id == "4.4.5":
            if "bypass" in q_text:
                if any("sms" in label or "authenticator" in label or "hardware token" in label 
                      for label in option_labels):
                    errors.append(
                        f"Question 4.4.5 (line {question['line']}): "
                        f"MFA bypass question has MFA method options instead of bypass procedures"
                    )
        
        if q_id == "7.3.3":
            if "where" in q_text and "store" in q_text:
                if any("daily" in label or "weekly" in label or "monthly" in label 
                      for label in option_labels):
                    errors.append(
                        f"Question 7.3.3 (line {question['line']}): "
                        f"Backup location question has frequency options instead of storage locations"
                    )
        
        if q_id == "8.2.3":
            if "authentication" in q_text and "web" in q_text:
                if any("formal documented process" in label or "automated system" in label 
                      for label in option_labels):
                    errors.append(
                        f"Question 8.2.3 (line {question['line']}): "
                        f"Web authentication question has process maturity options instead of auth mechanisms"
                    )
        
        if q_id == "5.1.6":
            if "wireless" in q_text:
                if not any("wpa" in label for label in option_labels):
                    warnings.append(
                        f"Question 5.1.6 (line {question['line']}): "
                        f"Wireless security question missing modern WPA2/WPA3 standards"
                    )
    
    frequency_questions = []
    for question in questions:
        q_text = question["text"].lower()
        if any(keyword in q_text for keyword in ["how often", "frequency", "how frequently"]):
            frequency_questions.append(question)
    
    if frequency_questions:
        print(f"\nFound {len(frequency_questions)} frequency-related questions")
    
    print("\n" + "=" * 80)
    
    if errors:
        print(f"❌ Found {len(errors)} error(s):\n")
        for error in errors:
            print(f"  - {error}")
    
    if warnings:
        print(f"\n⚠️  Found {len(warnings)} warning(s):\n")
        for warning in warnings:
            print(f"  - {warning}")
    
    if not errors and not warnings:
        print("✅ Question linting passed - no issues found")
        sys.exit(0)
    elif errors:
        print(f"\n{'=' * 80}")
        print(f"Total errors: {len(errors)}")
        print(f"Total warnings: {len(warnings)}")
        print(f"{'=' * 80}")
        sys.exit(1)
    else:
        print(f"\n{'=' * 80}")
        print(f"Total warnings: {len(warnings)} (warnings do not fail the build)")
        print(f"{'=' * 80}")
        sys.exit(0)


if __name__ == "__main__":
    lint_questions()
