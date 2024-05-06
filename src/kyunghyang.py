from pathlib import Path
from random import randint
from time import sleep

from bs4 import BeautifulSoup as bs
from requests import get
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from news import News


class Kyunghyang(News):
    
    def __init__(self, delay_time=None, saving_html=False):
        super().__init__(delay_time, saving_html)
        
    def _dynamic_crawl(self, url: str) -> str:
        assert url.startswith("https://www.khan.co.kr/"), "Given url does not seem to be from khan.co.kr."
        file_dir = Path("/kyunghyang/{}.html".format(url[len("https://www.khan.co.kr/"):]))
        
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
                with open(file_dir, "w", encoding="UTF-8") as f:
                    f.write(driver.page_source)
                    
            #crawl line by line
            line = 1
            article = str()
            while True:
                try:
                    article += (driver.find_element(By.XPATH, '//*[@id="articleBody"]/p[{}]'.format(line)).text + "\n")
                    line += 1
                except: break
            driver.quit()
            
            return article
    
    def static_crawl(self, url: str | list[str]) -> list[str]:
        raise Exception("This site blocks bot. We are trying to find the way.")
    
    def _parse_html(self, html: str) -> str:
        soup = bs(html, "lxml")
        text_list = [i + "\n" for i in soup.find_all("p", "content_text text-l")]
        
        return super().clean_text(text_list)
    
if __name__ == "__main__":
    kyunghyang_article_url = "https://www.khan.co.kr/national/incident/article/202405061426001"
    kyunghyang = Kyunghyang()
    kyunghyang_dynamic_article = kyunghyang.dynamic_crawl(kyunghyang_article_url)
    #kyunghyang_static_article = kyunghyang.static_crawl(kyunghyang_article_url)
    print(kyunghyang_dynamic_article[0])
    #print(kyunghyang_static_article[0])