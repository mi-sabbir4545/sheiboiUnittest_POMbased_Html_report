import time
from pages.LoginPage import LoginPage
from TestData.data import Data
from pages.BasePage import BasePage
from pages.logout import LOGOUT


class LoginLogoutTest(BasePage):

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.clickLoginIcon()
        lp.clickLoginButton()
        lp.enter_username(Data.USERNAME)
        lp.enter_password1()
        lp.enter_password2(Data.PASSWORD)
        lp.clickLogin()

        time.sleep(3)

        lg = LOGOUT(self.driver)
        lg.clickWelcome()
        lg.clickLogout()

        time.sleep(3)

        # lp.clickLogout()
        # time.sleep(3)
        # self.assertEqual("সেইবই - বাংলা বইয়ের একটি অনলাইন ইবুক লাইব্রেরী।", self.driver.title,
        #                  "webpage title is not matching")


# testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\reports')



