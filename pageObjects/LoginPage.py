class LoginPage:
    input_username_xpath = "//label[contains(text(),'Username')]/following-sibling::input"
    input_password_xpath = "//input[@type]"
    btn_login_xpath = "//button"

    def __init__(self,driver):
        self.driver = driver
    
    def set_username(self,username):
        self.driver.find_element_by_xpath(self.input_username_xpath).clear()
        self.driver.find_element_by_xpath(self.input_username_xpath).send_keys(username)
    
    def set_password(self,password):
        self.driver.find_element_by_xpath(self.input_password_xpath).clear()
        self.driver.find_element_by_xpath(self.input_password_xpath).send_keys(password)
    
    def click_login(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()