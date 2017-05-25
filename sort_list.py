#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/23 下午3:26
# @Author  : NcuLph
# @Site    : 
# @File    : sort_list.py
# @Software: PyCharm

import operator

somelist = [(1, 9, 5), (2, 5, 8), (5, 6, 3)]

somelist.sort(key=operator.itemgetter(0))
print 'the number one {0} but {1} every {0}'.format(somelist, "do you know")

somelist.sort(key=operator.itemgetter(1))
print somelist

somelist.sort(key=operator.itemgetter(2))
print "the third number %s" % somelist


'''
http://www.cnblogs.com/LyningCoder/p/4344649.html

1。关键代码可以依赖于扩展包
2。使用关键字排序
3。循环优化
4。使用最新版本
5。尝试多种编程方法
6。交叉编译实现 -- 在一个平台上生成另一个平台上可执行代码
'''

lowerlist = ["welcome", "to", "china"]
upper = str.upper
upperlist = []
append = upperlist.append

'''
不带括号时，调用的是函数本身，打印出来是地址
带函数时，调用的是函数return结果

关于类的使用，不加括号是类的引用，加了是实例化

类的属性？
'''

for word in lowerlist:
    append(upper(word))
    print upperlist


class City(object):

    country = "shenzhen"

    def __init__(self, city, address, name):
        self.city = city
        self._address = address
        self.__name = name

city = City("nanchang", "123", "lph")
print city, City

print city.city
print city._address
print city.country
print City.country


print dir(City)
print dir(operator)
