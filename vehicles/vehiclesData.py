#encoding = utf-8

import pandas as pd
import numpy as np
from ggplot import *
import matplotlib.pyplot as plt

vehicles = pd.read_csv("./data/vehicles.csv")
print(vehicles.head())
print(len(vehicles))
#- 查看有多少观测点（行）和多少变量（列）


#描述汽车油耗等数据
print(len(vehicles.columns))
print(vehicles.columns)

#查看年份信息
print(len(pd.unique(vehicles.year)))
#总共的年份p
print(min(vehicles.year))
#最小年份
print(max(vehicles.year))
#最大的年份