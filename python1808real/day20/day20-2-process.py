"""
并发编程：
1. 进程、线程、协程基本概念，创建、使用
2. 协程的应用（生成器----第三方模块）
3. 并发的实践
"""
# 一、进程
# 1.进程的相关概念
# 程序运行起来之后创建的一个进程。
# 创建进程已经学过使用multiprocessing.Process类创建
# （1）multiprocessing.Process()，指定target参数，创建对象
# （2）继承multiprocessing.Process，重写run方法

# 需求：通过比较案例的执行时长，来比较不同的创建进程方式的执行速度
# 案例: io   计算密集型
# 累加求和方法
import time
def sum(a,b):
    s=0
    for i in range(a,b+1):
        s+=i
        # time.sleep(0.5)
    return s

#不使用进程，不使用线程，直接执行
# 计算密集型：1.95s
# io 密集型： 16s
# if __name__=="__main__":
#     start=time.time()
#     # sum(0,10000000)
#     # sum(0,20000000)
#     sum(0,10)
#     sum(0,20)
#     end=time.time()
#     print("执行的时间{}".format(end-start))


# 2.使用进程池创建进程
"""
进程池：负责维护一定数量（最大）的进程，可以向进程池提交任务，如果进程池中进程数量没有达到上限，
        进程池会帮我们创建一个新的进程，执行任务，否则如果进程池中的进程数量已经达到上限
        新任务只能在进程池外等待，等待进程池内进程死亡，或者进程结束，
        才能再次创建新的进程执行任务。
"""
#from multiprocessing import Pool 进程池创建进程
# 方式
# from multiprocessing import Pool
# # Pool(进程池中最大的数量)
# pool=Pool(5)
# 相关方法
"""
apply:同步申请模式
apply_async:异步申请模式
close，暂停关闭
terminate，真正关闭进程池所有任务
join 阻塞主进程，等待子进程的退出（跟close联合使用）
"""
# （1）同步申请模式
# 串行（排队执行）
from multiprocessing import Pool
import os
# def work():
#     print("当前进程的id={}".format(os.getpid()))
#     time.sleep(1)
#
# # 使用进程池创建进程（同步模式创建进程）
# if __name__=="__main__":
#     pool = Pool(5)
#     # pool.apply(要执行的任务，args=任务的参数元组)
#     for i in range(3):
#         pool.apply(work)
#         print("第{}个任务执行完毕".format(i))

# 使用同步申请模式实现累加和案例
# 计算密集型  2.1s
# io密集型    16.2s
# 进程池中使用同步方式申请进程，反而执行的比正常串行慢，因为向进程池申请进程也需要时间。
# def sum2(b1,b2):
#     pool=Pool(4)
#     pool.apply(sum,args=(0,b1))
#     pool.apply(sum,args=(0,b2))
#
# if __name__=="__main__":
#     start=time.time()
#     # sum2(10000000,20000000)
#     sum2(10,20)
#     end=time.time()
#     print("执行的时间{}".format(end - start))

# （2）异步申请模式
#① 异步模式的使用方式
# def work(index):
#     print("第{}个任务".format(index))
#     time.sleep(1)
#
# if __name__=="__main__":
#     pool=Pool(4)
#     for i in range(3):
#         # pool.apply(work,args=(i,))
#         pool.apply_async(work,args=(i,))
#         # print("第{}个任务执行完毕".format(i)) # 不能保证执行完毕work之后才执行。
#     # 使用join抢占之前需要先关闭（暂时关闭，长久关闭）进程池
#     pool.close()
#     pool.join()
#     print("主进程执行结束")
# 使用multiprocessing.Pool异步模式申请的子进程被当成是后台进程。
# 如果希望子进程全部在主进程执行结束之前全部执行完毕，使用抢占进程的方式解决join
# 使用【进程池对象.join抢占主进程】


# ②回调函数
# 定义一个callback函数，来保证执行完每一个进程任务之后才执行的函数。
# 执行回调函数的时间: 异步提交申请时，执行完每一个进程之后，就会执行
# 回调函数定义：
"""
def 回调函数名(参数[任务函数的返回值]):
   pass
"""
# 回调函数的调用
# 在异步申请时，加入callback关键字=回调函数的名字
# （不需要传入参数，因为已经规定好就是任务函数的返回值）。
# def work(index):
#     print("第{}个任务".format(index))
#     time.sleep(1)
#     return index
# def back(value):
#     print("第{}个任务执行结束".format(value))
# if __name__=="__main__":
#     pool=Pool(4)
#     for i in range(8):
#         # pool.apply(work,args=(i,))
#         pool.apply_async(work,args=(i,),callback=back)
#     pool.close()
#     pool.join()
#     print("主进程执行结束")

