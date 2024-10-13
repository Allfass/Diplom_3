from pages.page import BasePage
from locators.order_feed import OrderFeedLocators
from helper import TestHelper


class OrderFeed(BasePage):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.order_feed_locators = OrderFeedLocators()
    
    def click_on_order_feed(self):
        super().click_on_element_with_javascript(
            self.order_feed_locators.order_feed_button
        )

    def wait_feed_page_loading(self):
        super().wait_for_load_page(self.order_feed_locators.order_feed_title)

        
    def click_first_order(self):
        super().click_on_element_with_javascript(self.order_feed_locators.first_order_in_list)
        
    def check_first_order_title(self):
        return super().get_element_text(self.order_feed_locators.first_order_title)
    
    def get_order_by_id(self, id):
        super().get_element_text(TestHelper.replacer(self.order_feed_locators.order_by_id, id))
        
    def get_completed_all_time_text(self):
        super().get_element_text(self.order_feed_locators.complete_all_time)
        
    def get_completed_today_text(self):
        super().get_element_text(self.order_feed_locators.complete_today)
        
    def get_today_order_by_id(self, id):
        super().get_element_text(TestHelper.replacer(self.order_feed_locators.today_in_work, id))
        
    