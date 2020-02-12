from .ABC_Processor import ProcessorABC


class NullProcessor(ProcessorABC):

    def __init__(self, stockticker, df):
        self.stockticker = stockticker
        self.df = df

    def processor(self,stock_ticker, df):
        print("Unknown Processor Type")

#test