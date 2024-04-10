'''File to store tests.'''
from selenium import webdriver
import pytest
import allure

from pom.pages.home_page import HomeP
from pom.pages.results_page import ResultsP


@pytest.fixture(name="devices", params=['Pixel 7', 'iPhone 14 Pro Max', 'Samsung Galaxy S20 Ultra'])
@allure.title('Choose devices for tests')
def fixture_devices(request) -> str:
    '''this would be a good place for configurations (throttle, cookies, auth, i/o)
    apparently can also group tests by fixtures'''
    return request.param


@pytest.fixture(name="perf_buffer", params=[0, 3])
@allure.title('Set fixed wait time')
@allure.description('Not very good practice, sometimes useful.')
def fixture_perf_buffer(request) -> int:
    '''these are only to demo use of merged fixtures and fixtures for fixtures
    '''
    return request.param


@pytest.fixture(name="default_user")
@allure.title('Configure client to be used')
@allure.description('This would be a good place to store session.')
def fixture_default_user(devices):
    '''Fixture for client configuration.'''
    mobile_emulation = {"deviceName": devices}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://ecommerce-playground.lambdatest.io/')
    yield driver


@allure.parent_suite("E2E")
@allure.suite("Home Page")
@allure.title("Search by text only")
@allure.description("This is a description for this test.")
def test_text_search(default_user, perf_buffer):
    '''Test to search by text-only'''
    home_page = HomeP(default_user)
    home_page.main_nav.search_bar.send_keys('iPad')
    home_page.main_nav.search_button.click()
    default_user.implicitly_wait(perf_buffer)
    assert 'There is no product that matches the search criteria.' in default_user.page_source

    default_user.quit()


@allure.parent_suite("E2E")
@allure.suite("Home Page")
@allure.title("Search by category only")
@allure.description("This is a description for this test.")
def test_categorical_search(default_user, perf_buffer):
    '''Test to search by category'''
    home_page = HomeP(default_user)
    home_page.main_nav.expand_dropdown()
    home_page.main_nav.dropdown_options.desktops.click()
    home_page.main_nav.search_button.click()
    default_user.implicitly_wait(perf_buffer)

    results_page = ResultsP(default_user)
    assert 'Desktops' in results_page.category_dropdown.first_selected_option.text

    default_user.quit()


@allure.parent_suite("E2E")
@allure.suite("Home Page")
@allure.title("Search by text and category")
@allure.description("This is a description for this test.")
def test_text_categorical_search(default_user, perf_buffer):
    '''Test to search by text AND category'''
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
