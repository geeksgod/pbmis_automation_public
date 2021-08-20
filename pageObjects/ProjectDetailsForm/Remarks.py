import time
import Utils.ComplexElement as utils
class Remarks:
    #Project justification
    remarks_xpath = '//li//p[text()="Remarks"]'
    active_remarks_xpath = '//li//p[text()="Remarks" and @class="form-section-link active"]'

    #Details
    text_box_remark_xpath = '//div[@role="textbox"]'
    input_file_xpath = '//input[@type="file"]'

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'
    
    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.remarks_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_remarks_xpath)
        except:
            self.goto()
            time.sleep(1)
    
    def set_details(self,remark,path=""):
        self.check()
        utils.write_using_xpath(self.driver,self.text_box_remark_xpath,remark)
        if len(path) > 0:
            utils.upload_file(self.driver,self.input_file_xpath,path)        

    
    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)
