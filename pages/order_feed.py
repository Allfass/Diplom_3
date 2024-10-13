from pages.page import BasePage
from locators.order_feed import OrderFeedLocators
from helper import TestHelper
import allure


class OrderFeed(BasePage):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.order_feed_locators = OrderFeedLocators()

    @allure.step('Нажимаем кнопку ленты заказов')
    def click_on_order_feed(self):
        super().click_on_element_with_javascript(
            self.order_feed_locators.order_feed_button
        )

    @allure.step('Ждем загрузку страницы с лентой заказов')
    def wait_feed_page_loading(self):
        super().wait_for_load_page(self.order_feed_locators.order_feed_title)

    @allure.step('Нажимаем кнопку первого заказа')
    def click_first_order(self):
        super().click_on_element_with_javascript(self.order_feed_locators.first_order_in_list)

    @allure.step('Проверяем заголовок открытого заказа')
    def check_first_order_title(self):
        return super().get_element_text(self.order_feed_locators.first_order_title)

    @allure.step('Получаем текущий заказ по идентификатору')
    def get_order_by_id(self, id):
        return super().get_element_text(TestHelper.replacer(self.order_feed_locators.order_by_id, id))
