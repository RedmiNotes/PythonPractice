from POMDemo.Locators.Locator import Locate
class HomePages():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_button_id = Locate.welcome_button_id
        self.logout_button_text = Locate.logout_button_text


    def welcome_page(self):
        self.driver.find_element_by_id(Locate.welcome_button_id).click()

    def logout_page(self):
        self.driver.find_element_by_link_text(Locate.logout_button_text).click()
