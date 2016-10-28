#!/usr/bin/python
# coding:utf-8

'''

Description:多线程
http://www.cnblogs.com/fnng/p/3670789.html

'''
import threading
from time import ctime, sleep

def music(func):
    for i in range(2):
        print "i was at the %s! %s" %(func,ctime())
        sleep(2)

def move(func):
    for i in range(3):
        print "i was at the %s! %s" %(func,ctime())
        sleep(5)

'''
    科技在发展，时代在进步，我们的cpu也越来越快，cpu抱怨，p大点事儿占了我一定的时间，
其实我同时干多个活都没问题；于是，操作系统就进入了多任务时代。
'''
threads = []
t1 = threading.Thread(target=music, args=("爱情买卖",))
threads.append(t1)
t2 = threading.Thread(target=move, args=("阿凡达",))
threads.append(t2)


if __name__ == "__main__":
    # music("爱情买卖")
    # move("阿凡达")

    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    #join()的作用是，在子线程完成运行之前，这个子线的父线程将一直被阻塞。

    print "all over %s" % ctime()

'''
从执行结果来看，子线程（muisc 、move ）和主线程（print "all over %s" %ctime()）都是同一时间启动，
但由于主线程执行完结束，所以导致子线程也终止。
'''

'''
为什么在python里推荐使用多进程而不是多线程
http://blog.csdn.net/universe_ant/article/details/51243137

全局解释器锁GIL(Global Interpreter Lock), 来源于python设计之初的考虑，为了数据安全所做的决定。

在单核cup下的多线程都只是并发，不是并行。并发是多个事件在同一时间间隔内发生。
    并行是多个事件在同一时刻发生。那么核又是什么呢？处理器中的计算内核？

    线程的执行方式：
    1。获取GIL.
    2。执行代码直到sleep或者python虚拟机将其挂起。
    3。释放GIL.
    可见，某个线程想要执行，必须先拿到GIL，我们可以把GIL看作是"通行证"，并且在一个python进程中，
    GIL只有一个。拿不到通行证的线程，就不允许进入CPU执行。

cpu密集型代码（各种循环处理，计数等等）
io密集型代码（文件处理，网络爬虫）

'''
import multiprocessing

'''
python中的多线程其实并不是真正的多线程，如果想要充争得用多核cpu的资源，在python中大部分情况需要使用多进程。

'''