from MiniProject_2.Locators.Locator_Demo import locate
class Home():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_button_id = "welcome"
        self.logout_text = "Logout"


    def welcome_but(self):
        self.driver.find_element_by_id(locate.welcome_button_id).click()

    def logout_but(self):
        self.driver.find_element_by_link_text(locate.logout_text).click()