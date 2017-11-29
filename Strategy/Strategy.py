# encoing=utf8
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure
import datetime


class BaseStrategy(object):
    def __init__(self):
        self.db=None

    def dbConnect(self):
        if not self.db:
            try:
                self.db=MongoClient('127.0.0.1',27017)[str(self.__magic)]
            except ConnectionFailure:
                print "error when connecting to mongodb"
                pass

    def SendBuyOrder(self):
        return False

    def SendSellOrder(self):
        return False

    def CloseOrder(self, ticket):
        return True

    def ModifyOrder(self, ticket):
        return True


