import requests


class StockPrice:

    def __init__(self, stock_ticker):
        self.stock_ticker = stock_ticker

        response = requests.get(f"https://financialmodelingprep.com/api/v3/stock/real-time-price/{self.stock_ticker}")
        #print(response.status_code)
        print(f"{stock_ticker} has a current Stock price of : {response.json()['price']}")

