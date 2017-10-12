# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:46:37 2017

@author: q
"""

#how to use matplotlib to make hist chart

#hist parameter
'''
plt.hist(x, bins=10, range=None, normed=False, 
        weights=None, cumulative=False, bottom=None, 
        histtype='bar', align='mid', orientation='vertical', 
        rwidth=None, log=False, color=None, 
        label=None, stacked=False)
x：指定要绘制直方图的数据；
bins：指定直方图条形的个数；
range：指定直方图数据的上下界，默认包含绘图数据的最大值和最小值；
normed：是否将直方图的频数转换成频率；
weights：该参数可为每一个数据点设置权重；
cumulative：是否需要计算累计频数或频率；
bottom：可以为直方图的每个条形添加基准线，默认为0；
histtype：指定直方图的类型，默认为bar，除此还有’barstacked’, ‘step’,  ‘stepfilled’；
align：设置条形边界值的对其方式，默认为mid，除此还有’left’和’right’；
orientation：设置直方图的摆放方向，默认为垂直方向；
rwidth：设置直方图条形宽度的百分比；
log：是否需要对绘图数据进行log变换；
color：设置直方图的填充色；
label：设置直方图的标签，可通过legend展示其图例；
stacked：当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放；
'''
# 导入第三方包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取Titanic数据集
titanic = pd.read_csv('titanic_train.csv')
# 检查年龄是否有缺失any(titanic.Age.isnull())
# 不妨删除含有缺失年龄的观察
titanic.dropna(subset=['Age'], inplace=True)

# 设置图形的显示风格
plt.style.use('ggplot')
# 绘图：乘客年龄的频数直方图
plt.hist(titanic.Age, # 绘图数据
        bins = 20, # 指定直方图的条形数为20个
        color = 'steelblue', # 指定填充色
        edgecolor = 'k', # 指定直方图的边界色
        label = '直方图' )# 为直方图呈现标签

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top='off', right='off')
# 显示图例
plt.legend()
# 显示图形
plt.show()