from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure


class Page:
    def __init__(self, driver, main_url) -> None:
        self.main_url = main_url
        self.driver = driver

    @allure.step("Устанавливаем страницу для загрузки")
    def load_page(self):
        self.driver.get(self.main_url)

    @allure.step("Находим элемент на странице")
    def check_page_load(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ждем загрузки элемента на странице")
    def wait_for_load_page(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Кликаем на элемент")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Кликаем на элемент через javascript")
    def click_on_element_with_javascript(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Отправляем данные в поле")
    def input_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step("Получаем аттрибут со страницы")
    def get_element_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step("Переключаемся на новую вкладку")
    def swith_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Перемещаем элемент из одного локатора в другой')
    def drag_and_drop(self, source_locator, destination_locator):
        source = self.driver.find_element(*source_locator)
        destination = self.driver.find_element(*destination_locator)
        action = ActionChains(self.driver)
        action.click_and_hold(source).move_to_element(destination).release().perform()

    @allure.step('Получаем текст элемента страницы')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Проверяем что элемент отображается')
    def element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Ждём пока элемент станет невидимым')
    def wait_invisible_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator)
        )
