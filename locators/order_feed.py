from selenium.webdriver.common.by import By


class OrderFeedLocators:
    order_feed_button = [By.XPATH, "//p[contains(text(), 'Лента Заказов')]"]
    order_feed_title = [By.XPATH, "//h1[contains(text(), 'Лента заказов')]"]
    first_order_in_list = [By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//descendant::a[1]"]
    first_order_title = [By.XPATH, "//div[contains(@class, 'Modal_orderBox')]//descendant::h2"]
    order_by_id = [By.XPATH, "//p[contains(text(), '#098557')]"]
    complete_all_time = []
    complete_today = []
    today_in_work = []