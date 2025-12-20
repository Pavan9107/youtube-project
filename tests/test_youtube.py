import pytest

from pages import youtube_page
from pages.youtube_page import YoutubePage
@pytest.mark.smoke
def test_youtube():
    youtube_page = YoutubePage()
    youtube_page.open()
    youtube_page.search("Music")
    print("URL after search:", youtube_page.driver.current_url)

    youtube_page.wait_for_search()
    title_details = youtube_page.get_title()
    print("This is the title details",title_details)

    current_url = youtube_page.driver.current_url
    print("Final URL:", current_url)

    assert "search_query=Music" in current_url


@pytest.mark.regression
def test_youtube_trailer():
    youtube_page1 = YoutubePage()
    youtube_page1.open()
    youtube_page1.search("Rajasaab")
    youtube_page1.get_youtube_trailer()
