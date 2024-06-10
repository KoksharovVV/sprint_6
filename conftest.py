import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    options.add_argument('--window-size=1920,1080')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()
