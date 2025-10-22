# 📝 Task Manager CLI App (with SQLAlchemy + Pytest + Allure)
[![Python Tests](https://github.com/SamoylovRoman/Pytest_TaskManager/actions/workflows/python-tests.yml/badge.svg?branch=master)](https://github.com/SamoylovRoman/Pytest_TaskManager/actions)
[![codecov](https://codecov.io/gh/SamoylovRoman/Pytest_TaskManager/branch/master/graph/badge.svg)](https://codecov.io/gh/SamoylovRoman/Pytest_TaskManager)

A simple command-line to-do app built with Python, featuring:

- 🗃️ **SQLite** + **SQLAlchemy ORM** for storage
- 🧪 **pytest** + **pytest-cov** for test execution and coverage
- 📊 **Allure** for beautiful test reporting
- 💻 Minimal **CLI interface** using `input()` and `print()`

---

## 🚀 Features

- ➕ Add tasks
- 📋 List tasks
- ✅ Mark tasks as done
- ❌ Delete tasks
- 🧪 Unit + CLI tests with full test coverage
- 🧼 In-memory test DB setup with `pytest` fixtures
- 📊 Visual test reports with **Allure**

---

## 📦 Requirements

- Python 3.10+
- Install dependencies:

```bash
pip install -r requirements.txt
