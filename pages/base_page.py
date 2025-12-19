from utils.driver_manager import Driver_Manager
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self):
        self.driver = Driver_Manager.get_driver()
        self.wait = WebDriverWait(self.driver, 10)

