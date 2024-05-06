from pathlib import Path
from random import randint
from time import sleep

from bs4 import BeautifulSoup as bs
from requests import get
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from news import News


class Munhwa(News):
    
    def __init__(self, delay_time=None, saving_html=False):
        super().__init__(delay_time, saving_html)
    
    def _dynamic_crawl(self, url: str) -> str:
        assert "https://www.munhwa.com/news/view.html?" in url, "Given url does not seem to be from munhwa.com."
        file_dir = Path("/munhwa/{}.html".format(url[len("https://www.munhwa.com/news/view.html?"):]))
        
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
                    
            #crawl article
            article = str()
            try:
                article = driver.find_element(By.XPATH, '//*[@id="News_content"]').text
                driver.quit()
            except: driver.quit()
            
            return article
    
    def _static_crawl(self, url: str) -> str:
        assert url.startswith("https://www.munhwa.com/news/view.html?"), "Given url does not seem to be from munhwa.com."
        file_dir = Path("/munhwa/{}.html".format(url[len("https://www.munhwa.com/news/view.html?"):]))
        
        #sleep
        if isinstance(self.delay_time, float): sleep(self.delay_time)
        elif isinstance(self.delay_time, tuple): sleep(float(randint(self.delay_time[0], self.delay_time[1])))
        elif self.delay_time == None: pass
        else: raise TypeError("You must give delay_time float or tuple type.")
        
        if file_dir.is_file() and self.saving_html:
            #call file
            with open(file_dir.name, "br", encoding="UTF-8") as f:
                html_file = f.read()
                return self._parse_html(html_file.decode("euc-kr", "replace"))
        else:
            #call url
            req = get(url, verify=False)
            if self.saving_html:
                with open(file_dir.name, "w", encoding="UTF-8") as f:
                    f.write(req.text)
            return self._parse_html(req.content.decode("euc-kr", "replace"))
 
    def _parse_html(self, html: str) -> str:
        soup = bs(html, "html.parser")
        text_list = [i.text + " " for i in soup.find_all("div", {"id":"News_content"}) if i is not None]
        
        return super().clean_text(text_list)
    
if __name__ == "__main__":
    munhwa_article_url = "https://www.munhwa.com/news/view.html?no=2024041801039910226003"
    munhwa = Munhwa()
    munhwa_dynamic_article = munhwa.dynamic_crawl(munhwa_article_url)
    munhwa_static_article = munhwa.static_crawl(munhwa_article_url)
    print(munhwa_dynamic_article[0])
    print(munhwa_static_article[0])