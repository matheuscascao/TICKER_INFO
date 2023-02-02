from typing import Dict, List, Optional

# Classe anêmica
class News():
    def __init__(
            self,
            ticker: str,
            title: str,
            content: str,
            source: str,
            url: str
    )  -> None:
        self.ticker = ticker
        self.title = title
        self.content = content
        self.source = source
        self.url = url

    def get_news(self):
        news_object: Dict = {}
        
        news_object['title'] = self.title
        news_object['content'] = self.content
        news_object['source'] = self.source
        news_object['url'] = self.url

        return news_object

class Stock():
    def __init__(
            self,
            ticker: str,
            stock_name: str,
            price_variation: float,
            market_cap: float,
            current_price: float,
            news_list: List[News] = None
    ) -> None:
        self.ticker = ticker
        self.stock_name = stock_name
        self.price_variation = price_variation
        self._market_cap = market_cap
        self.current_price = current_price
        self.news_list = news_list

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
