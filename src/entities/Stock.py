from typing import Dict, List, Optional

# Classe anêmica
class News():
    title: str
    description: str
    source: str
    url: str

    def get_news(self):
        news_object: Dict = {}
        
        news_object['title'] = self.title
        news_object['description'] = self.description
        news_object['source'] = self.source
        news_object['url'] = self.url

        return news_object

class Stock():
    news_list: List[News] = []
    def __init__(
            self,
            ticker: str,
            stock_name: str,
            price_variation: float,
            market_cap: float,
            current_price: float,
    ) -> None:
        self.ticker = ticker
        self.stock_name = stock_name
        self.price_variation = price_variation
        self._market_cap = market_cap
        self.current_price = current_price

    @property
    def _market_cap(self) -> float:
        #formatting and validation
        return self._market_cap
    
    @_market_cap.setter
    def _market_cap(self, value: float) -> float:
        self._market_cap = value

    @property
    def _market_cap(self):
        #formatting and validation
        return self._market_cap
    
    @_market_cap.setter
    def _market_cap(self, value):
        self._market_cap = value

    def get_stock(self):
        stock_object: Dict = {}
        
        stock_object['ticker'] = self.ticker
        stock_object['stock_name'] = self.stock_name
        stock_object['price_variation'] = self.price_variation
        stock_object['_market_cap'] = self._market_cap
        stock_object['current_price'] = self.current_price
        stock_object['news_list'] = self.news_list

        return stock_object
