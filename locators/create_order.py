from selenium.webdriver.common.by import By


class CreateOrderLocators:
    constructor_button = [By.XPATH, "//p[contains(text(), 'Конструктор')]"]
    constructor_title = [By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"]
    order_feed_button = [By.XPATH, "//p[contains(text(), 'Лента Заказов')]"]
    order_feed_title = [By.XPATH, "//h1[contains(text(), 'Лента заказов')]"]
    fluorescent_bread_ingredient = [
        By.XPATH,
        "//p[contains(text(), 'Флюоресцентная булка R2-D3')]//ancestor::a[contains(@class, 'BurgerIngredient_ingredient')]",
    ]
    fluorescent_bread_ingredient_title = [
        By.XPATH,
        "//div[contains(@class, 'undefined')]//following::p[contains(text(), 'Флюоресцентная булка R2-D3')]",
    ]
    ingredient_close_button = [By.CSS_SELECTOR, ".Modal_modal_opened button"]
    order_drop_field = [
        By.XPATH,
        "//span[contains(text(), 'Перетяните булочку сюда (верх)')]",
    ]
    fluorescent_bread_ingredient_counter = [
        By.XPATH,
        "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]//ancestor::p[contains(@class, 'counter_counter')]",
    ]
    create_order_button = [By.XPATH, "//button[contains(text(), 'Оформить заказ')]"]
    order_id = [
        By.XPATH,
        "//p[contains(text(), 'идентификатор заказа')]//preceding::h2[contains(@class, 'text_type_digits-large mb-8')]",
    ]
