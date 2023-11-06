from re import sub

from bs4 import BeautifulSoup as bs
from requests import get

from news import News


class Munhwa(News):
    
    def __init__(self, delay_time = 5):
        pass
    
    def dynamic_crawl(self, URL: str) -> str:
        pass
    
    def static_crawl(self, URL: str) -> str:
        request = get(URL, verify=False)
        soup = bs(request.content.decode("euc-kr", "replace"), "html.parser")
        
        fragment_list = soup.find_all("div", {"id":"News_content"})
        if fragment_list is not None:
            for fragment in fragment_list:
                if fragment.text != None: article += (fragment.text + " ")
                else: continue
                
        article = sub(r'[^가-힣a-zA-Z0-9\s\.\(\)\"\']', "", article)
        article = article.replace("\n", " ")
        article = article.replace("\t", " ")
        article = " ".join(article.split())
        
        return article