import unittest
# import HtmlTestRunner

# from unittest import runner
# from pages.BasePage import BasePage

from testcases.test_Login_LogoutTest import LoginLogoutTest
from testcases.test_TopNavBarTest import TopNavBarTest
from testcases.test_BottomNavBarTest import BottomNavBarTest

login_logout = unittest.TestLoader().loadTestsFromTestCase(LoginLogoutTest)
top_nab_bar = unittest.TestLoader().loadTestsFromTestCase(TopNavBarTest)
bottom_nab_bar = unittest.TestLoader().loadTestsFromTestCase(TopNavBarTest)
# htmlReport = unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Project/sheiboiUnittest_POMbased_Html_report/reports'))
# suite = unittest.TestLoader().loadTestsFromTestCase(BasePage)
suite = unittest.TestSuite([login_logout, top_nab_bar, bottom_nab_bar]) #htmlReport
unittest.TextTestRunner(verbosity=2).run(suite)


# test_suite = unittest.TestSuite([login_logout, htmlReport])
# outfile = open("D:/Project/sheiboiUnittest_POMbased_Html_report/reports", "w")
# runner = HTMLTestRunner.HTMLTestRunner("D:/Project/sheiboiUnittest_POMbased_Html_report/reports", "w")
# unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Project/sheiboiUnittest_POMbased_Html_report/reports'))


runner.run(suite)
