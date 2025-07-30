import allure


class TestCreateRecipe:

    @allure.title("Проверка отображения карточки созданного рецепта")
    def test_check_visibility_created_recipe(self, login_user, create_recipe_page, generate_recipe_data):
        recipe_name, grams, time_cooking, description = generate_recipe_data
        create_recipe_page.create_recipe(recipe_name, grams, time_cooking, description)

        assert create_recipe_page.check_visibility_of_recipe_card() is True


    @allure.title("Проверка отображения названия созданного рецепта")
    def test_check_visibility_recipe_name(self, login_user, create_recipe_page, generate_recipe_data):
        recipe_name, grams, time_cooking, description = generate_recipe_data
        recipe_name = create_recipe_page.create_recipe(recipe_name, grams, time_cooking, description)

        assert create_recipe_page.check_visibility_recipe_name(recipe_name) is True

