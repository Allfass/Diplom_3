import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from pages.account_login import AccountLogin
from data import TestData


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="no")

@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    if request.config.getoption("--headless") == "yes":
        firefox_opts = FirefoxOptions()
        chrome_opts = ChromeOptions()
        firefox_opts.add_argument("--headless")
        chrome_opts.add_argument("--headless=new")

        if request.param == "firefox":
            service = FirefoxService(TestData.FIREFOX_DRIVER_PATH)
            browser = webdriver.Firefox(options=firefox_opts, service=service)
        else:
            service = ChromeService(TestData.CHROME_DRIVER_PATH)
            browser = webdriver.Chrome(options=chrome_opts, service=service)
    else:
        if request.param == "firefox":
            service = FirefoxService(TestData.FIREFOX_DRIVER_PATH)
            browser = webdriver.Firefox(service=service)
        else:
            service = ChromeService(TestData.CHROME_DRIVER_PATH)
            browser = webdriver.Chrome(service=service)
    request.cls.driver = browser
    yield request.cls.driver
    request.cls.driver.quit()


@pytest.fixture()
def logined_user(driver):
    logined_user = AccountLogin(driver, TestData.LOGIN_URL)
    logined_user.load_page()
    logined_user.input_email()
    logined_user.input_password()
    logined_user.click_login_button()
    logined_user.wait_loading_page_after_login()
    return logined_user.driver
