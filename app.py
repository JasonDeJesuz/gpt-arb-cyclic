from fastapi import FastAPI
from fastapi.responses import FileResponse

from pydantic import BaseModel
import requests

app = FastAPI()


class Item(BaseModel):
    item_id: int


class ArbitrageData(BaseModel):
    coin: str
    buyAt: str
    buyPrice: float
    sellAt: str
    sellPrice: float
    profit: float

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get('/favicon.ico', include_in_schema=False)
# async def favicon():
#     return FileResponse('favicon.ico')


# @app.get("/item/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# @app.get("/items/")
# async def list_items():
#     return [{"item_id": 1, "name": "Foo"}, {"item_id": 2, "name": "Bar"}]


# @app.post("/items/")
# async def create_item(item: Item):
#     return item

@app.get("/get-arbitrage-data", response_model=List[ArbitrageData])
async def get_arbitrage_data():
    url = "https://crypto-arbitrage-scanner1.p.rapidapi.com/arbitrage/"
    headers = {
        "X-RapidAPI-Key": "e425c2f704mshad63aedb69abd7bp1d6e6ejsn36df2e9115d1",
        "X-RapidAPI-Host": "crypto-arbitrage-scanner1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return response.json()
