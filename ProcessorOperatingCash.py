import requests
import pandas as pd
import json


class OperatingCash:

    def Processor(self, stock_ticker, df):
        co_value_investing_data = df
        response = requests.get(f"https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/{stock_ticker}")
        print(response.status_code)
        for _ in response.json()['financials']:
            print(f"{stock_ticker} had Operating Cash of : {_['Operating Cash Flow']} on : {_['date']}")

        text = json.dumps(response.json()['financials'], sort_keys = True, indent = 4)

        json_df = pd.read_json(text)

        json_df = json_df[['date', 'Operating Cash Flow']]
        json_df.rename(columns = {'date': 'DATE', 'Operating Cash Flow': 'OPERATING_CASH_FLOW'}, inplace = True)
        json_df['STOCK_TICKER'] = stock_ticker
        co_value_investing_data["OPERATING_CASH_FLOW"] = json_df["OPERATING_CASH_FLOW"].iloc[1]
        return json_df, co_value_investing_data

