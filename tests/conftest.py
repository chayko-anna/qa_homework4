import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.driver_options = webdriver.FirefoxOptions()
    #browser.config.base_url = "https://demoqa.com"
    browser.driver.maximize_window()
    browser.open('https://demoqa.com/automation-practice-form')

    yield

    browser.quit()
