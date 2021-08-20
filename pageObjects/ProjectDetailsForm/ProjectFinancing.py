import time
import Utils.ComplexElement as utils

class ProjectFinancing():

    #Project Financing 
    project_financing_xpath = '//li//p[text()="Project Financing Arrangement"]'
    active_project_financing_xpath = '//li//p[text()="Project Financing Arrangement" and @class="form-section-link active"]'


    #Financing structure
    input_government_share_xpath = '//input[@name="governmentNepalShare"]'
    input_loan_xpath = '//input[@name="loan"]'
    input_grant_xpath = '//input[@name="grant"]'
    input_private_equity_xpath = '//input[@name="privateEquity"]'
    input_other_xpath = '//input[@name="others"]'

    #Financing status
    radio_is_financing_xpath = '//input[@name="financingStatus" and @value="Yes"]'
    radio_is_not_financing_xpath = '//input[@name="financingStatus" and @value="No"]'
    textbox_plan_xpath_xpath = '//input[@name="financingStatus" and @value="No"]/../../../../..//div[@role="textbox"]'
    file_financial_arrangements = '//input[@id="file-input-briefDescription"]'

    #source of funding for gov project
    input_gov_agency_xpath = '(//label[text()="Government of Nepal"]/../..//input[@name="fundingAgency"])[1]'
    input_gov_fund_xpath = '(//label[text()="Government of Nepal"]/../..//input[@name="fund"])[1]'
    input_gov_fund_word_xpath = '(//label[text()="Government of Nepal"]/../..//input[@name="fundInWord"])[1]'
    input_gov_internal_loan_agency_xpath = '//label[text()="Internal loan"]/../..//input[@name="fundingAgency"]'
    input_gov_internal_loan_fund_xpath = '//label[text()="Internal loan"]/../..//input[@name="fund"]'
    input_gov_internal_loan_fund_word_xpath = '//label[text()="Internal loan"]/../..//input[@name="fundInWord"]'
    input_gov_external_loan_agency_xpath = '//label[text()="External Source (Loan)"]/../..//input[@name="fundingAgency"]'
    input_gov_external_loan_fund_xpath = '//label[text()="External Source (Loan)"]/../..//input[@name="fund"]'
    input_gov_external_loan_fund_word_xpath = '//label[text()="External Source (Loan)"]/../..//input[@name="fundInWord"]'    
    input_gov_external_grant_agency_xpath = '//label[text()="External Source (Grant)"]/../..//input[@name="fundingAgency"]'
    input_gov_external_grant_xpath = '//label[text()="External Source (Grant)"]/../..//input[@name="fund"]'
    input_gov_external_grant_word_xpath = '//label[text()="External Source (Grant)"]/../..//input[@name="fundInWord"]'

    #Source of funding for provate project
    input_private_internal_loan_agency_xpath = '//label[text()="Internal Loan (PP)"]/../..//input[@name="fundingAgency"]'
    input_private_internal_loan_fund_xpath = '//label[text()="Internal Loan (PP)"]/../..//input[@name="fund"]'
    input_private_internal_loan_fund_word_xpath = '//label[text()="Internal Loan (PP)"]/../..//input[@name="fundInWord"]'
    input_private_external_loan_agency_xpath = '//label[text()="External Loan (PP)"]/../..//input[@name="fundingAgency"]'
    input_private_external_loan_fund_xpath = '//label[text()="External Loan (PP)"]/../..//input[@name="fund"]'
    input_private_external_loan_fund_word_xpath = '//label[text()="External Loan (PP)"]/../..//input[@name="fundInWord"]'    
    input_private_foreign_external_grant_agency_xpath = '//label[text()="Private Equity (Foreign)"]/../..//input[@name="fundingAgency"]'
    input_private_foreign_external_grant_xpath = '//label[text()="Private Equity (Foreign)"]/../..//input[@name="fund"]'
    input_private_foreign_external_grant_word_xpath = '//label[text()="Private Equity (Foreign)"]/../..//input[@name="fundInWord"]'
    input_private_local_external_grant_agency_xpath = '//label[text()="Private Equity (Local)"]/../..//input[@name="fundingAgency"]'
    input_private_local_external_grant_xpath = '//label[text()="Private Equity (Local)"]/../..//input[@name="fund"]'
    input_private_local_external_grant_word_xpath = '//label[text()="Private Equity (Local)"]/../..//input[@name="fundInWord"]'
    input_private_gov_agency_xpath = '(//label[text()="Government of Nepal"]/../..//input[@name="fundingAgency"])[2]'
    input_private_gov_fund_xpath = '(//label[text()="Government of Nepal"]/../..//input[@name="fund"])[2]'
    input_private_gov_fund_word_xpath = '(//label[text()="Government of Nepal"]/../..//input[@name="fundInWord"])[2]'
    input_private_other_grant_agency_xpath = '//label[text()="Others"]/../..//input[@name="fundingAgency"]'
    input_private_other_grant_xpath = '//label[text()="Others"]/../..//input[@name="fund"]'
    input_private_other_grant_word_xpath = '//label[text()="Others"]/../..//input[@name="fundInWord"]'
    
    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'  

    def __init__(self,setup) -> None:
        self.driver = setup
        utils.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = utils.explicit_wait_present(self.driver,self.project_financing_xpath)
        utils.js_session_click(self.driver,link)
    
    def check(self):
        try:
            utils.get_element(self.driver,self.active_project_financing_xpath)
        except:
            self.goto()
            time.sleep(1)

    def set_financing_structure(self,share_percent,loan,grant,private_equity,other):
        self.check()
        utils.write_using_xpath(self.driver,self.input_government_share_xpath,share_percent)
        utils.write_using_xpath(self.driver,self.input_loan_xpath,loan)
        utils.write_using_xpath(self.driver,self.input_grant_xpath,grant)
        utils.write_using_xpath(self.driver,self.input_private_equity_xpath,private_equity)
        utils.write_using_xpath(self.driver,self.input_other_xpath,other)
    
    def set_financing_status(self,value,desc=" "):
        self.check()
        if value.lower() == "yes":
            utils.js_click(self.driver,self.radio_is_financing_xpath)
        else:
            utils.js_click(self.driver,self.radio_is_not_financing_xpath)
            self.driver.find_element_by_xpath(self.textbox_plan_xpath_xpath).send_keys(desc)

    def set_source_gov_project_gon(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_gov_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_gov_fund_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_gov_fund_word_xpath,fund_words)
    
    def set_source_gov_project_internal(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_gov_internal_loan_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_gov_internal_loan_fund_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_gov_internal_loan_fund_word_xpath,fund_words)
    
    def set_source_gov_project_external_loan(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_gov_external_loan_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_gov_external_loan_fund_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_gov_external_loan_fund_word_xpath,fund_words)
    
    def set_source_gov_project_external_grant(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_gov_external_grant_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_gov_external_grant_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_gov_external_grant_word_xpath,fund_words)
    
    def set_source_private_project_internal(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_private_internal_loan_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_private_internal_loan_fund_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_private_internal_loan_fund_word_xpath,fund_words)
    
    def set_source_private_project_external_loan(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_private_external_loan_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_private_external_loan_fund_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_private_external_loan_fund_word_xpath,fund_words)
    
    def set_source_private_foreign_project_external_grant(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_private_foreign_external_grant_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_private_foreign_external_grant_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_private_foreign_external_grant_word_xpath,fund_words)
    
    def set_source_private_local_project_external_grant(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_private_local_external_grant_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_private_local_external_grant_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_private_local_external_grant_word_xpath,fund_words)
    
    def set_source_private_gov_project_gon(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_private_gov_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_private_gov_fund_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_private_gov_fund_word_xpath,fund_words)
    
    def set_source_private_project_other(self,agency,fund,fund_words):
        self.check()
        utils.write_using_xpath(self.driver,self.input_private_other_grant_agency_xpath,agency)
        utils.write_using_xpath(self.driver,self.input_private_other_grant_xpath,fund)
        utils.write_using_xpath(self.driver,self.input_private_other_grant_word_xpath,fund_words)
    
    def click_save(self):
        utils.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        utils.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        utils.js_click(self.driver,self.button_to_prev_xpath)