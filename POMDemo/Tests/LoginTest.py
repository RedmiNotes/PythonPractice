from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POMDemo.Locators.Locator import Locate
from POMDemo.Pages.LoginPage import Loginpages
from POMDemo.Pages.HomePage import HomePages

class LoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome(executable_path="C:\\Users\\computer003\\Desktop\\Python Practice\\Driver\\chromedriver.exe")
       cls.driver.implicitly_wait(10)

    def test_login(self):
       self.driver.get("https://opensource-demo.orangehrmlive.com")
       self.driver.maximize_window()

       login = Loginpages(self.driver)
       login.enter_username('Admin')
       time.sleep(1)
       login.enter_password('admin123')
       time.sleep(1)
       login.login_button()
       time.sleep(1)

       logout = HomePages(self.driver)
       logout.welcome_button_id
       time.sleep(1)
       logout.logout_button_text
       time.sleep(2)
       # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
       # time.sleep(2)
       # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
       # time.sleep(2)
       # self.driver.find_element_by_id("btnLogin").click()
       # time.sleep(3)
       # self.driver.find_element_by_id("welcome").click()
       # time.sleep(2)
       # self.driver.find_element_by_link_text("Logout").click()
       # time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed...")


if __name__ == "__main__":
    unittest.main()