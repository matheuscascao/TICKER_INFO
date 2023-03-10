from typing import Dict, List
from src.entities.Asset import News

class StockInfoDtoInput:
    asset_name: str

class StockInfoDtoOutput:
    identifier: str
    asset_name: str
    daily_price_variation: float
    weekly_price_variation: float
    market_cap: float
    current_price: float
    news_list: List[News] = None

