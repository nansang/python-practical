#!/usr/bin/python
# coding:utf-8

'''
 pandas 读取excel文件,这里仅仅实现创建excel文件

 函数名首字母不大写，类才大写
'''
import pandas as pd
import matplotlib.pyplot as plt
import sys
import matplotlib
import numpy.random as np


np.seed(111)

'''
函数参数之间要隔开，等号不用；
外部等号要隔开；
'''
def createDataSet(Number):
    output = []
    for i in range(Number):

        # Create a weekly data rang
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')

        #create random data
        data = np.randint(low=25, high=1000, size=len(rng))

        #status pool
        status = [1, 2, 3]

        random_status = [status[np.randint(low=0, high=len(status))] for i in range(len(rng))]
        states = ['GA', 'FL', 'f1', 'NY', 'NJ', 'TX']

        random_states = [states[np.randint(low=0, high=len(states))] for i in range(len(rng))]

        output.extend(zip(random_states, random_status, data, rng))

    return output


dataset = createDataSet(4)

# print dataset

df = pd.DataFrame(data=dataset, columns=['state', 'status', 'CustomerCount', 'StatusDate'])

print df

#写入excel表有问题
# df.to_excel('lesson3.xlsx', index=False)
# df.to_csv('lesson3.csv', index=False, header=False)


print 'done'

df = pd.read_excel('./lesson3.xlsx', 0, index_col='StatusDate')
df.dtypes

# print df.dtypes, df.index
print df.head()


df['CustomerCount'].plot(figsize=(15, 5))#画图

sortdf = df[df['state'] == 'NY'].sort_index(axis=0)#按照横轴进行排序
print sortdf.head(10)

