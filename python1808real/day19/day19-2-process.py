"""
第十八章 进程
"""
# 一、进程的概念
# 正在执行的一个搓成或者一个任务，负责任务执行的是cpu
# 多进程：一个cpu可以同时处理多个程序
# 多进程，一个电脑又执行qq，执行微信，同时执行pycharm
# 多线程，一个电脑执行qq，上了很多个qq

# 二、进程的创建
# 跟线程类似，大概分为两种，
# 一种，multiprocessing.Process类创建
# 另外一种，第三方模块创建进程

# 本章学的是第一种方式
#（1）一种使用multiprocessing.Process(target,args)创建进程对象
#（2）继承multiprocessing.Process，重写run方法

# 跟线程不一样的一个重要问题：
# 在window平台，创建子进程的时候，一定会将当前的模块先导入一次。
# 使用 if __name__=="__main__"来创建进程。

from multiprocessing import Process
import os
import time
# def mission():
#     print("子进程执行")
#     time.sleep(10)
# # print("ccc")
# if __name__=="__main__":
# # 创建方式一：
#     p=Process(target=mission)
#     p.start()
#     print("主进程执行")
#     time.sleep(10)

# 方式二：创建类继承Process，重写run方法
class MyProcess (Process):
    def run(self):
        print("子进程执行")
        time.sleep(2)
        print("子进程执行:当前运行的进程id：{}".format(os.getpid()))
        print("子进程执行:当前进程的父进程的id：{}".format(os.getppid()))
if __name__=="__main__":
    p=MyProcess()
    # 将p设置成守护线程
    # p.daemon = True
    p.start()
    print("主进程执行")
    # time.sleep(10)
    p.join()
    print("当前运行的进程id：{}".format(os.getpid()))
    print("当前进程的父进程的id：{}".format(os.getppid()))


# 进程相关的特殊的一个函数
# os.fork()   # linux下复制一个进程

# run  start  is_alive  name, daemon 都跟线程类似

# 进程不涉及到资源共享问题，进程的资源是独享，所以不用去解决修改并发问题。

# 进程之间区域不共享，不存在进程不安全，需要解决进程之间资源通信的问题。

# python进程Process本身已经解决了通信资源同步问题。
# 使用pickle序列化，对两个进程中的资源进程同步
# 工作原理，当两个进程同时执行的时候，一个进程中写入内容，同时会向另个进程使用pickle序列化
# 的方式写入内容（字节序列），当传送到另外一个进程中之后，再使用pickle序列化恢复成原来的对象。


# 进程队列




