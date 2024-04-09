'''pom for elements'''
import sys
from dataclasses import dataclass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pom.locators.locators import MainNavLocators
from pom.locators.locators import CategoryDropdownOptions
sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())


@dataclass
class Dropdown:
    '''Object to represent dropdown element'''
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



class MainNav:
    '''Object main nav element '''
    def __init__(self, driver, root):
        self.driver = driver
        self.root = root
        self.search_bar = root.find_element(*MainNavLocators.SEARCH_BAR)
        self.dropdown_toggle = root.find_element(
            *MainNavLocators.DROPDOWN_TOGGLE)
        self.search_button = root.find_element(*MainNavLocators.SEARCH_BUTTON)
        self.dropdown_options = None

    def expand_dropdown(self):
        '''encapsulate actions needed to expand the main nav's dropdown'''
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainNavLocators.DROPDOWN_TOGGLE))
        self.dropdown_toggle.click()
        self.dropdown_options = Dropdown(self.driver, self.root)
