#encoding=utf8

# 事件驱动

from Queue import Queue,Empty
from threading import *

class EventEngine(object):
    """
    事件处理引擎，用于根据不同事件找到事件处理对应函数
    """
    def __init__(self):
        self.__eventQueue = Queue()
        self.__active = False
        self.__thread = Thread(target=self.__Run)
        self.__handlers = {}

    def __Run(self):
        while self.__active==True:
            try:
                event=self.__eventQueue.get(block=True,timeout=1)
                self.__EventProcess(event)
            except Empty:
                pass

    def __EventProcess(self,event):
        if event.type in self.__handlers:
            for handler in self.__handlers[event.type]:
                handler(event)

    def Start(self):
        self.__active=True
        self.__thread.start()

    def Stop(self):
        self.__active=False
        self.__thread.join()

    def AddEventListener(self,type_,handler):
        try:
            handlerList=self.__handlers[type_]
        except KeyError:
            handlerList=[]
        self.__handlers[type_] = handlerList
        if handler not in handlerList:
            handlerList.append(handler)

    def RemoveEventListener(self,type_,handler):
        handlerList = self.__handlers[type_]
        if handler in handlerList:
            handlerList.remove(handler)
        if not handlerList:
            del self.__handlers[type_]

    def SendEvent(self,event):
        self.__eventQueue.put(event)

class Event(object):
    def __init__(self,type=None):
        self.type=type
        self.dict={}

