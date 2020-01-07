import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import settings
from  SQL_CLASS import Sql
import requests
from ProcessorStockPrice import StockPrice
from ProcessorNetIncome import NetIncome
from ProcessorOperatingCash import OperatingCash

__app_name__ = 'EVesting_Main'

# root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# stream handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
root_logger.addHandler(stream_handler)

# file handler
if not os.path.exists(settings.DIRECTORY_LOGS):
    os.makedirs(settings.DIRECTORY_LOGS)
logfile = '{}/{}.log'.format(settings.DIRECTORY_LOGS, __app_name__)
fileHandler = TimedRotatingFileHandler(logfile, when='midnight', backupCount=7)
fileHandler.setFormatter(formatter)
root_logger.addHandler(fileHandler)

# local logger
logger = logging.getLogger(__app_name__)

class Evesting:

    def __init__(self):

        sqlite_connection_dict = {

            'sqlite_Financials_table': "Financials",
            'sqlite_Net_Income_table': "Net_Income",
            'sqlite_Operating_Cash_table': 'Operating_Cash'

        }

        sqal_engine = Sql.create_sqlite_engine(self)
        query = '''select * from Financials'''
        fin_data = Sql.sqlite_read(self, query, sqal_engine, sqlite_connection_dict)
        print(fin_data.head())




        print("What stock ticker would you like to know about ? : ")

        stock_ticker = input()
        StockPrice(stock_ticker)


        logger.info('Retreiving Net Income...')
        ni_df = NetIncome.processor(self, stock_ticker)
        logger.info('Writing Net Income to sqlite...')
        Sql.sqlite_df_insert(self, sqal_engine, sqlite_connection_dict['sqlite_Net_Income_table'], ni_df)


        logger.info('Retreiving Operating Cash...')
        oc_df = OperatingCash.processor(self, stock_ticker)
        logger.info('Writing Operating Cash to sqlite...')
        Sql.sqlite_df_insert(self, sqal_engine, sqlite_connection_dict['sqlite_Operating_Cash_table'], oc_df)






Evesting()
