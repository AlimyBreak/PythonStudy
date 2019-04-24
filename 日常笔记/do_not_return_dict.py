# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:00:35 2019
来源:
 B站UP主：哲的王 的稿件<<大兄弟，写Python请别返回Dict>>
 https://www.bilibili.com/video/av20963030/
@ File author: AlimyBreak
"""
# 方案一:
def some_func():
    d = dict()
    d['field_1'] = 1
    d['field_2'] = 2
    return d
    
# 方案二:
from collections import namedtuple
someAPIDataModel = namedtuple('someAPIDataModel1',['field_1','field_2','field_3']);
print(someAPIDataModel)
model_data = someAPIDataModel(field_1 = 1,field_2 = 2,field_3 = 3)
print(model_data)
print(model_data.field_1)
print(model_data[0])
#model_data[0] = 2; #tuple不能修改


