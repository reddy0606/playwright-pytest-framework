# Playwright Pytest Automation Framework

This project is a UI automation framework built using:

- Playwright
- Pytest
- Page Object Model (POM)

## Features

- Reusable fixtures
- HTML reports
- JSON test data
- Page Object Model
- Parallel execution support
- Scalable framework structure

---

## Project Structure

```bash
playwright-pytest-framework/
│
├── pages/
├── tests/
├── utils/
├── test_data/
├── reports/
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
playwright install
```

---

## Run Tests

```bash
pytest
```

Run specific test:

```bash
pytest tests/test_login.py
```

Run parallel execution:

```bash
pytest -n 4
```

---

## Generate HTML Report

Report location:

```bash
reports/report.html
```

---

## Future Improvements

- Jenkins integration
- Docker support
- Allure reports
- API + UI automation
- Cross-browser execution