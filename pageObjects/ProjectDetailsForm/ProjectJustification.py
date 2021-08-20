import time
import Utils.ComplexElement as utils

class ProjectJustification:

    #Project justification
    project_justification_xpath = '//li//p[text()="Justification for Merging, Extending or Phasing out of the Project"]'
    active_project_justification_xpath = '//li//p[text()="Justification for Merging, Extending or Phasing out of the Project" and @class="form-section-link active"]'

    drop_down_justification_type_xpath = '//div[@role="combobox"]'
    options_justification_type_xpath = '//div[@role="option"]'
    file_justification_xpath = '//input[@type="file"]'

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'


    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.project_justification_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_project_justification_xpath)
        except:
            self.goto()
            time.sleep(1)
    
    def set_justification_type(self,type):
        self.check()
        utils.handle_dropdown(self.driver,self.drop_down_justification_type_xpath,self.options_justification_type_xpath,type)
    
    def send_file(self,path):
        self.check()
        utils.upload_file(self.driver,self.file_justification_xpath,path)

    def click_save(self):
        self.check()
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)
