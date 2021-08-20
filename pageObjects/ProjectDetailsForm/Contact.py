import time
import Utils.ComplexElement as utils
class Contact:
    #Project justification
    contact_xpath = '//li//p[text()="Contact"]'
    active_contact_xpath = '//li//p[text()="Contact"and @class="form-section-link active"]'

    #Details
    input_name_xpath = '//input[@name="fullName"]'
    input_designation_xpath = '//input[@name="designation"]'
    input_number_xpath = '//input[@name="phoneNumber"]'
    input_email_xpath = '//input[@name="email"]'
    input_name_focal_xpath = '//input[@name="fullNameFocal"]'
    input_designation_focal_xpath = '//input[@name="designationFocal"]'
    input_number_focal_xpath = '//input[@name="phoneNumberFocal"]'
    input_email_focal_xpath = '//input[@name="emailFocal"]'

      #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'
    
    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.contact_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_contact_xpath)
        except:
            self.goto()
            time.sleep(1)
    
    def set_details(self,name,designation,number,email):
        self.check()
        utils.write_using_xpath(self.driver,self.input_name_xpath,name)
        utils.write_using_xpath(self.driver,self.input_designation_xpath,designation)
        utils.write_using_xpath(self.driver,self.input_number_xpath,number)
        utils.write_using_xpath(self.driver,self.input_email_xpath,email)

    def set_focal_details(self,name,designation,number,email):
        self.check()
        utils.write_using_xpath(self.driver,self.input_name_focal_xpath,name)
        utils.write_using_xpath(self.driver,self.input_designation_focal_xpath,designation)
        utils.write_using_xpath(self.driver,self.input_number_focal_xpath,number)
        utils.write_using_xpath(self.driver,self.input_email_focal_xpath,email)
    
    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)
