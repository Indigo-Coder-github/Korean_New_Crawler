# Korean_News_Crawler

한국 10대 일간지 크롤링 및 유사어 사전 제공 Python 라이브러리입니다. 아직 PyPI에 정식등록되진 않은 beta 버전입니다.  
Open Source Project로 기여자, 참여자 상시 모집하고 있습니다. 연락주시면 감사하겠습니다.  
  
This is Python library for crawling articles from Korean Top 10 Newspaper sites and providing synonym dictionary.  
The copyright of articles are belong to original media company. We don't take any legal responsibility using of them. We assume that you have agreed to this.  
We're greeting to join you as contibutors, collaborator. Thanks to give me contact.  

## Supported News Sites

- [조선일보(Chosun Ilbo)](https://www.chosun.com/)
- [동아일보(Dong-a Ilbo)](https://www.donga.com/)
- [한국일보(Hankook Ilbo)](https://www.hankookilbo.com/)
- [한겨레(Hankyeoreh)](https://www.hani.co.kr/)
- [중앙일보(JoongAng Ilbo)](https://www.joongang.co.kr/)
- [국민일보(Kukmin Ilbo)](https://www.kmib.co.kr/)
- [경향신문(Kyunghyang Shinmun)](https://www.khan.co.kr/)
- [문화일보(Munhwa Ilbo)](https://www.munhwa.com/)
- [내일신문(Naeil News)](https://www.naeil.com/)
- [세계일보(Segye Ilbo)](https://segye.com/)
- [서울신문(Seoul Shinmun)](https://www.seoul.co.kr/)

## Contibutors

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
  </tbody>
</table>

## Installation

``` 
pip install korean_news_crawler
```

BeautifulSoup, Selenium, Requests are required.

## Quick Usage

```python
from korean_news_crawler import chosun

chosun = Chosun()
print(chosun.dynamic_crawl("https://www.chosun.com/..."))

chosun_url_list = list() #Chosun Ilbo url list
print(chosun.dynamic_crawl(chosun_url_list))
```

## API

1. [`Chosun()`](#korean_news_crawlerchosundelay_timenone-saving_htmlfalse)
2. [`Donga()`](#korean_news_crawlerdongadelay_timenone-saving_htmlfalse)
3. [`Hankook()`](#korean_news_crawlerhankookdelay_timenone-saving_htmlfalse)
4. [`Hankyoreh()`](#korean_news_crawlerhankyorehdelay_timenone-saving_htmlfalse)
5. [`Joongang()`](#korean_news_crawlerjoongangdelay_timenone-saving_htmlfalse)
6. [`Kukmin()`](#korean_news_crawlerkukmindelay_timenone-saving_htmlfalse)
7. [`Kyunghyang()`](#korean_news_crawlerkyunghyangdelay_timenone-saving_htmlfalse)
8. [`Munhwa()`](#korean_news_crawlermunhwadelay_timenone-saving_htmlfalse)
9. [`Naeil()`](#korean_news_crawlernaeildelay_timenone-saving_htmlfalse)
10. [`Segye()`](#korean_news_crawlersegyedelay_timenone-saving_htmlfalse)
11. [`Seoul()`](#korean_news_crawlerseouldelay_timenone-saving_htmlfalse)

### [`korean_news_crawler.Chosun(delay_time=None, saving_html=False)`](#api)

It provides crawling Chosun Ilbo.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Donga(delay_time=None, saving_html=False)`](#api)

It provides crawling Dong-a Ilbo.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Hankook(delay_time=None, saving_html=False)`](#api)

It provides crawling Hankook Ilbo.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Hankyoreh(delay_time=None, saving_html=False)`](#api)

It provides crawling Hankyoreh.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Joongang(delay_time=None, saving_html=False)`](#api)

It provides crawling Joongang Ilbo.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Kukmin(delay_time=None, saving_html=False)`](#api)

It provides crawling Kukmin Ilbo.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Kyunghyang(delay_time=None, saving_html=False)`](#api)

It provides crawling Kyunghyang Shinmun.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Munhwa(delay_time=None, saving_html=False)`](#api)

It provides crawling Munhwa Ilbo.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Naeil(delay_time=None, saving_html=False)`](#api)

It provides crawling Naeil News.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Segye(delay_time=None, saving_html=False)`](#api)

It provides crawling Segye Ilbo.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

### [`korean_news_crawler.Seoul(delay_time=None, saving_html=False)`](#api)

It provides crawling Seoul Shinmun.

#### Parameters

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**|- Optional, Defaults to None.</br>- When 'delay_time=float', it will crawl sites with delay.</br>- When 'delay_time=tuple', it will crawl sites with random delay.|
|**saving_html**|**bool**|- Optional, Defaults to False.</br>- When 'saving_html=False', it always requests url every function calling.</br>- When 'saving_html=True', It will save requested html only first time. After that, it calls saved html. This will help to alleviate server load.|

#### Attributes

|**Attributes**|**Type**|**Description**|
|:-:|:-:|:-|
|**delay_time**|**float or tuple**||
|**saving_html**|**bool**||

#### Methods

|**Methods**|**Description**|
|:-:|:-|
|[dynamic_crawl(url)](#dynamic_crawlurl)|Return article text using Selenium.|
|[static_crawl(url)](#static_crawlurl)|Return article text using BeautifulSoup.|

##### `dynamic_crawl(url)`

- Return article text using Selenium.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|

##### `static_crawl(url)`

- Return article text using BeautifulSoup.

|**Parameters**|**Type**|**Description**|
|:-:|:-:|:-|
|**url**|**str or list**|- When 'url=str', it will only crawl given url.</br>- When 'url=list', it will crawl with iterating url list.|

|**Returns Type**|**Description**|
|:-:|:-|
|**list**|Return article list.|
