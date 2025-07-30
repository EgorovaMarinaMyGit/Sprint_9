import allure


class TestCreateAccount:

    @allure.title("Проверка перехода на страницу авторизации после создания аккаунта и нажатия на 'Создать аккаунт'")
    def test_check_transition_to_login_page_after_create_account(self, create_account_page, generate_user_data):
        first_name, second_name, user_name, email, password = generate_user_data
        create_account_page.go_to_create_account_page()
        create_account_page.fill_in_registration_fields(first_name, second_name, user_name, email, password)
        expected_url = 'https://foodgram-frontend-1.prakticum-team.ru/signin'

        assert create_account_page.url_after_push_create_account() == expected_url


    @allure.title("Проверка отображения формы авторизации после создания аккаунта и нажатия на 'Создать аккаунт'")
    def test_check_visibility_login_form_after_create_account(self, create_account_page, generate_user_data):
        first_name, second_name, user_name, email, password = generate_user_data
        create_account_page.go_to_create_account_page()
        create_account_page.fill_in_registration_fields(first_name, second_name, user_name, email, password)

        assert create_account_page.check_visibility_autorisation_form() is True

        