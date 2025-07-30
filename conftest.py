import pytest
import random
import string
from selenium import webdriver
from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage
from pages.create_recipe_page import CreateRecipePage
from locators.login_page_locators import LoginPageLocators
from data import LOGIN_PAGE_URL, email, password


# вспомогательная функция для настройки браузера
def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    return options

# фикстура для браузера + выход
@pytest.fixture
def driver():
    server = 'http://selenoid:4444/wd/hub'
    options = get_default_chrome_options()
    driver = webdriver.Remote(command_executor=server, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


# фикстура для страницы создания аккаунта
@pytest.fixture
def create_account_page(driver):
    return CreateAccountPage(driver)

# фикстура для страницы логинации
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

# фикстура для страницы создания рецепта
@pytest.fixture
def create_recipe_page(driver):
    return CreateRecipePage(driver)


# фикстура генерации данных для регистрации пользователя
@pytest.fixture()
def generate_user_data():
    # генерируем уникальные данные для пользователя
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    
    first_name = generate_random_string(10)
    second_name = generate_random_string(10)
    user_name = generate_random_string(10)
    email = generate_random_string(10) + "@mail.ru"
    password = generate_random_string(10)
    return first_name, second_name, user_name, email, password


# фикстура создания аккаунта
@pytest.fixture()
def create_account(login_page, generate_user_data):
        first_name, second_name, user_name, email, password = generate_user_data

        login_page.go_to_url(LOGIN_PAGE_URL)
        login_page.click_to_element(LoginPageLocators.TITLE_CREATE_ACCOUNT)
        login_page.find_element_with_wait(LoginPageLocators.TITLE_REGISTRATION)
        login_page.add_text_to_element(LoginPageLocators.FIRST_NAME_FIELD, first_name)
        login_page.add_text_to_element(LoginPageLocators.SECOND_NAME_FIELD, second_name)
        login_page.add_text_to_element(LoginPageLocators.USER_NAME_FIELD, user_name)
        login_page.add_text_to_element(LoginPageLocators.EMAIL_FIELD, email)
        login_page.add_text_to_element(LoginPageLocators.PASSWORD_FIELD, password)
        login_page.click_to_element(LoginPageLocators.CREATE_ACCOUNT_BUTTON)
        login_page.find_element_with_wait(LoginPageLocators.EMAIL_FIELD)
        return email, password


# фикстура авторизации
@pytest.fixture()
def login_user(login_page):
    login_page.go_to_login_page()
    login_page.add_text_to_element(LoginPageLocators.EMAIL_FIELD, email)
    login_page.add_text_to_element(LoginPageLocators.PASSWORD_FIELD, password)
    login_page.click_to_element(LoginPageLocators.ENTER_BUTTON)
    login_page.find_element_with_wait(LoginPageLocators.TITLE_CREATE_RECIPE)


# фикстура генерации данных для рецепта
@pytest.fixture()
def generate_recipe_data():
    # генерируем уникальные данные для рецепта (текст)
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    recipe_name = generate_random_string(8)
    grams =  random.randint(1, 100)
    time_cooking = random.randint(1, 100)
    description = generate_random_string(20)
    return recipe_name, grams, time_cooking, description
