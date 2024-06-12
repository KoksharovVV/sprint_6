import allure
from pages.base_page import BasePage
from locators.order_page_locaters import OrderPageLocators
from locators.main_page_locators import MainPageLocators


class OrderPage(BasePage):
    @allure.step("Оформить заказ")
    def create_order(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_LOCATOR)
        self.add_text_to_element(OrderPageLocators.INPUT_NAME_LOCATOR, "Имя")
        self.add_text_to_element(OrderPageLocators.INPUT_SURNAME_LOCATOR, "Фамилия")
        self.add_text_to_element(OrderPageLocators.INPUT_ADDRESS_LOCATOR, "Адрес")
        self.add_text_to_element(OrderPageLocators.INPUT_METRO_LOCATOR, "Театральная")
        self.add_text_to_element(OrderPageLocators.INPUT_PHONE_LOCATOR, "89996662211")
        self.click_to_element(OrderPageLocators.BUTTON_NEXT_LOCATOR)
        self.add_text_to_element(OrderPageLocators.INPUT_DATE_LOCATOR, "")

    @allure.step("Проверить заказ")
    def check_order(self, ):
        return self.get_text_from_element()

