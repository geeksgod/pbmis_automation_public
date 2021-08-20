import time
import Utils.ComplexElement as util
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProjectSpecific:

    radio_is_year_on_year_xpath = '//input[@name="isYearlyFunding" and @value="Yes"]'
    radio_is_not_year_on_year_xpath = '//input[@name="isYearlyFunding" and @value="No"]'
    date_project_start_xpath = '(//div[@class="react-datepicker__input-container"]//input[@type="text"])[1]'
    date_project_end_xpath = '(//div[@class="react-datepicker__input-container"]//input[@type="text"])[2]'

    input_orginal_cost_xpath = '//input[@name="originalCost"]'
    input_orginal_cost_word_xpath = '//input[@name="originalCostWord"]'
    dropdown_fiscal_year_xpath = '//div[@name="fiscalYearForOriginalCost"]/input'
    date_project_estimate_xpath = '//p[text()="Project Cost for Implementation"]/..//div[@class="react-datepicker__input-container"]//input[@type="text"]'

    radio_is_revised_xpath = '//input[@name="isProjectCostRevise" and @value="Yes"]'
    radio_is_not_revised_xpath = '//input[@name="isProjectCostRevise" and @value="No"]'
    input_revised_cost_xpath = '//input[@name="revisedCost"]'
    input_revised_cost_word_xpath = '//input[@name="revisedCostWord"]'
    dropdown_revised_fiscal_year_xpath = '//div[@name="fiscalYearForRevised"]'
    dropdown_options_revised_fiscal_year_xpath = '//div[@name="fiscalYearForRevised"]//div[@role="option"]/span'
    date_revised_estimate_xpath = '//div[@name="fiscalYearForRevised"]/../..//div[@class="react-datepicker__input-container"]//input[@type="text"]'

    radio_is_break_of_cost_xpath = '//input[@name="isBreakOfCost" and @value="Yes"]'
    radio_is_not_break_of_cost_xpath = '//input[@name="isBreakOfCost" and @value="No"]'
    input_cost_heading_number_xpath = '//input[@name="costHeadingNumber"]'
    input_cost_heading_xpath = '//input[@name="costHeading"]'
    input_cost__word_xpath = '//input[@name="fCostComponentWord"]'
    input_cost__xpath = '//input[@name="fCostComponent"]'

    input_file_summary_cost_xpath = '//input[@type="file"]'    
    input_file_desc_xpath = '//p[@class="file-name" and text()="'
    button_file_delete = '//p[@class="file-name" and text()="'

    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'
    
    project_specific_xpath = '//li//p[text()="Project Specific"]'
    active_project_specific_xpath = '//li//p[text()="Project Specific" and @class="form-section-link active"]'

    def __init__(self,setup) -> None:
        self.driver = setup
        util.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = util.explicit_wait_present(self.driver,self.project_specific_xpath)
        util.js_session_click(self.driver,link)
    
    def check(self):
        try:
            util.get_element(self.driver,self.active_project_specific_xpath)
        except:
            self.goto()
            time.sleep(1)

    def is_year_on_year(self,value):
        self.check()
        if value:
            element = self.driver.find_element_by_xpath(self.radio_is_year_on_year_xpath)
            self.driver.execute_script("arguments[0].click()",element)        
        else:
            print("here")
            element = self.driver.find_element_by_xpath(self.radio_is_not_year_on_year_xpath)
            time.sleep(1) 
            self.driver.execute_script("arguments[0].click()",element)
           
    
    def set_start_end_date(self,start_date = "08/04/2021",end_date = "08/07/2021"):
        self.check()
        self.driver.find_element_by_xpath(self.date_project_start_xpath).send_keys(start_date)
        self.driver.find_element_by_xpath(self.date_project_end_xpath).send_keys(end_date)
           
        
    def set_project_cost_details(self,original_cost = "",original_cost_word  = "",fiscal_year = "",estimate_date = ""):
        self.check()
        self.driver.find_element_by_xpath(self.input_orginal_cost_xpath).send_keys(original_cost)
        self.driver.find_element_by_xpath(self.input_orginal_cost_word_xpath).send_keys(original_cost_word)
        self.driver.find_element_by_xpath(self.dropdown_fiscal_year_xpath).send_keys(fiscal_year)
        self.driver.find_element_by_xpath(self.date_project_estimate_xpath).send_keys(estimate_date)
    
    def is_cost_revised(self,value):
       self.check()
       if value:
           element = self.driver.find_element_by_xpath(self.radio_is_revised_xpath)
           self.driver.execute_script("arguments[0].click()",element)        
       else:
           print("here")
           element = self.driver.find_element_by_xpath(self.radio_is_not_revised_xpath)
           self.driver.execute_script("arguments[0].click()",element)

    def set_revised_project_cost_details(self,revised_cost = "",revised_cost_word  = "",fiscal_year = "",estimate_date = ""):
        self.check()
        self.driver.find_element_by_xpath(self.input_revised_cost_xpath).send_keys(revised_cost)
        self.driver.find_element_by_xpath(self.input_revised_cost_word_xpath).send_keys(revised_cost_word)
        util.handle_dropdown(self.driver,self.dropdown_revised_fiscal_year_xpath,self.dropdown_options_revised_fiscal_year_xpath,fiscal_year)
        self.driver.find_element_by_xpath(self.date_revised_estimate_xpath).send_keys(estimate_date)
        

    def is_break_down_available(self,value):
        self.check()
        if value:
           element = self.driver.find_element_by_xpath(self.radio_is_break_of_cost_xpath)
           self.driver.execute_script("arguments[0].click()",element)        
        else:
           print("here")
           element = self.driver.find_element_by_xpath(self.radio_is_not_break_of_cost_xpath)
           self.driver.execute_script("arguments[0].click()",element)
    
    def set_breakdown_details(self,cost_heading = "",cost_heading_word = "",cost = "",cost_word = ""):
        self.check()
        self.driver.find_element_by_xpath(self.input_cost_heading_number_xpath).send_keys(cost_heading)
        self.driver.find_element_by_xpath(self.input_cost_heading_xpath).send_keys(cost_heading_word)
        self.driver.find_element_by_xpath(self.input_cost__xpath).send_keys(cost)
        self.driver.find_element_by_xpath(self.input_cost__word_xpath).send_keys(cost_word)
    
    def upload_file(self,path):
        self.check()
        self.driver.find_element_by_xpath(self.input_file_summary_cost_xpath).send_keys(path)
    
    def delete_file(self,filename):
        self.check()
        button = self.driver.find_element_by_xpath(self.button_file_delete+filename+'"]/../../button')
        self.driver.execute_script("arguments[0].click()",button)
    
    def set_file_desc(self,filename,desc):
        self.check()
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.presence_of_element_located((By.XPATH,self.input_file_desc_xpath+filename+'"]/../..//input')))
        element.send_keys(desc)
    
    def click_save(self):
        util.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        util.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        util.js_click(self.driver,self.button_to_prev_xpath)

                
        






    
