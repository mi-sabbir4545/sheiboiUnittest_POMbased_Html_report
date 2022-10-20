from Locators.locators import TopNavBarLocator
from pages.HomePage import HomePage


class TopNavBar(HomePage):

    def __init__(self, driver):
        self.driver = driver
        self.locator = TopNavBarLocator
        super(TopNavBar, self).__init__(driver)

    # def enter_homeButton(self):
    #     self.driver.find_element(*self.locator.click_homepage).click()

    def click_home(self):
        self.Find_Element(*self.locator.click_homepage).click()

    def click_subject(self):
        self.Find_Element(*self.locator.click_subjectPage).click()

    def click_the_writer(self):
        self.Find_Element(*self.locator.click_writer).click()

    def click_the_books(self):
        self.Find_Element(*self.locator.click_allbooks).click()

    def send_search(self, bookname):
        self.Find_Element(*self.locator.send_searchopt).send_keys(bookname)

    def click_search(self):
        self.Find_Element(*self.locator.click_searchopt).click()

    def click_book(self):
        self.Find_Element(*self.locator.click_book).click()

    def click_addcart(self):
        self.Find_Element(*self.locator.click_addtocart).click()

    def click_Cart(self):
        self.Find_Element(*self.locator.click_cart).click()

    def click_deleteCart(self):
        self.Find_Element(*self.locator.click_deletecart).click()
