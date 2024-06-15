import allure
import pytest
from selenium.webdriver.common.by import By
from pages.header_page import HeaderPage
from data import url


class TestHeaderPage:
    @allure.title("Переход к главной странице сервиса по клику на логотип сервиса")
    def test_transition_main_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.driver.get(url["order_page"])
        header_page.transition_main_page()
        assert header_page.get_current_url() == url["main_page"]

    @allure.title("Переход на дзен по клику на логотип Яндекс")
    @pytest.mark.parametrize('page', [
        url["main_page"],
        url["order_page"]
    ])
    def test_transition_dzen(self, driver, page):
        header_page = HeaderPage(driver)
        header_page.driver.get(page)
        header_page.transition_dzen()
        assert header_page.find_element_with_wait((By.XPATH, './/header[contains(@class, "desktop-base-header")]'))
