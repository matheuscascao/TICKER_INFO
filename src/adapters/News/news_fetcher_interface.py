import abc
from typing import List
from src.entities.Asset import News 

class NewsFetcherInterface(metaclass= abc.ABCMeta):
    @abc.abstractclassmethod
    def return_news_by_ticker(self, ticker: str) -> List:
        ...

    @abc.abstractclassmethod
    def create_news_list(self, raw_news: List) -> List[News]:
        ...