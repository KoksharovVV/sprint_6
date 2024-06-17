import allure
from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):
    @allure.step("Клик на логотип яндекса")
    def transition_dzen(self):
        self.click_to_element(HeaderPageLocators.YANDEX_LOGO_LOCATORS)
        self.switch_browser_page()

    @allure.step("Клик на логотип сервиса")
    def transition_main_page(self):
        self.click_to_element(HeaderPageLocators.SCOOTER_LOGO_LOCATORS)
