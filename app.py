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
    current_time = time.time()
    cached_data = cache.get('data')

    # Check if cached data is available and not expired
    if cached_data and current_time - cached_data['time'] < cache_duration:
        data = cached_data['data']
    else:
        url = "https://crypto-arbitrage-scanner1.p.rapidapi.com/arbitrage/"
        headers = {
            "X-RapidAPI-Key": "your-api-key",
            "X-RapidAPI-Host": "crypto-arbitrage-scanner1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        cache['data'] = {'data': data, 'time': current_time}

    start = (page - 1) * page_size
    end = start + page_size
    return data[start:end]
