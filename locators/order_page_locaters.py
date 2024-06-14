from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_NAME_LOCATOR = [By.XPATH, './/input[@placeholder="* Имя"]']
    INPUT_SURNAME_LOCATOR = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    INPUT_ADDRESS_LOCATOR = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    INPUT_METRO_LOCATOR = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    STATION_METRO_LOCATOR = [By.XPATH, './/*[text()="Черкизовская"]/parent::button']
    INPUT_PHONE_LOCATOR = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    BUTTON_NEXT_LOCATOR = [By.XPATH, './/button[text()="Далее"]']
    INPUT_DATE_LOCATOR = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    BUTTON_NEXT_MONTH_LOCATOR = [By.XPATH, './/button[text()="Next Month"]']
    BUTTON_DAY_LOCATOR = [By.XPATH, './/*[contains(@class, "day--015")]']
    INPUT_RENTAL_PERIOD_LOCATOR = [By.XPATH, './/*[text()="* Срок аренды"]']
    DROPDOWN_RENTAL_PERIOD_LOCATOR = [By.XPATH, './/*[text()="сутки"]']
    CHECKBOX_COLOR_LOCATOR = [By.XPATH, './/input[@id="black"]']
    COMMENT_LOCATOR = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']
    BUTTON_ORDER_LOCATOR = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/*[text()="Заказать"]']
    BUTTON_YES_LOCATOR = [By.XPATH, './/*[text()="Да"]']
