"""
三、协程
"""
# 案例：仿真出租车系统：出库，载客，卸客，载客，卸客，载客，卸客，回家
# 使用协程实现，一个出租车是一个协程，多个携程并发
"""
分析：
1.一个出租车，出库，N次载客/卸客，回家
2.如果是多个出租车，每个出租车都有自己的时间轴，同时所有的出租车都有统一一个总时间
"""
# 1.1号出租车 ==出库==
# 2 2号出租车 ==出库==
# 5 1豪车     ==载客==
# 7 一号车    ==卸客==
# 命名元祖
import collections
# Event=collections.namedtuple("Event","time,texiNum,action")
# trips 载客的次数
# texi出租车编号
# start_time 初试时间
# send的参数时yield表达式的内容，希望每次的时间都是通过send传入
# 考虑一台车
# def taxi_process(texiNum,tripsNums,start_time=0):
#     time=yield Event(start_time,texiNum,"==出库==")
#
#     for i in range(tripsNums):
#         time = yield Event(time,texiNum,"==载客==")
#         time = yield Event(time,texiNum,"==卸客==")
#     yield Event(time,texiNum,"==回家==")
#
# if __name__=="__main__":
#     # 1号出租车，载客一次，0点开始出库
#     t1=taxi_process(1,1)
#
#     # 激活
#     a=next(t1)
#     print(a)   # 出库
#
#     # 第一次载客,传入的时间=上一次的时间+随机数（目前先自己写）
#     b=t1.send(a.time+5)
#     print(b)  #  第一次载客
#
#     # 第一次卸客
#     c=t1.send(b.time+8)
#     print(c)  # 第一次卸客
#
#     # 回家
#     d=t1.send(c.time+10)
#     print(d)

# 多台出租车
"""
1.三台车
t1=taxi_process(1,3,0）
t2=taxi_process(2,6,2）
t3=taxi_process(3,10,5）

2.三台车（三个协程对象）

3.要指定任务执行的时间表（优先队列）

4.当执行完一次操作（send），要继续讲该车的下一次时间加入时间列表

"""
Event=collections.namedtuple("Event","time,texiNum,action")
def taxi_process(texiNum,tripsNums,start_time=0):
    time=yield Event(start_time,texiNum,"==出库==")

    for i in range(tripsNums):
        time = yield Event(time,texiNum,"==载客==")
        time = yield Event(time,texiNum,"==卸客==")
    yield Event(time,texiNum,"==回家==")

import queue,random
class SimulatTaxi:
    def __init__(self,texis):
        # texis字典，多个协程（3台车）的字典
        self.texis=texis
        # events事件的时间表（优先队列）
        self.events=queue.PriorityQueue()
    def run(self):
        # 激活
        for k,v in self.texis.items():
            leaveEvent=next(v)
            # 把事件放入时间表，不是直接执行，最后的执行是按照时间表中的顺序执行的
            self.events.put(leaveEvent)

        while True:
            # 如果字典中所有车都回家（没有车了）break
            if self.events.empty():
                print("计算机仿真结束")
                break
            # 获取时间表中的第一个值get
            opertime,texinum,action=self.events.get()
            print("执行时间点{}，车租车编号{}，{}".format(opertime,texinum,action))

            # 准备当前车的下一个事件
            # 当前车的对象（先找到当前车存在self.texis）
            currenttexi=self.texis[texinum]
            next_oper_time=opertime+random.randint(1,20)
            try:
                nextEvent=currenttexi.send(next_oper_time)
            except StopIteration:
                del self.texis[texinum]
            else:
                self.events.put(nextEvent)


# if __name__=="__main__":
#     # 1号出租车，载客一次，0点开始出库
#     texis={1:taxi_process(1, 3, 0),
#            2:taxi_process(2, 6, 2),
#            3:taxi_process(3, 10, 5)}
#
#     # 定义模拟运行的类，调用类中的实例方法来完成模拟
#     st=SimulatTaxi(texis)
#     st.run()

    # # 激活
    # a=next(t1)
    # print(a)   # 出库
    #
    # # 第一次载客,传入的时间=上一次的时间+随机数（目前先自己写）
    # b=t1.send(a.time+5)
    # print(b)  #  第一次载客
    #
    # # 第一次卸客
    # c=t1.send(b.time+8)
    # print(c)  # 第一次卸客
    #
    # # 回家
    # d=t1.send(c.time+10)
    # print(d)

# 四、Asyncio模块
# 1.相关概念和方法：
# （1）协程函数：Asyncio通过创建协程函数，来创建协程对象。
#               协程对象执行的时候，需要先将携程对象注册（加入）到【事件循环】
#               再由事件循环进行调用
#               【事件循环】：程序开启了一个无线的循环，程序员会将一系列函数加入到事件循环上，
#                当事件循环运行时，协程才可以运行（可以理解仿了cpu）
# （2）待执行任务（task任务，future）：待执行任务
# （3）async关键字：用来定义协程函数的
# （4）iscorutinfunction：用来判断是否是协程函数。
# （5）get_event_loop 事件循环
# （6）await：关键字，用于挂起当前的协程。先走awiat 关键字后面的协程（相当于yeild）
# （7）sleep：协程的slepp，本身是协程
# （8）ensunre_future:将协程对象加入到计划函数中执行。
# （9）loop.run_until_complete:执行方式，直到所有任务结束后才会返回
# （10）add_done_callback:调用回调函数

# Asyncio模块 3.4版本加入到开发包中 pip insatll 模块

# 2.具体实现
# （1）定义协程
# 定义协程需要在函数前家async关键字------协程函数-----调用协程函数后，会产生携程对象
# import asyncio
# async def do_some_work():
#     pass
#
# print(asyncio.iscoroutinefunction(do_some_work))

# (2) 协程执行
"""
可以用两种方式：
协程可以自己注册到事件循环来执行
await的方式等待执行（在另外一x个协程中，调用当前协程，需要通过await）
"""
# 方式一：通过在另外一些协程函数中被await调用：
import asyncio
async def do_some_work(x):
    print("开始执行")
    await asyncio.sleep(x)
    print("执行结束，x={}".format(x))

print(asyncio.iscoroutinefunction(do_some_work))

# 方式二：注册到事件循环
# （1）先让程序开启一个无限循环对象，使用get_event_loop,获得事件循环
loop=asyncio.get_event_loop()
# （2）将要执行的协程，加入到要执行任务计划中。使用ensure_future()
# asyncio.ensure_future(要执行的协程名(参数))
# ensure_future 一次只能将一个协程对象加入到执行计划
f=asyncio.ensure_future(do_some_work(3))

# （3）需要执行，执行之前，需要先执行执行方式：
# 方式一般来说run_until_complete(只接受一个协程计划)
loop.run_until_complete(f)






