from selenium.webdriver.common.by import By
from Locators.locators import LogoutLocator
from pages.HomePage import HomePage


class LOGOUT(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = LogoutLocator
        super(LOGOUT, self).__init__(driver)

    # self.button_logout_xpath = Locators.button_logout_xpath
    # self.logout_link_xpath = Locators.logout_link_xpath

    def clickWelcome(self):
        self.Find_Element(*self.locator.button_logout_xpath).click()

    def clickLogout(self):
        self.Find_Element(*self.locator.logout_link_xpath).click()
