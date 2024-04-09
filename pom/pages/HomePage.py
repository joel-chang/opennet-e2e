from pom.locators.Locators import HomePageLocators as Locators
from selenium.webdriver.common.by import By
import sys

from pom.objects.MainNav import MainNav
sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())


class HomeP(object):
    def __init__(self, driver):
        self.driver = driver
        self.main_nav = MainNav(
            driver,
            driver.find_element(*Locators.MAIN_NAV)
        )
