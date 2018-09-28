# 二、线程
# 线程的概念：进程中的基本执行单元。
# 已学过创建线程的方式：
#(1) 使用init方法创建线程对象，指定target和args
#（2）继承Thread，重写run方法
from threading import Thread
#使用Thread完成案例
# IO密集型 10.5s
# 计算密集型  1.7s
import time
def sum(a,b):
    s=0
    for i in range(a,b):
        s+=i
        time.sleep(0.5)
    return s
# def sum_1(b1,b2):
#     t1=Thread(target=sum,args=(0,b1))
#     t2=Thread(target=sum,args=(0,b2))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
# if __name__=="__main__":
#     start = time.time()
#     sum_1(10000000,20000000)
#     # sum_1(10,20)
#     end=time.time()
#     print("执行的时间{}".format(end - start))

# 1. 使用from multiprocessing.pool import ThreadPool 创建线程
# 进程模块下的线程池，创建方式几乎跟进程池一致
from multiprocessing.pool import ThreadPool
# def work(index):
#     print("第{}任务执行".format(index))
#     time.sleep(0.5)
#     return index
#
# pool=ThreadPool(5)
# for i in range(10):
#     pool.apply_async(work,args=(i,))
#     # print("任务{}执行完毕".format(i))
# pool.close()
# pool.join()

# 改写之前的案例
# 计算密集型：1.91
# io密集型：10.5
# def sum_2(b1,b2):
#     pool = ThreadPool(5)
#     for i in [b1,b2]:
#         pool.apply_async(sum, args=(0,i))
#     pool.close()
#     pool.join()

# if __name__=="__main__":
#     start=time.time()
#     # sum_2(10000000,20000000)
#     sum_2(10,20)
#     end=time.time()
#     print("执行的时间{}".format(end - start))

#2. 使用threadpool模块实现线程对象(选讲)
# 进程下的线程池直接apply或者applyasync实现线程对象，一次加入一个任务
# threadpool
# 任务加入使用putRequest，在此之前需要使用makeRequests形成任务列表。
"""
(1)定义线程函数，创建线程池
（2）创建需要线程池处理的任务列表,makeRequest
（3）将创建的多个任务put到线程池中，等待cpu分配时间片执行
（4）希望所有任务执行完毕再操作threadpool.wait()
"""
import threadpool
# def work(index):
#     print("任务{}正在执行".format(index))
#     time.sleep(0.5)
#     return index
#
# if __name__=="__main__":
#     pool=threadpool.ThreadPool(5)
#
#     #形成任务列表：threadpool.makeRequests(func，args_list)
#     # 参数 func:要使用多线程执行的任务，args_list=函数的参数列表
#     """
#     如果是单参数，则直接传入多个线程的参数[序列]即可
#     如果是多参数，[((参数1，参数2...),(关键字参数1，关键字参数2)),(),()....]
#      要求如果没有对应的参数（位置、关键字），需要None占位
#     """
#     requests=threadpool.makeRequests(work,args_list=range(10))
#     # 将多个任务put到线程池中，需要一个一个put4
#     for r in requests:
#         pool.putRequest(r)
#
#     # 使用wait保证子线程全部在主程序执行完毕之前执行
#     pool.wait()
#     print("主程序执行完毕")

# 应用到案例上
# IO密集型：10.6s
# 计算密集型：1.74s
def sum_3(b1,b2):
    pool=threadpool.ThreadPool(5)
    arglist=[((0,b1),None),((0,b2),None)]
    requests=threadpool.makeRequests(sum,args_list=arglist)
    for r in requests:
        pool.putRequest(r)
    pool.wait()
# if __name__=="__main__":
#     start=time.time()
#     sum_3(10000000,20000000)
#     # sum_3(10,20)
#     end=time.time()
#     print("执行的时间{}".format(end - start))

# 3.使用concurrent.futures模块下ThreadPoolExecutor创建线程
# 跟进程基本一致
# 计算密集型：1.73s
# io密集型：10s
from concurrent.futures import ThreadPoolExecutor,as_completed
def sum_4(b1,b2):
    with ThreadPoolExecutor(max_workers=4) as executor:
        tasks=[executor.submit(sum,x,y) for x,y in [(0,b1),(0,b2)]]
        for i in as_completed((tasks)):
            print(i.result())

        # results = executor.map(sum, (0, 0), (b1, b2))
        # for i in results:
        #     print(i)
if __name__=="__main__":
    start=time.time()
    # sum_4(10000000,20000000)
    sum_4(10,20)
    end=time.time()
    print("执行的时间{}".format(end - start))
