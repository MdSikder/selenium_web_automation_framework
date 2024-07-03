# selenium_web_automation_framework
Designing a web automation testing framework using Selenium and pytest involves setting up the project structure and integrating various components like configuration files, logging, reporting, screenshot capture, data-driven testing (DDT), and utility functions. 

Project Structure
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

### Explanation of `pytest.ini` Settings

- **addopts**: Specifies additional options to pass to pytest. 
  - `--html=reports/report.html`: Generates an HTML report.
  - `--self-contained-html`: Embeds all assets in the HTML report.
  - `--capture=tee-sys`: Captures stdout/stderr and shows them in real-time.
  - `--maxfail=3`: Stops after three failures.

- **log_cli**: Enables live logging to the console.

- **log_cli_level**: Sets the log level for console logging.

- **log_file**: Specifies the log file location.

- **log_file_level**: Sets the log level for the log file.

- **testpaths**: Specifies the directories to search for tests.

- **markers**: Defines custom markers for categorizing tests.