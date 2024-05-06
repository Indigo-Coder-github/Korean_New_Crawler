from pathlib import Path
from random import randint
from time import sleep

from bs4 import BeautifulSoup as bs
from requests import get
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from news import News


class Seoul(News):
    
    def __init__(self, delay_time=None, saving_html=False):
        super().__init__(delay_time, saving_html)
    
    def _dynamic_crawl(self, url: str) -> str:
        assert url.startswith("https://www.seoul.co.kr/news"), "Given url does not seem to be from seoul.co.kr"
        file_dir = Path("/seoul/{}.html".format(url[len("https://www.seoul.co.kr/news"):]))
        
        #set chrome option
        options = webdriver.ChromeOptions()
        options.add_argument('Chrome/123.0.6312.122')
        options.add_argument('log-level=3')
        options.add_argument("headless")
        
        #sleep
        if isinstance(self.delay_time, float): sleep(self.delay_time)
        elif isinstance(self.delay_time, tuple): sleep(float(randint(self.delay_time[0], self.delay_time[1])))
        elif self.delay_time == None: pass
        else: raise TypeError("You must give delay_time float or tuple type.")
        
        if file_dir.is_file() and self.saving_html:
            #call file
            with open(file_dir.name, "r", encoding="UTF-8") as f:
                html_file = f.read()
                return self._parse_html(html_file)
        else:
            # call url
            driver = Chrome(options=options)
            driver.get(url)
            if self.saving_html:
                with open(file_dir.name, "w", encoding="UTF-8") as f:
                    f.write(driver.page_source)
                    
            #crawl article
            article = str()
            try:
                article = driver.find_element(By.XPATH, '//*[@id="articleContent"]/div').text
                driver.quit()
            except: driver.quit()
            
            return article
    
    def static_crawl(self, url: str | list[str]) -> list[str]:
        raise Exception("This media blocks bot, so we are trying to find the way.")
    
    def _static_crawl(self, url: str) -> str:
        return super()._static_crawl(url)
    
    def _parse_html(self, html: str) -> str:
        soup = bs(html, "lxml")
        text_list = [i + "\n" for i in soup.find_all("div", "viewContent body18 color700")]
        
        return super().clean_text(text_list)
    
if __name__ == "__main__":
    seoul_article_url = "https://www.seoul.co.kr/news/economy/industry/2024/05/06/20240506002002"
    seoul = Seoul()
    seoul_dynamic_article = seoul.dynamic_crawl(seoul_article_url)
    #seoul_static_article = seoul.static_crawl(seoul_article_url)
    print(seoul_dynamic_article[0])
    #print(seoul_static_article[0])