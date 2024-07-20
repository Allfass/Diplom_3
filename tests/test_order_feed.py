from pages.order_feed import OrderFeed
from pages.personal_account import PersonalAccountPage
from data import TestData
import pytest
import allure

class TestOrderFeed():
    @pytest.mark.skip()
    def test_click_on_order_display_description(self, user_with_order):
        order_feed = OrderFeed(user_with_order[1], TestData.LOGIN_URL)
        order_feed.load_page()
        order_feed.click_on_order_feed()
        order_feed.wait_feed_page_loading()
        order_feed.click_first_order()
        assert order_feed.check_first_order_title() == 'Флюоресцентный бургер'
        
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
        order_in_personal_page = personal_page.get_order_by_id(user_with_order[0])
        assert order_in_order_feed == order_in_personal_page
