# Include better exception handling and dynamic driver loading.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
import os
from config.config_reader import read_config

class BaseDriver:
    def __init__(self, env='default'):
        config = read_config(env)
        self.driver = None
        browser = config['browser']
        try:
            if browser == 'chrome':
                self.driver = webdriver.Chrome(service=Service('path_to_chromedriver'))
            elif browser == 'firefox':
                self.driver = webdriver.Firefox(service=FirefoxService('path_to_geckodriver'))
            else:
                raise ValueError("Unsupported browser!")
            self.driver.implicitly_wait(config['implicit_wait'])
            self.driver.get(config['url'])
        except Exception as e:
            print(f"Error initializing the driver: {e}")
