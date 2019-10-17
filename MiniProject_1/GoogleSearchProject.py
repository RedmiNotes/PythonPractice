from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import unittest

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_one(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation")
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        print(self.driver.title)

    def test_two(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Selenium")
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
          cls.driver.close()
          cls.driver.quit()
          print("Test Completed....")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\computer003\\Desktop\\Python Practice\\MiniProject_1\\Html Report"),verbosity=2)