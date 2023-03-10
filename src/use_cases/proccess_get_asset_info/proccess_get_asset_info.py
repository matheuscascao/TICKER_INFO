from src.entities.Asset import News, Asset
from src.use_cases.proccess_get_asset_info.dto_get_asset_info import StockInfoDtoInput, StockInfoDtoOutput
from src.adapters.News.news_fetcher_interface import NewsFetcherInterface

class ProccessCreateAsset():
    def __init__(
        self,
        news_fetcher: NewsFetcherInterface
    ) -> None:
        self.news_fetcher = news_fetcher

    def execute(self, input: StockInfoDtoInput) -> StockInfoDtoOutput:
        news_list = self.news_fetcher.create_news_list(ticker=input)

        output = StockInfoDtoOutput()
        
        output.identifier = input
        output.asset_name="Apple" #TODO
        output.daily_price_variation=12.2 #TODO
        output.weekly_price_variation=12.2 #TODO
        output.market_cap=14.1 #TODO
        output.current_price=3.1 #TODO

        if news_list:
            output.news_list = news_list
        
        return output
    
