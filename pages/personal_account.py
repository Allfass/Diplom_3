from pages.page import Page
from locators.personal_account import PersonalAccountLocators
from helper import TestHelper
import allure


class PersonalAccountPage(Page):
    def __init__(self, driver, main_url) -> None:
        super().__init__(driver, main_url)
        self.personal_account_locators = PersonalAccountLocators()

    @allure.step('Нажимаем кнопку личного кабинета')
    def click_personal_account_button(self):
        super().click_on_element_with_javascript(
            self.personal_account_locators.personal_account_button
        )

    @allure.step('Ждём загрузку личного кабинета')
    def wait_personal_account_is_loaded(self):
        super().wait_for_load_page(self.personal_account_locators.profile_button)

    @allure.step('Проверяем что страница личного кабинета загружена')
    def check_personal_account_is_loaded(self):
        return super().check_page_load(self.personal_account_locators.profile_button)

    @allure.step('Нажимаем кнопку истории заказов')
    def click_order_history_button(self):
        super().click_on_element_with_javascript(
            self.personal_account_locators.order_history_button
        )

    @allure.step('Ждем пока созданный заказ будет видимым')
    def wait_created_order_is_visiable(self):
        super().wait_for_load_page(self.personal_account_locators.created_order)

    @allure.step('Получить текущий заказ по идентификатору')
    def get_order_by_id(self, id):
        return super().get_element_text(TestHelper.replacer(self.personal_account_locators.created_order, id))

    @allure.step('Проверяем что созданный заказ будет видимым')
    def check_created_order_is_visiable(self):
        return super().check_page_load(self.personal_account_locators.created_order)

    @allure.step('Нажимаем кнопку выхода из аккаунта')
    def click_account_exit_button(self):
        super().click_on_element_with_javascript(
            self.personal_account_locators.account_exit_button
        )

    @allure.step('Ждём загрузку страницы личного кабинета')
    def wait_login_page_loading(self):
        super().wait_for_load_page(self.personal_account_locators.login_page_title)

    @allure.step('Проверяем что страница личного кабинета загружена')
    def check_login_page_loading(self):
        return super().check_page_load(self.personal_account_locators.login_page_title)
