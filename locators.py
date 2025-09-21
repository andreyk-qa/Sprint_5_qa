from selenium.webdriver.common.by import By


class TestLocators:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/../input") # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/../input") # Поле ввода почты
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/../input") # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт", на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']") # Кнопка "Личный Кабинет", на главной
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти"
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
    REGISTER_LINK_IN_LOGIN_PAGE = (By.XPATH, ".//a[@href='/register']") # Кнопка "Зарегистрироваться" на странице авторизации
    FORGOT_PASSWORD_LINK_IN_LOGIN_PAGE = (By.XPATH, ".//a[@href='/forgot-password']") # Кнопка "Восстановить пароль" на странице авторизации
    LOGIN_LINK = (By.XPATH, ".//a[@href='/login']") # Кнопка "Войти" на странице регистрации
    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']") # Кнопка "Восстановить" на странице восстановления пароля
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[@href='/account/order-history']") # Кнопка "История заказов" на странице личного кабинета
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"
    ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]") # Всплывающее сообщение об ошибке
    LOGO = (By.XPATH, ".//div[@class= 'AppHeader_header__logo__2D0X2']") # Логотип Stellar Burgers
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход" на странице личного кабинета
    ASSEMBLE_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок "Соберите бургер"
