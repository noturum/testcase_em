from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.url = None
        self.driver = driver
        self.timeout = 10
        self.wait = wait(
            self.driver,
            self.timeout
        )

    def click_to_element(self, element):
        ActionChains(self.driver).click(element).perform()

    def get(self, url):
        browser = self.driver.get(url)
        return browser

    def find_elements(self, by_locator):
        return self.wait.until(
            ES.visibility_of_any_elements_located(by_locator),
            f"Elements {by_locator} not found after waiting for {self.timeout} seconds."
        )

    def find_element(self, by_locator):
        return self.wait.until(
            ES.visibility_of_element_located(by_locator),
            f"Element {by_locator} not found after waiting for {self.timeout} seconds."
        )

    def get_text(self, by_locator):
        element = self.find_element(by_locator)
        return element.text
