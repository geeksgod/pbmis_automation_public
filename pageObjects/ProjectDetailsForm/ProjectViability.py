import time
import Utils.ComplexElement as utils

class ProjectViability:

    #Project Viability
    project_viability_xpath = '//li//p[text()="Project Viability"]'
    active_project_viability_xpath = '//li//p[text()="Project Viability" and @class="form-section-link active"]'

    #Economic indicator 
    input_eirr_xpath = '//p[text()="Economic Indicators"]/..//input[@name="rateOfReturn"]'
    input_npv_xpath = '//p[text()="Economic Indicators"]/..//input[@name="NPV"]'
    input_bcr_xpath = '//p[text()="Economic Indicators"]/..//input[@name="BCRatio"]'
    input_other_xpath = '//p[text()="Economic Indicators"]/..//input[@name="other"]'

    #Financial indicator
    input_firr_xpath = '//p[text()="Financial Indicators"]/..//input[@name="rateOfReturn"]'
    input_fnpv_xpath = '//p[text()="Financial Indicators"]/..//input[@name="NPV"]'
    input_fbcr_xpath = '//p[text()="Financial Indicators"]/..//input[@name="BCRatio"]'
    input_irr_xpath = '//p[text()="Financial Indicators"]/..//input[@name="IRREquity"]'
    input_fpayback_xpath = '//p[text()="Financial Indicators"]/..//input[@name="payback"]'
    input_fother_xpath = '//p[text()="Financial Indicators"]/..//input[@name="other"]'

    #Social indicatiors
    input_sce_xpath = '//p[text()="Social Sector Indicators"]/..//input[@name="costEffectiveness"]'
    input_seg_xpath = '//p[text()="Social Sector Indicators"]/..//input[@name="employmentGeneration"]'
    input_sbcr_xpath = '//p[text()="Social Sector Indicators"]/..//input[@name="BCRatio"]'
    file_sio_xpath = '//input[@id="file-input-socialIndicatorOutputFile"]'

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'

    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.project_viability_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_project_viability_xpath)
        except:
            self.goto()
            time.sleep(1)
    
    def set_economic_indicators(self,rate_of_return,npv,bcr,other):
        self.check()
        utils.write_using_xpath(self.driver,self.input_eirr_xpath,rate_of_return)
        utils.write_using_xpath(self.driver,self.input_npv_xpath,npv)
        utils.write_using_xpath(self.driver,self.input_other_xpath,other)
        utils.write_using_xpath(self.driver,self.input_bcr_xpath,bcr)
    
    def set_financial_indicators(self,rate_of_return,npv,bcr,irr,payback,other):
        self.check()
        utils.write_using_xpath(self.driver,self.input_firr_xpath,rate_of_return)
        utils.write_using_xpath(self.driver,self.input_fnpv_xpath,npv)
        utils.write_using_xpath(self.driver,self.input_fbcr_xpath,bcr)
        utils.write_using_xpath(self.driver,self.input_irr_xpath,irr)
        utils.write_using_xpath(self.driver,self.input_fpayback_xpath,payback)
        utils.write_using_xpath(self.driver,self.input_fother_xpath,other)
    
    def set_social_indicators(self,sce,seg,sbcr,sio):
        self.check()
        utils.write_using_xpath(self.driver,self.input_sce_xpath,sce)
        utils.write_using_xpath(self.driver,self.input_seg_xpath,seg)
        utils.write_using_xpath(self.driver,self.input_sbcr_xpath,sbcr)
        utils.upload_file(self.driver,self.file_sio_xpath,sio)

    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)