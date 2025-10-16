# Online Bookstore Testing

This repository contains a comprehensive automated test suite for the Online Bookstore web application built with Flask. The suite validates both functional requirements and non‑functional requirements, ensuring the system is correct, performant, and audit‑ready.

Functional Requirements Covered:

FR‑002: Shopping Cart

FR‑003: Checkout Process

FR‑004: Payment Processing

FR‑006: Account Management


Non‑Functional Requirements Covered
Security: Authentication, authorization, and input validation tests.

Performance: Benchmarks using timeit and scalability profiling with cProfile.

Usability & Responsiveness: Layout and rendering checks across devices.

Maintainability & Auditability: Traceable test IDs, structured documentation, and reproducible environments.

The test framework is fully integrated with GitHub Actions CI/CD, ensuring every code change is automatically validated and results are logged for traceability.




## CI/CD Integration

![CI](https://github.com/AnnieCodes8/Final_Assessment/actions/workflows/python_tests.yml/badge.svg)

This repository is integrated with GitHub Actions to ensure continuous validation of the system. The workflow file is located at `.github/workflows/python_tests.yml` and is triggered automatically on every push or pull request to the `main` branch.

The workflow file is located at .github/workflows/python_tests.yml and is triggered automatically on every push or pull request to the main branch.

## Workflow Steps
Checkout: Retrieves the latest repository state.

Set up Python: Provisions a fresh Python environment (3.13).

Install dependencies: Installs all packages from requirements.txt.

Run tests: Executes the full pytest suite in the tests/ directory.

## Benefits
Continuous Validation: Every commit is tested automatically.

Audit Readiness: Results are logged in the Actions tab and can be exported.

Early Bug Detection: Failures are caught immediately, reducing integration risk.

The badge above reflects the live pipeline status:

    Green = all tests passing

    Red = one or more tests failing



## Naming Coventions
FR‑xxx = Functional Requirement
TS‑xxx = Test Scenario
UT‑xxx / IT‑xxx / PT‑xxx / PROF‑xxx = Unit, Integration, Performance, and Profiling test cases


## Prerequisites
Before running the project locally, please ensure you have:

    - Python 3.10 or higher installed
    - Git installed.
    - A virtual environment tool available (like venv or virtualenv)

## Creating and Activating a Virtual Environment
It’s best practice to run the project inside a virtual environment so dependencies don’t interfere with your global Python setup. Here's how to launch your own:
1. Open a terminal in your VS Code.
2. Clone or copy the application files into a short path locally. For example:
    `C:\dev\Final_Assessment`
3. Create the virtual environment by typing the following in your terminal:
    `python -m venv venv`
4. Activate the environment:

    Linux/macOS: `source venv/bin/activate`
    Windows (CMD): `venv\Scripts\activate`
    Windows (PowerShell): `.\venv\Scripts\Activate.ps1`

## Running the Project
1. Create a Python virtual environment in the project root:
   ```bash
   `python -m venv venv`
2. Activate the virtual environment:
    Linux/macOS:
        `source venv/bin/activate`
    Command Prompt (Windows):
        `venv\Scripts\activate`
    PowerShell (Windows):
        `.\venv\Scripts\Activate.ps1`
3. Install the required dependencies:
        `pip install -r requirements.txt`
4. Start the application locally:
        `python app.py`

## Executing Tests
To execute the unit tests:
1. Ensure the virtual environment is active.
2. From the project root, run:
    `pytest -v`
3. Pytest will automatically run all test scripts inside the tests/ folder:
    - Unit Tests: tests/Unit_Tests/
    - Integration Tests: tests/Integration_Tests/
    - Performance Tests: tests/Performance_Tests/ (timeit benchmarks)
    - Profiling Tests: tests/Profiling_Tests/ (cProfile bottleneck analysis)

## Test Results
Functional & Integration Results: Logged in `test_results/Unit_Tests` and `test_results/Integration_Tests.`

Performance Results: Execution times stored in `test_results/Performance_Tests.`

Profiling Results: cProfile reports stored in `test_results/Profiling_Tests.`
