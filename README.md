# Pytest Foundational Knowledge
The goal of this project is to demonstrate strong proficiency in automated testing using `pytest` through hands-on examples. These include unit testing, fixtures, test filtering, configuration, and integration with API and UI workflows.

All tests will be written for the **AI-Language-Tutor** application, which includes both frontend and backend components.

- 🔗 **Frontend Repository:** [ai-language-tutor-frontend](https://github.com/bryan-melo/ai-language-tutor-frontend)  
- 🔗 **Backend Repository:** [ai-language-tutor-backend](https://github.com/bryan-melo/ai-language-tutor-backend)  
- 🌐 **Hosted App:** [Live Fullstack App](https://ai-language-tutor-frontend-sable.vercel.app/)

---

## 📘 Table of Contents

1. [Unit Testing with Classes](#unit-testing-with-classes)  
2. [Using Fixtures](#using-fixtures)  
3. [Pytest Commands & Configuration](#pytest-commands--configuration)  
4. [Filtering Tests](#filtering-tests)  
5. [Plugins](#plugins)  
6. [API Testing](#api-testing)  
7. [UI Testing](#ui-testing)

---

## Unit Testing with Classes

_This section will cover how to structure unit tests using Python classes with `pytest`, including setup and teardown methods._

---

## Using Fixtures

_This section will explain how to use `@pytest.fixture` to share setup logic across multiple test functions and manage test dependencies._

---

## Pytest Commands & Configuration

### Pytest Commands
```bash
   python -m pytest tests/ --verbose
   - python -m pytest tests/ --quiet 
   - python -m pytest tests/ --exitfirst
   - python -m pytest tests/ --maxfail=[num of failed tests wanted before exiting]
   - python -m pytest tests/ --junit-xml reports/test.xml
```

### Pytest Configuration File
```bash
   - pytest.ini 
```

---

## Filtering Tests

### Using -K to filter tests
```bash
- -k
```

---

## Plugins

### Generated HTML test results
```bash
   pip install pytest-html
   python -m pytest --html=[directory]/[filename].html
```

### Coverage.py
```bash
   pip install pytest-cov
   python -m pytest --cov=[directory]
```

### Coverage HTML Test Reports
```bash
   python -m pytest --cov=stuff --cov-report=html:[directory]/[filename]  
```

### Coverage Branch Test
```bash
   python -m pytest --cov=stuff --cov-branch
```

### Pytest-XDist
```bash
   pip install pytest-xdist
   python -m pytest -n 3
```

### Behavior-Driven Development
- BDD

---

## API Testing

### Requests Package
```bash
   pip install requests
```

---

## UI Testing

### Playwright
```bash
   pip install playwright
   pip install pytest-playwright
   playwright install
```

```bash
   python -m pytest [directory]/[filename] --headed --slowmo 1000
```
   