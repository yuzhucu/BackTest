from pymongo import MongoClient

class MongoHandler(object):
    def __init__(self,magic):
        self.__magic=magic
        self.__client=MongoClient('localhost',27017)
        self.__db=self.__client[self.__magic]
        self.__collection=self.__db[self.__magic]


    def save_orderinfo(self,info=None):
        res=self.__collection.insert_one(info)
    def get_allorderinfo(self):
        pass

    def get_orderdetail(self,ticket=None):
        pass

    def modify_order(self,ticket=None):
        pass