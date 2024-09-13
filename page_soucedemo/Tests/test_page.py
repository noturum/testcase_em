from page_soucedemo.Config.config import TestData


def test_auth(saucedemo_page):
    saucedemo_page.login(
        TestData.USERNAME,
        TestData.PASSWORD,
    )



def test_add_to_cart(saucedemo_page):
    saucedemo_page.add_to_cart(TestData.PRODUCT_NAME)


def test_purchase(saucedemo_page):
    saucedemo_page.make_purchase()
