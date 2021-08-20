from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

class ProjectDetails:

    btn_edit_xpath = '//button[text()="Edit"]'

    def __init__(self, driver):
        self.driver =  driver
    
    def click_edit(self):
        wait = WebDriverWait(self.driver,10)
        edit_btn =  wait.until(EC.presence_of_element_located((By.XPATH,self.btn_edit_xpath)))
        self.driver.execute_script("arguments[0].click()",edit_btn)