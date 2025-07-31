import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import LOGIN_PAGE_URL


class LoginPage(BasePage): 

    @allure.step("Перейти на страницу авторизации")
    def go_to_login_page(self):
        self.go_to_url(LOGIN_PAGE_URL)


    @allure.step("Заполнить email и password")
    def fill_email_and_password(self, email, password):
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, email)
        self.add_text_to_element(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_to_element(LoginPageLocators.ENTER_BUTTON)


    @allure.step("Проверка перехода на главную страницу после нажатия на 'Войти'")
    def get_current_url_after_enter(self):
        self.find_element_with_wait(LoginPageLocators.TITLE_RECIPES)
        return self.get_current_url()
    

    @allure.step("Проверка отображения кнопки 'Выход'")
    def check_visibility_exit_button(self):
        self.find_element_with_wait(LoginPageLocators.EXIT_BUTTON)
        return self.check_displaying_of_element(LoginPageLocators.EXIT_BUTTON)
    