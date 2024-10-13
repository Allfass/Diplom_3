from locators.password_recover import PasswordRecoverLocators
from pages.page import BasePage


class PasswordRecoverPage(BasePage):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.password_recover_locators = PasswordRecoverLocators()

    def click_link_to_recover_password_page(self):
        super().click_on_element_with_javascript(
            self.password_recover_locators.link_to_page
        )

    def wait_load_recover_page(self):
        super().wait_for_load_page(self.password_recover_locators.title)

    def check_recover_page_is_loaded(self):
        return super().check_page_load(self.password_recover_locators.title)

    def input_email(self, mail):
        super().input_value(self.password_recover_locators.email_input, mail)

    def click_recover_password_button(self):
        super().click_on_element_with_javascript(
            self.password_recover_locators.recover_button
        )

    def wait_second_recover_stage(self):
        super().wait_for_load_page(self.password_recover_locators.show_hide_button)

    def check_second_recover_stage_is_loaded(self):
        return super().check_page_load(
            self.password_recover_locators.verification_code_input
        )

    def click_show_hide_button(self):
        super().click_on_element_with_javascript(
            self.password_recover_locators.show_hide_button
        )

    def check_password_field_in_focus(self):
        return super().check_page_load(
            self.password_recover_locators.password_field_in_focus
        )
