#!/usr/bin/python
# coding:utf-8

'''
Created on:
@author:
Email:
Version:
Description:
Help:
'''

'''
python数据库上的操作

查询通常有两种方式：一种是使用cursor.fetchall（）获取所有查询结果，然后再一行一行的迭代；
另一种每次通过cursor.fetchone()获取一条记录，直到获取的结果为空为止。

http://www.runoob.com/python/python-mysql.html
'''

import MySQLdb


conn = MySQLdb.connect(host="127.0.0.1", user="user_tv", passwd="abc@123%", db="douyu_danmu")
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print "MYSQL server version:", row[0]
# cursor.close()
conn.close()




