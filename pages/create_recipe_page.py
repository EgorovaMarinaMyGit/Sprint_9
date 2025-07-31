from pathlib import Path
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.create_recipe_page_locators import CreateRecipePageLocators



class CreateRecipePage(BasePage):


    @allure.step("Загрузка изображения")
    def upload_file(self, file_name):
        # Получаем директорию текущего файла (корень проекта)
        project_dir = Path(__file__).parent.parent
    
        # Формируем путь к файлу в папке assets
        file_path = project_dir / 'assets' / file_name
    
        # Получаем абсолютный путь (нужно для send_keys)
        absolute_path = str(file_path.resolve())
    
        # Находим input для загрузки файла
        file_input = self.check_element_is_located(CreateRecipePageLocators.IMAGE_LOCATOR)
    
        # Передаём путь к файлу
        file_input.send_keys(absolute_path)


    @allure.step("Создание рецепта")
    def create_recipe(self, recipe_name, grams, time_cooking, description):
        self.click_to_element(CreateRecipePageLocators.TITLE_CREATE_RECIPE)
        self.add_text_to_element(CreateRecipePageLocators.RECIPE_NAME_FIELD, recipe_name)
        self.add_text_to_element(CreateRecipePageLocators.INGREDIENT_NAME_FIELD, 'к')
        self.click_to_element(CreateRecipePageLocators.INGREDIENT)
        self.add_text_to_element(CreateRecipePageLocators.INGREDIENT_GRAMM_FIELD, grams)
        self.click_to_element(CreateRecipePageLocators.ADD_INGREDIENT)
        self.add_text_to_element(CreateRecipePageLocators.COOKING_TIME_FIELD, time_cooking)
        self.add_text_to_element(CreateRecipePageLocators.DESCRIPTION_FIELD, description)
        self.upload_file('image.jpg')
        self.click_to_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)
        return recipe_name


    @allure.step("Проверка отображения карточки созданного рецепта")
    def check_visibility_of_recipe_card(self):
        self.find_element_with_wait(CreateRecipePageLocators.RECIPE_CARD)
        return self.check_displaying_of_element(CreateRecipePageLocators.RECIPE_CARD)
        

    @allure.step("Проверка отображения названия созданного рецепта")
    def check_visibility_recipe_name(self, recipe_name):
        recipe_name_locator = (CreateRecipePageLocators.RECIPE_NAME_HEADER[0], CreateRecipePageLocators.RECIPE_NAME_HEADER[1].format(recipe_name=recipe_name))
        self.find_element_with_wait(CreateRecipePageLocators.EDIT_RECIPE)
        return self.check_displaying_of_element(recipe_name_locator)