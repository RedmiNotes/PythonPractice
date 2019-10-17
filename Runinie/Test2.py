from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

caps = webdriver.DesiredCapabilities.INTERNETEXPLORER

caps['ignoreProductedModeSettings'] = True

path = "../Driver/IEDriverServer.exe"

driver = webdriver.Ie(executable_path=path,desired_capabilities=caps)

driver.get("https://www.google.com")

driver.maximize_window()

time.sleep(2)

driver.find_element_by_name("q").send_keys("Selenium Python")

time.sleep(3)

ActionChains(driver).send_keys(Keys.ENTER).perform()

time.sleep(2)

driver.close()

print("Success..")