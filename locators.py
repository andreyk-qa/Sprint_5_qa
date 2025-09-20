from selenium.webdriver.common.by import By

class TestUrls:
    REGISTER_URL = "https://stellarburgers.nomoreparties.site/register" # адрес страницы регистрации
    LOGIN_URL = "https://stellarburgers.nomoreparties.site/login" # адрес страницы входа в аккаунт

class TestLocators:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/../input") # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/../input") # Поле ввода почты
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/../input") # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка Зарегистрироваться
    ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]") # Всплывающее сообщение об ошибке