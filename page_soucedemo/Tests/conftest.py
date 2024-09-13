import os

import pytest
from selenium.webdriver import ChromeOptions, Remote

from page_soucedemo.Config.config import TestData
from page_soucedemo.Pages.SaucedemoPage import SaucedemoPage
from dotenv import load_dotenv

load_dotenv()
SELENIUM_URL = os.environ.get('SELENIUM_URL')


@pytest.fixture(scope="session")
def saucedemo_page():
    driver = Remote(command_executor=SELENIUM_URL, options=ChromeOptions())
    page = SaucedemoPage(driver)
    page.get(TestData.LOGIN_URL)
    yield page
    driver.quit()
