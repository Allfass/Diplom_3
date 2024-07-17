from pages.password_recover import PasswordRecoverPage
from data import TestData
import pytest
import allure 


@pytest.mark.usefixtures("driver")
class TestPasswordRecover():
    def test_password_recover_transition_to_page(self):
        recover_page = PasswordRecoverPage(self.driver, TestData.LOGIN_URL)
        recover_page.load_page()
        recover_page.click_link_to_recover_password_page()
        recover_page.wait_load_recover_page()
        assert recover_page.check_recover_page_is_loaded() is not None
        
    def test_enter_password_and_click_recover_button_transition_to_second_recover_stage(self):
        recover_page = PasswordRecoverPage(self.driver, TestData.RECOVER_PASSWORD_URL)
        recover_page.load_page()
        recover_page.input_email(TestData.TESTER_EMAIL)
        recover_page.click_recover_password_button()
        assert recover_page.check_second_recover_stage_is_loaded is not None
        
    def test_click_eye_button_activate_css_style(self):
        recover_page = PasswordRecoverPage(self.driver, TestData.RECOVER_PASSWORD_URL)
        recover_page.load_page()
        recover_page.input_email(TestData.TESTER_EMAIL)
        recover_page.click_recover_password_button()
        recover_page.wait_second_recover_stage()
        recover_page.click_show_hide_button()
        assert recover_page.check_password_field_in_focus is not None