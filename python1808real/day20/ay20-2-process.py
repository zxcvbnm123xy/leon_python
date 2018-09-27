"""
并发编程：
1.进程，线程，协成的基本概念，创建、使用
2.协成的应用（生成器------第三方模块）
3.并发的实践
"""
# 一、进程
# 1.进程的相関概念
# 程序运行起来之后创建的一个进程。
# 创建进程已经学过了使用multprocessing.Process类创建
# （1）multprocessing.Process，指定target参数，创建对象
# （2）继承multprocessing.Process，重写run方法

# 需求：通过比较案例的执行时长，来比较不同的创建进程方式的执行速度
# 案例：io ：16s
# 计算密集型:1.95s
# 累加求和 方法
import time
def sum(a,b):
    s=0
    for i in range(a,b+1):
        s+=i
        # time.sleep(0.5)
    return s

# 不适用进程，不适用线程，直接执行
# if __name__=="__main__":
#     start=time.time()
#     # sum(0,100000000)
#     # sum(0,200000000)
#     sum(0, 10)
#     sum(0, 20)
#     end=time.time()
#     print("执行的时间{}".format(end-start))

# 2.使用进程池创建进程
"""
进程池：负责维护一定数量(最大)的进程，可以向进程池提交任务，如果进程池中的数量没有达到生鲜
        进程池会帮我们创建一个新的进程，执行任务，负责如果进程池中的进程数量已经达到上限
        新任务只能在进程池外等待，等待进程池内进程死亡，或者进程结束，
        才能再次创建新的进程执行任务。        
"""
# from multiprocessing import Pool 进程池创建进程
# 方式
# from multiprocessing import Pool
# Pool(进程池中最大的数量)
# pool=Pool(5)
# 相关方法
"""
apply：同步申请模式
apply_async：异步申请模式
close：暂停关闭
terminate：真正关闭进程池所有服务
join 阻塞主进程，等到子进程的退出（跟close联合使用）
"""
# （1）同步申请模式
# 穿行（排队执行）
from multiprocessing import Pool
import os,time
# def work():
#     print("当前进程的id={}".format(os.getpid()))
#     time.sleep(1)
#
# # 使用进程池创建进程（同步模式创建进程）
# if __name__=="__main__":
#     pool=Pool(5)
#     # pool.apply(要执行的任务，args=任务的参数元祖)
#     for i in range(3):
#         pool.apply(work)
#         print("第{}个任务执行完毕".format(i))

# 使用同步申请模式实现累加案例
# 计算密集型: 2.1s
# io密集型: 16.2s
# 进程池中使用同步方式申请进程，反而执行的比正常串行慢，
def sum2(b1,b2):
    pool=Pool(4)
    pool.apply(sum,args=(0,b1))
    pool.apply(sum, args=(0, b2))

# if __name__=="__main__":
#     start=time.time()
#     # sum2(10000000,20000000)
#     sum2(10,20)
#     end=time.time()
#     print("执行的时间{}".format(end - start))

# （2）异步申请模式
# 1.异步模式的使用方式
# def work(index):
#     print("第{}几个任务".format(index))
#
# if __name__=="__main__":
#     pool=Pool(4)
#     for i in range(3):
#         # pool.apply(work,args=(i,))
#         pool.apply_async(work,args=(i,))
#         # print("第{}几个任务".format(i))  不能保证执行完毕在work之后执行
#     # 使用join抢占之前需要先关闭(暂时关闭，长久关闭)进程池
#     pool.close()
#     pool.join()
#     print("主进程执行结束")
# 使用multiprocessing.Pool异步模式申请的子进程被当成是后台进程
# 如果希望子进程全部在主进程执行结束之前全部执行完毕，一般使用抢占进程的方式解决
# 使用进程池对象.join抢占主进程

# 2.回调函数
# 定义一个callback函数，来保证执行完每一个进程任务之后才执行的函数
# 执行回调函数的时间：异步提交神奇是，执行完每一个进程之后就会执行
# 回调函数的定义：
"""
def 回调函数名（参数[任务函数的返回值]）：
    pass
"""
# 回调函数的调用
# 在异步申请是，加入callback关键字=回调函数的名字，因为已经规定好就是任务返回值
def work(index):
    print("第{}几个任务".format(index))
    time.sleep(1)
    return index

def back(value):
    print("第{}个任务执行结束".format(value))

# if __name__=="__main__":
#     pool=Pool(4)
#     for i in range(8):
#         # pool.apply(work,args=(i,))
#         pool.apply_async(work,args=(i,),callback=back)
#     pool.close()
#     pool.join()
#     print("主进程执行结束")

# 使用异步申请模式完成案例
# 计算密集型
# io密集型
# def sum3(b1,b2):
#     pool=Pool(4)
#     for i in [b1,b2]:
#         pool.apply_async(sum,args=(0,i))
#     pool.close()
#     pool.join()
#
# if __name__=="__main__":
#     start=time.time()
#     sum2(10000000,20000000)
#     # sum3(10,20)
#     end=time.time()
#     print("执行的时间{}".format(end - start))