# 使用异步申请模式完成案例
# io密集型：10.8s
# 计算密集型：1.92s
# def sum3(b1,b2):
#     pool=Pool(4)
#     for i in [b1,b2]:
#         pool.apply_async(sum,args=(0,i))
#     pool.close()
#     pool.join()
# if __name__=="__main__":
#     start=time.time()
#     sum3(10000000,20000000)
#     # sum3(10,20)
#     end=time.time()
#     print("执行的时间{}".format(end - start))


# 3. 使用第三方包创建进程
# 3.1之前需要手动安装，3.1之后被纳入到python的开发包中
# 进程池和线程池的用法几乎一样
# concurrent.futures
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# 提供的都是异步调用
# ProcessPoolExecutor
# ThreadPoolExecutor

# (1) 抽象类Executor（抽象类：只用来被继承，不用来被实例化对象）
# 上下文管理器：上下文管理器的类实现了进入with__enter__，离开with语句体的__exit__
# ProcessPoolExecutor
# ThreadPoolExecutor
# 都继承了Executor上下文管理器，都实现__enter__、__exit__

# 创建进程（线程）方式：
# max_workers进程池或者线程池支持的最大数量(默认4)
# with ProcessPoolExecutor(max_workers=4) as executor:
#     pass

# (2)相关方法
# ①submit(func,*args,**kwargs)
# 异步提交任务，往进程池中加入task任务，一次只能加一个任务，如果有多个任务，多次submit
# func: 被异步调用的函数
# *args,**kwargs： 被调用函数的参数（不需要以元组的形式传入）
# submit返回值：是即将异步执行的任务。
def doTask(item):
    # s="{}发试卷".format(item)
    # print(s)
    time.sleep(0.1)
    return "返回值--{}".format(item)

def doTask2(a,b):
    print("第一个参数={},第二参数={}".format(a,b))

# if __name__=="__main__":
#     #任务函数只有一个参数
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         # executor.submit(doTask,"班长")
#         # executor.submit(doTask,"学委")
#         li=["班长","学委","体委"]
#         # for i in li:
#         #     executor.submit(doTask, i)
#
#         # 列表推导式
#         tasks=[executor.submit(doTask,i) for i in li]
#         # tasks是即将要执行的任务列表
#         for i in tasks:
#             print(i.result())

    # 任务函数有两个参数，submit函数中，func=函数名，其余都是函数的参数（自动将参数打包成元组）
    # with ProcessPoolExecutor(max_workers=4) as executor:
    #     # args=[(1,"a"),(2,"b")]
    #     # for x,y in args:
    #     #     executor.submit(doTask2, x,y)
    #     # 列表推导式
    #     tasks2=[executor.submit(doTask2, x,y) for x,y in args]

#② result() 获得进程执行后的返回值。 是一个阻塞函数（保证任务一定执行完毕，才能获得返回值）
# 任务.result()

# ③任务.running()  可以显示执行那一刻的运行状态
#  任务.done()     可以显示执行的那一刻任务是否已经执行完毕。
# if __name__=="__main__":
#     #任务函数只有一个参数
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         # 列表推导式
#         tasks=[executor.submit(doTask,i) for i in range(100)]
#         # tasks是即将要执行的任务列表
#         for index,i in enumerate(tasks):
#             # print(i.result())
#             time.sleep(0.3)
#             print("{}---执行状态{}----完成状态{}".format(index,i.running(),i.done()))

# ④as_completed(迭代器，timeout)
# 获得已经执行完毕的任务
# 使用场合：遇到有些模块必须是任务执行完毕之后才能执行的
# 语法as_completed（待执行的任务，超时时间），默认阻塞等待任务完成
from concurrent.futures import as_completed
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        tasks=[executor.submit(doTask,i) for i in range(100)]
        # tasks是即将要执行的任务列表
        for index,i in enumerate(as_completed(tasks)):
            # 保证第i个任务一定是执行完毕了，才执行for循环里面的内容
            # print(i.result())
            # time.sleep(0.3)
            print("{}---执行状态{}----完成状态{}".format(index,i.running(),i.done()))

# ⑤wait(func,timeout,return_when)
# wait函数可以返回一个元组，一个是执行完，一个是还没有执行完的任务
# return_when： ALL_COMPLETED：全部执行完成
# return_when：FIRST_COMPLETED:保证第一个任务执行完毕
# timeout=超时时间，如果超过了timeout，则阻塞，wait返回值。
# from concurrent.futures import as_completed,wait,ALL_COMPLETED,FIRST_COMPLETED
# if __name__=="__main__":
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         tasks=[executor.submit(doTask,i) for i in range(100)]
#         # tasks是即将要执行的任务列表
#         done,undone=wait(tasks,return_when=ALL_COMPLETED)
#         for i in done:
#             print("已完成{}".format(i))
#         for i in undone:
#             print("未完成{}".format(i))
# 从执行结果上来说，as_completed跟wait+ALL_COMPLETED是一样的，但是执行的过程不一样
#as_completed 执行完当前的进程之后，就往下继续执行。
#wait+ALL_COMPLETED 会一直等到所有进程全部执行完毕之后，才继续往下执行。
