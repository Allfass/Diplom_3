from pages.page import Page
import time
import allure
from locators.create_order import CreateOrderLocators


class CreateOrderPage(Page):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.create_order_locators = CreateOrderLocators()

    @allure.step('Нажимаем кнопку - конструктор')
    def click_on_constructor_button(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.constructor_button
        )

    @allure.step('Ждём загрузку страницы конструктора')
    def wait_constructor_page_loading(self):
        super().wait_for_load_page(self.create_order_locators.constructor_title)

    @allure.step('Проверяем что страница конструктора загружена')
    def check_constructor_page_is_loaded(self):
        return super().check_page_load(self.create_order_locators.constructor_title)

    @allure.step('Нажимаем на кнопку ленты заказов')
    def click_on_order_feed(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.order_feed_button
        )

    @allure.step('Ожидаем загрузку ленты заказов')
    def wait_feed_page_loading(self):
        super().wait_for_load_page(self.create_order_locators.order_feed_title)

    @allure.step('Проверяем что лента заказов загружена')
    def check_order_feed_is_loaded(self):
        return super().check_page_load(self.create_order_locators.order_feed_title)

    @allure.step('Ждем загрузки поля с ингредиентами')
    def wait_ingredients_field(self):
        super().wait_for_load_page(self.create_order_locators.fluorescent_bread_ingredient)

    @allure.step('Нажимаем на поле созданного заказа')
    def click_on_fluorescent_bread_ingredient(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.fluorescent_bread_ingredient
        )

    @allure.step('Ждем загрузку поля с ингредиентами')
    def wait_ingredient_field(self):
        super().wait_for_load_page(self.create_order_locators.fluorescent_bread_ingredient_title)

    @allure.step('Проверяем загрузку описания заказа')
    def check_fluorescent_bread_ingredient_title(self):
        return super().check_page_load(
            self.create_order_locators.fluorescent_bread_ingredient_title
        )

    @allure.step('Закрываем поле заказа')
    def click_ingredient_close_button(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.ingredient_close_button
        )

    @allure.step('Ждем пока поле заказа закроется')
    def wait_invisible_ingredient_field(self):
        super().wait_invisible_element(
            self.create_order_locators.fluorescent_bread_ingredient_title
        )

    @allure.step('Проверяем что поле заказа закрылось')
    def check_ingredient_field_is_closed(self):
        return not super().element_is_displayed(
            self.create_order_locators.fluorescent_bread_ingredient_title
        )

    @allure.step('Переносим булку в поле заказа')
    def drag_and_drop_fluorescent_bread_ingredient(self):
        super().drag_and_drop(
            self.create_order_locators.fluorescent_bread_ingredient,
            self.create_order_locators.order_drop_field,
        )

    @allure.step('Ждем пока счётчик заказа увеличится')
    def wait_counter_loading(self):
        super().wait_for_load_page(self.create_order_locators.fluorescent_bread_ingredient_counter)

    @allure.step('Получить текущий счётчик заказа')
    def get_counter_of_fluorescent_bread(self):
        return super().get_element_text(
            self.create_order_locators.fluorescent_bread_ingredient_counter
        )

    @allure.step('Нажимаем кнопку создания заказа')
    def click_create_order_button(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.create_order_button
        )

    @allure.step('Получить текущий идентификатор заказа')
    def get_order_id(self):
        for _ in range(10):
            element = super().get_element_text(self.create_order_locators.order_id)
            if element == "9999":
                time.sleep(1)
            else:
                return element
        return None
