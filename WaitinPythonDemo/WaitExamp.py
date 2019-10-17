from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")

driver.get("https://www.google.com")

#implicit Wait
#driver.implicitly_wait(10)

driver.maximize_window()

driver.find_element_by_name("q").send_keys("Selenium Automation")

time.sleep(2)

ActionChains(driver).send_keys(Keys.ESCAPE).perform()

wait = WebDriverWait(driver,10)

element = wait.until(Ec.element_to_be_clickable(By.XPATH("//div[@class='FPdoLc VlcLAe']//input[@name='btnK']")))

element.click()

print("Test Completed")

driver.close()

driver.quit()