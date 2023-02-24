from src.entities.Stock import News, Stock
from src.use_cases.proccess_get_stock_info.dto_get_stock_info import StockInfoDtoInput, StockInfoDtoOutput
from src.adapters.get_news_list_by_name.news_fetcher_interface import NewsFetcherInterface

class ProccessCreateStock():
    def __init__(
        self,
        news_fetcher: NewsFetcherInterface
    ) -> None:
        self.news_fetcher = news_fetcher

    def execute(self, input: StockInfoDtoInput) -> StockInfoDtoOutput:
        news_list = self.news_fetcher.create_news_list(ticker=input)

        output = StockInfoDtoOutput()
        
        output.ticker = input
        output.stock_name="Apple"
        output.price_variation=12.2
        output.market_cap=14.1
        output.current_price=3.1

        if news_list:
            output.news_list = news_list
        
        return output
    
