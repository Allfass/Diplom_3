from pages.order_feed import OrderFeed
from pages.personal_account import PersonalAccountPage
from pages.create_order import CreateOrderPage
from data import TestData
import pytest
import allure

class TestOrderFeed():
    @allure.title('Проверка клика на заказ')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_on_order_display_description(self, user_with_order):
        order_feed = OrderFeed(user_with_order[1], TestData.LOGIN_URL)
        order_feed.load_page()
        order_feed.click_on_order_feed()
        order_feed.wait_feed_page_loading()
        order_feed.click_first_order()
        assert order_feed.check_first_order_title() == 'Флюоресцентный бургер'

    @allure.title('Проверка заказов пользователя')
    @allure.description('Заказы пользователя из раздела История заказов отображаются на странице Лента заказов')
    def test_order_in_order_feed_display_in_personal_account(self, user_with_order):
        order_feed = OrderFeed(user_with_order[1], TestData.LOGIN_URL)
        order_feed.load_page()
        order_feed.click_on_order_feed()
        order_feed.wait_feed_page_loading()
        order_in_order_feed = order_feed.get_order_by_id(user_with_order[0])
        personal_page = PersonalAccountPage(order_feed.driver, TestData.LOGIN_URL)
        personal_page.click_personal_account_button()
        personal_page.wait_personal_account_is_loaded()
        personal_page.click_order_history_button()
        personal_page.wait_created_order_is_visiable()
        order_in_personal_page = personal_page.get_order_by_id(user_with_order[0])
        assert order_in_order_feed == order_in_personal_page

    @allure.title('Проверка счётчика Выполнено за всё время')
    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_create_order_increase_completed_all_time_counter(self, logined_user):
        order_feed = OrderFeed(logined_user, TestData.LOGIN_URL)
        order_feed.load_page()
        order_feed.click_on_order_feed()
        order_feed.wait_feed_page_loading()
        current_orders = order_feed.get_completed_all_time_text()
        user_with_order = CreateOrderPage(logined_user, TestData.MAIN_URL)
        user_with_order.load_page()
        user_with_order.wait_ingredients_field()
        user_with_order.drag_and_drop_fluorescent_bread_ingredient()
        user_with_order.click_create_order_button()
        user_with_order.click_ingredient_close_button()
        order_feed.click_on_order_feed()
        order_feed.wait_feed_page_loading()
        new_orders = order_feed.get_completed_all_time_text()
        assert int(new_orders) == int(current_orders) + 1

    @allure.title('Проверка счётчика Выполнено за сегодня')
    @allure.description('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_order_increase_complete_today_counter(self, logined_user):
        order_feed = OrderFeed(logined_user, TestData.LOGIN_URL)
        order_feed.load_page()
        order_feed.click_on_order_feed()
        order_feed.wait_feed_page_loading()
        current_orders = order_feed.get_completed_today_text()
        user_with_order = CreateOrderPage(logined_user, TestData.MAIN_URL)
        user_with_order.load_page()
        user_with_order.wait_ingredients_field()
        user_with_order.drag_and_drop_fluorescent_bread_ingredient()
        user_with_order.click_create_order_button()
        user_with_order.click_ingredient_close_button()
        order_feed.click_on_order_feed()
        order_feed.wait_feed_page_loading()
        new_orders = order_feed.get_completed_today_text()
        assert int(new_orders) == int(current_orders) + 1

    @allure.title('Проверка раздела В работе')
    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_create_order_add_order_to_working_table(self, user_with_order):
        order_feed = OrderFeed(user_with_order[1], TestData.LOGIN_URL)
        order_feed.load_page()
        order_feed.click_on_order_feed()
        order_feed.wait_feed_page_loading()
        assert order_feed.get_today_order_by_id() == f'0{user_with_order[0]}'