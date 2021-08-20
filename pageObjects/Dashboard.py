from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Utils.ComplexElement as utils
class Dashboard:

    btn_add_new_project_xpath = '//div//a[@class="link item add-project no-print"]'
    list_project_xpath = "//*[text()='"


    def __init__(self,driver):
        self.driver = driver
    
    def click_add_new_project(self):
        wait = WebDriverWait(self.driver,10)
        element =  wait.until(EC.presence_of_element_located((By.XPATH,self.btn_add_new_project_xpath)))
        utils.js_session_click(self.driver,element)
        # self.driver.find_element_by_xpath(self.btn_add_new_project_xpath).click()
    
    def click_project(self, project_name):
        wait = WebDriverWait(self.driver,10)
        element =  wait.until(EC.element_to_be_clickable((By.XPATH,self.list_project_xpath + project_name + "']/../..")))
        self.driver.execute_script("arguments[0].click()",element)
    
