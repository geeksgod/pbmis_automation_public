import time
import Utils.ComplexElement as util
class PhysicalProgress:

    physical_financial_progress_xpath = '//li//p[text()="Physical/Financial Progress"]'
    active_physical_financial_progress_xpath = '//li//p[text()="Physical/Financial Progress" and @class="form-section-link active"]'

    #Financial Progress section
    input_financial_progress_percentage_xpath = '//input[@name="financialProgress"]'
    input_financial_progress_amount_xpath = '//input[@name="financialProgressAmt"]'
    input_financial_progress_file_xpath = '//input[@name="financialProgressFile"]'

    #Expenditure of last 2 Fiscal Year
    dropdown_fiscal_year_l2_xapth = '(//div[@name="fiscalYear"])[1]'
    dropdown_option_fiscal_year_l2_xpath = '(//div[@name="fiscalYear"])[1]//div[@role="option"]'
    input_allocate_budget_l2_xpath = '//input[@name="allocatedBudget"]'
    input_allocate_budget_word_l2_xpath = '//input[@name="allocatedBudgetWord"]'
    input_total_expenditure_l2_xpath = '//input[@name="expenditureBudget"]'
    input_total_expenditure_word_l2_xpath = '//input[@name="expenditureBudgetWord"]'
    input_total_expenditure_file_l2_xpath = '//input[@name="expenditureTillDateFile"]'

    #Expenditure of the current Fiscal Year
    dropdown_fiscal_year_current_xapth = '(//div[@name="fiscalYear"])[2]'
    dropdown_option_fiscal_year_current_xpath = '(//div[@name="fiscalYear"])[2]//div[@role="option"]'
    input_allocate_budget_current_xpath = '//input[@name="currentAllocatedBudget"]'
    input_allocate_budget_word_current_xpath = '//input[@name="currentAllocatedBudgetWord"]'
    input_total_expenditure_current_xpath = '//input[@name="currentExpenditureBudget"]'
    input_total_expenditure_word_current_xpath = '//input[@name="currentExpenditureBudgetWord"]'
    input_total_expenditure_file_current_xpath = '//input[@name="expenditureCurrentFYearFile"]'

    #Expenditure Budgeted Requirement for coming fiscal year
    dropdown_fiscal_year_coming_xapth = '(//div[@name="fiscalYear"])[3]'
    dropdown_option_fiscal_year_coming_xpath = '(//div[@name="fiscalYear"])[3]//div[@role="option"]'
    input_allocate_budget_coming_xpath = '//input[@name="comingEstimatedAnnualBudget"]'
    input_allocate_budget_word_coming_xpath = '//input[@name="comingEstimatedAnnualBudgetWord"]'
    input_total_expenditure_file_coming_xpath = '//input[@name="expenditureComingFYearFile"]'

    #Projected Budget Requirement for following 2 Fiscal Year
    dropdown_fiscal_year_f2_xapth = '(//div[@name="fiscalYear"])[4]'
    dropdown_option_fiscal_year_f2_xpath = '(//div[@name="fiscalYear"])[4]//div[@role="option"]'
    input_allocate_budget_f2_xpath = '//input[@name="projectedBudgetRequirement"]'
    input_allocate_budget_word_f2_xpath = '//input[@name="projectedBudgetRequirementWord"]'
    input_total_expenditure_file_f2_xpath = '//input[@name="projectedBudgetFile"]'

    #Physical progress
    input_physical_progress_xpath = '//input[@name="physicalProgress"]'
    input_physical_progress_file_xpath = '//input[@name="physicalProgressFile"]'

    #action buttons
    button_save_xpath = '//button[text()="Save and continue"]'
    button_cancel_xpath = '//button[text()="Save and exit"]'
    button_to_prev_xpath = '//button[text()="Back to previous form"]'

    def __init__(self,setup) -> None:
        self.driver = setup
        util.check_loader(setup)
        self.goto()
    
    def goto(self):
        link = util.explicit_wait_present(self.driver,self.physical_financial_progress_xpath)
        util.js_session_click(self.driver,link)
    
    def check(self):
        try:
            util.get_element(self.driver,self.active_physical_financial_progress_xpath)
        except:
            self.goto()
            time.sleep(1)

    def set_financial_progress(self,percent):
        self.check()
        util.write_using_xpath(self.driver,self.input_financial_progress_percentage_xpath,percent)
    
    def set_financial_progress_amount(self,amount):
        self.check()
        util.write_using_xpath(self.driver,self.input_financial_progress_amount_xpath,amount)
    
    def upload_financial_progress(self,path):
        self.check()
        util.upload_file(self.driver,self.input_financial_progress_file_xpath,path)
    
    def set_fiscal_year_for_last_2(self,year):
        self.check()
        util.handle_dropdown(self.driver,self.dropdown_fiscal_year_l2_xapth,self.dropdown_option_fiscal_year_l2_xpath,year)

    def set_allocated_budget_for_last_2(self,amount):
        self.check()
        util.write_using_xpath(self.driver,self.input_allocate_budget_l2_xpath,amount)
    
    def set_acllocated_budget_word_for_last_2(self,amount_word):
        self.check()
        util.write_using_xpath(self.driver,self.input_allocate_budget_word_l2_xpath,amount_word)
    
    def set_total_expenditure_for_last_2(self,amount):
        self.check()
        util.write_using_xpath(self.driver,self.input_total_expenditure_l2_xpath,amount)
    
    def set_total_expenditure_word_for_last_2(self,amount_word):
        self.check()
        util.write_using_xpath(self.driver,self.input_total_expenditure_word_l2_xpath,amount_word)
    
    def upload_file_last_2(self,path):
        self.check()
        util.upload_file(self.driver,self.input_total_expenditure_file_l2_xpath,path)
    
    def set_fiscal_year_for_current(self,year):
        self.check()
        util.handle_dropdown(self.driver,self.dropdown_fiscal_year_current_xapth,self.dropdown_option_fiscal_year_current_xpath,year)

    def set_allocated_budget_for_current(self,amount):
        self.check()
        util.write_using_xpath(self.driver,self.input_allocate_budget_current_xpath,amount)
    
    def set_acllocated_budget_word_for_current(self,amount_word):
        self.check()
        util.write_using_xpath(self.driver,self.input_allocate_budget_word_current_xpath,amount_word)
    
    def set_total_expenditure_for_current(self,amount):
        self.check()
        util.write_using_xpath(self.driver,self.input_total_expenditure_current_xpath,amount)
    
    def set_total_expenditure_word_for_current(self,amount_word):
        self.check()
        util.write_using_xpath(self.driver,self.input_total_expenditure_word_current_xpath,amount_word)
    
    def upload_file_current(self,path):
        self.check()
        util.upload_file(self.driver,self.input_total_expenditure_file_current_xpath,path)
    
    def set_fiscal_year_for_coming(self,year):
        self.check()
        util.handle_dropdown(self.driver,self.dropdown_fiscal_year_coming_xapth,self.dropdown_option_fiscal_year_coming_xpath,year)

    def set_allocated_budget_for_coming(self,amount):
        self.check()
        util.write_using_xpath(self.driver,self.input_allocate_budget_coming_xpath,amount)
    
    def set_acllocated_budget_word_for_coming(self,amount_word):
        self.check()
        util.write_using_xpath(self.driver,self.input_allocate_budget_word_coming_xpath,amount_word)
    
    def upload_file_coming(self,path):
        self.check()
        util.upload_file(self.driver,self.input_total_expenditure_file_coming_xpath,path)
    
    def set_fiscal_year_for_f2(self,year):
        self.check()
        util.handle_dropdown(self.driver,self.dropdown_fiscal_year_f2_xapth,self.dropdown_option_fiscal_year_f2_xpath,year)

    def set_allocated_budget_for_f2(self,amount):
        self.check()
        util.write_using_xpath(self.driver,self.input_allocate_budget_f2_xpath,amount)
    
    def set_acllocated_budget_word_for_f2(self,amount_word):
        self.check()
        util.write_using_xpath(self.driver,self.input_allocate_budget_word_f2_xpath,amount_word)
    
    def upload_file_f2(self,path):
        self.check()
        util.upload_file(self.driver,self.input_total_expenditure_file_f2_xpath,path)
    
    def set_physical_progress(self,percent):
        self.check()
        util.write_using_xpath(self.driver,self.input_physical_progress_xpath,percent)

    def upload_file_physical_progress(self,path):
        self.check()
        util.upload_file(self.driver,self.input_physical_progress_file_xpath,path)
    
    def click_save(self):
        self.check()
        util.js_click(self.driver,self.button_save_xpath)
    
    def click_cancel(self):
        self.check()
        util.js_click(self.driver,self.button_cancel_xpath)

    def click_previous(self):
        self.check()
        util.js_click(self.driver,self.button_to_prev_xpath)