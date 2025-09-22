Проектная работа Кульчинского Андрея, 31я когорта, 5 спринт QA
В проекте тестируем сайт https://stellarburgers.nomoreparties.site/

В корневой директории находится:
    Директория tests, в которой расположены тестовые файлы:
        test_register_page.py
        test_authorization.py
        test_enter_to_personal_account.py
        test_constructor.py
        test_logout_account.py
        test_transition_to_section.py
    
    conftest.py
    data.py
    locators.py
    README.md

Файл test_register_page.py тестирует функциональность регистрации:
    test_register_successful - проверка на регистрацию пользователя с использованием допустимых данных, согласно требованиям
    test_register_repeat - проверка на регистрацию пользователя с уже зарегистрированными данными
    test_register_no_name - проверка на регистрацию пользователя без указания имени
    test_register_no_email - проверка на регистрацию пользователя без указания электронной почты
    test_register_no_password - проверка на регистрацию пользователя без указания пароля
    test_register_len_password_4_symbol - проверка на регистрацию пользователя с паролем длиною в 4 символа

Файл test_authorization.py тестирует функциональность авторизации:
    test_authorization_via_login_account_button - проверка авторизации с помощью кнопки «Войти в аккаунт» на главной странице
    test_authorization_via_personal_account_button - проверка авторизации с помощью кнопки «Личный кабинет» на главной странице
    test_authorization_via_login_button_in_register_page - проверка авторизации с помощью кнопки "Вход" в форме регистрации
    test_authorization_via_login_button_in_password_recovery_page - проверка авторизации с помощью кнопки "Вход" в форме восстановления пароля

Файл test_enter_to_personal_account.py тестирует работу кнопки перехода в личный кабинет:
    test_enter_to_personal_account_via_personal_account_button - проверка кнопки "Личный кабинет" на главной странице

Файл test_constructor.py тестирует работу кнопки "Конструктор" и Логотипа:
    test_enter_to_constructor_from_personal_account - проверка кнопки "Конструктор", которая открывает страницу с выбором состава бургера
    test_enter_to_constructor_from_personal_account_via_logo - проверка Логотипа, который открывает страницу с выбором состава бургера

Файл test_logout_account.py проверяет возможность выхода из аккаунта:
    test_logout_from_personal_account - проверка на выход из аккаунта пользователя через личный кабинет

Файл test_transition_to_section.py тестирует переходы между разделами ингредиентов бургера:
    test_transition_to_section_buns - тест на переход к списку с булками
    test_transition_to_section_sauces - тест на переход к списку с соусами
    test_transition_to_section_fillings - тест на переход к списку с начинками

Файл conftest.py содержит фикстуры проекта

Файл data.py содержит используемые url-адреса

Файл locators.py содержит локаторы:
    NAME_INPUT - Поле ввода имени
    EMAIL_INPUT - Поле ввода почты
    PASSWORD_INPUT - Поле ввода пароля
    REGISTER_BUTTON - Кнопка "Зарегистрироваться"
    LOGIN_ACCOUNT_BUTTON - Кнопка "Войти в аккаунт", на главной
    PERSONAL_ACCOUNT_BUTTON - Кнопка "Личный Кабинет", на главной
    LOGIN_BUTTON - Кнопка "Войти"
    PLACE_ORDER_BUTTON - Кнопка "Оформить заказ"
    REGISTER_LINK_IN_LOGIN_PAGE - Кнопка "Зарегистрироваться" на странице авторизации
    FORGOT_PASSWORD_LINK_IN_LOGIN_PAGE - Кнопка "Восстановить пароль" на странице авторизации
    LOGIN_LINK - Кнопка "Войти" на странице регистрации
    RECOVERY_BUTTON - Кнопка "Восстановить" на странице восстановления пароля
    ORDER_HISTORY_BUTTON - Кнопка "История заказов" на странице личного кабинета
    CONSTRUCTOR_BUTTON - Кнопка "Конструктор"
    ERROR_MESSAGE - Всплывающее сообщение об ошибке
    LOGO - Логотип Stellar Burgers
    LOGOUT_BUTTON - Кнопка "Выход" на странице личного кабинета
    ASSEMBLE_BURGER - Заголовок "Соберите бургер"
    BUNS_BUTTON - Кнопка "Булки" на главной странице
    SAUCES_BUTTON - Кнопка "Соусы" на главной странице
    FILLINGS_BUTTON - Кнопка "Начинки" на главной странице
    BUNS_LIST - Список "Булки" на главной странице
    SAUCES_LIST - Список "Соусы" на главной странице
    FILLINGS_LIST - Список "Начинки" на главной странице

Файл README.md содержит описание проекта