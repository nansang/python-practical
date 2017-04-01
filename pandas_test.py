#!/usr/bin/python
# coding:utf-8

'''

http://blog.csdn.net/u012780602/article/details/52577771#t1

'''

'''
元组与列表的区别：一个可变一个不可变；

zip()函数，将两个或者多个列表合并成一个包含元组的列表；如果带＊是逆向操作；


'''
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib


print "Python version" + sys.version
print "Pandas version" + pd.__version__
print "Matplotlib version" + matplotlib.__version__

# create data
names = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
ages = [11, 12, 13, 14]

dataset = zip(names, ages, names)

# print dataset

# 将我们的数据变为pandas的格式； 像关系数据库表格式
# df = pd.DataFrame(data=dataset, columns=['names', "age", 'names'])

# print df

# 将我们的数据写入到一个csv文件中去，利用pandas的接口
# df.to_csv('age.csv', index=False,header= False)

print "\n#########################\n"
# 获取数据
location = './douyu_s_20161005.txt'
# df = pd.read_csv(location, nrows=3)



# print df

# print "\n"
# 出现一个问题是我们的df会将数据的第一条判定为header,所以我们需要指定名字
df = pd.read_csv(location, names=["id", "url", "user_device", "user_isp_uid", "douyu_uid", "cnt"], nrows=3)
pd.isnull(df)
print df


'''
 分析数据
 pandas提供了一些接口就像数据库一样的操作一样。
'''

print "\n-------------------\n"

# mySorted = df.sort_values(['age'], ascending=False)
# print mySorted, df["age"].max()

'''
 呈现数据
 pandas提供了数据的可视化
'''
# df["age"].plot()

print "\n--------------------\n"

'''
    pandas读取txt文件和读联csv很像。
'''
print "\n--------------------\n"

'''
    pandas读取excel文件，在此文件中pandas_excel.py
'''

