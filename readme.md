# Python Selenium Framework

A robust, data-driven test automation framework built with Python, Selenium, and Pytest. This framework implements the Page Object Model (POM) design pattern for maintainable and scalable automation testing.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Test Data Management](#test-data-management)
- [Utilities](#utilities)
- [Running Tests](#running-tests)
- [Reports](#reports)
- [Logging](#logging)

## Features

- **Page Object Model (POM)**: Clean separation of page objects and test logic
- **Data-Driven Testing**: Support for Excel and Google Sheets
- **Custom Logging**: Comprehensive logging with custom logger utility
- **Database Integration**: Database utilities for backend validation
- **Pytest Integration**: Powerful testing framework with plugins
- **Parallel Execution**: Run tests in parallel using pytest-xdist
- **Allure Reporting**: Generate beautiful test reports
- **Retry Logic**: Automatic test reruns for flaky tests
- **Headless Mode**: Support for headless browser execution

## Project Structure

```
PythonSeleniumFramework/
├── base/
│   ├── __init__.py
│   └── base_driver.py              # Base class for page objects with common methods
├── configs/
│   └── config.ini                  # Configuration file for app settings
├── pages/
│   ├── __init__.py
│   └── login_page.py               # Page objects for login functionality
├── tests/
│   ├── __init__.py
│   ├── conftest.py                 # Pytest fixtures and configurations
│   ├── test_login.py               # Login test cases
│   ├── test_login_ddt.py           # Data-driven login tests
│   ├── test_excel.py               # Excel utility tests
│   └── test_db.py                  # Database utility tests
├── utils/
│   ├── __init__.py
│   ├── custom_logger.py            # Custom logging utility
│   ├── excel_utils.py              # Excel file operations
│   ├── db_utils.py                 # Database operations
│   ├── read_config.py              # Configuration reader
│   └── google_sheets_utils.py      # Google Sheets operations (optional)
├── testdata/
│   └── data.xlsx                   # Test data file
├── Logs/
│   └── automation.log              # Log files
├── reports/
│   └── allure-results/             # Allure test reports
├── pytest.ini                       # Pytest configuration
├── requirements.txt                # Project dependencies
├── Jenkinsfile                     # CI/CD pipeline configuration
└── readme.md                       # This file
```

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- Git

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd PythonSeleniumFramework
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Allure (for reports):**
   ```bash
   # On Windows
   choco install allure
   # On macOS
   brew install allure
   # On Linux
   sudo apt-get install allure
   ```

## Configuration

### pytest.ini

Configuration for Pytest:
- `base_url`: Base URL of the application under test
- `testpaths`: Path where tests are located
- `addopts`: Additional options for Pytest execution

### config.ini

Application-specific configuration (database, API endpoints, etc.)

### Environment Variables

You can set environment variables for sensitive data:
```bash
set BROWSER_NAME=chrome
set HEADLESS=false
```

## Usage

### Running Tests

**Run all tests:**
```bash
pytest
```

**Run specific test file:**
```bash
pytest tests/test_login.py
```

**Run specific test function:**
```bash
pytest tests/test_login.py::test_valid_login
```

**Run with verbose output:**
```bash
pytest -v
```

**Run in parallel (requires pytest-xdist):**
```bash
pytest -n=auto
```

**Run with Allure reporting:**
```bash
pytest --alluredir=reports/allure-results --clean-alluredir
```

**Generate HTML report after tests:**
```bash
allure serve reports/allure-results
```

## Test Data Management

### Excel Files

Test data is stored in `testdata/data.xlsx`. Use the `ExcelUtils` class to read/write data:

```python
from utils.excel_utils import ExcelUtils

# Read data
value = ExcelUtils.read_data('testdata/data.xlsx', 'Sheet1', 2, 1)

# Write data
ExcelUtils.write_data('testdata/data.xlsx', 'Sheet1', 2, 1, 'new_value')

# Get row and column counts
rows = ExcelUtils.get_row_count('testdata/data.xlsx', 'Sheet1')
cols = ExcelUtils.get_col_count('testdata/data.xlsx', 'Sheet1')
```

### Google Sheets (Optional)

Use `GoogleSheetsUtils` for cloud-based test data management:

```python
from utils.google_sheets_utils import GoogleSheetsUtils

# Read data from Google Sheets
data = GoogleSheetsUtils.read_data(spreadsheet_id, sheet_name, row, column)

# Write data to Google Sheets
GoogleSheetsUtils.write_data(spreadsheet_id, sheet_name, row, column, value)
```

## Utilities

### custom_logger.py

Provides logging functionality:

```python
from utils.custom_logger import LogGen

logger = LogGen.loggen()
logger.info("Test started")
logger.error("Test error")
```

### excel_utils.py

Excel file operations:
- `read_data()`: Read specific cell value
- `write_data()`: Write value to specific cell
- `get_row_count()`: Get total rows
- `get_col_count()`: Get total columns

### db_utils.py

Database operations for backend testing

### read_config.py

Read configuration from `config.ini`

### google_sheets_utils.py

Google Sheets integration for cloud-based test data

## Reports

### Allure Reports

After running tests with Allure, view the report:

```bash
allure serve reports/allure-results
```

### HTML Reports

Pytest can generate HTML reports using pytest-html:

```bash
pytest --html=reports/report.html
```

## Logging

Logs are generated in the `Logs/automation.log` file. The custom logger automatically logs:
- Test execution steps
- Errors and exceptions
- Element interactions

## CI/CD Integration

The `Jenkinsfile` provides pipeline configuration for CI/CD integration. Update it based on your Jenkins setup.

## Best Practices

1. **Page Object Model**: Keep page elements and methods in page classes
2. **DRY Principle**: Use base classes and utilities to avoid code duplication
3. **Naming Convention**: Use descriptive names for tests and page objects
4. **Assertions**: Use pytest assertions for test validations
5. **Wait Strategies**: Use explicit waits instead of implicit waits
6. **Test Data**: Separate test data from test logic
7. **Logging**: Log meaningful information for debugging

## Troubleshooting

### Common Issues

**WebDriver not found:**
- Install geckodriver (Firefox) or chromedriver (Chrome)
- Add driver path to system PATH

**Import errors:**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python path and virtual environment

**Test data not found:**
- Verify `testdata/data.xlsx` exists
- Check file path in test configuration

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests to ensure nothing breaks
4. Submit a pull request

## License

MIT License - feel free to use this framework in your projects.

## Support

For issues or questions, please open an issue in the repository. 
