from selenium import webdriver
import pytest
import time
import sys

class TestSample():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("../Driver/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.find_element_by_id("welcome").click()
        time.sleep(2)
        driver.find_element_by_link_text("Logout").click()
        driver.close()
        driver.quit()
        print("Success...")

    def test_log(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        print(driver.title)
        driver.find_element_by_id("btnLogin").click()