# 3.使用第三方包创建进程
# 3.1之前需要手动安装，3.1之后被纳入到python开发包中
# 进程池和线程池的用法几乎一样
# concurrent.futures
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# 提供的都是异步调用
# ProcessPoolExecutor
# ThreadPoolExecutor

# （1）抽象类Exceutor（抽象类，只用来被继承，不用来被实例化）
# 上下文管理器：上下文管理器的类实现了进入with__enter__，离开with语句体__exit__
# ProcessPoolExecutor
# ThreadPoolExecutor
# 都继承了Exector上下文管理器，都实现了__enter、__exit__
# 创建进程（线程）方式：
# max_workers进程池活线程池支持的最大数量（默认4）
# with ProcessPoolExecutor(max_workers=4) as executor:
#     pass

# （2）相关方法
# 1.sunbmit（func，*args，**kwargs）
# 异步提交任务，往进程池中加入task任务，一次只能加一个任务，如果有多个任务，多个submit
# func：被异步调用的函数
# *args，**kwargs：被调用函数的参数（不需要以元组的形式传入）
# submit返回值：是即将异步执行的任务。
def doTask(item):
    # s="{}发试卷".format(item)
    # print(s)
    # time.sleep(1)
    time.sleep(0.2)
    return "返回值----{}".format(item)

def doTask2(a,b):
    print("第一个参数a={},第二个参数b={}".format(a,b))

# if __name__=="__main__":
#     # 任务函数只有一个
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         # executor.submit(doTask,"班长")
#         # executor.submit(doTask, "学委")
#         li=["班长","学委","体委"]
#         # for i in li:
#         #     executor.submit(doTask,i)
#         # 列表推导式
#         tasks=[executor.submit(doTask,i) for i in li ]
#         # tasks 是即将要执行的任务列表
#         for i in tasks:
#             print(i.result())
#     #
    # 任务函数有两个参数，submit函数中，func=函数名，其余都是函数参数（自动打包成元组）
    # with ProcessPoolExecutor(max_workers=4) as executor:
    #     args=[(1,"a"),(2,"b")]
    #     # for x,y in args:
    #     #     executor.submit(doTask2,x,y)
    #        #列表推导式
    #     tasks=[executor.submit(doTask2,x,y) for x,y in args]

# ② result（） 获得进程执行后的返回值。是一个阻塞函数（保证任务一定执行，才能获得返回值）
#  任务.result（）

# ③ 任务.running()可以显示执行那一刻的运行状态
#    任务.done（） 可以显示执行的那一刻任务时候已经执行完毕
# if __name__=="__main__":
#     # 任务函数只有一个
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         li=["班长","学委","体委"]
#         # 列表推导式
#         tasks=[executor.submit(doTask,i) for i in range(100)]
#         # tasks 是即将要执行的任务列表
#         for index,i in enumerate(tasks):
#             # print(i.result())
#             # time.sleep(1)
#             print("{}----执行状态{}----完成状态{}".format(index,i.running(),i.done()))

# ④ as_completed（迭代器，timeout）
# 获得已经执行完毕的任务
# 使用场合：遇到有些模块必须是任务执行完毕之后才能执行的
# 语法as_completed（待执行的任务，超时时间）,默认阻塞等待完成
# from concurrent.futures import as_completed
# if __name__=="__main__":
#     # 任务函数只有一个
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         li=["班长","学委","体委"]
#         # 列表推导式
#         tasks=[executor.submit(doTask,i) for i in range(100)]
#         # tasks 是即将要执行的任务列表
#         for index,i in enumerate(tasks):
#             # 保证第i个任务一定是执行完毕了，才执行for循环里面的内容
#             # print(i.result())
#             # time.sleep(0.5)
#             print("{}----执行状态{}----完成状态{}".format(index,i.running(),i.done()))

# ⑤ wait（func，timeout，return_when）
# wait可以返回一个元组，一个是执行完，一个是还没有执行完
# return_when：ALL_COMPLETE：全部执行完成
# return_when： FIRST_COMPLETE：保证第一个任务执行完毕
# timeout=超时时间，如果超过了timeout，则阻塞，wait返回值
# from concurrent.futures import as_completed,wait,ALL_COMPLETED,FIRST_COMPLETED
# if __name__=="__main__":
#     # 任务函数只有一个
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         li=["班长","学委","体委"]
#         # 列表推导式
#         tasks=[executor.submit(doTask,i) for i in range(100)]
#         # tasks 是即将要执行的任务列表
#         done,undone=wait(tasks,return_when=FIRST_COMPLETED)
#         for i in done:
#             print("已完成{}".format(i))
#         for i in undone:
#             print("未完成{}".format(i))
# 从执行结果来说，as_completed跟wait+ALL_CIOMPLETED是一样的，但是执行过程不一样
#








