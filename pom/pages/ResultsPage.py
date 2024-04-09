from pom.locators.Locators import ResultsPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())


class ResultsP(object):
    def __init__(self, driver):
        self.driver = driver
        self.category_dropdown = Select(driver.find_element(
            *ResultsPageLocators.CATEGORY_DROPDOWN))
        self.keyword = driver.find_element(*ResultsPageLocators.KEYWORD)
