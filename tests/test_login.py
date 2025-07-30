import allure


class TestLogin:

    @allure.title("Проверка перехода на главную страницу после авторизации")
    def test_check_transition_to_main_page_after_login(self, login_page, create_account):
        email, password = create_account
        login_page.go_to_login_page()
        login_page.fill_email_and_password(email, password)
        expected_url = 'https://foodgram-frontend-1.prakticum-team.ru/recipes'

        assert login_page.get_current_url_after_enter() == expected_url


    @allure.title("Проверка отображения кнопки 'Выход' после авторизации и нажатия 'Войти'")
    def test_check_visibility_exit_button_after_login(self, login_page, create_account):
        email, password = create_account
        login_page.go_to_login_page()
        login_page.fill_email_and_password(email, password)

        assert login_page.check_visibility_exit_button() is True