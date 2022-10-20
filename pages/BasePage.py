import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from TestData.data import Data
import sys
# from Suite.test_suite import htmlReport

sys.path.append("D:/Project/sheiboiUnittest_POMbased_Html_report")


class BasePage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # options = webdriver.ChromeOptions()
        # options.add_argument("start-maximized")
        serv_obj = Service(executable_path="D:\\Project\\sheiboiUnittest_POMbased_Html_report\\driver"
                                           "\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj)
        # cls.driver = webdriver.Chrome(options=options,executable_path="D:\\Project\\sheiboiUnittest_POMbased_Html_report\\driver"
        #                                               "\\chromedriver.exe")
        cls.driver.get(Data.BASE_URL)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main() #Suite.test_suite

# testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Project/sheiboiUnittest_POMbased_Html_report/reports')
