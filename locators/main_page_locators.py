from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = [By.XPATH, './/*[@id="accordion__heading-{}"]']
    ANSWER_LOCATOR = [By.XPATH, './/*[@id="accordion__panel-{}"]']
    BUTTON_ORDER_LOCATOR = [By.XPATH, './/div[contains(@class, "FinishButton")]/button']
