import time

import allure
import pytest
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from locators.header_page_locators import HeaderPageLocators
from data import url


class TestOrderPage:
    @allure.title("Создание заказа с переходом через хедер и кнопку на странице")
    @pytest.mark.parametrize("button_order", [
        MainPageLocators.BUTTON_ORDER_LOCATOR,
        HeaderPageLocators.BUTTON_ORDER_LOCATORS
    ])
    def test_create_order(self, driver, button_order):
        order_page = OrderPage(driver)
        order_page.open_page(url["main_page"])
        order_page.create_order(button_order)
        order_page.check_order()
