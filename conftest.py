import pytest
import random
from selenium import webdriver
from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage
from pages.create_recipe_page import CreateRecipePage
from data import LOGIN_PAGE_URL, email, password
from helper.helper_random import generate_random_string


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
    
    first_name = generate_random_string(10)
    second_name = generate_random_string(10)
    user_name = generate_random_string(10)
    email = generate_random_string(10) + "@mail.ru"
    password = generate_random_string(10)
    return first_name, second_name, user_name, email, password


# фикстура создания аккаунта
@pytest.fixture()
def create_account(create_account_page, generate_user_data):
        first_name, second_name, user_name, email, password = generate_user_data
        create_account_page.go_to_create_account_page()   
        create_account_page.fill_in_registration_fields(first_name, second_name, user_name, email, password)
        return email, password


# фикстура авторизации
@pytest.fixture()
def login_user(login_page):
    login_page.go_to_login_page()
    login_page.fill_email_and_password(email, password)


# фикстура генерации данных для рецепта
@pytest.fixture()
def generate_recipe_data():

    recipe_name = generate_random_string(8)
    grams =  random.randint(1, 100)
    time_cooking = random.randint(1, 100)
    description = generate_random_string(20)
    return recipe_name, grams, time_cooking, description
