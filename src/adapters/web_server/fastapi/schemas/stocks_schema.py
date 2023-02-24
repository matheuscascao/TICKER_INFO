from pydantic import BaseModel

class StocksEntities(BaseModel):
    stock_name: str
    