#!/usr/bin/python
# coding:utf-8

import thread
import time

# 创建一个新的线程，返回一个线程标识符。function是线程函数，args是线程函数的参数，是一个list.
#kwargs可选参数，可不填。
def work_thread(id):

    cnt = 1

    print "thread %d is running...\n" %id

    while True:

        print "thread with id %d has counter value %d \n" %(id, cnt)
        time.sleep(2)
        cnt += 1

for i in range(1, 5):
    thread.start_new_thread(work_thread, (i,))

print "Main thread doing an infinite wait loop...\n"

while True:
    pass


