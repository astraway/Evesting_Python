from fastapi import FastAPI
from Manual_Main import Evesting
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{stock_ticker}")
def read_item(stock_ticker: str):

    evst = Evesting(stock_ticker)
    json_obj = evst.process_stock()

    #  to access locally http: // localhost: 8000 / items /
    return json_obj