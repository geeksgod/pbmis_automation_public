from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def explicit_wait_clickable(driver,locator):
    wait = WebDriverWait(driver,10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH,locator)))
    return element

def explicit_wait_present(driver,locator):
    wait = WebDriverWait(driver,10)
    element = wait.until(EC.presence_of_element_located((By.XPATH,locator)))
    return element

def js_click(setup,locator):
    driver = setup
    button = driver.find_element_by_xpath(locator)
    driver.execute_script("arguments[0].click()",button)

def write_using_xpath(driver,locator,value):
    element = explicit_wait_present(driver,locator)
    element.clear()
    element.send_keys(value)

def upload_file(driver,locator,path):
    driver.find_element_by_xpath(locator).send_keys(path)


def explicit_wait_multiple_element_present(driver,locator):
    wait = WebDriverWait(driver,10)
    element = wait.until(EC.presence_of_all_elements_located((By.XPATH,locator)))
    return element

def fluent_wait_element_present(driver,locator):
    wait = WebDriverWait(driver,20,0.5,ignored_exceptions=[NoSuchElementException])
    element = wait.until(EC.presence_of_element_located((By.XPATH,locator)))
    return element


def handle_dropdown(driver,drop_down_xpath,drop_option_xpath,value):
    drop = explicit_wait_present(driver,drop_down_xpath)
    driver.execute_script("arguments[0].click()",drop)
    options = explicit_wait_multiple_element_present(driver,drop_option_xpath)
    for option in options:
        if (option.text).lower() == value.lower():
            driver.execute_script("arguments[0].click()",option)

def js_session_click(driver,session):
    driver.execute_script("arguments[0].click()",session)        

def get_element(driver,locator):
    ele = driver.find_element_by_xpath(locator)
    return ele

def check_loader(driver):
    wait = WebDriverWait(driver,10)
    wait.until_not(EC.presence_of_element_located((By.XPATH,"//*[text()[contains(.,'Please Wait')]]")))