from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import time

# Chrome
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  # -- Run in Chrome

#Firefox
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())  # -- Run in Firefox

#Internet Explorer
driver = webdriver.Ie(executable_path=IEDriverManager().install())  # -- Run in InternetExplorer

driver.get("http://www.google.com/")

driver.maximize_window()

print(driver.title)

time.sleep(2)

driver.close()

print("Success..")