from selenium.webdriver.common.by import By


class AccountLoginLocators:
    email_field = [
        By.XPATH,
        "//label[contains(text(), 'Email')]//following::input[contains(@class, 'text')]",
    ]
    password_field = [
        By.XPATH,
        "//label[contains(text(), 'Пароль')]//following::input[contains(@class, 'text')]",
    ]
    login_button = [By.XPATH, "//button[contains(text(), 'Войти')]"]
    main_page_title = [By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"]
