import time
from pages.BasePage import BasePage
from pages.BottomNavBar import BottomNavBar


class BottomNavBarTest(BasePage):

    def test_clickfacebook(self):
        tf = BottomNavBar(self.driver)
        time.sleep(3)
        tf.click_facebook()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        tf.scroll_to_up()


    def test_clicktwitter(self):
        tt = BottomNavBar(self.driver)
        time.sleep(3)
        tt.click_twitter()
        time.sleep(3)
        self.driver.back()
        time.sleep(2)

    def test_clickyoutube(self):
        ty = BottomNavBar(self.driver)
        time.sleep(3)
        ty.click_youtube()
        time.sleep(3)
        self.driver.back()
        time.sleep(2)

    def test_clickplaystore(self):
        tp = BottomNavBar(self.driver)
        time.sleep(3)
        tp.click_playstore()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

    def test_clickappstore(self):
        tap = BottomNavBar(self.driver)
        time.sleep(3)
        tap.click_appstore()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

    def test_help(self):
        th = BottomNavBar(self.driver)
        time.sleep(3)
        th.click_help()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)