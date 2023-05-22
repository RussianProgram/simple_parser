from bs4 import BeautifulSoup

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from utils import save_to_csv
from config import DELAY


class Parser:
    def __init__(
            self, 
            url: str, 
            pages_to_parse: int
            ) -> None:
        self.url = url
        self.pages_to_parse = pages_to_parse

    # Parsing a single news post
    def parse_post(self, post):
        post_title = post.find("h6", class_="typography__StyledTypography-owin6q-0 hjHKEC")
        link = post_title.parent.get('href')
        title = post_title.text
        date = post.find("div", class_="searchstyles__DateWrapper-ci5zlg-24 coTxPZ").text

        return title, link, date

    # Parsing a whole news page
    def parse_page(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        page_data = []

        news = soup.find_all("div", class_="searchstyles__SearchCardWrapper-ci5zlg-21 hZygnS")
        for post in news:
            try:
                post_data = self.parse_post(post)
                if not post_data in page_data:
                    page_data.append(self.parse_post(post))
                    print("Parsed")
            
            except AttributeError:
                print("Not parsed")
                     
        return page_data

    # Start parser
    def start_parser(self, driver: WebDriver):
        parsed_data = []
        
        for i in range(0, self.pages_to_parse + 1):
            url = self.url + f"&i={i}"
            driver.get(url)
            html = driver.page_source
            parsed_data.extend(self.parse_page(html))
          
        save_to_csv(parsed_data)
        