"""Random answer generation for testing"""
import random
from typing import Any, Dict, List, Optional


class AnswerGenerator:
    """Generate random answers based on question types"""
    
    @staticmethod
    def generate_answer(question: Dict[str, Any]) -> Any:
        """Generate a random answer based on question type"""
        question_type = question.get('type')
        options = question.get('options', [])
        
        if not options:
            return None
        
        if question_type == 'yes_no':
            return random.choice([opt['value'] for opt in options])
        
        elif question_type == 'multiple_choice':
            return random.choice([opt['value'] for opt in options])
        
        elif question_type == 'multiple_select':
            all_values = [opt['value'] for opt in options]
            num_to_select = random.randint(1, len(all_values))
            return random.sample(all_values, num_to_select)
        
        return None
    
    @staticmethod
    def generate_comment(min_words: int = 10, max_words: int = 150) -> str:
        """Generate a random comment"""
        words = [
            "security", "implementation", "process", "system", "network",
            "data", "protection", "monitoring", "compliance", "policy",
            "access", "control", "authentication", "encryption", "backup",
            "recovery", "incident", "response", "vulnerability", "assessment",
            "risk", "management", "audit", "review", "testing", "validation",
            "documentation", "training", "awareness", "procedure", "standard",
            "framework", "guideline", "requirement", "measure", "control",
            "mechanism", "solution", "approach", "strategy", "plan"
        ]
        
        num_words = random.randint(min_words, max_words)
        comment_words = random.choices(words, k=num_words)
        
        comment = ' '.join(comment_words)
        return comment.capitalize() + '.'
    
    @staticmethod
    def should_add_comment(probability: float = 0.3) -> bool:
        """Decide whether to add a comment (30% chance by default)"""
        return random.random() < probability
    
    @staticmethod
    def generate_consultation_details(min_words: int = 200, max_words: int = 300) -> str:
        """Generate consultation details (200-300 words)"""
        topics = [
            "We need assistance with implementing a comprehensive security framework",
            "Our organization requires guidance on cloud security best practices",
            "We are looking to improve our incident response capabilities",
            "We need help with compliance requirements and audit preparation",
            "Our team needs training on security awareness and best practices",
            "We want to establish a robust vulnerability management program",
            "We need consultation on data protection and privacy regulations",
            "Our organization is planning a security architecture review",
            "We require assistance with network segmentation and access controls",
            "We need guidance on implementing zero trust security model"
        ]
        
        details = [
            "security posture assessment", "risk management framework",
            "compliance requirements", "security controls implementation",
            "incident response planning", "disaster recovery procedures",
            "business continuity planning", "security awareness training",
            "vulnerability management", "penetration testing", "security audits",
            "access control policies", "data encryption strategies",
            "network security architecture", "cloud security configuration",
            "identity and access management", "security monitoring solutions",
            "threat detection capabilities", "security operations center",
            "security governance framework", "third-party risk management"
        ]
        
        consultation = random.choice(topics) + ". "
        
        current_words = len(consultation.split())
        while current_words < min_words:
            detail = random.choice(details)
            consultation += f"We are particularly interested in {detail}. "
            current_words = len(consultation.split())
        
        words = consultation.split()
        if len(words) > max_words:
            words = words[:max_words]
            consultation = ' '.join(words) + '.'
        
        return consultation
