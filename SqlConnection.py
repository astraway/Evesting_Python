import sqlite3
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import settings


__app_name__ = 'SqlConnection'

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



class Sql:
    def __init__(self,sqal_engine,connectDict,df,query ):
        self.sqal_engine = sqal_engine
        self.connectDict = connectDict
        self.df = df
        self.query = query


    @staticmethod
    def sqlite_df_insert(self, sqal_engine, connectDict, df):
        logger.info('Appending data into sqlite...')
        try:
            connection = sqal_engine.connect()
            # connection.execute(snowflake_query)
            df.to_sql(connectDict, con=connection, index=False, if_exists='append')
        except Exception:
            logger.error('Error Appending to: {}'.format(connectDict))
        finally:
            connection.close()
            sqal_engine.dispose()

        return None

    @staticmethod
    def sqlite_read(self, query, sqal_engine, connectDict):
        df = pd.DataFrame()

        logger.info('Reading snowflake data...')
        try:
            connection = sqal_engine.connect()
            df = pd.read_sql(query, connection)
        except Exception:
            logger.error('Error Reading from: {}'.format(connectDict['sqlite_Financials_table']))
        finally:
            connection.close()
            sqal_engine.dispose()

        if not df.empty:
            df.columns = map(str.upper, df.columns)

        # print(df)

        return df




    @staticmethod
    def create_sqlite_engine(self):

        logger.info('Creating snowflake engine...')
        # snowflake_parameter_dict = connectDict.get('snowflake_parameter_dict', None)

        engine = create_engine('sqlite:///Evesting_Py.db')

        return engine

