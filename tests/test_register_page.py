import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestUrls, TestLocators


class TestRegisterPage:

    def test_register_successful(self, driver):
        driver.get(TestUrls.REGISTER_URL)

        current_time = int(time.time())
        time_part = str(current_time)[-3:]
        unique_email = f"Andrey_Kulchinskiy_31_{time_part}@mail.ru"

        driver.find_element(*TestLocators.NAME_INPUT).send_keys("User")
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(TestUrls.LOGIN_URL))

        assert driver.current_url == TestUrls.LOGIN_URL

    def test_register_repeat(self, driver):
        driver.get(TestUrls.REGISTER_URL)

        driver.find_element(*TestLocators.NAME_INPUT).send_keys("User")
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.ERROR_MESSAGE))

        assert error.text == "Такой пользователь уже существует"

    def test_register_no_name(self, driver):
        driver.get(TestUrls.REGISTER_URL)

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        assert driver.current_url == TestUrls.REGISTER_URL

    def test_register_no_email(self, driver):
        driver.get(TestUrls.REGISTER_URL)

        driver.find_element(*TestLocators.NAME_INPUT).send_keys("User")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        assert driver.current_url == TestUrls.REGISTER_URL

    def test_register_no_password(self, driver):
        driver.get(TestUrls.REGISTER_URL)

        driver.find_element(*TestLocators.NAME_INPUT).send_keys("User")
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        assert driver.current_url == TestUrls.REGISTER_URL

    def test_register_len_password_4_symbol(self, driver):
        driver.get(TestUrls.REGISTER_URL)

        driver.find_element(*TestLocators.NAME_INPUT).send_keys("User")
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqw")
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.ERROR_MESSAGE))

        assert error.text == "Некорректный пароль"
