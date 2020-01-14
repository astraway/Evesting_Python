import abc


class ProcessorABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def processor(self,stock_ticker, df):
        pass


#test