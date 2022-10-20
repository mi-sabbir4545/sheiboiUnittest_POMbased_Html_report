from pages.HomePage import HomePage
from Locators.locators import BottomNavBarLocator
from selenium.webdriver import ActionChains
from pages.BasePage import BasePage


class BottomNavBar(HomePage):

    def __init__(self, driver):
        self.driver = driver
        self.locator = BottomNavBarLocator
        super(BottomNavBar, self).__init__(driver)

    def click_facebook(self):
        self.Find_Element(*self.locator.click_facebookicon).click()

    def click_twitter(self):
        self.Find_Element(*self.locator.click_twittericon).click()

    def click_youtube(self):
        self.Find_Element(*self.locator.click_youtubeicon).click()

    def click_playstore(self):
        self.Find_Element(*self.locator.click_playstoreicon).click()

    def click_appstore(self):
        self.Find_Element(*self.locator.click_appstoreicon).click()

    def click_help(self):
        self.Find_Element(*self.locator.click_helpbutton).click()

    def scroll_to_up(self):
        self.scroll_to_element()