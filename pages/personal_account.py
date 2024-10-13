from pages.page import BasePage
from locators.personal_account import PersonalAccountLocators
from helper import TestHelper


class PersonalAccountPage(BasePage):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.personal_account_locators = PersonalAccountLocators()

    def click_personal_account_button(self):
        super().click_on_element_with_javascript(
            self.personal_account_locators.personal_account_button
        )

    def wait_personal_account_is_loaded(self):
        super().wait_for_load_page(self.personal_account_locators.profile_button)

    def check_personal_account_is_loaded(self):
        return super().check_page_load(self.personal_account_locators.profile_button)

    def click_order_history_button(self):
        super().click_on_element_with_javascript(
            self.personal_account_locators.order_history_button
        )

    def wait_created_order_is_visiable(self):
        super().wait_for_load_page(self.personal_account_locators.created_order)

    def get_order_by_id(self, id):
        super().get_element_text(TestHelper.replacer(self.personal_account_locators.created_order, id))

    def check_created_order_is_visiable(self):
        return super().check_page_load(self.personal_account_locators.created_order)

    def click_account_exit_button(self):
        super().click_on_element_with_javascript(
            self.personal_account_locators.account_exit_button
        )

    def wait_login_page_loading(self):
        super().wait_for_load_page(self.personal_account_locators.login_page_title)

    def check_login_page_loading(self):
        return super().check_page_load(self.personal_account_locators.login_page_title)
