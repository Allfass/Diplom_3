from pages.page import BasePage
import time
from locators.create_order import CreateOrderLocators


class CreateOrderPage(BasePage):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.create_order_locators = CreateOrderLocators()

    def click_on_constructor_button(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.constructor_button
        )

    def wait_constructor_page_loading(self):
        super().wait_for_load_page(self.create_order_locators.constructor_title)

    def check_constructor_page_is_loaded(self):
        return super().check_page_load(self.create_order_locators.constructor_title)

    def click_on_order_feed(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.order_feed_button
        )

    def wait_feed_page_loading(self):
        super().wait_for_load_page(self.create_order_locators.order_feed_title)

    def check_order_feed_is_loaded(self):
        return super().check_page_load(self.create_order_locators.order_feed_title)

    def wait_ingredients_field(self):
        super().wait_for_load_page(self.create_order_locators.fluorescent_bread_ingredient)

    def click_on_fluorescent_bread_ingredient(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.fluorescent_bread_ingredient
        )
    
    def wait_ingredient_field(self):
        super().wait_for_load_page(self.create_order_locators.fluorescent_bread_ingredient_title)

    def check_fluorescent_bread_ingredient_title(self):
        return super().check_page_load(
            self.create_order_locators.fluorescent_bread_ingredient_title
        )

    def click_ingredient_close_button(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.ingredient_close_button
        )

    def wait_invisible_ingredient_field(self):
        super().wait_invisible_element(
            self.create_order_locators.fluorescent_bread_ingredient_title
        )

    def check_ingredient_field_is_closed(self):
        return not super().element_is_displayed(
            self.create_order_locators.fluorescent_bread_ingredient_title
        )

    def drag_and_drop_fluorescent_bread_ingredient(self):
        super().drag_and_drop(
            self.create_order_locators.fluorescent_bread_ingredient,
            self.create_order_locators.order_drop_field,
        )

    def wait_counter_loading(self):
        super().wait_for_load_page(self.create_order_locators.fluorescent_bread_ingredient_counter)

    def get_counter_of_fluorescent_bread(self):
        return super().get_element_text(
            self.create_order_locators.fluorescent_bread_ingredient_counter
        )

    def click_create_order_button(self):
        super().click_on_element_with_javascript(
            self.create_order_locators.create_order_button
        )
    
    def get_order_id(self):
        for _ in range(10):
            element = super().get_element_text(self.create_order_locators.order_id)
            if element == "9999":
                time.sleep(1)
            else:
                return element
        return None
