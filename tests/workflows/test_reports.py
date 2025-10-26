"""Reports Testing - Test report generation and download"""
import sys
import os
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.api_client import APIClient
from utils.answer_generator import AnswerGenerator
from utils.user_factory import UserFactory
from config import TestConfig


class ReportsTest:
    """Test report generation and download"""
    
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
        """Run report tests"""
        print("=" * 80)
        print("REPORTS E2E TEST")
        print("=" * 80)
        
        try:
            self.setup_completed_assessment()
            
            self.test_standard_report()
            
            self.test_report_download()
            
            self.test_multiple_reports()
            
            print("\n" + "=" * 80)
            print("✅ REPORTS TEST PASSED")
            print("=" * 80)
            return True
            
        except Exception as e:
            print(f"\n❌ TEST FAILED: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    def setup_completed_assessment(self):
        """Setup: Create and complete an assessment"""
        print(f"\n[Setup] Creating completed assessment")
        
        if self.is_new_user:
            self.client.register(self.email, self.password)
        else:
            self.client.login(self.email, self.password)
        
        structure = self.client.get_structure()
        response = self.client.start_assessment()
        self.assessment_id = response['data']['id']
        
        total_questions = sum(len(s['questions']) for s in structure['data']['sections'])
        answered = 0
        
        for section in structure['data']['sections']:
            for question in section['questions']:
                answer = self.answer_gen.generate_answer(question)
                self.client.submit_response(self.assessment_id, question['id'], answer)
                answered += 1
                
                if answered % 50 == 0:
                    print(f"  Progress: {answered}/{total_questions} questions")
        
        details = self.answer_gen.generate_consultation_details()
        self.client.save_consultation(self.assessment_id, True, details)
        self.client.complete_assessment(self.assessment_id)
        
        print(f"✓ Assessment completed with {total_questions} questions answered")
    
    def test_standard_report(self):
        """Test standard report generation"""
        print(f"\n[Test 1] Standard Report Generation")
        
        response = self.client.generate_report(self.assessment_id, "standard")
        report_id = response['data']['id']
        
        print(f"  ✓ Report generation initiated")
        print(f"    Report ID: {report_id}")
        print(f"    Status: {response['data']['status']}")
        
        status = self.wait_for_report(report_id)
        
        if status == 'completed':
            print(f"  ✓ Report generated successfully")
        else:
            raise Exception(f"Report generation failed with status: {status}")
    
    def test_report_download(self):
        """Test report download"""
        print(f"\n[Test 2] Report Download")
        
        reports = self.client.get_reports(self.assessment_id)
        
        if not reports['data']:
            raise Exception("No reports found")
        
        report = reports['data'][0]
        report_id = report['id']
        
        pdf_content = self.client.download_report(report_id)
        
        if not pdf_content.startswith(b'%PDF'):
            raise Exception("Downloaded file is not a valid PDF")
        
        TestConfig.ensure_dirs()
        output_path = os.path.join(
            TestConfig.REPORTS_DIR,
            f"test_report_{report_id}.pdf"
        )
        with open(output_path, 'wb') as f:
            f.write(pdf_content)
        
        print(f"  ✓ Report downloaded successfully")
        print(f"    Size: {len(pdf_content)} bytes")
        print(f"    Saved to: {output_path}")
    
    def test_multiple_reports(self):
        """Test generating multiple reports"""
        print(f"\n[Test 3] Multiple Report Generations")
        
        report_ids = []
        
        for i in range(2):
            response = self.client.generate_report(self.assessment_id, "standard")
            report_id = response['data']['id']
            report_ids.append(report_id)
            print(f"  Report {i+1} generation initiated: {report_id}")
        
        for i, report_id in enumerate(report_ids, 1):
            status = self.wait_for_report(report_id)
            if status == 'completed':
                print(f"  ✓ Report {i} completed")
            else:
                raise Exception(f"Report {i} failed with status: {status}")
        
        print(f"✓ All reports generated successfully")
    
    def wait_for_report(self, report_id: str, max_wait: int = 120) -> str:
        """Wait for report to complete"""
        wait_interval = 5
        elapsed = 0
        
        while elapsed < max_wait:
            reports = self.client.get_reports(self.assessment_id)
            
            for report in reports['data']:
                if report['id'] == report_id:
                    status = report['status']
                    
                    if status in ['completed', 'failed']:
                        return status
            
            time.sleep(wait_interval)
            elapsed += wait_interval
        
        raise Exception(f"Report generation timed out after {max_wait} seconds")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Reports E2E Test')
    parser.add_argument('--email', help='Test user email (optional)')
    parser.add_argument('--password', help='Test user password (optional)')
    args = parser.parse_args()
    
    test = ReportsTest(email=args.email, password=args.password)
    success = test.run()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
