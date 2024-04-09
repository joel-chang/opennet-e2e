from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class HomePageLocators(object):
    MAIN_NAV = (By.XPATH, '//*[@id="main-navigation"]')
    CATEGORY_ID = (By.NAME, 'category_id')


class MainNavLocators(object):
    SEARCH_BAR = (By.NAME, 'search')
    DROPDOWN_TOGGLE = (By.CLASS_NAME, 'search-category')
    SEARCH_BUTTON = (By.CLASS_NAME, 'search-button')


class ResultsPageLocators(object):
    CATEGORY_DROPDOWN = (By.XPATH, '//*[@id="entry_212457"]/div/div[2]/select')
    KEYWORD = (By.XPATH, '//*[@id="input-search"]')


class CategoryDropdownOptions(object):
    DESKTOPS = (By.LINK_TEXT, 'Desktops')
    LAPTOPS = (By.LINK_TEXT, 'Laptops')
    COMPONENTS = (By.LINK_TEXT, 'Components')
    TABLETS = (By.LINK_TEXT, 'Tablets')
    SOFTWARE = (By.LINK_TEXT, 'Software')
    PHONES = (By.LINK_TEXT, 'Phones & PDAs')
    CAMERAS = (By.LINK_TEXT, 'Cameras')
    MP3 = (By.LINK_TEXT, 'MP3 Players')
