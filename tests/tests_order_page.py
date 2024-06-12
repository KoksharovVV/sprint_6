from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators


class TestOrderPage:
    def test_create_order(self, driver):
        order_page = OrderPage(driver)
