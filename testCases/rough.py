from selenium import webdriver
import pytest
import sys
sys.path.insert(1, '/home/bipin/YIPL/PBMIS')
from pageObjects.rough import Rough 
print(sys.path)
driver = webdriver.Chrome(executable_path='/home/bipin/Downloads/chromedriver_linux64/chromedriver')

temp = Rough(driver)
temp.test_google()

driver.quit()
