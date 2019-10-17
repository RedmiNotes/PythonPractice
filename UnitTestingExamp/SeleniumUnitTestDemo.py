import unittest
import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class MyTestCase(unittest.TestCase):

     @classmethod
     def setUpClass(cls):
         cls.driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
         cls.driver.implicitly_wait(10)
         cls.driver.maximize_window()

     def test_search_1(self):
         self.driver.get("https://www.google.com")
         self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
         time.sleep(2)
         ActionChains(self.driver).send_keys(Keys.ENTER).perform()
         a = self.driver.title
         print("The title is :",a)

     def test_search_2(self):
         self.driver.get("https://www.google.com")
         self.driver.find_element_by_name("q").send_keys("Selenium")
         time.sleep(2)
         ActionChains(self.driver).send_keys(Keys.ENTER).perform()
         a = self.driver.title
         print("The title is :",a)

     @classmethod
     def tearDownClass(cls):
         cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
