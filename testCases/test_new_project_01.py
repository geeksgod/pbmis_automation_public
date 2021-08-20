import os
import time
import allure
import pytest
import configparser
from allure_commons.types import AttachmentType
from selenium.webdriver.common.action_chains import ActionChains

import Utils.ComplexElement as utils
from Utils.customeLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.Dashboard import Dashboard
from pageObjects.ProjectDetails import ProjectDetails
from pageObjects.NewProjectForm import NewProjectForm
from pageObjects.ProjectDetailsForm.Contact import Contact
from pageObjects.ProjectDetailsForm.Remarks import Remarks
from pageObjects.ProjectDetailsForm.GeneralInfo import GeneralInfo
from pageObjects.ProjectDetailsForm.ProjectReadiness import Readiness
from pageObjects.ProjectDetailsForm.ProjectSpecific import ProjectSpecific
from pageObjects.ProjectDetailsForm.ProjectModality import ProjectModality
from pageObjects.ProjectDetailsForm.ProjectFinancing import ProjectFinancing
from pageObjects.ProjectDetailsForm.PhysicalProgress import PhysicalProgress
from pageObjects.ProjectDetailsForm.ProjectSelection import ProjectSelection
from pageObjects.ProjectDetailsForm.ProjectViability import ProjectViability
from pageObjects.ProjectDetailsForm.ProjectModeration import ProjectModeration
from pageObjects.ProjectDetailsForm.ProjectPriotization import ProjectPriotization
from pageObjects.ProjectDetailsForm.ProjectJustification import ProjectJustification
from pageObjects.ProjectDetailsForm.ProjectLandAcquisition import ProjectLandAcquisition

userconfig =  configparser.RawConfigParser()

