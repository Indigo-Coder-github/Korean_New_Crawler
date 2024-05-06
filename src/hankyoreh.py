from pathlib import Path
from random import randint
from time import sleep

from bs4 import BeautifulSoup as bs
from requests import get
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from news import News


class Hankyoreh(News):
    
    def __init__(self, delay_time=None, saving_html=False):
        super().__init__(delay_time, saving_html)
    
    def _dynamic_crawl(self, url: str) -> str:
        assert url.startswith("https://www.hani.co.kr/arti/"), "Given url does not seem to be from hani.co.kr"
        file_dir = Path("/hani/{}.html".format(url[len("https://www.hani.co.kr/arti/"):]))
        
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
                    article += (driver.find_element(By.XPATH, '//*[@id="renewal2023"]/div[3]/p[{}]'.format(line)).text + "\n")
                    line += 1
                except: break
            driver.quit()
            
            return article
    
    def static_crawl(self, url: str | list[str]) -> list:
        raise Exception("This site blocks bot. We are trying to find the way.")
    
    def _static_crawl(self, url: str) -> str:
        assert url.startswith("https://www.hani.co.kr/arti/"), "Given url does not seem to be from hani.co.kr"
        file_dir = Path("/hani/{}.html".format(url[len("https://www.hani.co.kr/arti/"):]))
        
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
        
        text_list = [i.text + " " for i in soup.select("#renewal2023 > div.article-text > p:nth-child(2)") if i is not None]
        
        return super().clean_text(text_list)
    
if __name__ == "__main__":
    hankyoreh_article_url = "https://www.hani.co.kr/arti/area/capital/1137118.html"
    hankyoreh = Hankyoreh()
    hankyoreh_dynamic_article = hankyoreh.dynamic_crawl(hankyoreh_article_url)
    hankyoreh_static_article = hankyoreh.static_crawl(hankyoreh_article_url)
    print(hankyoreh_dynamic_article[0])
    print(hankyoreh_static_article[0])