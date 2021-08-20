import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Utils.ComplexElement as utils
class GeneralInfo:

    dropdown_project_type_xpath = "//div[@role='option']//span[contains(text(),'Service Oriented')]"
    radio_categorization_below_three_xpath = '//input[@name="categorization" and @value="belowThree"]'
    radio_categorization_three_five_xpath = '//input[@name="categorization" and @value="threeToFive"]'
    radio_categorization_five_seven_xpath = '//input[@name="categorization" and @value="fiveToSeven"]'
    radio_categorization_seven_ten_xpath = '//input[@name="categorization" and @value="sevenToTen"]'
    radio_categorization_more_ten_xpath = '//input[@name="categorization" and @value="moreThanTen"]'
    button_save_xpath = "//form//button[@type='submit'][1]"
    button_cancel_xpath = "//button[@type='submit'][2]"

    general_info_xpath = '//li//p[text()="General Information"]'
    active_general_info_xpath = '//li//p[text()="General Information" and @class="form-section-link active"]'

    def __init__(self,setup) -> None:
        self.driver = setup
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.general_info_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_general_info_xpath)
        except:
            self.goto()
            time.sleep(1)
    
    def select_project_type(self,option='Service Oriented'):
        self.check()
        drop = self.driver.find_element_by_css_selector("div[name='projectType']")
        self.driver.execute_script("arguments[0].click()",drop)
        sub_drop = self.driver.find_element_by_xpath("//div[@role='option']//span[text()='"+option+"']")
        self.driver.execute_script("arguments[0].click()",sub_drop)

    def select_project_priority(self,option='National Pride Project'):
        self.check()
        drop = self.driver.find_element_by_css_selector("div[name='projectPriority']")
        self.driver.execute_script("arguments[0].click()",drop)
        sub_drop = self.driver.find_element_by_xpath("//div[@role='option']//span[text()='"+option+"']")
        self.driver.execute_script("arguments[0].click()",sub_drop)
    
    def select_categorization(self,year):
        self.check()
        if (year == "below 3 years"):
            button = self.driver.find_element_by_xpath(self.radio_categorization_below_three_xpath)
            self.driver.execute_script('arguments[0].click()',button)
        elif(year == "3-5 years"):
            button = self.driver.find_element_by_xpath(self.radio_categorization_three_five_xpath)
            self.driver.execute_script('arguments[0].click()',button)
        elif(year == "5-7 years"):
            button = self.driver.find_element_by_xpath(self.radio_categorization_five_seven_xpath)
            self.driver.execute_script('arguments[0].click()',button)
        elif(year == "7-10 years"):
            button = self.driver.find_element_by_xpath(self.radio_categorization_seven_ten_xpath)
            self.driver.execute_script('arguments[0].click()',button)
        else:
            button = self.driver.find_element_by_xpath(self.radio_categorization_more_ten_xpath)
            self.driver.execute_script('arguments[0].click()',button)

    def select_sector(self,option):
        self.check()
        tick_box = self.driver.find_element_by_xpath("//input[@id='"+option+"']") 
        self.driver.execute_script('arguments[0].click()',tick_box)
        
    def select_district(self,district):
        self.check()
        input = self.driver.find_element_by_xpath("//div[@name='districts']/input")
        input.send_keys(district)
        input.send_keys(Keys.ENTER)
        # sub = self.driver.find_element_by_xpath("//div/span[text()='Bhojpur']/..")
        # self.driver.execute_script('arguments[0].click()',sub)
        
    def click_save(self):
        self.check()
        wait =  WebDriverWait(self.driver,10)
        button = wait.until(EC.presence_of_element_located((By.XPATH,self.button_save_xpath)))
        self.driver.execute_script('arguments[0].click()',button)

    def click_no_save(self):
        self.check()
        button = self.driver.find_element_by_xpath(self.button_cancel_xpath)
        self.driver.execute_script('arguments[0].click()',button)  
        

        