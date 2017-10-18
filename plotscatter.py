# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:07:14 2017

@author: q
"""

#explain parameters of plt.scatter
'''
plt.scatter(x, y, s=20, 
            c=None, marker='o', 
            cmap=None, norm=None, 
            vmin=None, vmax=None, 
            alpha=None, linewidths=None, 
            edgecolors=None)
x：指定散点图的x轴数据；
y：指定散点图的y轴数据；
s：指定散点图点的大小，默认为20，通过传入新的变量，实现气泡图的绘制；
c：指定散点图点的颜色，默认为蓝色；
marker：指定散点图点的形状，默认为圆形；
cmap：指定色图，只有当c参数是一个浮点型的数组的时候才起作用；
norm：设置数据亮度，标准化到0~1之间，使用该参数仍需要c为浮点型的数组；
vmin、vmax：亮度设置，与norm类似，如果使用了norm则该参数无效；
alpha：设置散点的透明度；
linewidths：设置散点边界线的宽度；
edgecolors：设置散点边界线的颜色；
'''

# 导入模块
import pandas as pd
import matplotlib.pyplot as plt

# 设置绘图风格
plt.style.use('ggplot')
# 设置中文编码和负号的正常显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 读入数据
cars = pd.read_csv('cars.csv')
# 绘图
plt.scatter(cars.speed, # x轴数据为汽车速度
            cars.dist, # y轴数据为汽车的刹车距离
            s = 30, # 设置点的大小 
            c = 'steelblue', # 设置点的颜色
            marker = 's', # 设置点的形状
            alpha = 0.9, # 设置点的透明度
            linewidths = 0.3, # 设置散点边界的粗细
            edgecolors = 'red' # 设置散点边界的颜色
            )

# 添加轴标签和标题
plt.title('汽车速度与刹车距离的关系')
plt.xlabel('汽车速度')
plt.ylabel('刹车距离')

# 去除图边框的顶部刻度和右边刻度
plt.tick_params(top = 'off', right = 'off')

# 显示图形
plt.show()
