from fastapi import APIRouter
from src.use_cases.proccess_get_stock_info.proccess_get_stock_info import ProccessCreateStock
from src.adapters.get_news_list_by_name.news_fetcher.news_fetcher import NewsFetcher 
from src.adapters.get_news_list_by_name.news_fetcher_interface import NewsFetcherInterface

news_fetcher_adapter = NewsFetcher()
router = APIRouter()

@router.get("/stock_info/{stock_name}")
def get_stock_info(stock_name: str):
    stock_info = ProccessCreateStock(news_fetcher=news_fetcher_adapter)
    stock_info = stock_info.execute(stock_name)
    return stock_info
