# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:03:31 2017

@author: q
"""

#导入第三方包
import datetime
import calendar
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# 采集数据
# 上海2017年9月份历史气温数据
url = 'http://lishi.tianqi.com/shanghai/201709.html'

# 发送爬虫请求
response = requests.get(url).text
# 解析源代码
soup = BeautifulSoup(response, 'html.parser')
# 根据HTML标记语言，查询目标标记下的数据
datas = soup.findAll('div',{'class':'tqtongji2'})[0].findAll('ul')[1:]

# 抓取日期数据
date = [i.findAll('li')[0].text for i in datas]
# 抓取最高温数据
high = [i.findAll('li')[1].text for i in datas]

# 创建数据框
df = pd.DataFrame({'date':date, 'high':high})
# 变量类型
df.dtypes
# 将date变量转换为日期类型
df.date = pd.to_datetime(df.date)
# 将high变量转换成数值型
df.high = df.high.astype('int')

# 数据处理
# 由日期型数据衍生出weekday
df['weekday'] = df.date.apply(pd.datetime.weekday)

# 由日期型数据计算week_of_month，即当前日期在本月中是第几周
# 由于没有现成的函数，这里自定义一个函数来计算week_of_month
def week_of_month(tgtdate):
    # 由日期型参数tgtdate计算该月的天数
    days_this_month = calendar.mdays[tgtdate.month]    # 通过循环当月的所有天数，找出第二周的第一个日期
    for i in range(1, days_this_month + 1):
        d = datetime.datetime(tgtdate.year, tgtdate.month, i)        
        if d.day - d.weekday() > 0:
            startdate = d            
            break
    # 返回日期所属月份的第一周
    return (tgtdate - startdate).days //7 + 1

df['week_of_month'] = df.date.apply(week_of_month)
df.head()
# ==================绘图前的数据整理=====================
# 构建数据表（日历）
target = pd.pivot_table(data = df.iloc[:,1:],values = 'high', 
                        index = 'week_of_month', columns = 'weekday')
target

# 缺失值填充（不填充的话pcolor函数无法绘制）
target.fillna(0,inplace=True)
# 删除表格的索引名称
target.index.name = None
# 对索引排序（为了让“第一周”到“第五周”的刻度从y轴的高到底显示）
target.sort_index(ascending=False, inplace=True)

# ======================开始绘图=========================
# 设置中文和负号正常显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

plt.pcolor(target, # 指定绘图数据
           cmap=plt.cm.Blues, # 指定填充色
           edgecolors = 'white' # 指点单元格之间的边框色
          )

# 添加x轴和y轴刻度标签(加0.5是为了让刻度标签居中显示)
plt.xticks(np.arange(7)+0.5,['周一','周二','周三','周四','周五','周六','周日'])
plt.yticks(np.arange(5)+0.5,['第五周','第四周','第三周','第二周','第一周'])

# 消除图框顶部和右部的刻度线
plt.tick_params(top='off', right = 'off')
# 添加标题
plt.title('上海市2017年9月份每日最高气温分布图')
# 显示图形
plt.show()
# 通过透视图函数形成绘图数据
target = pd.pivot_table(data = df.iloc[:,1:],values = 'high', 
                        index = 'week_of_month', columns = 'weekday')

# 绘图
ax = sns.heatmap(target, # 指定绘图数据
                 cmap=plt.cm.Blues, # 指定填充色
                 linewidths=.1, # 设置每个单元方块的间隔
                 annot=True # 显示数值
                )

# 添加x轴刻度标签(加0.5是为了让刻度标签居中显示)
plt.xticks(np.arange(7)+0.5,['周一','周二','周三','周四','周五','周六','周日'])
# 可以将刻度标签置于顶部显示
# ax.xaxis.tick_top()

# 添加y轴刻度标签
plt.yticks(np.arange(5)+0.5,['第一周','第二周','第三周','第四周','第五周'])
# 旋转y刻度0度，即水平显示
plt.yticks(rotation = 0)

# 设置标题和坐标轴标签
ax.set_title('上海市2017年9月份每日最高气温分布图')
ax.set_xlabel('')
ax.set_ylabel('')

# 显示图形
plt.show()