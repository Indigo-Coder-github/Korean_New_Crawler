from pathlib import Path
from random import randint
from time import sleep

from bs4 import BeautifulSoup as bs
from requests import get
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from news import News


class Donga(News):
    
    def __init__(self, delay_time=None, saving_html=False):
        super().__init__(delay_time, saving_html)
    
    def _dynamic_crawl(self, url: str) -> str:
        assert url.startswith("https://www.donga.com/"), "Given url does not seem to be from donga.com"
        file_dir = Path("/donga/{}.html".format(url[len("https://www.donga.com/"):]))
        
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
            #call url
            driver = Chrome(options=options)
            driver.get(url)
            if self.saving_html:
                with open(file_dir.name, "w", encoding="UTF-8") as f:
                    f.write(driver.page_source)
                    
            #crawl line by line
            article = str()
            try:
                article += (driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div/div[1]/section[1]').text + "\n")
            except: pass
            driver.quit()
            
            return article
            
    def _static_crawl(self, url: str) -> str:      
        assert "https://www.donga.com/" in url, "Given url does not seem to be from donga.com"
        file_dir = Path("/donga/{}.html".format(url[22:]))
        
        #sleep
        if isinstance(self.delay_time, float): sleep(self.delay_time)
        elif isinstance(self.delay_time, tuple): sleep(float(randint(self.delay_time[0], self.delay_time[1])))
        elif self.delay_time == None: pass
        else: raise TypeError("You must give delay_time float or tuple type.")
        
        if file_dir.is_file() and self.saving_html:
            #call file
            with open(file_dir.name, "r", encoding="UTF-8") as f:
                html_file = f.read()
                parsed_html = self._parse_html(html_file)
                return parsed_html
        else:
            #call url
            req = get(url, verify=False)
            if self.saving_html:
                with open(file_dir.name, "w", encoding="UTF-8") as f:
                    f.write(req.text)
            return self._parse_html(req.text)
    
    def _parse_html(self, html: str) -> str:
        soup = bs(html, "lxml")
        text_list = [i.text for i in soup.find("section", "news_view")]
        
        return super().clean_text(text_list)
    
if __name__ == "__main__":
    donga_article_url = donga_article_url = "https://www.donga.com/news/Politics/article/all/20240418/124537818/2"
    donga = Donga()
    donga_dynamic_article = donga.dynamic_crawl(donga_article_url)
    donga_static_article = donga.static_crawl(donga_article_url)
    print(donga_dynamic_article[0])
    print(donga_static_article[0])