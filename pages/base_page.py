from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookie(self, locator):
        self.click_to_element(locator)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(locator)).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def switch_browser_page(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_page(self, page):
        self.driver.get(page)

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)
