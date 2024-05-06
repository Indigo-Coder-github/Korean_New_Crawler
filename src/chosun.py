from pathlib import Path
from random import randint
from time import sleep

from bs4 import BeautifulSoup as bs
from requests import get
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from news import News


class Chosun(News):
    
    def __init__(self, delay_time=None, saving_html=False):
        super().__init__(delay_time, saving_html)
        
    def _dynamic_crawl(self, url: str) -> str:
        assert url.startswith("https://www.chosun.com/"), "Given url does not seem to be from chosun.com."
        file_dir = Path("/chosun/{}.html".format(url[len("https://www.chosun.com/"):]))
        
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
                    article += (driver.find_element(By.XPATH, f'//*[@id="fusion-app"]/div[1]/div[2]/div/section/article/section/p[{line}]').text + "\n")
                    line += 1
                except: break
            driver.quit()
            
        return article
    
    def static_crawl(self, url: str | list[str]) -> list:
        raise Exception("This site blocks bot. We are trying to find the way.")
    
    def _parse_html(self, html: str) -> str:
        soup = bs(html, "lxml")
        article = str([i + "\n" for i in soup.find_all("p", "article-body__content article-body__content-text | text--black text font--size-sm-18 font--size-md-18 font--primary")])
        return super().clean_text(article)
    
if __name__ == "__main__":
    chosun_article_url = "https://www.chosun.com/international/international_general/2024/04/18/DGJJ2JKV3VEHZNVRVGU3OTDSZU/"
    chosun = Chosun()
    chosun_dynamic_article = chosun.dynamic_crawl(chosun_article_url)
    #chosun_static_article = chosun.static_crawl(chosun_article_url)
    print(chosun_dynamic_article[0])
    #print(chosun_static_article[0])