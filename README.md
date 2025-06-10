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

- python -m pytest tests/ --verbose
- python -m pytest tests/ --quiet 
- python -m pytest tests/ --exitfirst
- python -m pytest tests/ --maxfail=[num of failed tests wanted before exiting]
- python -m pytest tests/ --junit-xml reports/test.xml

---

- pytest.ini 

---

## Filtering Tests

- -k
- 

---

## Plugins

_This section will introduce useful plugins like `pytest-cov` for test coverage and how to install and use them._

---

## API Testing

_This section will show how to test RESTful APIs using `requests` + `pytest`, including response validation and error handling._

---

## UI Testing

_This section will demonstrate basic Selenium-based UI testing within a `pytest` test suite, covering DOM assertions and form validations._