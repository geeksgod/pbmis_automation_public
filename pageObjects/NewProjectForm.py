from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewProjectForm:
    
    dropdown_ministry_name_xpath = "//div[contains(text(),'Select a Ministry')]"
    input_ministry_name_xpath = "//div[contains(text(),'Select a Ministry')]/..//div//input"
    radio_is_part_of_program_xpath = '//input[@name="part_of_program" and @value="Yes"]'
    radio_not_part_of_program_xpath = '//input[@name="part_of_program" and @value="No"]'
    radio_is_sub_project_xpath = '//input[@name="is_sub_project" and @value="Yes"]'
    radio_not_sub_project_xpath = '//input[@name="is_sub_project" and @value="No"]'
    input_project_name_eng_xpath = '//div[@class="form-group-container"]//input[@required]'
    input_project_name_nep_xpath = '((//div[@class="form-group-container"]//input[@required])[1]/../../following::div)[1]//input'
    radio_projecct_status_ongoing_xpath = '//input[@name="project_status" and @value="ongoing"]'
    radio_project_status_new_xpath = '//input[@name="project_status" and @value="new"]'
    radio_project_status_new_identification_xpath = '//input[@name="stage" and @value="identification"]'
    radio_project_status_new_appraisal_xpath = '//input[@name="stage" and @value="appraisal"]'
    radio_project_theme_infrastructure_xpath = '//input[@name="area" and @value="infrastructure"]'
    radio_project_theme_service_xpath = '//input[@name="area" and @value="service"]'
    btn_save_xpath = "//button[@type='submit']"
    btn_cancel_xpath = "//button[@type='button']"

    def __init__(self,driver):
        self.driver = driver

    def set_ministry_name(self,ministry_id):
        self.driver.find_element_by_xpath(self.dropdown_ministry_name_xpath).click()
        wait = WebDriverWait(self.driver,10)
        option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#react-select-2-option-'+ministry_id)))
        option.click()

    def is_part_of_program(self,is_part):
        if is_part == True:
            button = self.driver.find_element_by_xpath(self.radio_is_part_of_program_xpath)
            self.driver.execute_script('arguments[0].click()',button)
        else:
            button = self.driver.find_element_by_xpath(self.radio_not_part_of_program_xpath)
            self.driver.execute_script('arguments[0].click()',button)
    
    def is_subproject(self,is_sub):
        if is_sub == True:
            button = self.driver.find_element_by_xpath(self.radio_is_sub_project_xpath)
            self.driver.execute_script('arguments[0].click()',button)
        else:
            button = self.driver.find_element_by_xpath(self.radio_not_sub_project_xpath)
            self.driver.execute_script('arguments[0].click()',button)

    def set_project_details(self,eng_name,budget_code,nep_name = None):
        elements = self.driver.find_elements_by_xpath(self.input_project_name_eng_xpath)
        elements[0].send_keys(eng_name)
        elements[1].send_keys(budget_code)

        if nep_name:
            self.driver.find_element_by_xpath(self.input_project_name_nep_xpath).clear()
            self.driver.find_element_by_xpath(self.input_project_name_nep_xpath).send_keys(nep_name)

    def is_project_new(self,value,stage=None):
        """if project status is new please provide the stage too"""
        if value == True:
            button = self.driver.find_element_by_xpath(self.radio_project_status_new_xpath)
            self.driver.execute_script('arguments[0].click()',button)
            if stage == "identification":
                wait = WebDriverWait(self.driver,10)
                option = wait.until(EC.presence_of_element_located((By.XPATH,self.radio_project_status_new_identification_xpath)))
                self.driver.execute_script('arguments[0].click()',option)
            else:
                wait = WebDriverWait(self.driver,10)
                option = wait.until(EC.presence_of_element_located((By.XPATH,self.radio_project_status_new_appraisal_xpath)))
                self.driver.execute_script('arguments[0].click()',option)

        else:
            button = self.driver.find_element_by_xpath(self.radio_projecct_status_ongoing_xpath)
            self.driver.execute_script('arguments[0].click()',button)
    
    def select_project_theme(self,value):
        """ Provide 'I' for infrastructure and 'S' for service/social"""

        if value.lower() == 'i':
            button = self.driver.find_element_by_xpath(self.radio_project_theme_infrastructure_xpath)
            self.driver.execute_script('arguments[0].click()',button)
        else:
            button = self.driver.find_element_by_xpath(self.radio_project_theme_service_xpath)
            self.driver.execute_script('arguments[0].click()',button)
    
    def click_save(self):
        button = self.driver.find_element_by_xpath(self.btn_save_xpath)
        self.driver.execute_script('arguments[0].click()',button)
    
    def click_cancel(self):
        button = self.driver.find_element_by_xpath(self.btn_cancel_xpath)
        self.driver.execute_script('arguments[0].click()',button)

       