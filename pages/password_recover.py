from locators.password_recover import PasswordRecoverLocators
from pages.page import Page
import allure


class PasswordRecoverPage(Page):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.password_recover_locators = PasswordRecoverLocators()

    @allure.step('Нажимаем на кнопку восстановления пароля')
    def click_link_to_recover_password_page(self):
        super().click_on_element_with_javascript(
            self.password_recover_locators.link_to_page
        )

    @allure.step('Ждём загрузку страницы восстановления пароля')
    def wait_load_recover_page(self):
        super().wait_for_load_page(self.password_recover_locators.title)

    @allure.step('Проверяем что страница восстановления пароля загружена')
    def check_recover_page_is_loaded(self):
        return super().check_page_load(self.password_recover_locators.title)

    @allure.step('Вводим почту')
    def input_email(self, mail):
        super().input_value(self.password_recover_locators.email_input, mail)

    @allure.step('Нажимаем на кнопку восстановления пароля')
    def click_recover_password_button(self):
        super().click_on_element_with_javascript(
            self.password_recover_locators.recover_button
        )

    @allure.step('Ждём загрузку второй стадии восстановления пароля')
    def wait_second_recover_stage(self):
        super().wait_for_load_page(self.password_recover_locators.show_hide_button)

    @allure.step('Проверяем что страница второй стадии восстановления пароля загружена')
    def check_second_recover_stage_is_loaded(self):
        return super().check_page_load(
            self.password_recover_locators.verification_code_input
        )

    @allure.step('Нажимаем на кнопку отображения пароля')
    def click_show_hide_button(self):
        super().click_on_element_with_javascript(
            self.password_recover_locators.show_hide_button
        )

    @allure.step('Проверяем что поле пароля в фокусе')
    def check_password_field_in_focus(self):
        return super().check_page_load(
            self.password_recover_locators.password_field_in_focus
        )
