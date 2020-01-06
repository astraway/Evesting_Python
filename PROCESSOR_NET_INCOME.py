import requests
import pandas as pd
import json

class NET_INCOME:

    # def __init__(self, stock_ticker):
    #     self.stock_ticker = stock_ticker
    #
    #     response = requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{self.stock_ticker}")
    #     print(response.status_code)
    #     for _ in response.json()['financials']:
    #         print(f"{stock_ticker} had a NET_INCOME of : {_['Net Income']} on : {_['date']}")
    #
    #     text = json.dumps(response.json()['financials'], sort_keys = True, indent = 4)
    #
    #     json_df = pd.read_json(text)
    #
    #     json_df = json_df[['date', 'Net Income']]
    #     json_df.rename(columns = {'date': 'DATE', 'Net Income': 'NET_INCOME'}, inplace = True)
    #     json_df['STOCK_TICKER'] = self.stock_ticker

        # return json_df
    @staticmethod
    def processor(self, stock_ticker):
        self.stock_ticker = stock_ticker

        response = requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{self.stock_ticker}")
        print(response.status_code)
        for _ in response.json()['financials']:
            print(f"{stock_ticker} had a NET_INCOME of : {_['Net Income']} on : {_['date']}")

        text = json.dumps(response.json()['financials'], sort_keys = True, indent = 4)

        json_df = pd.read_json(text)

        json_df = json_df[['date', 'Net Income']]
        json_df.rename(columns = {'date': 'DATE', 'Net Income': 'NET_INCOME'}, inplace = True)
        json_df['STOCK_TICKER'] = self.stock_ticker

        return json_df

