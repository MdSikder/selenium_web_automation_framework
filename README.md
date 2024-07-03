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
