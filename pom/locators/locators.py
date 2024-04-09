'''File in which to store locators, would probably split into
    many due to having a lot of interactable elements in a page.'''
from dataclasses import dataclass
from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

@dataclass
class HomePageLocators:
    '''Locators for homepage (I would put the url here)'''
    MAIN_NAV = (By.XPATH, '//*[@id="main-navigation"]')
    CATEGORY_ID = (By.NAME, 'category_id')


@dataclass
class MainNavLocators:
    '''Locators for object called main nav (I would put the class name/ id here)'''
    SEARCH_BAR = (By.NAME, 'search')
    DROPDOWN_TOGGLE = (By.CLASS_NAME, 'search-category')
    SEARCH_BUTTON = (By.CLASS_NAME, 'search-button')


@dataclass
class ResultsPageLocators:
    '''Locators for the results page'''
    CATEGORY_DROPDOWN = (By.XPATH, '//*[@id="entry_212457"]/div/div[2]/select')
    KEYWORD = (By.XPATH, '//*[@id="input-search"]')


@dataclass
class CategoryDropdownOptions:
    '''Locators for the category dropdown'''
    DESKTOPS = (By.LINK_TEXT, 'Desktops')
    LAPTOPS = (By.LINK_TEXT, 'Laptops')
    COMPONENTS = (By.LINK_TEXT, 'Components')
    TABLETS = (By.LINK_TEXT, 'Tablets')
    SOFTWARE = (By.LINK_TEXT, 'Software')
    PHONES = (By.LINK_TEXT, 'Phones & PDAs')
    CAMERAS = (By.LINK_TEXT, 'Cameras')
    MP3 = (By.LINK_TEXT, 'MP3 Players')
