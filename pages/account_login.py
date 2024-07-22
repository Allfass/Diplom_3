from locators.account_login import AccountLoginLocators
from pages.page import Page
from data import TestData
import allure


class AccountLogin(Page):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.account_login_locators = AccountLoginLocators()

    @allure.step('Вводим email')
    def input_email(self):
        super().input_value(
            self.account_login_locators.email_field, TestData.TESTER_EMAIL
        )

    @allure.step('Вводим пароль')
    def input_password(self):
        super().input_value(
            self.account_login_locators.password_field, TestData.TESTER_PASSWORD
        )

    @allure.step('Нажимаем на кнопку логина')
    def click_login_button(self):
        super().click_on_element_with_javascript(
            self.account_login_locators.login_button
        )

    @allure.step('Ждем загрузки страницы после авторизации')
    def wait_loading_page_after_login(self):
        super().wait_for_load_page(self.account_login_locators.main_page_title)
