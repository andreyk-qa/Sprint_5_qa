import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls


class TestTransitionToSection:

    def test_transition_to_section_buns(self, driver):
        driver.get(TestUrls.MAIN_URL)

        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        driver.find_element(*TestLocators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SAUCES_LIST))

        driver.find_element(*TestLocators.BUNS_BUTTON).click()

        h2 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.BUNS_LIST))

        assert h2.text == "Булки"

    def test_transition_to_section_sauces(self, driver):
        driver.get(TestUrls.MAIN_URL)

        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        driver.find_element(*TestLocators.SAUCES_BUTTON).click()

        h2 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SAUCES_LIST))

        assert h2.text == "Соусы"

    def test_transition_to_section_fillings(self, driver):
        driver.get(TestUrls.MAIN_URL)

        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys("qiwfw@mail.ru")
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys("qwqwqwqwqwqwqwqwqw")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))

        driver.find_element(*TestLocators.FILLINGS_BUTTON).click()

        h2 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.FILLINGS_LIST))

        assert h2.text == "Начинки"