#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/23 下午3:06
# @Author  : NcuLph
# @Site    : 
# @File    : singal.py
# @Software: PyCharm


'''

单例模式

'''

# 使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    a = 1
