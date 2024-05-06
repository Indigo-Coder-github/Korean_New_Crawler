from pathlib import Path
from random import randint
from time import sleep

from bs4 import BeautifulSoup as bs
from requests import get
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from news import News


class Joongang(News):
    
    def __init__(self, delay_time=None, saving_html=False):
        super().__init__(delay_time, saving_html)
    
    def _dynamic_crawl(self, url: str) -> str:
        assert url.startswith("https://www.joongang.co.kr/article/"), "Given url does not seem to be from joongang.co.kr."
        file_dir = Path("/joongang/{}.html".format(url[len("https://www.joongang.co.kr/article/"):]))
        
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
            line = 1
            article = str()
            while True:
                try:
                    article += (driver.find_element(By.XPATH, f'//*[@id="article_body"]/p[{line}]').text + "\n")
                    line += 1
                except: break
            driver.quit()
            
        return article
        
    def _static_crawl(self, url: str) -> str:
        assert url.startswith("https://www.joongang.co.kr/article/"), "Given url does not seem to be from joongang.co.kr"
        file_dir = Path("/joongang/{}.html".format(url[len("https://www.joongang.co.kr/article/"):]))
        
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
        soup = bs(html, "html.parser")
        text_list = [i.text + " " for i in soup.find("div", {"id":"article_body"}).findChildren("p", recursive=False) if i is not None]
        
        return super().clean_text(text_list)
    
if __name__ == "__main__":
    joongang_article_url = "https://www.joongang.co.kr/article/25243398"
    joongang = Joongang()
    joongang_dynamic_article = joongang.dynamic_crawl(joongang_article_url)
    joongang_static_article = joongang.static_crawl(joongang_article_url)
    print(joongang_dynamic_article[0])
    print(joongang_static_article[0])