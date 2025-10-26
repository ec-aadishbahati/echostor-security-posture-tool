# E2E Testing Framework

Automated end-to-end testing framework for the Security Posture Assessment Tool.

## Overview

This testing framework provides comprehensive automated testing of the complete user journey from registration through assessment completion and report generation. It uses API-based testing for speed and reliability while simulating real user behavior.

## Features

- ✅ **Automated User Management**: Auto-generate test users or use custom credentials
- ✅ **Random Answer Generation**: Intelligently generates answers based on question types
- ✅ **Multiple Test Workflows**: Happy path, navigation, reports, and more
- ✅ **Comprehensive Coverage**: Tests all major features and edge cases
- ✅ **Easy to Run**: Simple command-line interface
- ✅ **Detailed Reporting**: Clear output showing test progress and results

## Directory Structure

```
tests/
├── utils/                      # Shared utilities
│   ├── api_client.py          # API wrapper with authentication
│   ├── answer_generator.py    # Random answer generation
│   └── user_factory.py        # Test user creation
├── workflows/                  # Test workflows
│   ├── test_happy_path.py     # Complete assessment flow
│   ├── test_navigation.py     # Navigation patterns
│   └── test_reports.py        # Report generation/download
├── config.py                   # Test configuration
├── run_tests.py               # Main test runner
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Prerequisites

1. **Backend Running**: The backend API must be running on `http://localhost:8000` (or custom URL)
2. **Python 3.8+**: Required for running tests
3. **Dependencies**: Install with `pip install -r requirements.txt`

## Installation

```bash
# Navigate to tests directory
cd tests/

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### Run All Tests (Recommended for first time)

```bash
python run_tests.py --all
```

This will:
1. Auto-generate a test user
2. Run all test workflows
3. Display detailed progress
4. Show summary of results

### Run Specific Workflow

```bash
# Happy Path (complete assessment flow)
python run_tests.py --workflow happy_path

# Navigation Testing
python run_tests.py --workflow navigation

# Reports Testing
python run_tests.py --workflow reports
```

### Use Custom User Credentials

```bash
# Run with specific user (will create if doesn't exist)
python run_tests.py --all --email test@example.com --password mypassword

# Run single workflow with custom user
python run_tests.py --workflow happy_path --email test@example.com --password secret123
```

### Use Custom API URL

```bash
# Test against different environment
python run_tests.py --all --api-url http://staging.example.com:8000
```

## Test Workflows

### 1. Happy Path (`test_happy_path.py`)

**Purpose**: Verify the complete user journey works end-to-end

**Flow**:
1. Register new user (or login)
2. Fetch assessment structure
3. Start new assessment
4. Answer all questions with random answers
5. Add random comments to ~30% of questions
6. Save consultation interest (200-300 words)
7. Complete assessment
8. Generate standard report
9. Wait for report generation
10. Download PDF report

**Runtime**: ~5-10 minutes (depends on number of questions)

**When to Run**: Before every deployment, on every PR

### 2. Navigation Testing (`test_navigation.py`)

**Purpose**: Test various navigation patterns and edge cases

**Tests**:
- **Section Jumping**: Answer questions in sections 1, 2, 3, then jump back to section 1
- **Answer Modification**: Change answers to previously answered questions
- **Random Navigation**: Answer 20 questions in completely random order

**Runtime**: ~3-5 minutes

**When to Run**: On every PR, before releases

### 3. Reports Testing (`test_reports.py`)

**Purpose**: Thoroughly test report generation and download

**Tests**:
- **Standard Report Generation**: Generate and verify standard PDF report
- **Report Download**: Download report and verify it's a valid PDF
- **Multiple Reports**: Generate multiple reports for same assessment

**Runtime**: ~5-10 minutes

**When to Run**: Before releases, nightly builds

## Configuration

Edit `config.py` to customize test behavior:

```python
# API Configuration
API_BASE_URL = "http://localhost:8000"
FRONTEND_BASE_URL = "http://localhost:3000"

# Test User Configuration
TEST_EMAIL = None  # Or set default test email
TEST_PASSWORD = None  # Or set default password

# Timeouts
DEFAULT_TIMEOUT = 30000  # 30 seconds
REPORT_GENERATION_TIMEOUT = 120000  # 2 minutes

# Cleanup
CLEANUP_AFTER_TEST = True  # Auto-cleanup test data
```

## Environment Variables

You can also configure via environment variables:

```bash
# API URLs
export TEST_API_URL=http://localhost:8000
export TEST_FRONTEND_URL=http://localhost:3000

# Test User
export TEST_EMAIL=test@example.com
export TEST_PASSWORD=mypassword

# Timeouts (milliseconds)
export TEST_TIMEOUT=30000
export TEST_REPORT_TIMEOUT=120000

# Cleanup
export TEST_CLEANUP=true
```

## Understanding Test Output

### Successful Test Run

```
================================================================================
HAPPY PATH E2E TEST
================================================================================

[1/8] Registering new user: test_abc123@echostor-test.com
✓ User registered successfully
  User ID: 550e8400-e29b-41d4-a716-446655440000

