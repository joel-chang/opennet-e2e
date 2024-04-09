'''To represent HomePage'''
import sys
from pom.locators.locators import HomePageLocators as Locators

from pom.objects.main_nav import MainNav
sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())


class HomeP:
    '''To represent home page'''
    def __init__(self, driver):
        self.driver = driver
        self.main_nav = MainNav(
            driver,
            driver.find_element(*Locators.MAIN_NAV)
        )
