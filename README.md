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
