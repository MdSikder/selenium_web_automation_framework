# Web Automation Framework

This web automation framework uses Selenium and pytest, following industry standards. It includes setup configuration, logging, detailed reports and screenshots, data-driven testing, and useful tools. It also offers improvements like better configuration management, enhanced logging, improved reporting, a structured Page Object Model (POM), integration with Continuous Integration (CI), and support for different environments.

## Project Structure

    selenium_web_automation_framework/
    │
    ├── config/
    │   ├── config.yaml
    │   └── config_reader.py
    │
    ├── logs/
    │   └── test.log
    │
    ├── reports/
    │   └── report.html
    │
    ├── screenshots/
    │
    ├── src/
    │   ├── __init__.py
    │   ├── base/
    │   │   └── base_driver.py
    │   ├── pages/
    │   │   ├── __init__.py
    │   │   └── example_page.py
    │   └── utilities/
    │       ├── __init__.py
    │       ├── logger.py
    │       ├── read_data.py
    │       └── capture_screenshot.py
    │
    ├── test_cases/
    │   ├── __init__.py
    │   └── test_example.py
    │
    ├── TestData/
    │   └── data.xlsx
    │
    ├── ci/
    │   └── ci_config.yml
    │
    ├── pytest.ini
    ├── requirements.txt
    └── README.md

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run tests:
   ```
   pytest
   ```

## Configuration

The `config/config.yaml` file contains environment-specific configurations.

## Logging

Logs are configured in `src/utilities/logger.py` and can be found in the `logs/test.log` file.

## Reports

Test reports are generated in the `reports/report.html` file.

## Continuous Integration

The CI configuration is in the `ci/ci_config.yml` file. It is set up to run tests on push and upload test reports if any tests fail.

## Pytest Configuration

The `pytest.ini` file configures pytest settings, including:
- HTML report generation
- Live logging
- Custom markers for test categorization

## Running Tests

To run tests with specific markers:
```
pytest -m smoke
```
```

### Adding to GitHub

  1. Initialize a Git repository:
     ```sh
     git init
     ```
  
  2. Add all files:
     ```sh
     git add .
     ```
  
     3. Commit the changes:
        ```sh
        git commit -m "Initial commit"
        ```
  
     4. Add remote repository:
        ```sh
        git remote add origin <your-repo-url>
        ```
  
     5. Push to GitHub:
        ```sh
        git push -u origin master
        ```

This setup ensures that the framework is configurable, maintainable, and integrates well with CI pipelines, making it more industry-standard.
