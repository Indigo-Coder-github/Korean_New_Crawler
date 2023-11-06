# Korean_News_Crawler

한국 10대 일간지 크롤링 및 유사어 사전 제공 Python 라이브러리입니다. 아직 PyPI에 정식등록되진 않은 beta 버전입니다.  
Open Source Project로 기여자, 참여자 상시 모집하고 있습니다. 연락주시면 감사하겠습니다.  
크롤링된 기사에 대해서는 각 언론사에 저작권이 있으며 해당 라이브러리는 이에 대한 법적 문제를 책임지지 않습니다. 또한 사용자는 이 사항을 동의한 것으로 간주합니다.  
  
This is Python library providing crawling Korean Top 10 Newspaper site and synonym dictionary.  
We're greeting to join you as contibutors, collaborator. Thanks to give me contact.  
The copyright of crawled articles are belong to original media company. We don't take any legal responsibility using of them. We assume that you have agreed to this.  

## Quick Usage

```python
from korean_news_crawler import hankook

hankook = Hankook()
hankook.static_crawl("https://www.hankookilbo.com/~)
```

## API
