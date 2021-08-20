import time
import Utils.ComplexElement as utils

class ProjectLandAcquisition:

    #Project Land Acquisition
    project_land_acquisition_xpath = '//li//p[text()="Land Acquisition Status"]'
    active_project_land_acquisition_xpath = '//li//p[text()="Land Acquisition Status" and @class="form-section-link active"]'

    #General
    dropdown_land_type_xpath = '//div[@name ="landType"]'
    option_land__type_xpath = '//div[@role="option"]'
    input_required_land_xpath = '//input[@name="requiredLand"]'
    input_total_acquired_land_xpath = '//input[@name="totalAcquiredLand"]'
    input__remaining_acquired_land_xpath = '//input[@name="remainingAcquiredLand"]'
    input_date_remaining_land_xpath = '//div[@class="react-datepicker__input-container"]/input'
    textbox_land_acquistion_xpath = '//div[@role="textbox"]'
    file_land_acquisition_xpath = '//input[@id="file-input-remainingLandAcquisitionFile"]'

    #Resettlement Plan for the Project Affected Families (PAFs), if any
    input_affected_xpath = '//input[@name="noOfAffectedAreas"]'
    input_relocated_xpath = '//input[@name="noOfRelocated"]'
    input_resettled_xpath = '//input[@name="noOfRemainingRelocated"]'
    file_resettle_xpath = '//input[@id="file-input-resettlementPlanFile"]'

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'

    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.project_land_acquisition_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_project_land_acquisition_xpath)
        except:
            self.goto()
            time.sleep(1)
    
    def set_acquisition_details(self,land_type,required,total_acquired,remaining_acquired,date,desc,file_path):
        self.check()
        utils.handle_dropdown(self.driver,self.dropdown_land_type_xpath,self.option_land__type_xpath,land_type)
        utils.write_using_xpath(self.driver,self.input_required_land_xpath,required)
        utils.write_using_xpath(self.driver,self.input_total_acquired_land_xpath,total_acquired)
        utils.write_using_xpath(self.driver,self.input__remaining_acquired_land_xpath,remaining_acquired)
        utils.write_using_xpath(self.driver,self.input_date_remaining_land_xpath,date)
        #self.driver.find_element_by_xpath(self.input_date_remaining_land_xpath).send_keys(date)
        utils.write_using_xpath(self.driver,self.textbox_land_acquistion_xpath,desc)
        utils.upload_file(self.driver,self.file_land_acquisition_xpath,file_path)
    
    def set_resettlement_details(self,affected,relocated,resettled,file_path):
        self.check()
        utils.write_using_xpath(self.driver,self.input_affected_xpath,affected)
        utils.write_using_xpath(self.driver,self.input_relocated_xpath,relocated)
        utils.write_using_xpath(self.driver,self.input_resettled_xpath,resettled)
        utils.upload_file(self.driver,self.file_resettle_xpath,file_path)
    
    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)



    
