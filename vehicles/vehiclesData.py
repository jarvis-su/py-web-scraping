#encoding = utf-8
import pandas as pd
import numpy as np
from ggplot import *
import matplotlib.pyplot as plt

vehicles = pd.read_csv("./data/vehicles.csv")
print(vehicles.head())
print(len(vehicles))
#- 查看有多少观测点（行）和多少变量（列）