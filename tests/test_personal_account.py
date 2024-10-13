from pages.personal_account import PersonalAccountPage
from data import TestData
import pytest
import allure


@pytest.mark.usefixtures("logined_user")
class TestPersonalAccount:
    @allure.title('Проверка кнопки Личный кабинет')
    @allure.description('переход по клику на Личный кабинет')
    def test_transition_to_personal_account(self):
        personal_page = PersonalAccountPage(self.driver, TestData.MAIN_URL)
        personal_page.click_personal_account_button()
        personal_page.wait_personal_account_is_loaded()
        assert personal_page.check_personal_account_is_loaded() is not None

    @allure.title('Проверка кнопки История заказов')
    @allure.description('переход в раздел История заказов')
    def test_click_to_history_button_return_created_order(self):
        personal_page = PersonalAccountPage(self.driver, TestData.USER_PROFILE_URL)
        personal_page.load_page()
        personal_page.wait_personal_account_is_loaded()
        personal_page.click_order_history_button()
        personal_page.wait_created_order_is_visiable()
        assert personal_page.check_created_order_is_visiable() is not None

    @allure.title('Проверка кнопки Выход из аккаунта')
    @allure.description('Выход из аккаунта')
    def test_click_to_exit_button_load_main_page(self):
        personal_page = PersonalAccountPage(self.driver, TestData.USER_PROFILE_URL)
        personal_page.load_page()
        personal_page.wait_personal_account_is_loaded()
        personal_page.click_account_exit_button()
        personal_page.wait_login_page_loading()
        assert personal_page.check_login_page_loading() is not None
