#API for news: https://newsapi.org/
from fastapi import FastAPI
from src.adapters.get_news_list_by_name.news_fetcher.news_fetcher import NewsFetcher 
from src.use_cases.proccess_get_stock_info.proccess_get_stock_info import ProccessCreateStock
from src.adapters.web_server.fastapi.router import api_router

from src.adapters.get_news_list_by_name.news_fetcher_interface import NewsFetcherInterface

app = FastAPI(title="Stocks API", description="API for stocks", version="1.0.0")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=80,
        log_level="info",
        reload=True,
    )
    
# adapters = NewsFetcher()
# test = ProccessCreateStock(news_fetcher=adapters)
# test1 = test.execute("apple")
# print(test1.current_price)
# print(test1.market_cap)
# print((test1.news_list))
# print(test1.price_variation)
# print(test1.stock_name)
# print(test1.ticker)