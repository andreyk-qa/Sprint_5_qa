import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls


class TestAuthorization:

    def test_authorization_via_login_account_button(self, driver):
        driver.get(TestUrls.MAIN_URL)

        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        assert order_button.text == "Оформить заказ"

    def test_authorization_via_personal_account_button(self, driver):
        driver.get(TestUrls.MAIN_URL)

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        assert order_button.text == "Оформить заказ"

    def test_authorization_via_login_button_in_register_page(self, driver):
        driver.get(TestUrls.MAIN_URL)

        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.REGISTER_LINK_IN_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.REGISTER_BUTTON))

        driver.find_element(*TestLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        assert order_button.text == "Оформить заказ"

    def test_authorization_via_login_button_in_password_recovery_page(self, driver):
        driver.get(TestUrls.MAIN_URL)

        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.FORGOT_PASSWORD_LINK_IN_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.RECOVERY_BUTTON))

        driver.find_element(*TestLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        assert order_button.text == "Оформить заказ"