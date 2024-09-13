from page_soucedemo.Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from page_soucedemo.Config.config import TestData


class SaucedemoPageLocators:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ITEM_FIELD = (By.CLASS_NAME, 'inventory_item')
    CART_LINK = (By.ID, 'shopping_cart_container')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    ZIP_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    ORDER_HEADER = (By.CLASS_NAME, 'title')
    ADD_CART_ITEM = lambda product_name: (
        By.XPATH,
        f"//*[@class='inventory_item' and contains(.,'{product_name}')]//button",
    )


class SaucedemoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = TestData.LOGIN_URL

    def login(self, username: str, password: str):
        self.find_element(
            SaucedemoPageLocators.USERNAME_FIELD,
        ).send_keys(username)
        self.find_element(
            SaucedemoPageLocators.PASSWORD_FIELD,
        ).send_keys(password)
        self.find_element(
            SaucedemoPageLocators.LOGIN_BUTTON,
        ).click()

    def add_to_cart(self, product_name: str):
        product_button = self.find_element(
            SaucedemoPageLocators.ADD_CART_ITEM(product_name),
        )
        product_button.click()

    def make_purchase(self):
        self.find_element(
            SaucedemoPageLocators.CART_LINK,
        ).click()
        cart_items = self.find_elements(
            SaucedemoPageLocators.CART_ITEM,
        )
        assert len(cart_items) == 1, 'No items in the cart'

        self.find_element(
            SaucedemoPageLocators.CHECKOUT_BUTTON,
        ).click()

        self.find_element(
            SaucedemoPageLocators.FIRST_NAME_FIELD,
        ).send_keys(TestData.FIRST_NAME)
        self.find_element(
            SaucedemoPageLocators.LAST_NAME_FIELD,
        ).send_keys(TestData.LAST_NAME)
        self.find_element(
            SaucedemoPageLocators.ZIP_CODE_FIELD,
        ).send_keys(TestData.ZIP_CODE)
        self.find_element(
            SaucedemoPageLocators.CONTINUE_BUTTON,
        ).click()

        self.find_element(
            SaucedemoPageLocators.FINISH_BUTTON,
        ).click()

        assert self.get_text(
            SaucedemoPageLocators.ORDER_HEADER,
        ).find(TestData.CONFIRM_TITLE) != -1, 'Order confirmation failed'
