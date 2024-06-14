import allure
from pages.base_page import BasePage
from locators.order_page_locaters import OrderPageLocators
from locators.main_page_locators import MainPageLocators


class OrderPage(BasePage):

    @allure.step("Выбор станции метро")
    def choose_metro(self):
        self.click_to_element(OrderPageLocators.INPUT_METRO_LOCATOR)
        self.click_to_element(OrderPageLocators.STATION_METRO_LOCATOR)

    @allure.step("Выбор_даты")
    def choose_data(self):
        self.click_to_element(OrderPageLocators.INPUT_DATE_LOCATOR)
        self.click_to_element(OrderPageLocators.BUTTON_NEXT_MONTH_LOCATOR)
        self.click_to_element(OrderPageLocators.BUTTON_DAY_LOCATOR)

    @allure.step("Выбрать срок аренды")
    def choose_rental_period(self):
        self.click_to_element(OrderPageLocators.INPUT_RENTAL_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD_LOCATOR)

    @allure.step("Смена страницы")
    def switch_page(self, button_order):
        self.click_to_element(button_order)

    @allure.step("Создание заказа")
    def create_order(self, button_order):
        self.accept_cookie(MainPageLocators.ACCEPT_COOKIE_LOCATOR)
        self.switch_page(button_order)
        self.add_text_to_element(OrderPageLocators.INPUT_NAME_LOCATOR, "Имя")
        self.add_text_to_element(OrderPageLocators.INPUT_SURNAME_LOCATOR, "Фамилия")
        self.add_text_to_element(OrderPageLocators.INPUT_ADDRESS_LOCATOR, "Адрес")
        self.choose_metro()
        self.add_text_to_element(OrderPageLocators.INPUT_PHONE_LOCATOR, "89998882211")
        self.click_to_element(OrderPageLocators.BUTTON_NEXT_LOCATOR)
        self.choose_data()
        self.choose_rental_period()
        self.click_to_element(OrderPageLocators.CHECKBOX_COLOR_LOCATOR)
        self.add_text_to_element(OrderPageLocators.COMMENT_LOCATOR, "COMMENT")
        self.click_to_element(OrderPageLocators.BUTTON_ORDER_LOCATOR)
        self.click_to_element(OrderPageLocators.BUTTON_YES_LOCATOR)

    @allure.step("Проверить заказ")
    def check_order(self, ):
        return self.get_text_from_element()

