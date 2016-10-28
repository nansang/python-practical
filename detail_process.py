#!/usr/bin/python
# coding:utf-8

'''
Description:多进程并行（同一时刻）
http://www.cnblogs.com/kaituorensheng/p/4445418.html

daemon是什么鬼？
'''

import multiprocessing
import time
from time import ctime

def worker_1(intervail):
    print "worker_1" + ctime()
    time.sleep(intervail)
    print "end worker_1" + ctime()

def worker_2(intervail):
    print "worker_2 %s" %ctime()
    time.sleep(intervail)
    print "end worker_2 %s"%ctime()

def worker_3(intervail):
    print "worker_3 %s" %ctime()
    time.sleep(intervail)
    print "end worker_3"+ctime()

def worker_4(intervail):
    print "worker_4 %s" %ctime()
    time.sleep(intervail)
    print "end worker_4"+ctime()

def worker_5(intervail):
    print "worker_5 %s" %ctime()
    time.sleep(intervail)
    print "end worker_5"+ctime()

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=worker_1, args=(2,))
    p2 = multiprocessing.Process(target=worker_2, args=(3,))
    p3 = multiprocessing.Process(target=worker_3, args=(4,))
    p4 = multiprocessing.Process(target=worker_4, args=(5,))
    p5 = multiprocessing.Process(target=worker_5, args=(6,))
    # p6 = multiprocessing.Process(target=worker_3, args=(4,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    # p6.start()

    print ("the number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print ("child p.name:"+p.name + "＼tp.id" + str(p.pid))

    print "END!!!!!!!!!!!!!!"




