import datetime

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.read_properties import ReadProperties


def take_screenshot(driver):
    file_name = f"{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S_%F')}" \
        .replace("/", "_").replace("::", "__")
    capture_path = f"./screenshots/{file_name}.png"
    driver.save_screenshot(capture_path)
    allure.attach(
        driver.get_screenshot_as_png(),
        name=f'screenshot {file_name}',
        attachment_type=allure.attachment_type.PNG
    )

class ConfigDriver:
    # Configures driver based on JSON browser value
    @staticmethod
    def configure_driver():
        browser = ReadProperties.get_config_browser()
        if browser == 'chrome':
            driver = webdriver.Firefox(executable_path=ChromeDriverManager().install())
            return driver
        if browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            return driver
        if browser == 'edge':
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
            return driver

    # Initialises and opens page based on JSON baseUrl
    @staticmethod
    def init_driver(driver):
        driver.maximize_window()
        driver.get(ReadProperties.get_config_url())

    @staticmethod
    def close_driver(driver):
        take_screenshot(driver)
        driver.quit()
