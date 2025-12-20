from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class YoutubePage(BasePage):

    search_box = (By.NAME, 'search_query')
    search_button = (By.XPATH, "//button[@aria-label='Search']")
    video_results = (By.XPATH, "//a[@id='video-title']")

    def open(self):
        self.driver.get("https://www.youtube.com")

    def search(self,text):
        self.driver.find_element(*self.search_box).send_keys(text)
        self.driver.find_element(*self.search_button).click()

    def wait_for_search(self):
        self.wait.until(EC.url_contains("results"))

    def get_title(self):
        return self.driver.title

    def get_youtube_trailer(self):
        results = self.wait.until(EC.presence_of_all_elements_located(self.video_results))
        for result in results:
            title = result.text.strip().lower()
            if "trailer" in title:
                print("clicking trailer", result.text)
                result.click()
                break
        print(self.driver.current_url)
        assert "trailer" in title
        assert "watch" in self.driver.current_url




