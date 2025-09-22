import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls


class TestEnterToPersonalAccount:

    def test_enter_to_personal_account_via_personal_account_button(self, driver):
        driver.get(TestUrls.MAIN_URL)

        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        order_history_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.ORDER_HISTORY_BUTTON))

        assert order_history_button.text == "История заказов"