import time
from pages.BasePage import BasePage
from pages.TopNavBar import TopNavBar
from TestData.data import Data


class TopNavBarTest(BasePage):

    def test_home(self):
        hm = TopNavBar(self.driver)
        time.sleep(3)
        hm.click_home()
        time.sleep(3)

    def test_subject(self):
        sb = TopNavBar(self.driver)
        sb.click_subject()
        time.sleep(3)

    def test_thewriter(self):
        tw = TopNavBar(self.driver)
        tw.click_the_writer()
        time.sleep(3)

    def test_allbooks(self):
        ta = TopNavBar(self.driver)
        time.sleep(3)
        ta.click_the_books()
        time.sleep(3)

    def test_search(self):
        ts = TopNavBar(self.driver)
        ts.send_search(Data.BOOKNAME)
        time.sleep(2)
        ts.click_search()
        time.sleep(3)

    def test_addCart(self):
        ta = TopNavBar(self.driver)
        self.test_search()
        time.sleep(3)
        ta.click_book()
        time.sleep(3)
        ta.click_addcart()
        time.sleep(3)

    def test_deletecart(self):
        ta = TopNavBar(self.driver)
        self.test_addCart()
        time.sleep(3)
        ta.click_Cart()
        time.sleep(3)
        ta.click_deleteCart()
        time.sleep(3)
