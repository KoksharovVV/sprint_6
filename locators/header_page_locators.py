from selenium.webdriver.common.by import By


class HeaderPageLocators:
    YANDEX_LOGO_LOCATORS = [By.XPATH, './/a[contains(@class, "Header_LogoYandex")]']
    SCOOTER_LOGO_LOCATORS = [By.XPATH, './/a[contains(@class, "Header_LogoScooter")]']