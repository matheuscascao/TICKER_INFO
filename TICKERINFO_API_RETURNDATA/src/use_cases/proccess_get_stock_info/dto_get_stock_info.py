from typing import Dict, List
from TICKERINFO_API_RETURNDATA.src.entities.News import News

class StockInfoDtoInput:
    stock_name: str

class StockInfoDtoOutput:
    ticker: str
    stock_name: str
    price_variation: float
    market_cap: float
    current_price: float
    news_list: List[News] = None

