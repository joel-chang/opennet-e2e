from time import sleep
from pom.locators.Locators import MainNavLocators
from pom.locators.Locators import CategoryDropdownOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())


class Dropdown(object):
    def __init__(self, driver, root):
        self.driver = driver
        self.root = root
        self.desktops = root.find_element(*CategoryDropdownOptions.DESKTOPS)
        self.laptops = root.find_element(*CategoryDropdownOptions.LAPTOPS)
        self.components = root.find_element(
            *CategoryDropdownOptions.COMPONENTS)
        self.tablets = root.find_element(*CategoryDropdownOptions.TABLETS)
        self.software = root.find_element(*CategoryDropdownOptions.SOFTWARE)
        self.phones = root.find_element(*CategoryDropdownOptions.PHONES)
        self.cameras = root.find_element(*CategoryDropdownOptions.CAMERAS)
        self.mp3 = root.find_element(*CategoryDropdownOptions.MP3)


class MainNav(object):
    def __init__(self, driver, root):
        self.driver = driver
        self.root = root
        self.search_bar = root.find_element(*MainNavLocators.SEARCH_BAR)
        self.dropdown_toggle = root.find_element(
            *MainNavLocators.DROPDOWN_TOGGLE)
        self.search_button = root.find_element(*MainNavLocators.SEARCH_BUTTON)

    def expand_dropdown(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainNavLocators.DROPDOWN_TOGGLE))
        self.dropdown_toggle.click()
        self.dropdown_options = Dropdown(self.driver, self.root)
