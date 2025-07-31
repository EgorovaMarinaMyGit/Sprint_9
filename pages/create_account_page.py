import allure
from pages.base_page import BasePage
from locators.create_account_page_locators import CreateAccountPageLocators
from data import LOGIN_PAGE_URL


class CreateAccountPage(BasePage):

    @allure.step("Перейти на страницу регистрации")
    def go_to_create_account_page(self):
        self.go_to_url(LOGIN_PAGE_URL)
        self.click_to_element(CreateAccountPageLocators.TITLE_CREATE_ACCOUNT)
        self.find_element_with_wait(CreateAccountPageLocators.TITLE_REGISTRATION)

    
    @allure.step("Заполнить поля регистрации и нажать на кнопку 'Создать аккаунт'")
    def fill_in_registration_fields(self, first_name, second_name, user_name, email, password):
        self.add_text_to_element(CreateAccountPageLocators.FIRST_NAME_FIELD, first_name)
        self.add_text_to_element(CreateAccountPageLocators.SECOND_NAME_FIELD, second_name)
        self.add_text_to_element(CreateAccountPageLocators.USER_NAME_FIELD, user_name)
        self.add_text_to_element(CreateAccountPageLocators.EMAIL_FIELD, email)
        self.add_text_to_element(CreateAccountPageLocators.PASSWORD_FIELD, password)
        self.find_element_with_wait(CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON)
        self.click_to_element(CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON)
        self.find_element_with_wait(CreateAccountPageLocators.TITLE_ENTER_ON_WEBSITE)
        

    @allure.step("Проверка URL'а после нажатия на 'Создать аккаунт'")
    def url_after_push_create_account(self):
        self.find_element_with_wait(CreateAccountPageLocators.TITLE_ENTER_ON_WEBSITE)
        return self.get_current_url()


    @allure.step("Проверка отображения формы авторизации")
    def check_visibility_autorisation_form(self):
        self.find_element_with_wait(CreateAccountPageLocators.EMAIL_FIELD)
        return self.check_displaying_of_element(CreateAccountPageLocators.EMAIL_FIELD) and self.check_displaying_of_element(CreateAccountPageLocators.PASSWORD_FIELD)

