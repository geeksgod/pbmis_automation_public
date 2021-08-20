# Automationsetup (Page Object Model framework) 
This is the simple automation framework for PBMIS project 
## Pre-requisites
* python installed
* Chrome or Mozilla installed  
  
## Libraries used
* Selenium: to automate browser  
* pytest: to manage testcases  
* openpyxl: to read/write excelfiles  
* pytest-html: to generate simple html report  
* pytest-xdist: to execute testcases parallely  
* pytest-allure: to integrate allure json files  
additonally  



# Enviroment Setup 
```console
pip install -r req.txt
```  
this will install all the required python libraries

# Running the automation script
Make sure the you are in project directory.then run  
> Before runnng make sure to provide new name and id to project (pbmis_automation/testCases/test_new_project_01.py > line 70  ) and login creds in (Configurations/user.ini) 
* ## Normal execution  
```console
python3 -m pytest -s -v testcases
``` 
* ## Normal execution with generation of HTML report  
```console
python3 -m pytest -s -v testcases --html=./Reports/demo.html
``` 
Preferred directory location should be passed where reports are to be generated as argument for  --html 
