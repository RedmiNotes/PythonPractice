from MiniProject_2.Locators.Locator_Demo import locate
class Lpage():

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def uname(self,username):
        self.driver.find_element_by_id(locate.username_textbox_id).send_keys(username)

    def upass(self,password):
        self.driver.find_element_by_id(locate.password_textbox_id).send_keys(password)

    def logbutton(self):
        self.driver.find_element_by_id(locate.login_button_id).click()