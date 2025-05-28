import pytest
import allure
from selenium import webdriver
from pages.route_page import RoutePage
from urls import Urls


@pytest.fixture(scope='function')
def driver():
    with allure.step('Open browser.'):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)
    with allure.step('Open main page.'):
        driver.get(Urls.ROUTE_PAGE)
    yield driver
    with allure.step('Close browser.'):
        driver.quit()


@pytest.fixture(scope='function')
def route_page(driver):
    route_page = RoutePage(driver)
    return route_page
