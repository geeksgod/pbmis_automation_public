import pytest
import configparser
import os
import time
from selenium import webdriver


@pytest.fixture(scope="session")
def setup(browser):
    print("settingup")

    #Changing the browser as per the users request
    if browser == 'chrome':
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        driver = webdriver.Chrome(executable_path="./Drivers/chromedriver",options=op)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="./Drivers/geckodriver")
        driver.set_window_position(0,0)        
    else:
        driver = webdriver.Chrome(executable_path="./Drivers/chromedriver")
        driver.set_window_position(0,0)
    
    yield driver

    time.sleep(2)
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
   


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'PBMIS'
    config._metadata['Module Name'] = 'PBMIS Test'
    config._metadata['Tester'] = 'Bipin'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
