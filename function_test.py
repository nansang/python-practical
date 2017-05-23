#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/22 下午4:45
# @Author  : NcuLph
# @Site    : 
# @File    : function_test.py
# @Software: PyCharm


'''

函数传递参数

'''

a = 1
def fun(a):
    a = 2

fun(a)

print a

b = [2]
def funb(b):
    b[0] = 1
    print id(b)

funb(b)
print b, id(b)


c = (3)

def func(c):
    print c, id(c)
    c = (1)
    print c, id(c)
func(c)
c = (4)
print c, id(c)

