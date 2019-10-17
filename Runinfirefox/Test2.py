from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

Option = webdriver.FirefoxOptions()

Option.add_argument("--headless")

path = "../Driver/geckodriver.exe"

driver = webdriver.Firefox(options=Option,executable_path=path)

driver.get("https://www.google.com")

driver.maximize_window()

time.sleep(3)

driver.find_element_by_name("q").send_keys("Selenium Python")

time.sleep(2)

ActionChains(driver).send_keys(Keys.RETURN).perform()

time.sleep(3)

driver.close()

print("Success..")