[2/8] Fetching assessment structure
✓ Structure loaded: 19 sections, 409 questions

[3/8] Starting new assessment
✓ Assessment started
  Assessment ID: 660e8400-e29b-41d4-a716-446655440000

[4/8] Answering all questions

  Section 1/19: Governance & Strategy
    Progress: 10/409 questions answered
    Progress: 20/409 questions answered
    ...

✓ All 409 questions answered
  Saving progress...
✓ Progress saved

[5/8] Saving consultation interest
  Interested: Yes
  Details: 250 words
✓ Consultation interest saved

[6/8] Completing assessment
✓ Assessment completed
  Status: completed
  Progress: 100%

[7/8] Generating report
✓ Report generation started
  Report ID: 770e8400-e29b-41d4-a716-446655440000
  Status: generating

[8/8] Waiting for report generation and downloading
  Report status: generating (waited 0s)
  Report status: generating (waited 5s)
  Report status: completed (waited 10s)
✓ Report downloaded successfully
  Size: 245678 bytes
  Saved to: tests/test_reports/test_report_660e8400.pdf

================================================================================
✅ HAPPY PATH TEST PASSED
================================================================================
```

### Failed Test Run

```
================================================================================
HAPPY PATH E2E TEST
================================================================================

[1/8] Registering new user: test_xyz789@echostor-test.com
✓ User registered successfully

[2/8] Fetching assessment structure
✓ Structure loaded: 19 sections, 409 questions

[3/8] Starting new assessment
❌ TEST FAILED: HTTPError: 500 Server Error: Internal Server Error

Traceback (most recent call last):
  File "workflows/test_happy_path.py", line 67, in run
    self.step_start_assessment()
  ...
```

## Troubleshooting

### Backend Not Running

**Error**: `Connection refused` or `Failed to establish connection`

**Solution**: Make sure the backend is running:
```bash
cd backend/
poetry run uvicorn app.main:app --reload
```

### Authentication Errors

**Error**: `401 Unauthorized`

**Solution**: 
- Check if user already exists (try with `--email` and `--password`)
- Verify backend authentication is working
- Check backend logs for errors

### Report Generation Timeout

**Error**: `Report generation timed out after 120 seconds`

**Solution**:
- Check backend logs for report generation errors
- Verify WeasyPrint is installed correctly
- Increase timeout in `config.py`: `REPORT_GENERATION_TIMEOUT = 300000`

### Import Errors

**Error**: `ModuleNotFoundError: No module named 'requests'`

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

## Advanced Usage

### Running Tests in CI/CD

```yaml
# .github/workflows/e2e-tests.yml
name: E2E Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Start Backend
        run: |
          cd backend
          poetry install
          poetry run uvicorn app.main:app &
          sleep 10
      
      - name: Run E2E Tests
        run: |
          cd tests
          pip install -r requirements.txt
          python run_tests.py --all
```

### Custom Test Workflow

Create your own test workflow in `workflows/`:

```python
# workflows/test_custom.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.api_client import APIClient
from utils.answer_generator import AnswerGenerator
from config import TestConfig

class CustomTest:
    def __init__(self):
        self.client = APIClient(TestConfig.API_BASE_URL)
        self.answer_gen = AnswerGenerator()
    
    def run(self):
        # Your custom test logic here
        pass

if __name__ == "__main__":
    test = CustomTest()
    test.run()
```

## Test Data

### Generated Test Users

Test users are automatically created with format:
- Email: `test_<random>@echostor-test.com`
- Password: 12-character random string
- Full Name: "Test User"

### Random Answers

The answer generator intelligently handles different question types:

- **Yes/No**: Randomly selects "yes" or "no"
- **Multiple Choice**: Randomly selects one option
- **Multiple Select**: Randomly selects 1 to N options

### Random Comments

- Generated for ~30% of questions
- 10-150 words
- Uses security-related vocabulary
- Grammatically correct sentences

### Consultation Details

- 200-300 words (as required)
- Security-focused content
- Covers various consultation topics

## Best Practices

1. **Run Tests Regularly**: Run on every PR and before deployments
2. **Check Logs**: Always check backend logs if tests fail
3. **Clean Up**: Tests auto-cleanup, but verify no orphaned data
4. **Use Custom Users**: For debugging, use `--email` and `--password`
5. **Monitor Performance**: Track test execution time over releases
6. **Review Reports**: Occasionally review generated PDFs manually

## Future Enhancements

Planned improvements:
- [ ] UI testing with Playwright
- [ ] Stress testing (concurrent users)
- [ ] Save & Resume workflow
- [ ] Validation testing workflow
- [ ] Performance benchmarking
- [ ] Test report generation (HTML/JSON)
- [ ] Screenshot capture on failures
- [ ] Video recording of test runs

## Support

For issues or questions:
1. Check backend logs: `backend/logs/`
2. Review test output carefully
3. Try with `--email` and `--password` for debugging
4. Check this README for troubleshooting tips

## License

Same as main project.
