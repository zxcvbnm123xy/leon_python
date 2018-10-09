# 1.携程对象需要每次调用的时候，先激活
# 装饰器：扩展函数功能
# （1）装饰器（闭包函数） （2）调用装饰器，在被装饰函数上面@
# def alive(funcname):
#     def inner(*args,**kwargs):
#         g=funcname(*args,**kwargs) # 声称其对象
#         g.send(None)
#         return g
#     return inner
#
# @alive
# def gen():
#     print("协程开始")
#     while True:
#         x=yield
#         print("x={}".format(x))
# g=gen()
# # next(g)
# g.send(10)
# g.send(20)

# 2.小狗吃骨头的问题，使用协程实现，一共有两只小狗
# 一个生产者，当骨头数>5的时候，小狗可以啃骨头
# 但是每一次只有一只小狗吃骨头，随机选择小狗
import random,time
# def consume(name):
#     print("{}要开始啃骨头".format(name))
#     while True:
#         bone=yield
#         print("{}正在啃{}骨头".format(name,bone))
#         time.sleep(0.2)
#         li.remove(bone)
#
# li=[]
# n=0
# dog1=consume("tome")
# dog2=consume("jerry")
# dog1.send(None)
# dog2.send(None)
#
# while True:
#     n+=1
#     li.append("骨头{}".format(n))
#     time.sleep(1)
#     print("已生产骨头{}".format(n))
#     if len(li)>5:
#         dog=random.choice([dog1,dog2])
#         dog.send(random.choice(li))
#         # dog2.send(random.choices(li))

# 3.使用子生成器，委派生成器获得多组数据的平方和
# yield from 的生成器是委派生成器
# 委派生成器可以调用子生成器，委派生成器可以获得子生成器返回值的内容
# 子生成器
# [[3,4,5],[5,6],[7,8,9,10]]
# def powsum():
#     s=0
#     while True:
#         i=yield
#         if i is None:
#             break
#         s+=i**2
#     return s
#
# # 委派生成器
# def grouper(li):
#     while True:
#         r=yield from powsum()
#         li.append(r)
#
# # 客户端
# data=[[3,4,5],[5,6],[7,8,9,10]]
#
# # 调用委派生成器，产生委派生成器对象
# li=[]
# for i in data:
#     coroutine=grouper(li)
#
#     # 激活委派生成器(可以同时激活委派生成器和子生成器)
#     # coroutine.send(None)
#     next(coroutine)
#     for j in i :
#         coroutine.send(j)
#     coroutine.send(None)
# print(li)

# 4.threadpool 得到线程返回值的方法
def task(index):
    print("任务{}开始执行".format(index))
    time.sleep(0.5)
    return "success{}".format(index)
# threadpool 线程获得返回值的方式，需要设置回调函数
# 调用回调函数makeRequests，指定callback=回调函数名字
def callback(request,result):
    print("线程返回值{}".format(result))

import threadpool
pool=threadpool.ThreadPool(5)
requests=threadpool.makeRequests(task,range(10),callback=callback)
for i in requests:
    pool.putRequest(i)
pool.wait()



















