# Korean_News_Crawler

한국 10대 일간지 크롤링 및 유사어 사전 제공 Python 라이브러리입니다.  
Open Source Project로 기여자, 참여자 상시 모집하고 있습니다. 연락주시면 감사하겠습니다.  
크롤링된 기사에 대해서는 각 언론사에 저작권이 있으며 해당 라이브러리는 이에 대한 법적 문제를 책임지지 않습니다. 또한 사용자는 이 사항을 동의한 것으로 간주합니다.  
  
This is Python library for crawling articles from Korean Top 10 Newspaper sites and providing synonym dictionary.  
We're greeting to join you as contibutors, collaborator. Thanks to give me contact.  
The copyright of articles are belong to original media company. We don't take any legal responsibility using of them. We assume that you have agreed to this.  

# Quick Usage

```python
from korean_news_crawler import chosun

chosun = Chosun()
print(chosun.dynamic_crawl("https://www.chosun.com/..."))

chosun_url_list = list()#Chosun ILbo url list
print(chosun.dynamic_crawl(chosun_url_list))
```

# API
## `class korean_new_crawler.chosun.Chosun(delay_time=None, saving_html=False)`  
It provides crawling Chosun Ilbo.

### Parameters
#### delay_time `float | tuple`
- Optional, Defaults to None.
- When 'delay_time=float', it will crawl sites with delay.
- When 'delay_time=tuple', it will crawl sites with random delay.

#### saving_html `bool`
- Optional, Defaults to False.
- When 'saving_html=False', it always requests url every function calling.
- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.

### Methods
#### `dynamic_crawl(url)`
- Return article text using Selenium.
#### Parameters
##### url `str | list`
- When 'url=str', it will only crawl given url.
- When 'url=list', it will crawl with iterating url list.
#### Return `list`
- Return article list.

#### `static_crawl(url)`
- Return article text using BeautifulSoup.
#### Parameters
##### url `str | list`
- When 'url=str', it will only crawl given url.
- When 'url=list', it will crawl with iterating url list.
#### Return `list`
- Return article list.

# Contibutors
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href=https://github.com/Indigo-Coder-github>
          <img src="https://avatars.githubusercontent.com/u/49811400?v=4" width="100px;" alt="Indigo_Coder"/><br>
          <sub>
            <b> Indigo_Coder </b>
          </sub>
        </a><br>
      </td>
    </tr>
