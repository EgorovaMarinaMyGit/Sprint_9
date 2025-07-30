from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)


    @allure.step("Перейти по URL'у")
    def go_to_url(self, url):
        self.driver.get(url)


    @allure.step("Найти элемент")
    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator) 
    

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
    

    @allure.step("Кликнуть на элемент")
    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()


    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()


    @allure.step("Проверить, что элемент не отображается")
    def check_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))


    @allure.step("Проверить, что текст появился на элементе")
    def check_text_to_be_present_in_element(self, locator, number):
        return WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(locator, number))


    @allure.step("Добавить тест в элемент")
    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)


    @allure.step("Получить текст у элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    
    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
    

    @allure.step("Доскроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element) 


    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    

    @allure.step('Ожидание появления элемента')
    def check_element_is_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))