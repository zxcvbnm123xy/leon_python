# 二、线程
# 线程的概念，进程中的基本执行单元
# 已学过创建线程的方式：
# （1）使用init方法创建县城对象，指定taget
from threading import Thread
import time
def sum(a,b):
    s=0
    for i in range(a,b):
        s+=i
        return s
# def sum_1(b1,b2):
#     t1=Thread(target=sum,args=(0,b1))
#     t2=Thread(target=sum,args=(0,b2))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# if __name__ == "__main__":
#     start = time.time()
#     # sum_1(100000000,200000000)
#     # sum_1(10, 20)
#     end = time.time()
#     print("执行时间{}".format(end-start))

# 1.使用from multiprocessing.pool import ThreadPool 创建
# 进程模块下的线程池下 ，创建方式几乎跟进程池一致
from multiprocessing.pool import ThreadPool
# def work(index):
#     print("第{}任务执行".format(index))
#     return index

# pool= ThreadPool(5)
# for i in range(10):
#     pool.apply_async(work,args=(i,))
#     time.sleep(0.5)
#     # print("第{}任务执行完毕".format(i))
# pool.close()
# pool.join()

# 改写之前的案例
# def sum_2(b1,b2):
#     pool=ThreadPool(5)
#     for i in [b1,b2]:
#         pool.apply_async(work, args=(0,i))
#         pool.close()
#         pool.join()
#
# if __name__ == "__main__":
#     start = time.time()
#     sum_2(100000000,200000000)
#     # sum_1(10, 20)
#     end = time.time()
#     print("执行时间{}".format(end-start))

#2 使用threadpool模块实现线程对象（选讲）
# 进程下的线程池直接apply或者apply_async实现线程对象，一次加入一个对象
# threadpool
# 任务加入使用putRequest，在此之前需要使用makeRequest形成任务列表
"""
(1) 定义线程函数，创建线程池
（2）创建需要县城出处理的任务列表,makeREquest
（3）将创建的多个任务put到线程池中，等待cpu分配时间片执行
（4）希望所有任务执行完毕在操作threadpool.wait（）
"""
# import threadpool
# def work1(index):
#     print("任务{}正在执行".format(index))
#     return index

# if __name__=="__main":
#     pool=threadpool.ThreadPool(5)
    # 形成任务列表threadpool.makeRequests(func，args_list)
    # 参数 func：要使用多线程执行的任务，args_list要执行任务的函数的参数列表
    # """
    # 如果是单参数，则直接传入多个线程的参数【序列】即可
    # 如果是多参数，[（（参数1，参数2，参数3...），（关键字参数1，关键字参数2...）），（（））...]
    # 要求如果没有对应的参数（位置，关键字），需要None占位
    # """
    # request=threadpool.makeRequests(work1,args_list=range(10))
    # # 将多个任务put到线程池中，需要一个一个put
    # for r in request:
    #     pool.putRequest(r)
    #
    # # 使用wait保证子线程全部在主线程执行完毕之前执行
    # pool.wait()
    # print("主函数执行完毕")

# 应用到案例上
# Io密集型：
# 计算密集型：
# def sum_3(b1,b2):
#     pool=threadpool.ThreadPool(5)
#     arglist=[((0,b1),None),((0,b2),None)]
#     requests=threadpool.makeRequests(sum,args_list=arglist)
#     for r in requests:
#         pool.putRequest(r)
#     pool.wait()
# if __name__ == "__main__":
#     start = time.time()
#     sum_3(100000000,200000000)
#     # sum_1(10, 20)
#     end = time.time()
#     print("执行时间{}".format(end-start))

# 3.使用cincurrent.future模块下的ThreadPoolExecutor
# 跟进程基本一致
from concurrent.futures import ThreadPoolExecutor,as_completed
def sum_4(b1,b2):
    with ThreadPoolExecutor(max_workers=4) as executor:
        tasks=[executor.submit(sum,x,y) for x,y in [(0,b1),(0,b2)]]
        for i in as_completed(tasks):
            print(i.result())

if __name__ == "__main__":
    start = time.time()
    # sum_4(100000000,200000000)
    sum_4(10, 20)
    end = time.time()
    print("执行时间{}".format(end-start))















