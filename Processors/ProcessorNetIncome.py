import requests
import pandas as pd
import json
from .ABC_Processor import ProcessorABC
from helpers import  growth

class NetIncome(ProcessorABC):



    def processor(self, stock_ticker, df ):
        processor_name = 'Net Income'
        co_value_investing_data = df
        response = requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{stock_ticker}")
        print(response.status_code)
        for _ in response.json()['financials']:
            print(f"{stock_ticker} had a NET_INCOME of : {_['Net Income']} on : {_['date']}")

        text = json.dumps(response.json()['financials'], sort_keys = True, indent = 4)

        json_df = pd.read_json(text)

        json_df = json_df[['date', 'Net Income']]
        json_df.rename(columns = {'date': 'DATE', 'Net Income': 'NET_INCOME'}, inplace = True)

        ni_growth = growth(json_df['NET_INCOME'],processor_name)

        co_value_investing_data["NET_INCOME"] = ni_growth #json_df["NET_INCOME"].head(1)


        return  co_value_investing_data





