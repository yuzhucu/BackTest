# encoding=utf8
from EventEngine.EventType import EVENT_NEWDATA, EVENT_NEWORDER
from EventEngine.EventEngine import EventEngine
from Strategy.Strategy import BaseStrategy
from DataHandler.DataHandle import DataSliceHandle, DataHandle
import pandas as pd
from config.config import DATA_ROOT_PATH


class MyStrategy(BaseStrategy):
    def __init__(self, eventEngine):
        BaseStrategy.__init__(self, eventEngine)

    def GetNewData(self, event):
        if event.dict['data']['open'] > 1.07:
            self.SendEvent(type=EVENT_NEWORDER, orderinfo={'a': event.dict['data']['open'],'magic':'4'})


def test():
    # 事件处理引擎实例
    eventEngine = EventEngine()
    # mystrategy类的实例
    data_1 = MyStrategy(eventEngine)
    # 制定EVENT_NEWDATA类型时间由data_1.GetNewData函数处理
    eventEngine.AddEventListener(type_=EVENT_NEWDATA, handler=data_1.GetNewData)
    # 启动引擎
    eventEngine.Start()
    # 获取数据
    data = DataHandle(data=pd.read_csv(DATA_ROOT_PATH ), start='2017.01.01',
                      end='2017.02.01').SplitData()
    for i in data:
        # 获取迭代产生的每一个数据切片
        new_data = DataSliceHandle(magic='123', eventEngine=eventEngine, data=i)
        # 调用实例的发送事件接口，并指定事件类型
        new_data.SendDataEvent(type=EVENT_NEWDATA)
    # eventEngine.Stop()


if __name__ == '__main__':
    test()
