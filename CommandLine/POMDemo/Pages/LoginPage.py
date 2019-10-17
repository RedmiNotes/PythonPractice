from POMDemo.Locators.Locator import Locate

class Loginpages():

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = Locate.username_textbox_id
        self.password_textbox_id = Locate.password_textbox_id
        self.login_button_id = Locate.login_button_id

    def enter_username(self,username):
        self.driver.find_element_by_id(Locate.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locate.password_textbox_id).send_keys(password)

    def login_button(self):
        self.driver.find_element_by_id(Locate.login_button_id).click()