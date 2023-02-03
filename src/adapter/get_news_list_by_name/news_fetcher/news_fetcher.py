from src.adapter.get_news_list_by_name.news_fetcher_interface import NewsFetcherInterface
from src.entities.Stock import News 
from typing import List, Dict
import requests

apiKey = "ad95902286414996b0cbe1e22fce0859"

class NewsFetcher(NewsFetcherInterface):

    def return_news_by_ticker(self, ticker: str) -> List:
        _raw_news: List = []
        try:
            endpoint = "https://newsapi.org/v2/top-headlines"
            params = {
                "q": ticker,
                "apiKey": apiKey
            }
            r = requests.get(endpoint, params=params)
            
            _raw_news = r.json()["articles"]
        except Exception as e:
            raise Exception (e)
        finally:
            return _raw_news
        
    def create_news_list(self, ticker) -> List[News]:
        _raw_news = self.return_news_by_ticker(ticker)
        _news: List[News] = []
        
        for item in _raw_news:
            itemObject = News()

            itemObject.title = item["title"]
            itemObject.description = item["description"]
            itemObject.source = item["source"]["name"]
            itemObject.url = item["url"]

            _news.append(itemObject.get_news())

        return _news
