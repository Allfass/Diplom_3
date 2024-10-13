from selenium.webdriver.common.by import By


class PasswordRecoverLocators:
    link_to_page = [
        By.XPATH,
        "//a[contains(text(), 'Восстановить пароль') and contains(@class, 'Auth_link')]",
    ]
    title = [By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]"]
    email_input = [
        By.XPATH,
        "//label[contains(text(), 'Email')]//following::input[contains(@class, 'text')]",
    ]
    recover_button = [By.XPATH, "//button[contains(text(), 'Восстановить')]"]
    verification_code_input = [
        By.XPATH,
        "//label[contains(text(), 'Введите код из письма')]//following::input[contains(@class, 'text')]",
    ]
    show_hide_button = [By.XPATH, "//div[contains(@class, 'input__icon')]"]
    password_field_in_focus = [By.CSS_SELECTOR, ".input_status_active"]
