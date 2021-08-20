import time
import Utils.ComplexElement as utils

class ProjectPriotization:

    #project Priotization
    project_priotization_xpath = '//li//p[text()="Project Prioritization Score"]'
    active_project_priotization_xpath = '//li//p[text()="General Information" and @class="form-section-link active"]'

    #Economic Growth
    radio_econmic_growth_xpath = '//input[@name="economicGrowth" and @value="'

    #Achievement of SDG
    radio_sdg_xpath = '//input[@name="achievementOfSDG" and @value="'

    #Achievement of participation
    radio_participation_xpath = '//input[@name="participationLevel" and @value="'

    #Contribution to sectoral inclusiveness
    radio_sectoral_inclusive_xpath = '//input[@name="sectoralInclusiveness" and @value="'

    #Contribution to sectoral inclusiveness and gender ..
    radio_social_inclusive_xpath = '//input[@name="socialInclusiveness" and @value="'

    #sectoral goals
    radio_sector_goals_xpath = '//input[@name="sectoralGoal" and @value="'

    #sectoral sdg
    radio_sector_sdg_xpath = '//input[@name="achievementOfSectoralSDG" and @value="'

    #project priotization sheet
    file_project_priotization = '//input[@id="file-input-projectPrioritizationFile"]'

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'

    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.project_priotization_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_project_priotization_xpath)
        except:
            self.goto()
            time.sleep(1)

    def set_economic_growth(self,value):
        """Range = 0-3"""
        self.check()
        utils.js_click(self.driver,self.radio_econmic_growth_xpath+value+'"]')
    
    def set_sdg(self,value):
        """Range = 0-3"""
        self.check()
        utils.js_click(self.driver,self.radio_sdg_xpath+value+'"]')
    
    def set_participation(self,value):
        """Range = 0-3"""
        self.check()
        utils.js_click(self.driver,self.radio_participation_xpath+value+'"]')

    def set_sector_inclusive(self,value):
        """Range = 0-3"""
        self.check()
        utils.js_click(self.driver,self.radio_sectoral_inclusive_xpath+value+'"]')
    
    def set_social_inclusive(self,value):
        """Range = 0-3"""
        self.check()
        utils.js_click(self.driver,self.radio_social_inclusive_xpath+value+'"]')
    
    
    def set_sector_goals(self,value):
        """Range = 0-3"""
        self.check()
        utils.js_click(self.driver,self.radio_sector_goals_xpath+value+'"]')
    
    def set_sector_sdg(self,value):
        """Range = 0-3"""
        self.check()
        utils.js_click(self.driver,self.radio_sector_sdg_xpath+value+'"]')
    
    def upload_project_priotization_sheet(self,path):
        self.check()
        utils.upload_file(self.driver,self.file_project_priotization,path)
    
    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)