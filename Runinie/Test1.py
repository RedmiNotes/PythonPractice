from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Ie("../Driver/IEDriverServer.exe")

driver.get("https://www.google.com")

driver.maximize_window()

time.sleep(2)

driver.find_element_by_name("q").send_keys("Selenium Python")

time.sleep(3)

ActionChains(driver).send_keys(Keys.ENTER).perform()

time.sleep(2)

driver.close()

print("Success..")