from pages.order_feed import OrderFeed
from data import TestData
import pytest
import allure

@pytest.mark.usefixtures("user_with_order")
class TestOrderFeed():
    def test_click_on_order_display_description(self):
        
        order_feed = OrderFeed(self.driver, TestData.LOGIN_URL)
        order_feed.load_page()
        order_feed.click_on_order_feed()
        order_feed.wait_feed_page_loading()
        order_feed.click_first_order()
        assert order_feed.check_first_order_title() == 'Флюоресцентный бургер'
        