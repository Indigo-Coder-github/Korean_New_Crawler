class News():
    
    def __init__(self, delay_time=None, saving_html=False):
        """
        Args:
            delay_time (float or tuple, optional): Defaults to None.
                When 'delay_time=float', it will crawl sites with delay.
                When 'delay_time=tuple', it will crawl sites with random delay.
            
            saving_html (bool, optional): Defaults to False.
                When 'saving_html=False', it always requests url every function calling.
                When 'saving_html=True', It will save requested html only first time.
                After that, it calls saved html. This will help to alleviate server load.
        """        
        self.delay_time = delay_time
        self.saving_html = saving_html
    
    def dynamic_crawl(self, url: str | list) -> list:
        """
        Return News Text Using Selenium.
        
        Args:
            url (str | list):
                When 'url=str', it will only crawl given url.
                When 'url=list', it will crawl with iterating url list.

        Returns:
            list: Return article texts.
        """        
        pass
    
    def static_crawl(self, url: str | list) -> list:
        """
        Return News Text Using BeautifulSoup.
        
        Args:
            url (str | list):
                When 'url=str', it will only crawl given url.
                When 'url=list', it will crawl with iterating url list.

        Returns:
            list: Return article texts.
        """             
        pass