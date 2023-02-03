#API for news: https://newsapi.org/
from src.adapter.get_news_list_by_name.news_fetcher.news_fetcher import NewsFetcher 
from src.use_cases.proccess_get_stock_info.proccess_get_stock_info import ProccessCreateStock

from src.adapter.get_news_list_by_name.news_fetcher_interface import NewsFetcherInterface

adapter = NewsFetcher()
test = ProccessCreateStock(news_fetcher=adapter)
test1 = test.execute("apple")
print(test1.current_price)
print(test1.market_cap)
print(test1.news_list)
print(test1.price_variation)
print(test1.stock_name)
print(test1.ticker)

# fetch = NewsFetcher()
# fetch = fetch.create_news_list("Apple")[0].get_news()
# print(fetch)

