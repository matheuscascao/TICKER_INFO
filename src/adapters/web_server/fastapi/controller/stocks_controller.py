from fastapi import APIRouter
from src.use_cases.proccess_get_asset_info.proccess_get_asset_info import ProccessCreateAsset
from src.adapters.News.news_fetcher.news_fetcher import NewsFetcher 
from src.adapters.News.news_fetcher_interface import NewsFetcherInterface

news_fetcher_adapter = NewsFetcher()
router = APIRouter()

@router.get("/asset_info/{asset_name}")
def get_asset_info(asset_name: str):
    asset_info = ProccessCreateAsset(news_fetcher=news_fetcher_adapter)
    asset_info = asset_info.execute(asset_name)
    return asset_info
