from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import time

from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

cache = {}
cache_duration = 60  # cache duration in seconds

class Item(BaseModel):
    item_id: int


class ArbitrageData(BaseModel):
    coin: str
    buyAt: str
    buyPrice: float
    sellAt: str
    sellPrice: float
    profit: float

@app.get("/get-arbitrage-data")
async def get_arbitrage_data(page: int = Query(1, alias="page"), page_size: int = Query(10, alias="page_size")):
    url = "https://crypto-arbitrage-scanner1.p.rapidapi.com/arbitrage/"
    headers = {
        "X-RapidAPI-Key": "e425c2f704mshad63aedb69abd7bp1d6e6ejsn36df2e9115d1",
        "X-RapidAPI-Host": "crypto-arbitrage-scanner1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    print(f'fuck {data}')

    start = (page - 1) * page_size
    end = start + page_size

    print(f'start: {start} end: {end}')

    # Ensure slicing is done within the bounds of the list
    paginated_data = data[max(0, start):min(end, len(data))]
    
    return paginated_data
