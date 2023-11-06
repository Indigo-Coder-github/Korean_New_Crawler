from time import sleep

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from news import News


class Chosun(News):
    
    def __init__(self, delay_time = 5):
        self.delay_time = delay_time
    
    def dynamic_crawl(self, URL: str) -> str:
        article = str()
        
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('Chrome/117.0.0.0')
            options.add_argument("headless")
            driver = Chrome(options=options)
            sleep(self.delay_time)
            driver.get(URL)
        except:
            options = webdriver.ChromeOptions()
            options.add_argument('Chrome/117.0.0.0')
            options.add_argument("headless")
            driver = Chrome(options=options)
            sleep(self.delay_time)
            driver.get(URL)
        finally:
            line = 1
            while True:
                try:
                    article += (driver.find_element(By.XPATH, '//*[@id="fusion-app"]/div[1]/div[2]/div/section/article/section/p[{}]'.format(line)).text + "\n")
                    line += 1
                except: break
            driver.quit()
            return article
    
    def static_crawl(self, URL: str) -> str:
        pass