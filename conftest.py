from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.driver_manager import Driver_Manager

def pytest_sessionstart(session):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    Driver_Manager.set_driver(driver)

def pytest_sessionfinish(session, exitstatus):
    driver = Driver_Manager.get_driver()
    driver.quit()


#Fixture based
# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from utils.driver_manager import Driver_Manager
#
# @pytest.fixture(scope="session", autouse=True)
# def driver_session():
#
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     Driver_Manager.set_driver(driver)
#
#     yield driver
#
#
#     driver.quit()







