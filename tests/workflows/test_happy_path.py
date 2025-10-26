"""Happy Path E2E Test - Complete assessment flow"""
import sys
import os
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.api_client import APIClient
from utils.answer_generator import AnswerGenerator
from utils.user_factory import UserFactory
from config import TestConfig


class HappyPathTest:
    """Test the complete happy path flow"""
    
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
        self.report_id = None
    
    def run(self):
        """Run the complete happy path test"""
        print("=" * 80)
        print("HAPPY PATH E2E TEST")
        print("=" * 80)
        
        try:
            if self.is_new_user:
                self.step_register()
            else:
                self.step_login()
            
            structure = self.step_get_structure()
            
            self.step_start_assessment()
            
            self.step_answer_questions(structure)
            
            self.step_save_consultation()
            
            self.step_complete_assessment()
            
            self.step_generate_report()
            
            self.step_download_report()
            
            print("\n" + "=" * 80)
            print("✅ HAPPY PATH TEST PASSED")
            print("=" * 80)
            return True
            
        except Exception as e:
            print(f"\n❌ TEST FAILED: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    def step_register(self):
        """Step 1: Register new user"""
        print(f"\n[1/8] Registering new user: {self.email}")
        response = self.client.register(self.email, self.password)
        print(f"✓ User registered successfully")
        print(f"  User ID: {response.get('user', {}).get('id')}")
    
    def step_login(self):
        """Step 1: Login existing user"""
        print(f"\n[1/8] Logging in user: {self.email}")
        response = self.client.login(self.email, self.password)
        print(f"✓ User logged in successfully")
    
    def step_get_structure(self):
        """Step 2: Get assessment structure"""
        print(f"\n[2/8] Fetching assessment structure")
        structure = self.client.get_structure()
        num_sections = len(structure['data']['sections'])
        total_questions = sum(len(s['questions']) for s in structure['data']['sections'])
        print(f"✓ Structure loaded: {num_sections} sections, {total_questions} questions")
        return structure
    
    def step_start_assessment(self):
        """Step 3: Start new assessment"""
        print(f"\n[3/8] Starting new assessment")
        response = self.client.start_assessment()
        self.assessment_id = response['data']['id']
        print(f"✓ Assessment started")
        print(f"  Assessment ID: {self.assessment_id}")
    
    def step_answer_questions(self, structure):
        """Step 4: Answer all questions"""
        print(f"\n[4/8] Answering all questions")
        
        total_questions = sum(len(s['questions']) for s in structure['data']['sections'])
        answered = 0
        
        for section_idx, section in enumerate(structure['data']['sections'], 1):
            section_name = section['title']
            print(f"\n  Section {section_idx}/{len(structure['data']['sections'])}: {section_name}")
            
            for question in section['questions']:
                answer = self.answer_gen.generate_answer(question)
                
                comment = None
                if self.answer_gen.should_add_comment():
                    comment = self.answer_gen.generate_comment()
                
                self.client.submit_response(
                    self.assessment_id,
                    question['id'],
                    answer,
                    comment
                )
                
                answered += 1
                if answered % 10 == 0:
                    print(f"    Progress: {answered}/{total_questions} questions answered")
        
        print(f"\n✓ All {total_questions} questions answered")
        
        print(f"  Saving progress...")
        self.client.save_progress(self.assessment_id)
        print(f"✓ Progress saved")
    
    def step_save_consultation(self):
        """Step 5: Save consultation interest"""
        print(f"\n[5/8] Saving consultation interest")
        
        interested = True  # For happy path, always interested
        details = None
        
        if interested:
            details = self.answer_gen.generate_consultation_details()
            print(f"  Interested: Yes")
            print(f"  Details: {len(details.split())} words")
        else:
            print(f"  Interested: No")
        
        self.client.save_consultation(self.assessment_id, interested, details)
        print(f"✓ Consultation interest saved")
    
    def step_complete_assessment(self):
        """Step 6: Complete assessment"""
        print(f"\n[6/8] Completing assessment")
        response = self.client.complete_assessment(self.assessment_id)
        print(f"✓ Assessment completed")
        print(f"  Status: {response['data']['status']}")
        print(f"  Progress: {response['data']['progress_percentage']}%")
    
    def step_generate_report(self):
        """Step 7: Generate report"""
        print(f"\n[7/8] Generating report")
        response = self.client.generate_report(self.assessment_id, "standard")
        self.report_id = response['data']['id']
        print(f"✓ Report generation started")
        print(f"  Report ID: {self.report_id}")
        print(f"  Status: {response['data']['status']}")
    
    def step_download_report(self):
        """Step 8: Wait for report and download"""
        print(f"\n[8/8] Waiting for report generation and downloading")
        
        max_wait = 120  # 2 minutes
        wait_interval = 5  # Check every 5 seconds
        elapsed = 0
        
        while elapsed < max_wait:
            reports = self.client.get_reports(self.assessment_id)
            
            if reports['data']:
                report = reports['data'][0]
                status = report['status']
                
                print(f"  Report status: {status} (waited {elapsed}s)")
                
                if status == 'completed':
                    pdf_content = self.client.download_report(self.report_id)
                    
                    TestConfig.ensure_dirs()
                    output_path = os.path.join(
                        TestConfig.REPORTS_DIR,
                        f"test_report_{self.assessment_id}.pdf"
                    )
                    with open(output_path, 'wb') as f:
                        f.write(pdf_content)
                    
                    print(f"✓ Report downloaded successfully")
                    print(f"  Size: {len(pdf_content)} bytes")
                    print(f"  Saved to: {output_path}")
                    return
                
                elif status == 'failed':
                    raise Exception("Report generation failed")
            
            time.sleep(wait_interval)
            elapsed += wait_interval
        
        raise Exception(f"Report generation timed out after {max_wait} seconds")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Happy Path E2E Test')
    parser.add_argument('--email', help='Test user email (optional)')
    parser.add_argument('--password', help='Test user password (optional)')
    args = parser.parse_args()
    
    test = HappyPathTest(email=args.email, password=args.password)
    success = test.run()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
