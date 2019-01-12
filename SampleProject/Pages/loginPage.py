
class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.login_xpath = "//a[@data-js ='login']"
        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.login_btn_name = "button"

    def click_login_btn(self):
        self.driver.find_element_by_xpath(self.login_xpath).click()


    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)


    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)


    def click_login(self):
        self.driver.find_element_by_name(self.login_btn_name).click()
