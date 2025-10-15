# Online Bookstore Testing

This project forms a comprehensive automated test suit based on the given Online Bookstore web application built with Flask. The tests validate the app's core functionality covering unit testing across the following modules:

FR-002: Shopping Cart
FR-003: Checkout Process
FR-004: Payment Process
FR-006: Account Management
FR-007: Responsive Design.

The test suite also considers non-functional requirements including security, performance, and usability testing. Performance profiling tools (timeit, cProfile) are included to identify bottlenecks and suggest optimizations. The testing framework is fully integrated with GitHub Actions CI/CD ensuring that every code change is automatically validated with audit-ready documentation.

## Naming Coventions
FR_xxx = Functional Requirement
TSxxx = Test Scenario
UTxxx = Unit Test Case

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
    `pytest`
3. Pytest will automatically run all test scripts inside the tests/ folder:
    - Unit tests are prefixed with UT- for traceability.
    - Integration tests are prefixed with IT- for traceability.

## Test Results
Screenshots of successful test execution are stored in the test_results/ folder.
