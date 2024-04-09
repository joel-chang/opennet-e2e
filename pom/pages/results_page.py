'''Results page.'''
import sys
from selenium.webdriver.support.select import Select
from pom.locators.locators import ResultsPageLocators

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())


class ResultsP:
    '''Results page.'''
    def __init__(self, driver):
        self.driver = driver
        self.category_dropdown = Select(driver.find_element(
            *ResultsPageLocators.CATEGORY_DROPDOWN))
        self.keyword = driver.find_element(*ResultsPageLocators.KEYWORD)
