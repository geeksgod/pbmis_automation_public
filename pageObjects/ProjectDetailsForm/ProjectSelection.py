import time
import Utils.ComplexElement as utils


class ProjectSelection:

    project_selection_xpath = '//li//p[text()="Basis of Project Selection"]'
    active_project_selection_xpath = '//li//p[text()="Basis of Project Selection" and @class="form-section-link active"]'

    #Brief Description of Project Including Salient Features
    textbox_brief_description_xpath = '//label[contains(text(),"Brief")]/..//div[@role="textbox"]'
    file_brief_description_xapth = '//input[@id="file-input-projectDescriptionFile"]'

    #is the project part of bigger scheme
    radio_is_part_of_master_plan = '//input[@name="isMasterPlan" and @value="Yes"]'
    radio_is_not_part_of_master_plan = '//input[@name="isMasterPlan" and @value="No"]'
    file_master_plan_xpath = '//input[@id="file-input-masterPlanFile"]'
    radio_is_master_plan_approved = '//input[@name="isMasterPlanApproved" and @value="Yes"]'
    radio_is_master_plan_not_approved = '//input[@name="isMasterPlanApproved" and @value="No"]'
    textbox_approving_authority_xapth = '//input[@name="approvingAuthority"]'
    date_approval_date_xpath = '//input[@name="isMasterPlanApproved" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Selection Criteria
    textbox_selection_criteria_xpath = '(//div[@role="textbox"])[2]'
    file_selection_criteria_xapth = '//input[@id="file-input-selectionCriteriaFile"]'

    #Is the project derived from National Periodic Plan 
    textbox_is_derived_xpath = '(//div[@role="textbox"])[3]'
    file_is_derived_xapth = '//input[@id="file-input-projectDerivationFile"]'

    #Plan to develop master plan?
    radio_is_plan_for_master_plan_xpath = '//input[@name="anyPlanToDevelopMasterPlan" and @value="Yes"]'
    radio_is_not_plan_for_master_plan_xpath = '//input[@name="anyPlanToDevelopMasterPlan" and @value="No"]'
    date_master_plan_xpath = '//input[@name="anyPlanToDevelopMasterPlan" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #National Goal
    textbox_national_goal_xpath = '//label[contains(text(),"National")]/..//div[@role="textbox"]'
    file_national_goal_xapth = '//input[@id="file-input-nationalGoalFile"]'

    #Project Goal
    textbox_project_goal_xpath = '//label[contains(text(),"Project Goal")]/..//div[@role="textbox"]'
    file_project_goal_xapth = '//input[@id="file-input-projectGoalFile"]'

    #target benificiaries
    textbox_direct_benificiaries_xpath = '//input[@name="directBeneficiaries"]'
    textbox_indirect_benificiaries_xpath = '//input[@name="indirectBeneficiaries"]'
    textbox_benificiaries_xpath = '//label[contains(text(),"Benef")]/..//div[@role="textbox"]'

    #outcome deliverables
    textbox_outcome_deliverables_xpath = '//label[contains(text(),"indica")]/..//div[@role="textbox"]'
    file_deliverables_xapth = '//input[@id="file-input-outcomesAndDeliverableFile"]'

    #Sustainable development goals
    checkbox_sustainable_goals_xpath = '(//div[@class="four wide field"])//label'

    #Poverty sign
    radio_does_poverty_alleviation_xpath= '//input[@name="povertySign" and @value="true"]'
    radio_does_not_poverty_alleviation_xpath= '//input[@name="povertySign" and @value="false"]'

    #Gender sign
    radio_does_gender_alleviation_xpath= '//input[@name="genderSign" and @value="true"]'
    radio_does_not_gender_alleviation_xpath= '//input[@name="genderSign" and @value="false"]'

    #climate Sign
    radio_does_extreme_relevant_climate_alleviation_xpath= '//input[@name="climateSign" and @value="true"]'
    radio_does_relevant_climate_alleviation_xpath= '//input[@name="climateSign" and @value="false"]'
    radio_neutral_climate_alleviation_xpath= '//input[@name="climateSign" and @value="neutral"]'

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'
    
    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.project_selection_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_project_selection_xpath)
        except:
            self.goto()
            time.sleep(1)

    def set_brief_description(self,desc,path):
        self.check()
        utils.write_using_xpath(self.driver,self.textbox_brief_description_xpath,desc)
        utils.upload_file(self.driver,self.file_brief_description_xapth,path)

    def is_part_of_master_plan(self,value):
        """options = Yes,No if yes the set_approval_details function is required to set further details"""
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_is_part_of_master_plan)
        else:
            utils.js_click(self.driver,self.radio_is_not_part_of_master_plan)
    
    def set_approval_details(self,path,isapproved ="No",name="",date=""):
        self.check()
        file = utils.explicit_wait_present(self.driver,self.file_master_plan_xpath)
        utils.upload_file(self.driver,self.file_master_plan_xpath,path)
        """options = Yes,No"""
        if isapproved.lower() == "yes":
            utils.js_click(self.driver,self.radio_is_master_plan_approved)
            temp = utils.explicit_wait_present(self.driver,self.textbox_approving_authority_xapth)
            temp.send_keys(name)
            utils.write_using_xpath(self.driver,self.date_approval_date_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_is_master_plan_not_approved)
    
    def set_selection_criteria(self,desc,path):
        self.check()
        utils.write_using_xpath(self.driver,self.textbox_selection_criteria_xpath,desc)
        utils.upload_file(self.driver,self.file_selection_criteria_xapth,path)
    
    def set_is_derived(self,desc,path):
        self.check()
        utils.write_using_xpath(self.driver,self.textbox_is_derived_xpath,desc)
        utils.upload_file(self.driver,self.file_is_derived_xapth,path)

    def is_plan_for_master_plan(self,value,date="10/10/2019"):
        """options = Yes,No"""
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_is_plan_for_master_plan_xpath)
            utils.write_using_xpath(self.driver,self.date_master_plan_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_is_not_plan_for_master_plan_xpath)

    def set_national_goal(self,desc,path):
        self.check()
        utils.write_using_xpath(self.driver,self.textbox_national_goal_xpath,desc)
        utils.upload_file(self.driver,self.file_national_goal_xapth,path)

    def set_project_goal(self,desc,path):
        self.check()
        utils.write_using_xpath(self.driver,self.textbox_project_goal_xpath,desc)
        utils.upload_file(self.driver,self.file_project_goal_xapth,path)   

    def set_targeted_benificiaries(self,direct = None,indirect=None,benificiaries=None):
        self.check()
        if direct:
            utils.write_using_xpath(self.driver,self.textbox_direct_benificiaries_xpath,direct)
        if indirect:
            utils.write_using_xpath(self.driver,self.textbox_indirect_benificiaries_xpath,indirect)
        if benificiaries:
             utils.write_using_xpath(self.driver,self.textbox_benificiaries_xpath,benificiaries)

    def set_outcome_deliverables(self,desc,path):
        self.check()
        utils.write_using_xpath(self.driver,self.textbox_outcome_deliverables_xpath,desc)
        utils.upload_file(self.driver,self.file_deliverables_xapth,path)

    def select_sustainable_goals(self,goals=[]):
        """
        provide the array of number to select the goals
        (1) No Poverty
        (2) Zero Hunger
        (3) Good Health and Well-being
        (4) Quality Education
        (5) Gender Equality
        (6) Clean Water and SanitationDirect,Indirectities
        (12) Responsible Consumption and Production
        (13) Climate Action
        (14) Life Below Water
        (15) Life On Land
        (16) Peace, Justice, and Strong Institutions
        (17) Partnerships for the Goals
        """
        self.check()
        if len(goals) != 0:
            time.sleep(1)
            options = utils.explicit_wait_multiple_element_present(self.driver,self.checkbox_sustainable_goals_xpath)
            for goal in goals:
                self.driver.execute_script("arguments[0].click()",options[goal-1])
    
    def does_poverty_alleviation(self,value):
        """options = Direct,Indirect"""
        self.check()
        if value.lower() == "direct":
            utils.js_click(self.driver,self.radio_does_poverty_alleviation_xpath)
        else:
            utils.js_click(self.driver,self.radio_does_not_poverty_alleviation_xpath)
    

    def does_gender_alleviation(self,value):
        """options = Direct,Indirect"""
        self.check()
        if value.lower() == "direct":
            utils.js_click(self.driver,self.radio_does_gender_alleviation_xpath)
        else:
            utils.js_click(self.driver,self.radio_does_not_gender_alleviation_xpath)
    
    def does_climate_alleviation(self,value):
        """options = extremely relevant,relevant,neutral"""
        self.check()
        if value.lower() == "extremely relevant":
            utils.js_click(self.driver,self.radio_does_extreme_relevant_climate_alleviation_xpath)
        elif value.lower() == "relevant" :
            utils.js_click(self.driver,self.radio_does_relevant_climate_alleviation_xpath)
        else:
            utils.js_click(self.driver,self.radio_neutral_climate_alleviation_xpath)

    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)
    