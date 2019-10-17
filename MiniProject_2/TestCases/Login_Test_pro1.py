from selenium import webdriver
import unittest
import time
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import HtmlTestRunner
from MiniProject_2.TestPage.Login_page_1 import Lpage
from MiniProject_2.TestPage.Home_page_1 import Home
from MiniProject_2.Locators.Locator_Demo import locate

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/computer003/Desktop/Python Practice/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_validate(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")

        log = Lpage(driver)
        log.uname("Admin")
        log.upass("admin123")
        log.logbutton()

        out = Home(driver)
        out.welcome_but()
        out.logout_but()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Success..!!!!")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\computer003\\Desktop\\Python Practice\\MiniProject_2\\Report"))