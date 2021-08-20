import time
import Utils.ComplexElement as utils

class Readiness:

    project_readiliness_xpath = '//li//p[text()="Project Readiness"]'
    active_project_readiliness_xpath = '//li//p[text()="Project Readiness" and @class="form-section-link active"]'

    #Desk study
    radio_desk_study_has_xpath = '//input[@name="deskStudy" and @value="Yes"]'
    radio_desk_study_inprogress_xpath = '//input[@name="deskStudy" and @value="No"]'
    radio_desk_study_notrequired = '//input[@name="deskStudy" and @value="Not Required"]'
    file_desk_study_xpath = '//input[@name="deskStudy" and @value="Yes"]/../../../../..//input[@type="file"]'

    #Pre feasibility study
    radio_pre_feasibility_has_xpath = '//input[@name="preFeasibility" and @value="Yes"]'
    radio_pre_feasibility_inprogress_xpath = '//input[@name="preFeasibility" and @value="No"]'
    radio_pre_feasibility_notrequired = '//input[@name="preFeasibility" and @value="Not Required"]'
    file_pre_feasibility_xpath = '//input[@name="preFeasibility" and @value="Yes"]/../../../../..//input[@type="file"]'

    #Project Concept
    radio_project_concept_has_xpath = '//input[@name="projectConcept" and @value="Yes"]'
    radio_project_concept_inprogress_xpath = '//input[@name="projectConcept" and @value="No"]'
    radio_project_concept_notrequired = '//input[@name="projectConcept" and @value="Not Required"]'
    file_project_concept_xpath = '//input[@name="projectConcept" and @value="Yes"]/../../../../..//input[@type="file"]'

    #Fesibility Study
    radio_feasibility_has_xpath = '//input[@name="feasibilityStudy" and @value="Yes"]'
    radio_feasibility_inprogress_xpath = '//input[@name="feasibilityStudy" and @value="No"]'
    radio_feasibility_notrequired = '//input[@name="feasibilityStudy" and @value="Not Required"]'
    file_feasibility_xpath = '//input[@name="feasibilityStudy" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_feasibility_xpath = '//input[@name="feasibilityStudy" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Detailed project Report
    radio_detailed_project_report_has_xpath = '//input[@name="dpr" and @value="Yes"]'
    radio_detailed_project_report_inprogress_xpath = '//input[@name="dpr" and @value="No"]'
    radio_detailed_project_report_notrequired = '//input[@name="dpr" and @value="Not Required"]'
    file_detailed_project_report_xpath = '//input[@name="dpr" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_detailed_project_report_xpath = '//input[@name="dpr" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Project Proposal
    radio_project_proposal_has_xpath = '//input[@name="projectProposal" and @value="Yes"]'
    radio_project_proposal_inprogress_xpath = '//input[@name="projectProposal" and @value="No"]'
    radio_project_proposal_notrequired = '//input[@name="projectProposal" and @value="Not Required"]'
    file_project_proposal_xpath = '//input[@name="projectProposal" and @value="Yes"]/../../../../..//input[@type="file"]'

    #Enviromental Impact
    radio_environmental_impact_has_xpath = '//input[@name="eia" and @value="Yes"]'
    radio_environmental_impact_inprogress_xpath = '//input[@name="eia" and @value="No"]'
    radio_environmental_impact_notrequired = '//input[@name="eia" and @value="Not Required"]'
    file_environmental_impact_xpath = '//input[@name="eia" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_environmental_impact_xpath = '//input[@name="eia" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Inital Environmental Examination
    radio_environmental_exam_has_xpath = '//input[@name="iee" and @value="Yes"]'
    radio_environmental_exam_inprogress_xpath = '//input[@name="iee" and @value="No"]'
    radio_environmental_exam_notrequired = '//input[@name="iee" and @value="Not Required"]'
    file_environmental_exam_xpath = '//input[@name="iee" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_environmental_exam_xpath = '//input[@name="iee" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Master Procurement Plan
    radio_procurement_has_xpath = '//input[@name="masterProcurement" and @value="Yes"]'
    radio_procurement_inprogress_xpath = '//input[@name="masterProcurement" and @value="No"]'
    radio_procurement_notrequired = '//input[@name="masterProcurement" and @value="Not Required"]'
    file_procurement_xpath = '//input[@name="masterProcurement" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_procurement_xpath = '//input[@name="masterProcurement" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Annual Procurement Plan current
    radio_current_procurement_has_xpath = '//input[@name="annualProcurement" and @value="Yes"]'
    radio_current_procurement_inprogress_xpath = '//input[@name="annualProcurement" and @value="No"]'
    radio_current_procurement_notrequired = '//input[@name="annualProcurement" and @value="Not Required"]'
    file_current_procurement_xpath = '//input[@name="annualProcurement" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_current_procurement_xpath = '//input[@name="annualProcurement" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Annual procurement plan from next year
    radio_next_procurement_has_xpath = '//input[@name="annualProcurementComing" and @value="Yes"]'
    radio_next_procurement_inprogress_xpath = '//input[@name="annualProcurementComing" and @value="No"]'
    radio_next_procurement_notrequired = '//input[@name="annualProcurementComing" and @value="Not Required"]'
    file_next_procurement_xpath = '//input[@name="annualProcurementComing" and @value="Yes"]/../../../../..//input[@type="file"]'

    #Proposed Project Implementation Plan
    radio_proposed_project_has_xpath = '//input[@name="implementationPlan" and @value="Yes"]'
    radio_proposed_project_inprogress_xpath = '//input[@name="implementationPlan" and @value="No"]'
    radio_proposed_project_notrequired = '//input[@name="implementationPlan" and @value="Not Required"]'
    file_proposed_project_xpath = '//input[@name="implementationPlan" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_proposed_project_xpath = '//input[@name="implementationPlan" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Procurement and Contract Award
    radio_procurement_contract_has_xpath = '//input[@name="procurementAward" and @value="Yes"]'
    radio_procurement_contract_inprogress_xpath = '//input[@name="procurementAward" and @value="No"]'
    radio_procurement_contract_notrequired = '//input[@name="procurementAward" and @value="Not Required"]'
    file_procurement_contract_xpath = '//input[@name="procurementAward" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_procurement_contract_xpath = '//input[@name="procurementAward" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Risk Management and Mitigation 
    radio_risk_management_has_xpath = '//input[@name="riskManagement" and @value="Yes"]'
    radio_risk_management_inprogress_xpath = '//input[@name="riskManagement" and @value="No"]'
    radio_risk_management_notrequired = '//input[@name="riskManagement" and @value="Not Required"]'
    file_risk_management_xpath = '//input[@name="riskManagement" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_risk_management_xpath = '//input[@name="riskManagement" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Development of Logical/Result Framework
    radio_log_frame_has_xpath = '//input[@name="logFrame" and @value="Yes"]'
    radio_log_frame_inprogress_xpath = '//input[@name="logFrame" and @value="No"]'
    radio_log_frame_notrequired = '//input[@name="logFrame" and @value="Not Required"]'
    file_log_frame_xpath = '//input[@name="logFrame" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_log_frame_xpath = '//input[@name="logFrame" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Monitoring and Evalutaion Plan
    radio_monitor_evaluate_has_xpath = '//input[@name="monitorEvaluation" and @value="Yes"]'
    radio_monitor_evaluate_inprogress_xpath = '//input[@name="monitorEvaluation" and @value="No"]'
    radio_monitor_evaluate_notrequired = '//input[@name="monitorEvaluation" and @value="Not Required"]'
    file_monitor_evaluate_xpath = '//input[@name="monitorEvaluation" and @value="Yes"]/../../../../..//input[@type="file"]'
    date_monitor_evaluate_xpath = '//input[@name="monitorEvaluation" and @value="Yes"]/../../../../..//div[@class="react-datepicker-wrapper"]//input'

    #Land acquisition
    radio_land_acquisition_has_xpath = '//input[@name="landAcquisition" and @value="Yes"]'
    radio_land_acquisition_inprogress_xpath = '//input[@name="landAcquisition" and @value="No"]'
    radio_land_acquisition_notrequired = '//input[@name="landAcquisition" and @value="Not Required"]'
    file_land_acquisition_xpath = '//input[@name="landAcquisition" and @value="Yes"]/../../../../..//input[@type="file"]'

    #Land acquisition completion
    input_land_acquisition_completetion_xpath = '//input[@name="landAcquisitionComplete"]'
    file_legal_docs_land_xpath = '//input[@id="file-input-otherDocumentFile"]'
    file_legal_docs_2_land_xpath = '//input[@id="file-input-anyOtherDocumentFile"]'

    #Mention challenges/risk/issue
    textbox_challenges_xpath = '//div[@role="textbox"]'
    file_challenges_xpath = '//input[@id="file-input-riskAndIssueFile"]'

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'


    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.project_readiliness_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_project_readiliness_xpath)
        except:
            self.goto()
            time.sleep(1)
    
    def set_desk_study(self,value,path = None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_desk_study_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_desk_study_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_desk_study_inprogress_xpath)
        else:
            utils.js_click(self.driver,self.radio_desk_study_notrequired)

    def set_pre_feasibility_study(self,value,path = None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_pre_feasibility_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_pre_feasibility_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_pre_feasibility_inprogress_xpath)
        else:
            utils.js_click(self.driver,self.radio_pre_feasibility_notrequired)
    
    def set_project_concept_study(self,value,path = None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_project_concept_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_project_concept_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_project_concept_inprogress_xpath)
        else:
            utils.js_click(self.driver,self.radio_project_concept_notrequired)
    
    def set_feasibility_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_feasibility_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_feasibility_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_feasibility_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_feasibility_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_feasibility_notrequired)
    
    def set_detailed_project_report_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_detailed_project_report_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_detailed_project_report_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_detailed_project_report_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_detailed_project_report_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_detailed_project_report_notrequired)

    def set_project_proposal_study(self,value,path = None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_project_proposal_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_project_proposal_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_project_proposal_inprogress_xpath)
        else:
            utils.js_click(self.driver,self.radio_project_proposal_notrequired)
    
    def set_environmental_impact_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_environmental_impact_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_environmental_impact_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_environmental_impact_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_environmental_impact_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_environmental_impact_notrequired)
    
    def set_environmental_exam_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_environmental_exam_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_environmental_exam_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_environmental_exam_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_environmental_exam_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_environmental_exam_notrequired)
    
    def set_procurement_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_procurement_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_procurement_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_procurement_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_procurement_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_procurement_notrequired)
    
    def set_current_procurement_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_current_procurement_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_current_procurement_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_current_procurement_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_current_procurement_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_current_procurement_notrequired)
    
    def set_next_procurement_study(self,value,path = None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_next_procurement_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_next_procurement_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_next_procurement_inprogress_xpath)
        else:
            utils.js_click(self.driver,self.radio_next_procurement_notrequired)
    
    def set_proposed_project_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_proposed_project_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_proposed_project_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_proposed_project_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_proposed_project_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_proposed_project_notrequired)
    
    def set_procurement_contract_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_procurement_contract_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_procurement_contract_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_procurement_contract_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_procurement_contract_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_procurement_contract_notrequired)
    
    def set_risk_management_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_risk_management_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_risk_management_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_risk_management_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_risk_management_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_risk_management_notrequired)
    
    def set_log_frame_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_log_frame_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_log_frame_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_log_frame_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_log_frame_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_log_frame_notrequired)

    def set_monitor_evaluate_study(self,value,path = None,date=None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_monitor_evaluate_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_monitor_evaluate_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_monitor_evaluate_inprogress_xpath)
            if date:
                utils.write_using_xpath(self.driver,self.date_monitor_evaluate_xpath,date)
        else:
            utils.js_click(self.driver,self.radio_monitor_evaluate_notrequired)
    
    def set_land_acquisition_study(self,value,path = None):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_land_acquisition_has_xpath)
            if path:
                utils.upload_file(self.driver,self.file_land_acquisition_xpath,path)
        elif value.lower() == "in progress":
            utils.js_click(self.driver,self.radio_land_acquisition_inprogress_xpath)
        else:
            utils.js_click(self.driver,self.radio_land_acquisition_notrequired)
    
    def set_land_acquisition_completion(self,percent,path1 = None,path2= None):
        self.check()
        utils.write_using_xpath(self.driver, self.input_land_acquisition_completetion_xpath,percent)

        if path1:
            utils.upload_file(self.driver,self.file_legal_docs_land_xpath,path1)
        
        if path2:
            utils.upload_file(self.driver,self.file_legal_docs_2_land_xpath,path2)
      
      
    def test_textbox(self,text):
        self.check()
        utils.write_using_xpath(self.driver,self.textbox_challenges_xpath,text) 
      
    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)