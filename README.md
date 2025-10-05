# Playwright in Python for TRG assignment

This project contains automated tests for a web application using **Python** and **Playwright**, organized following the **Page Object Model (POM)** pattern.

---

## 🔹 Prerequisites

Before running the tests, make sure you have installed:

- Python 3.13+  
- Git  

---

## 🔹 Installation

1. Clone the repository:

```bash
git clone https://github.com/MarkoBlago/py-playwright-trg
cd py-playwright-trg
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies and Playwright browsers:
```bash
pip install pytest playwright
pip install requests
playwright install
```
## 🔹 Running tests

Run tests with the -s flag to disable output capturing, which ensures that print() statements in tests are shown in the terminal.

```bash
pytest -s .\tests\test_trg_assignment.py  
```

## 🟡 NOTE: 
Do not move your mouse cursor while the test is running in headed mode 🙂

## 🔹 Project Structure
```bash
project/
│
├── pages/ # Page Object Model classes
│ ├── base_page.py
│ ├── home_page.py
│ ├── careers_page.py
│ └── lifeAtTRG_page.py
│
├── utils/ # Utility classes and methods
│ └── utility.py
│
├── tests/ # Pytest test files
│ └── test_trg_assignment.py
│
├── conftest.py # Pytest fixtures
├── playwright.config.py # Playwright configuration
└── README.md
```

## 🔹 How POM Works

• BasePage contains common methods for navigation and interaction

• Each page (HomePage, CareersPage, LifeAtTRGPage) inherits from BasePage and defines its own locators and methods

• Tests use page instances to perform actions

• Any functionality that is not page-specific, like generating random names, is located in utils/utility.py

