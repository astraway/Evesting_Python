import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import settings
from  SQL_CLASS import SQL
import requests
from PROCESSOR_STOCK_PRICE import STOCK_PRICE
from PROCESSOR_NET_INCOME import NET_INCOME
from PROCESSOR_OPERATING_CASH import OPERATING_CASH

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

        sqal_engine = SQL.create_sqlite_engine(self)
        query = '''select * from Financials'''
        fin_data = SQL.sqlite_read(self, query, sqal_engine, sqlite_connection_dict)
        print(fin_data.head())




        print("What stock ticker would you like to know about ? : ")

        stock_ticker = input()
        STOCK_PRICE(stock_ticker)


        logger.info('Retreiving Net Income...')
        ni_df = NET_INCOME.processor(self, stock_ticker)
        logger.info('Writing Net Income to sqlite...')
        SQL.sqlite_df_insert(self, sqal_engine, sqlite_connection_dict['sqlite_Net_Income_table'] , ni_df)


        logger.info('Retreiving Operating Cash...')
        oc_df = OPERATING_CASH.processor(self, stock_ticker)
        logger.info('Writing Operating Cash to sqlite...')
        SQL.sqlite_df_insert(self, sqal_engine, sqlite_connection_dict['sqlite_Operating_Cash_table'] , oc_df)






Evesting()
