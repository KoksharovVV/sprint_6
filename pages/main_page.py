import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Получение текста ответа на вопрос")
    def get_answer_text(self, num):
        locator_1_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_2_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        element = self.driver.find_element(*locator_1_formatted)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_to_element(locator_1_formatted)
        return self.get_text_from_element(locator_2_formatted)

    @allure.step("Оформить заказ")
    def set_order(self):
        pass

    @allure.step("Проверить заказ")
    def check_order(self, ):
        return self.get_text_from_element()
