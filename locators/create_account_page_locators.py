from selenium.webdriver.common.by import By

class CreateAccountPageLocators:
    
    TITLE_CREATE_ACCOUNT = (By.XPATH, "//a[contains(text(),'Создать аккаунт')]") # надпись "Создать аккаунт"
    TITLE_REGISTRATION = (By.XPATH, "//h1[contains(text(),'Регистрация')]") # надпись "Регистрация"
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='first_name']") # поле "Имя"
    SECOND_NAME_FIELD = (By.XPATH, "//input[@name='last_name']") # поле "Фамилия"
    USER_NAME_FIELD = (By.XPATH, "//input[@name='username']") # поле "Имя пользователя"
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']") # поле "Электронная почта"
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']") # поле "Пароль"
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]") # кнопка "Создать аккаунт"
    TITLE_ENTER_ON_WEBSITE = (By.XPATH, "//h1[contains(text(),'Войти на сайт')]") # надпись "Войти на сайт"