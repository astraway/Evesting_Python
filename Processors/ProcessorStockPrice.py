import requests

from .ABC_Processor import ProcessorABC

class StockPrice(ProcessorABC):

    def processor(self,stock_ticker, df):

        response = requests.get(f"https://financialmodelingprep.com/api/v3/stock/real-time-price/{stock_ticker}")
        #print(response.status_code)
        print(f"{stock_ticker} has a current Stock price of : {response.json()['price']}")

