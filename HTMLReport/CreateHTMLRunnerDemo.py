from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
from selenium import webdriver
import unittest
import pytest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../Driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_one(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Selenium Python")
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        a = self.driver.title
        print(a)

    def test_two(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Selenium Java")
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        b = self.driver.title
        print(b)

    def test_three(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("JAVA")
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        c = self.driver.title
        print(c)

    def test_fail(self):
        """ This test should fail. """

    @unittest.skip("This is skipped test.")
    def test_skip(self):
        """ This test should be skipped. """

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/computer003/Desktop/Python Practice/Customized_HTML_Report'),verbosity=2)