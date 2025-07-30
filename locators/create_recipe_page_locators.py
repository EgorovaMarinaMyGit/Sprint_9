from selenium.webdriver.common.by import By

class CreateRecipePageLocators:

    TITLE_CREATE_RECIPE = (By.XPATH, "//a[contains(text(),'Создать рецепт')]") # надпись "Создать рецепт"
    RECIPE_NAME_FIELD = (By.XPATH, "//div[contains(text(), 'Название рецепта')]/following::input[@type='text']") # поле "Название рецепта"
    INGREDIENT_NAME_FIELD = (By.XPATH, "//div[contains(text(), 'Ингредиенты')]/following::input[@type='text']") # поле "Ингридиенты (название)"
    INGREDIENT_GRAMM_FIELD = (By.XPATH, "//input[@class='styles_inputField__3eqTj styles_ingredientsAmountValue__2matT']") # поле "Ингридиенты (кол-во)"
    ADD_INGREDIENT = (By.XPATH, "//div[contains(text(),'Добавить ингредиент')]") # кнопка "Добавить ингредиент"
    INGREDIENT = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]//div[text()='кабачки']") # ингредиент
    COOKING_TIME_FIELD = (By.XPATH, "//div[contains(text(), 'Время приготовления')]/following::input[@type='text']") # поле "Время приготовления"
    DESCRIPTION_FIELD =  (By.XPATH, "//div[contains(text(), 'Описание рецепта')]/following::textarea[1]") # поле "Описание рецепта" 
    IMAGE_LOCATOR = (By.CSS_SELECTOR, "input[type='file']") # изображение 
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[contains(text(),'Создать рецепт')]") # кнопка "Создать рецепт"
    RECIPE_CARD = (By.XPATH, "//div[@class='styles_single-card__1yTTj']") # карточка созданного рецепта
    EDIT_RECIPE = (By.XPATH, "//a[contains(text(),'Редактировать рецепт')]") # кнопка "Редактировать рецепт"

  