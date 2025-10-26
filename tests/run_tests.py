#!/usr/bin/env python3
"""Main test runner for E2E tests"""
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from workflows.test_happy_path import HappyPathTest
from workflows.test_navigation import NavigationTest
from workflows.test_reports import ReportsTest
from config import TestConfig


def run_all_tests(email=None, password=None):
    """Run all test workflows"""
    print("\n" + "=" * 80)
    print("RUNNING ALL E2E TESTS")
    print("=" * 80)
    
    results = {}
    
    print("\n\n")
    test = HappyPathTest(email=email, password=password)
    results['happy_path'] = test.run()
    
    print("\n\n")
    test = NavigationTest(email=email, password=password)
    results['navigation'] = test.run()
    
    print("\n\n")
    test = ReportsTest(email=email, password=password)
    results['reports'] = test.run()
    
    print("\n\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    
    for name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{name.upper()}: {status}")
    
    all_passed = all(results.values())
    print("\n" + "=" * 80)
    if all_passed:
        print("✅ ALL TESTS PASSED")
    else:
        print("❌ SOME TESTS FAILED")
    print("=" * 80)
    
    return all_passed


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Run E2E tests for Security Posture Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_tests.py --all
  
  python run_tests.py --workflow happy_path
  
  python run_tests.py --all --email test@example.com --password mypassword
  
  python run_tests.py --workflow navigation --email test@example.com --password mypassword

Available workflows:
  - happy_path: Complete assessment flow (register → answer → complete → report)
  - navigation: Test navigation patterns (section jumping, answer modification)
  - reports: Test report generation and download
        """
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Run all test workflows'
    )
    
    parser.add_argument(
        '--workflow',
        choices=['happy_path', 'navigation', 'reports'],
        help='Run specific workflow'
    )
    
    parser.add_argument(
        '--email',
        help='Test user email (optional, will generate random if not provided)'
    )
    
    parser.add_argument(
        '--password',
        help='Test user password (optional, will generate random if not provided)'
    )
    
    parser.add_argument(
        '--api-url',
        default='http://localhost:8000',
        help='API base URL (default: http://localhost:8000)'
    )
    
    args = parser.parse_args()
    
    if args.api_url:
        TestConfig.API_BASE_URL = args.api_url
    
    TestConfig.ensure_dirs()
    
    if not args.all and not args.workflow:
        parser.error("Must specify either --all or --workflow")
    
    success = False
    
    if args.all:
        success = run_all_tests(email=args.email, password=args.password)
    
    elif args.workflow == 'happy_path':
        test = HappyPathTest(email=args.email, password=args.password)
        success = test.run()
    
    elif args.workflow == 'navigation':
        test = NavigationTest(email=args.email, password=args.password)
        success = test.run()
    
    elif args.workflow == 'reports':
        test = ReportsTest(email=args.email, password=args.password)
        success = test.run()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
