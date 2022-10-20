from selenium.webdriver.common.by import By
from Locators.locators import LoginLocators
from pages.HomePage import HomePage
# from pages.BasePage import BasePage


class LoginPage(HomePage):

    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginLocators
        super(LoginPage, self).__init__(driver)

        # self.textbox_username_xpath = Locators.textbox_username_xpath
        # self.textbox_password1_xpath = Locators.textbox_password1_xpath
        # self.textbox_password2_xpath = Locators.textbox_password2_xpath
        # self.button_login_xpath = Locators.button_login_xpath

    def clickLoginIcon(self):
        self.Find_Element(*self.locator.click_login_icon).click()

    def clickLoginButton(self):
        self.Find_Element(*self.locator.click_login_button).click()

    def enter_username(self, username):
        # self.driver.find_element(self.textbox_username_xpath).click()
        self.Find_Element(*self.locator.textbox_username_xpath).send_keys(username)

    def enter_password1(self):
        self.Find_Element(*self.locator.textbox_password1_xpath).click()

    def enter_password2(self, password):
        self.Find_Element(*self.locator.textbox_password2_xpath).send_keys(password)

    def clickLogin(self):
        self.Find_Element(*self.locator.button_login_xpath).click()
