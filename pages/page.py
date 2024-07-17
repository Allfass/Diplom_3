from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class Page():
    def __init__(self, driver, main_url) -> None:
        self.main_url = main_url
        self.driver = driver

    @allure.step('Устанавливаем страницу для загрузку')
    def load_page(self):
        self.driver.get(self.main_url)

    @allure.step('Находим элемент на странице')
    def check_page_load(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ждем загрузки элемента на странице')
    def wait_for_load_page(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Кликаем на элемент через javascript')
    def click_on_element_with_javascript(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Отправляем данные в поле')
    def input_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Получаем аттрибут со страницы')
    def get_element_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)
    
    @allure.step('Переключаемся на новую вкладку')
    def swith_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])