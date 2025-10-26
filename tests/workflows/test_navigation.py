"""Navigation Testing - Test various navigation patterns"""
import sys
import os
import random
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.api_client import APIClient
from utils.answer_generator import AnswerGenerator
from utils.user_factory import UserFactory
from config import TestConfig


class NavigationTest:
    """Test navigation patterns"""
    
    def __init__(self, email: str = None, password: str = None):
        self.config = TestConfig()
        self.client = APIClient(self.config.API_BASE_URL)
        self.answer_gen = AnswerGenerator()
        
        if email and password:
            self.email = email
            self.password = password
            self.is_new_user = False
        else:
            user = UserFactory.create_test_user()
            self.email = user['email']
            self.password = user['password']
            self.is_new_user = True
        
        self.assessment_id = None
    
    def run(self):
        """Run navigation tests"""
        print("=" * 80)
        print("NAVIGATION E2E TEST")
        print("=" * 80)
        
        try:
            if self.is_new_user:
                self.client.register(self.email, self.password)
            else:
                self.client.login(self.email, self.password)
            
            structure = self.client.get_structure()
            response = self.client.start_assessment()
            self.assessment_id = response['data']['id']
            
            self.test_section_jumping(structure)
            
            self.test_answer_modification(structure)
            
            self.test_random_navigation(structure)
            
            print("\n" + "=" * 80)
            print("✅ NAVIGATION TEST PASSED")
            print("=" * 80)
            return True
            
        except Exception as e:
            print(f"\n❌ TEST FAILED: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    def test_section_jumping(self, structure):
        """Test jumping between sections"""
        print(f"\n[Test 1] Section Jumping")
        
        sections = structure['data']['sections']
        
        for i in range(min(3, len(sections))):
            section = sections[i]
            question = section['questions'][0]
            
            answer = self.answer_gen.generate_answer(question)
            self.client.submit_response(self.assessment_id, question['id'], answer)
            print(f"  ✓ Answered first question in section {i+1}: {section['title']}")
        
        section = sections[0]
        question = section['questions'][1] if len(section['questions']) > 1 else section['questions'][0]
        answer = self.answer_gen.generate_answer(question)
        self.client.submit_response(self.assessment_id, question['id'], answer)
        print(f"  ✓ Jumped back to section 1 and answered another question")
        
        print(f"✓ Section jumping test passed")
    
    def test_answer_modification(self, structure):
        """Test modifying previously answered questions"""
        print(f"\n[Test 2] Answer Modification")
        
        section = structure['data']['sections'][0]
        question = section['questions'][0]
        
        answer1 = self.answer_gen.generate_answer(question)
        self.client.submit_response(self.assessment_id, question['id'], answer1)
        print(f"  ✓ Initial answer submitted")
        
        answer2 = self.answer_gen.generate_answer(question)
        self.client.submit_response(self.assessment_id, question['id'], answer2)
        print(f"  ✓ Answer modified")
        
        print(f"✓ Answer modification test passed")
    
    def test_random_navigation(self, structure):
        """Test random navigation pattern"""
        print(f"\n[Test 3] Random Navigation Pattern")
        
        sections = structure['data']['sections']
        
        for i in range(20):
            section = random.choice(sections)
            question = random.choice(section['questions'])
            
            answer = self.answer_gen.generate_answer(question)
            self.client.submit_response(self.assessment_id, question['id'], answer)
            
            if (i + 1) % 5 == 0:
                print(f"  Progress: {i+1}/20 random questions answered")
        
        print(f"✓ Random navigation test passed")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Navigation E2E Test')
    parser.add_argument('--email', help='Test user email (optional)')
    parser.add_argument('--password', help='Test user password (optional)')
    args = parser.parse_args()
    
    test = NavigationTest(email=args.email, password=args.password)
    success = test.run()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
