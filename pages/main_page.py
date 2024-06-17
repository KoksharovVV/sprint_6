import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Получение текста ответа на вопрос")
    def get_answer_text(self, num):
        locator_1_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_2_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(locator_1_formatted)
        self.click_to_element(locator_1_formatted)
        return self.get_text_from_element(locator_2_formatted)

    @allure.step("Перейти к форме оформления заказа")
    def click_button_order(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_LOCATOR)
        self.click_to_element(MainPageLocators.BUTTON_ORDER_LOCATOR)
