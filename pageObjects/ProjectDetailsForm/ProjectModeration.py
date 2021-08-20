import time
import Utils.ComplexElement as utils

class ProjectModeration:

    #Project moderation
    project_moderation_xpath = '//li//a[text()="Project Moderation Status"]'
    active_project_moderation_xpath = '//li//a[text()="Project Moderation Status" and @class="form-section-link active"]'

    drop_down_moderation_type_xpath = '//div[@name="moderation_status"]'
    options_moderation_type_xpath = '//div[@role="option"]'
    

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'


    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.project_moderation_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_project_moderation_xpath)
        except:
            self.goto()
            time.sleep(1)
    
    def set_moderation_type(self,type):
        self.check()
        utils.handle_dropdown(self.driver,self.drop_down_moderation_type_xpath,self.options_moderation_type_xpath,type)
    
    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)
