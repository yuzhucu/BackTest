# encoding=utf8
from config.config import DATA_ROOT_PATH
import pandas as pd

POINT = 5


class Indicator(object):
    def __init__(self, period=None, shift=None, dataslice=None):
        self.__period = period
        self.__shift = shift
        self.__dataslice = dataslice
        data = pd.read_csv(DATA_ROOT_PATH)
        time = self.__dataslice['time']
        self.data = data[data['Time (UTC)'] <= time][-self.__period + self.__shift:-self.__shift]


class Ma(Indicator):
    def __init__(self, period=None, shift=None, dataslice=None):
        Indicator.__init__(self, period, shift, dataslice)

    def get_Ma(self):
        return round(self.data['Close'].mean(), POINT)


class High(Indicator):
    def __init__(self, period=None, shift=None, dataslice=None):
        Indicator.__init__(self, period, shift, dataslice)

    def get_High(self):
        return round(self.data['High'].max(), POINT)


class Low(Indicator):
    def __init__(self, period=None, shift=None, dataslice=None):
        Indicator.__init__(self, period, shift, dataslice)

    def get_Low(self):
        return round(self.data['Low'].min(), POINT)