class Test001Login:
    
    baseUrl = "https://p1.pbmis.staging.yipl.com.np/login"   

    dir = os.getcwd()
    log = LogGen.log_gen()
    userconfig.read('./Configurations/user.ini')
    username = userconfig.get('UserInfo','username')
    password = userconfig.get('UserInfo','pass')
    project = userconfig.get('ProjectInfo','project')


    def test_login(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(3)
        language = utils.explicit_wait_clickable(self.driver,'//div[@class="language-select"]//div[@text]')
        language_option = self.driver.find_element_by_xpath('//div[@class="language-select"]//div[@class="option"]/div')
        if language.text == 'NEP':
            action = ActionChains(self.driver)
            action.move_to_element(language).click(language_option).perform()
            print("Language changed")
        self.driver.implicitly_wait(0)
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()
        print('yes')

    def test_new_project_creation(self,setup):
        self.driver = setup
        dasb = Dashboard (self.driver)
        dasb.click_add_new_project()
        newform = NewProjectForm(self.driver)
        newform.set_ministry_name("1")
        newform.is_part_of_program(False)
        newform.is_subproject(False)
        newform.set_project_details("Demo","1262")
        newform.is_project_new(False)
        newform.select_project_theme('i')
        newform.click_save()
        try:
            utils.explicit_wait_present(setup,"//*[text()[contains(.,'Congratulations')]]")
            self.log.info("Project creation was sucessfull")
        except:
            self.log.info("Could not create a project ")
            assert False
            
    
    def test_edit_general_information(self,setup):
        self.driver = setup
        gb = GeneralInfo(self.driver)
        time.sleep(1)
        gb.select_project_type('Service Oriented')
        gb.select_project_priority('National Pride Project')
        #gb.select_categorization("below 3 years")
        gb.select_sector("Agriculture ,Land Management,Cooperative and Forest Area")
        gb.select_sector("Agriculture and Vetenary Development")
        gb.select_sector("Social")
        gb.select_district("Bhojpur")
        gb.select_district("jhapa")
        gb.click_save()
        
    
    def test_edit_project_specific(self,setup):
        self.driver = setup
        ps = ProjectSpecific(self.driver)
        time.sleep(2)
        ps.is_year_on_year(False)
        ps.set_start_end_date()
        ps.set_project_cost_details("20000","twenty thousand","2068/69","08/07/2021")
        ps.is_cost_revised(True)
        ps.set_revised_project_cost_details("20000","twenty thousand","2068/69","08/07/2021")
        ps.is_break_down_available(True)
        ps.set_breakdown_details("2","Two","30000","Thirty thousand")
        ps.upload_file(self.dir+"/testData/pbmis9.png")
        ps.set_file_desc("pbmis9.png","this is test")
        ps.click_save()
        

    def test_edit_phy_finan_progress(self,setup):
        self.driver =  setup
        pfp = PhysicalProgress(self.driver)
        time.sleep(1)
        pfp.set_financial_progress("50")
        pfp.set_financial_progress_amount("20000")
        pfp.upload_financial_progress(self.dir+"/testData/sample.pdf")
        pfp.set_fiscal_year_for_last_2("2068/69")
        pfp.set_allocated_budget_for_last_2("20000")
        pfp.set_acllocated_budget_word_for_last_2("Twenty Thousand")
        pfp.set_total_expenditure_for_last_2("15000")
        pfp.set_total_expenditure_word_for_last_2("fifteen thousand")
        pfp.upload_file_last_2(self.dir+"/testData/sample.pdf")
        pfp.set_fiscal_year_for_current("2068/69")
        pfp.set_allocated_budget_for_current("20000")
        pfp.set_acllocated_budget_word_for_current("Twenty Thousand")
        pfp.set_total_expenditure_for_current("15000")
        pfp.set_total_expenditure_word_for_current("fifteen thousand")
        pfp.upload_file_current(self.dir+"/testData/sample.pdf")
        pfp.set_fiscal_year_for_coming("2068/69")
        pfp.set_allocated_budget_for_coming("20000")
        pfp.set_acllocated_budget_word_for_coming("Twenty Thousand")
        pfp.upload_file_coming(self.dir+"/testData/sample.pdf")
        pfp.set_fiscal_year_for_f2("2068/69")
        pfp.set_allocated_budget_for_f2("20000")
        pfp.set_acllocated_budget_word_for_f2("Twenty Thousand")
        pfp.upload_file_f2(self.dir+"/testData/sample.pdf")
        pfp.set_physical_progress("20")
        pfp.upload_file_physical_progress(self.dir+"/testData/sample.pdf")
        pfp.click_save()
        
           
    def test_project_readiness(self,setup):    
        rad = Readiness(setup)
        time.sleep(2)
        rad.set_desk_study("Yes",self.dir+"/testData/sample.pdf")
        rad.set_pre_feasibility_study("not required")
        rad.set_project_concept_study("not required")
        rad.set_feasibility_study("in progress",date="08/11/2021")
        rad.set_detailed_project_report_study("not required")
        rad.set_project_proposal_study("not required")
        rad.set_environmental_impact_study("not required")
        rad.set_environmental_exam_study("not required")
        rad.set_procurement_study("not required")
        rad.set_current_procurement_study("not required")
        rad.set_next_procurement_study("not required")
        rad.set_proposed_project_study("in progress",date="08/11/2021")
        rad.set_procurement_contract_study("not required")
        rad.set_risk_management_study("not required")
        rad.set_log_frame_study("not required")
        rad.set_monitor_evaluate_study("not required")
        rad.set_land_acquisition_study("not required")
        rad.set_land_acquisition_completion("20",self.dir+"/testData/sample.pdf",self.dir+"/testData/sample.pdf")       
        rad.test_textbox("This is generated automatically")
        rad.click_save()
        
    
    def test_edit_project_selection(self,setup):
        ps = ProjectSelection(setup)
        time.sleep(1)
        ps.set_brief_description("this is brief",self.dir+"/testData/sample.pdf")
        ps.is_part_of_master_plan("yes")
        ps.set_approval_details(self.dir+"/testData/sample.pdf",isapproved="Yes",name="test",date = "08/12/2021")
        ps.set_national_goal("this is national goals",self.dir+"/testData/sample.pdf")
        ps.set_project_goal("this is project goals",self.dir+"/testData/sample.pdf")
        ps.set_targeted_benificiaries(direct="2",indirect="3",benificiaries="this is benific")
        ps.set_outcome_deliverables("this is test",self.dir+"/testData/sample.pdf")
        ps.select_sustainable_goals(goals=[1,2,3])
        ps.does_poverty_alleviation("Direct")
        ps.does_gender_alleviation("indirect")
        ps.does_climate_alleviation("neutral")
        ps.click_save()
        

    def test_edit_project_priotization(self,setup):
        pp = ProjectPriotization(setup)
        time.sleep(1)
        pp.set_economic_growth("2")
        pp.set_sdg("1")
        pp.set_participation("0")
        pp.set_sector_inclusive("2")
        pp.set_social_inclusive("3")
        pp.set_sector_goals("3")
        pp.set_sector_sdg("1")
        pp.upload_project_priotization_sheet(self.dir+"/testData/sample.pdf")
        pp.click_save()
        
        
    def test_edit_project_modality(self,setup):
        pm = ProjectModality(setup)
        time.sleep(1)
        pm.set_modality("PPP")
        pm.set_ppp_type_details("other","test company","test other")
        pm.click_save()
        

    def test_edit_project_financing(self,setup):
        pf=ProjectFinancing(setup)
        time.sleep(1)
        pf.set_financing_structure("50","20","50","10","50")
        pf.set_financing_status("No","this is test")
        pf.set_source_gov_project_gon("test","30000","Thirty thousand")
        pf.set_source_gov_project_internal("test","30000","Thirty thousand")
        pf.set_source_gov_project_external_loan("test","30000","Thirty thousand")
        pf.set_source_gov_project_external_grant("test","30000","Thirty thousand")
        pf.set_source_private_project_internal("test","40000","fourty thousand")
        pf.set_source_private_project_external_loan("test","40000","fourty thousand")
        pf.set_source_private_local_project_external_grant("test","40000","fourty thousand")
        pf.set_source_private_foreign_project_external_grant("test","40000","fourty thousand")
        pf.set_source_private_gov_project_gon("test","40000","fourty thousand")
        pf.set_source_private_project_other("test","40000","fourty thousand")
        pf.click_save()
        

    def test_edit_project_viability(self,setup):
        pv = ProjectViability(setup)
        time.sleep(1)
        pv.set_economic_indicators("50","45","57","45")
        pv.set_financial_indicators("50","45","57","45","3","")
        pv.set_social_indicators("50","50","30",self.dir+"/testData/sample.pdf")
        pv.click_save()
        
        
    def test_land_acquisition(self,setup):
        pla = ProjectLandAcquisition(setup)
        time.sleep(1)
        pla.set_acquisition_details("Guthi","200","1000","2000","2/2/2021","test",self.dir+"/testData/sample.pdf")
        pla.set_resettlement_details("20","30","50",self.dir+"/testData/sample.pdf")
        pla.click_save()
        
        

    def test_justification(self,setup): 
        pj = ProjectJustification(setup)
        time.sleep(1)
        pj.set_justification_type("merged")
        pj.click_save()
        

    def test_contact(self,setup):
        co = Contact(setup)
        time.sleep(1)
        co.set_details("test","test","9841563214","test@gmail.com")
        co.set_focal_details("focal","focal","9845653214","focal@gmail.com")
        co.click_save()
        

    def test_remark(self,setup):
        re=Remarks(setup)
        time.sleep(1)
        re.set_details(" this is test")
        re.click_save()
        

    def test_moderation(self,setup):
        mod = ProjectModeration(setup)
        mod.set_moderation_type("Send to verification")
        time.sleep(5)
        
        
