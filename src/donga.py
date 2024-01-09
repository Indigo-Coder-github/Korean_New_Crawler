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
    
    def dynamic_crawl(self, url: str | list) -> list:
        """
        Return News Text Using Selenium.
        The url must be started with "https://www.donga.com/"

        Args:
            url (str | list):
                When 'url=str', it will only crawl given url.
                When 'url=list', it will crawl with iterating url list.

        Returns:
            list: Return article texts.
        """        
        
        if type(url) == str:
            return [self._dynamic_crawl(url)]
        elif type(url) == list:
            return [self._dynamic_crawl(url_str) for url_str in url]
        else: raise TypeError("You must give url string or list type.")
    
    def _dynamic_crawl(self, url: str) -> str:
        assert "https://www.donga.com/" in url, "Given url does not seem to be from donga.com"
        file_dir = Path("/donga/{}.html".format(url[22:]))
        
        #set chrome option
        options = webdriver.ChromeOptions()
        options.add_argument('Chrome/117.0.0.0')
        options.add_argument("headless")
        
        #sleep
        if type(self.delay_time) == float: sleep(self.delay_time)
        elif type(self.delay_time) == tuple: sleep(float(randint(self.delay_time[0], self.delay_time[1])))
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
                    article += (driver.find_element(By.XPATH, '//*[@id="article_txt"]/text()[{}]'.format(line)).text + "\n")
                    line += 1
                except: break
            driver.quit()
            
            return article
    
    def static_crawl(self, url: str | list) -> list:
        
        """
        Return News Text Using BeautifulSoup.
        The url must be started with "https://www.donga.com/"
        
        Args:
            url (str | list):
                When 'url=str', it will only crawl given url.
                When 'url=list', it will crawl with iterating url list.

        Returns:
            list: Return article texts.
        """

        if type(url) == str:
            return [self._static_crawl(url)]
        elif type(url) == list:
            return [self._static_crawl(url_str) for url_str in url]
        else: raise TypeError("You must give url string or list type.")
            
    def _static_crawl(self, url: str) -> str:      
        assert "https://www.donga.com/" in url, "Given url does not seem to be from donga.com"
        file_dir = Path("/donga/{}.html".format(url[22:]))
        
        #sleep
        if type(self.delay_time) == float: sleep(self.delay_time)
        elif type(self.delay_time) == tuple: sleep(float(randint(self.delay_time[0], self.delay_time[1])))
        elif self.delay_time == None: pass
        else: raise TypeError("You must give delay_time float or tuple type.")
        
        if file_dir.is_file() and self.saving_html:
            #call file
            with open(file_dir.name, "r", encoding="UTF-8") as f:
                html_file = f.read()
                parsed_html = self._parse_html(html_file)
                return super().clean_text(parsed_html)
        else:
            #call url
            req = get(url, verify=False)
            if self.saving_html:
                with open(file_dir.name, "w", encoding="UTF-8") as f:
                    f.write(req.text)
            return self._parse_html(req.text)
    
    def _parse_html(self, html: str) -> str:
        soup = bs(html, "lxml")
        text_list = [i.text for i in soup.find("div", {"id":"article_txt"}).find_all("div")]
        
        return super().clean_text(text_list)