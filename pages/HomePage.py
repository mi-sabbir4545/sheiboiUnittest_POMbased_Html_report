

class HomePage(object):
    def __init__(self, driver, base_url=""):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def Find_Element(self, *locator):
        return self.driver.find_element(*locator)

    # def find_all_element(self, *locator):
    #     return self.driver.find_elements(*locator)

    def scroll_to_element(self):
        self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
        # value = driver.execute_script("return window.pageYOffset;")
