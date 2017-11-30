# encoing=utf8
from EventEngine.EventEngine import Event
from EventEngine.EventType import EVENT_CLOSEORDER,EVENT_MODIFYORDER,EVENT_NEWORDER
from DataHandler.MongoHandler import MongoHandler

class BaseStrategy(object):
    def __init__(self, eventEngine):
        self.__eventEngine = eventEngine
        self.__eventEngine.AddEventListener(type_=EVENT_NEWORDER, handler=self.SendOrder)
        self.__eventEngine.AddEventListener(type_=EVENT_CLOSEORDER, handler=self.CloseOrder)
        self.__eventEngine.AddEventListener(type_=EVENT_MODIFYORDER, handler=self.ModifyOrder)
    def GetNewData(self, data=None):
        """

        :param data:
        :return:
        """
        self.SendBuyOrder(dataslice=data)
        self.SendSellOrder(dataslice=data)
        self.ModifyOrder(ticket=None, dataslice=data)
        self.CloseOrder(ticket=None, dataslice=data)

    def SendOrder(self, event):
        magic=event.dict['magic']
        mongo_handler=MongoHandler(magic)
        mongo_handler.save_orderinfo(event.dict)

    def CloseOrder(self, ticket, dataslice=None):
        res = False
        orderinfo = {}
        if res == True:
            self.SendEvent(type=EVENT_CLOSEORDER, orderinfo=orderinfo)

    def ModifyOrder(self, ticket, dataslice=None):
        res = False
        orderinfo = {}
        if res == True:
            self.SendEvent(type=EVENT_MODIFYORDER, orderinfo=orderinfo)

    def SendEvent(self, type=None, orderinfo=None):
        OrderEvent = Event(type=type)
        OrderEvent.dict = orderinfo
        self.__eventEngine.SendEvent(OrderEvent)
