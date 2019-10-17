from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("../Driver/chromedriver.exe")

time.sleep(2)

driver.get("https://www.google.com")

driver.maximize_window()

driver.find_element_by_name("q").send_keys("Selenium Python")

time.sleep(3)

ActionChains(driver).send_keys(Keys.ENTER).perform()

time.sleep(3)

driver.close()

print("Success...")