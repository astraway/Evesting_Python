import pandas as pd
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import settings
from  SqlConnection import Sql
from processorfactory import ProcessorFactory

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



        column_names = ["STOCK_TICKER", "NET_INCOME", "OPERATING_CASH"]
        co_value_investing_data = pd.DataFrame(columns = column_names)



        sqlite_connection_dict = {

            'sqlite_co_value_investing_data_table' : "value_investing",
            'sqlite_Financials_table': "financials",
            'sqlite_Net_Income_table': "net_income",
            'sqlite_Operating_Cash_table': 'operating_cash'

        }

        factory = ProcessorFactory()

        #sqal_engine = Sql.create_postgres_engine(self)
        sqal_engine = Sql.create_sqlite_engine(self)
        query = '''select * from financials'''
        fin_data = Sql.sqlite_read(self, query, sqal_engine, sqlite_connection_dict)
        print(fin_data.head())




        print("What stock ticker would you like to know about ? : ")


        #takes user input for stock tick...
        stock_ticker = input()
        co_value_investing_data = co_value_investing_data.append({'STOCK_TICKER': stock_ticker}, ignore_index=True)


        logger.info('Retreiving Stock Price...')
        sp= factory.create_instance("StockPrice")
        sp.processor(stock_ticker,co_value_investing_data)





        logger.info('Retreiving Net Income...')
        ni = factory.create_instance("NetIncome")
        co_value_investing_data = ni.processor(stock_ticker, co_value_investing_data)




        logger.info('Retreiving Operating Cash...')
        oc = factory.create_instance("OperatingCash")
        co_value_investing_data = oc.processor(stock_ticker, co_value_investing_data)


        logger.info('Retreiving Sales...')
        s = factory.create_instance("Sales")
        co_value_investing_data = s.processor(stock_ticker, co_value_investing_data)


        #writting all values to SQL
        logger.info('Writing co_value_investing_data to sqlite...')
        Sql.sqlite_df_insert(self, sqal_engine, sqlite_connection_dict['sqlite_co_value_investing_data_table'], co_value_investing_data)


        print(co_value_investing_data.head())

Evesting()


