# Quick Start Guide - E2E Testing

## 5-Minute Setup

### Step 1: Start the Backend

```bash
# Terminal 1: Start backend
cd backend/
poetry install
poetry run uvicorn app.main:app --reload
```

Wait for: `Application startup complete`

### Step 2: Install Test Dependencies

```bash
# Terminal 2: Install test dependencies
cd tests/
pip install -r requirements.txt
```

### Step 3: Run Your First Test

```bash
# Run the happy path test
python run_tests.py --workflow happy_path
```

That's it! The test will:
- Create a test user automatically
- Complete an entire assessment with random answers
- Generate and download a report
- Show you the results

## Common Commands

```bash
# Run all tests
python run_tests.py --all

# Run specific test
python run_tests.py --workflow navigation
python run_tests.py --workflow reports

# Use your own test user
python run_tests.py --workflow happy_path --email mytest@example.com --password mypassword
```

## What to Expect

### Happy Path Test (~5-10 minutes)
```
[1/8] Registering new user
[2/8] Fetching assessment structure
[3/8] Starting new assessment
[4/8] Answering all questions (this takes a few minutes)
[5/8] Saving consultation interest
[6/8] Completing assessment
[7/8] Generating report
[8/8] Waiting for report and downloading

✅ HAPPY PATH TEST PASSED
```

### Navigation Test (~3-5 minutes)
```
[Test 1] Section Jumping
[Test 2] Answer Modification
[Test 3] Random Navigation Pattern

✅ NAVIGATION TEST PASSED
```

### Reports Test (~5-10 minutes)
```
[Setup] Creating completed assessment
[Test 1] Standard Report Generation
[Test 2] Report Download
[Test 3] Multiple Report Generations

✅ REPORTS TEST PASSED
```

## Troubleshooting

### "Connection refused"
→ Backend not running. Start it with:
```bash
cd backend && poetry run uvicorn app.main:app --reload
```

### "Module not found"
→ Dependencies not installed. Run:
```bash
pip install -r requirements.txt
```

### Test takes too long
→ Normal! The happy path test answers 400+ questions. Grab a coffee ☕

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Create custom test workflows in `workflows/`
- Integrate tests into your CI/CD pipeline
- Run tests before every deployment

## Tips

💡 **Use custom credentials for debugging**: `--email test@example.com --password mypass`

💡 **Check backend logs** if tests fail: `backend/logs/`

💡 **Generated reports** are saved to: `tests/test_reports/`

💡 **Run tests regularly** to catch regressions early
