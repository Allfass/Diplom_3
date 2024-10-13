from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    personal_account_button = [By.XPATH, "//a[contains(@href, '/account')]"]
    order_history_button = [By.XPATH, "//a[contains(text(), 'История заказов')]"]
    account_exit_button = [By.XPATH, "//button[contains(text(), 'Выход')]"]
    profile_button = [By.XPATH, "//a[contains(text(), 'Профиль')]"]
    created_order = [By.XPATH, "//p[contains(text(), '#098557')]"]
    login_page_title = [By.XPATH, "//h2[contains(text(), 'Вход')]"]
    
