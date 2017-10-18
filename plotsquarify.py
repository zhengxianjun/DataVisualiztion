# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:13:11 2017

@author: q
"""

'''
squarify.plot(sizes, 
            norm_x=100, 
            norm_y=100, 
            color=None, 
            label=None, 
            value=None, 
            alpha,
            **kwargs)
sizes：指定离散变量各水平对应的数值，即反映树地图子块的面积大小；
norm_x：默认将x轴的范围限定在0-100之内；
norm_y：默认将y轴的范围限定在0-100之内；
color:自定义设置树地图子块的填充色；
label：为每个子块指定标签；
value：为每个子块添加数值大小的标签；
alpha：设置填充色的透明度；
**kwargs：关键字参数，与条形图的关键字参数类似，如设置边框色、边框粗细等；
'''

# 导入第三方包
import matplotlib.pyplot as plt
import squarify

#中文及负号处理办法
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 创建数据
name = ['国内增值税','国内消费税','企业所得税','个人所得税',
        '进口增值税、消费税','出口退税','城市维护建设税',
        '车辆购置税','印花税','资源税','土地和房税','车船税烟叶税等']
income = [3908,856,801,868,1361,1042,320,291,175,111,414,63]
        
# 绘图
colors = ['steelblue','#9999ff','red','indianred',
          'green','yellow','orange']
plot = squarify.plot(sizes = income, # 指定绘图数据
     label = name, # 指定标签
     color = colors, # 指定自定义颜色
     alpha = 0.6, # 指定透明度
     value = income, # 添加数值标签
     edgecolor = 'white', # 设置边界框为白色
     linewidth =3 # 设置边框宽度为3
        )
# 设置标签大小
plt.rc('font', size=8)
# 设置标题大小
plot.set_title('2017年8月中央财政收支情况',fontdict = {'fontsize':15})

# 去除坐标轴
plt.axis('off')
# 去除上边框和右边框刻度
plt.tick_params(top = 'off', right = 'off')
# 显示图形
plt.show()