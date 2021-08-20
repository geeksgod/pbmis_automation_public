import time
import Utils.ComplexElement as utils

class ProjectModality:

    #project Modality
    project_modality_xpath = '//li//p[text()="Project Implementation Modality"]'
    active_project_modality_xpath = '//li//p[text()="Project Implementation Modality" and @class="form-section-link active"]'

    #Modality
    dropdown_project_modality_xpath = '//div[@name="projectImplementationModalType"]'
    options_project_modality_xpath = '//div[@name="projectImplementationModalType"]//div[@role="option"]'

    #PPP type
    dropdown_ppp_xpath = '//div[@name="PPPType"]'
    options_ppp_xpath = '//div[@name="PPPType"]//div[@role="option"]'
    input_company_name_xpath = '//input[@name="companyName"]'
    input_other_ppp_xpath = '//input[@name="otherPPPType"]'

    #private type
    dropdown_private_xpath = '//div[@name="privateType"]'
    options_private_xpath = '//div[@name="privateType"]//div[@role="option"]'

    #other type
    input_other_xpath = '//input[@name="otherImplementationModal"]'

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'
    
    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.project_modality_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_project_modality_xpath)
        except:
            self.goto()
            time.sleep(1)

    def set_modality(self,value,other = None):
        self.check()
        utils.handle_dropdown(self.driver,self.dropdown_project_modality_xpath,self.options_project_modality_xpath,value)
        if other:
            utils.write_using_xpath(self.driver,self.input_other_xpath,other)
    
    def set_ppp_type_details(self,option,company_name,other=""):
        self.check()
        if option.lower() == "other":
            utils.handle_dropdown(self.driver,self.dropdown_ppp_xpath,self.options_ppp_xpath,option)
            utils.write_using_xpath(self.driver,self.input_other_ppp_xpath,other)
            utils.write_using_xpath(self.driver,self.input_company_name_xpath,company_name)
        else:
            utils.handle_dropdown(self.driver,self.dropdown_ppp_xpath,self.options_ppp_xpath,option)
            utils.write_using_xpath(self.driver,self.input_company_name_xpath,company_name)
           
    
    def set_private_type_details(self,option,company_name):
            self.check()
            utils.handle_dropdown(self.driver,self.dropdown_private_xpath,self.options_private_xpath,option)
            utils.write_using_xpath(self.driver,self.input_company_name_xpath,company_name)
    
    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)