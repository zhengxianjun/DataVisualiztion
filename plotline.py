# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:00:13 2017

@author: q
"""

#how to use matplotlib to make line chart

#explain parameter of plt.plot
'''
plt.plot(x,y,linestyle,
        linewidth,color,marker,
        markersize,markeredgecolor,
        markerfactcolor,label,alpha)
x：指定折线图的x轴数据；
y：指定折线图的y轴数据；
linestyle：指定折线的类型，可以是实线、虚线、点虚线、点点线等，默认文实线；
linewidth：指定折线的宽度
marker：可以为折线图添加点，该参数是设置点的形状；
markersize：设置点的大小；
markeredgecolor：设置点的边框色；
markerfactcolor：设置点的填充色；
label：为折线图添加标签，类似于图例的作用；
'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

#设置绘图风格
plt.style.use('ggplot')

#设置中文编码和负号的正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取需要绘图的数据
article_reading = pd.read_excel('wechart.xlsx')
# 取出8月份至9月28日的数据
sub_data = article_reading.loc[article_reading.date >= '2017-08-01' ,:]


# 设置图框的大小
fig = plt.figure(figsize=(10,6))

# 绘图--阅读人数趋势
plt.plot(sub_data.date, # x轴数据
         sub_data.article_reading_cnts, # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'steelblue', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='steelblue', # 点的填充色
         label = '阅读人数') # 添加标签

# 绘图--阅读人次趋势
plt.plot(sub_data.date, # x轴数据
         sub_data.article_reading_times, # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#ff9999', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='#ff9999', # 点的填充色
         label = '阅读人次') # 添加标签

# 添加标题和坐标轴标签
plt.title('公众号每天阅读人数和人次趋势图')
plt.xlabel('日期')
plt.ylabel('人数')

# 剔除图框上边界和右边界的刻度
plt.tick_params(top = 'off', right = 'off')

# 获取图的坐标信息
ax = plt.gca()
# 设置日期的显示格式  
date_format = mpl.dates.DateFormatter('%m-%d')  
ax.xaxis.set_major_formatter(date_format) 

# 设置x轴显示多少个日期刻度
#xlocator = mpl.ticker.LinearLocator(10)
# 设置x轴每个刻度的间隔天数
xlocator = mpl.ticker.MultipleLocator(3)
ax.xaxis.set_major_locator(xlocator)

# 为了避免x轴日期刻度标签的重叠，设置x轴刻度自动展现，并且45度倾斜
fig.autofmt_xdate(rotation = 45)

# 显示图例
plt.legend()
# 显示图形
plt.show()