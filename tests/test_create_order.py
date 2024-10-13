from pages.create_order import CreateOrderPage
from data import TestData
import pytest
import allure


@pytest.mark.usefixtures("logined_user")
class TestCreateOrder:
    @allure.title('Проверка перехода по клику на Конструктор')
    @allure.description('При нажатии на кнопку конструктора будет выполнен переход на страницу')
    def test_click_constructor_button_transfer_to_constuctor_page(self):
        order_page = CreateOrderPage(self.driver, TestData.MAIN_URL)
        order_page.load_page()
        order_page.click_on_constructor_button()
        order_page.wait_constructor_page_loading()
        assert order_page.check_constructor_page_is_loaded() is not None

    @allure.title('Проверка перехода по клику на Лента заказов')
    @allure.description('При нажатии на кнопку ленты заказов будет выполнен переход на страницу')
    def test_click_feed_button_transfer_to_feed_page(self):
        order_page = CreateOrderPage(self.driver, TestData.MAIN_URL)
        order_page.load_page()
        order_page.click_on_order_feed()
        order_page.wait_feed_page_loading()
        assert order_page.check_order_feed_is_loaded() is not None

    @allure.title('Проверка клика на ингредиент')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_return_pop_up_window(self):
        order_page = CreateOrderPage(self.driver, TestData.MAIN_URL)
        order_page.load_page()
        order_page.wait_ingredients_field()
        order_page.click_on_fluorescent_bread_ingredient()
        order_page.wait_ingredient_field()
        assert order_page.check_fluorescent_bread_ingredient_title() is not None

    @allure.title('Проверка всплывающее окно')
    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_click_ingredient_exit_button_close_windows(self):
        order_page = CreateOrderPage(self.driver, TestData.MAIN_URL)
        order_page.load_page()
        order_page.wait_ingredients_field()
        order_page.click_on_fluorescent_bread_ingredient()
        order_page.wait_ingredient_field()
        order_page.click_ingredient_close_button()
        order_page.wait_invisible_ingredient_field()
        assert order_page.check_ingredient_field_is_closed()

    @allure.title('Проверка добавления ингредиента в заказ')
    @allure.description('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_adding_ingredient_increase_counter(self):
        order_page = CreateOrderPage(self.driver, TestData.MAIN_URL)
        order_page.load_page()
        order_page.wait_ingredients_field()
        order_page.drag_and_drop_fluorescent_bread_ingredient()
        assert order_page.get_counter_of_fluorescent_bread() == '2'

    @allure.title('Проверка создания заказа пользователем')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_creating_order_with_one_ingredient_return_order_id(self):
        order_page = CreateOrderPage(self.driver, TestData.MAIN_URL)
        order_page.load_page()
        order_page.wait_ingredients_field()
        order_page.drag_and_drop_fluorescent_bread_ingredient()
        order_page.click_create_order_button()
        assert order_page.get_order_id() is not None
    