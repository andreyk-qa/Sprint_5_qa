import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls


class TestEnterToConstructor:

    def test_enter_to_constructor_from_personal_account(self, driver):
        driver.get(TestUrls.MAIN_URL)

        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_HISTORY_BUTTON))

        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()

        button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        assert button.text == "Войти"
