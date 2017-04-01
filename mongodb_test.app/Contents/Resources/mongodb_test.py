#!/usr/bin/python
# coding:utf-8

'''

'''
import pymongo
import pymongo.collection

# 创建一个mongo客户端
client = pymongo.MongoClient("127.0.0.1", 27017)

#获得mongoDB中的数据库对象
db = client.runoob

#在数据库中创建一个集合
collection = db.runoob


jike = {'_id':'324', 'name ':'刘生tg ', "age":5, "skill":"python"}

god = {"_id":34, "name":"张三", "teacher":"unknow"}

#插入数据
collection.insert(jike)
collection.insert(god)

print collection
