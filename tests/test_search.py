from ast import Assert
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from pom.pages.HomePage import HomeP
from pom.pages.ResultsPage import ResultsP


# this would be a good place for configurations (throttle, cookies, auth, i/o)
# apparently can also group tests by fixtures
@pytest.fixture(params=['Pixel 7', 'iPhone 14 Pro Max', 'Samsung Galaxy S20 Ultra'])
def devices(request) -> str:
    return request.param


# these are only to demo use of merged fixtures and fixtures for fixtures
@pytest.fixture(params=[0, 3])
def perf_buffer(request) -> int:
    return request.param


@pytest.fixture
def default_user(devices):
    mobile_emulation = {"deviceName": devices}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://ecommerce-playground.lambdatest.io/')
    yield driver


def test_text_search(default_user, perf_buffer):
    home_page = HomeP(default_user)
    home_page.main_nav.search_bar.send_keys('iPad')
    home_page.main_nav.search_button.click()
    default_user.implicitly_wait(perf_buffer)
    assert 'There is no product that matches the search criteria.' in default_user.page_source

    default_user.quit()


def test_categorical_search(default_user, perf_buffer):
    home_page = HomeP(default_user)
    home_page.main_nav.expand_dropdown()
    home_page.main_nav.dropdown_options.desktops.click()
    home_page.main_nav.search_button.click()
    default_user.implicitly_wait(perf_buffer)

    results_page = ResultsP(default_user)
    assert 'Desktops' in results_page.category_dropdown.first_selected_option.text

    default_user.quit()


def test_text_categorical_search(default_user, perf_buffer):
    home_page = HomeP(default_user)
    home_page.main_nav.search_bar.send_keys('iPad')
    home_page.main_nav.expand_dropdown()
    home_page.main_nav.dropdown_options.laptops.click()
    home_page.main_nav.search_button.click()
    default_user.implicitly_wait(perf_buffer)

    results_page = ResultsP(default_user)
    assert 'Laptops' in results_page.category_dropdown.first_selected_option.text
    assert 'iPad' in results_page.keyword.get_attribute('value')

    default_user.quit()
