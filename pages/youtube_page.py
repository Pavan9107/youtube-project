from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class YoutubePage(BasePage):

    search_box = (By.NAME, 'search_query')
    search_button = (By.XPATH, "//button[@aria-label='Search']")

    def open(self):
        self.driver.get("https://www.youtube.com")

    def search(self,text):
        self.driver.find_element(*self.search_box).send_keys(text)
        self.driver.find_element(*self.search_button).click()

    def wait_for_search(self):
        self.wait.until(EC.url_contains("results"))

    def get_title(self):
        return self.driver.title

