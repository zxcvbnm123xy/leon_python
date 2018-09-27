"""
第十七章  线程

六、死锁
死锁的定义：当两个或者多个线程同时拥有自己的资源，又互相等待对方的资源，
           导致程序永远先入僵持状态
"""
# 共有两把锁
# A----锁1-----希望拥有锁2
# B----锁2-----希望拥有锁1

# 多线程并发访问数据的时候，要在共享资源上加锁。如果加的锁不只一把，可能会出现死锁
import threading,time
# lock1=threading.Lock()
# lock2=threading.Lock()
#
# def mission(l1,l2): #l1,l2代表传入的两把锁
#     l1.acquire()
#     print("{}获得了{}".format(threading.current_thread().name,id(l1)))
#     time.sleep(1)
#     l2.acquire()
#     l1.release()
#     l2.release()
# a=threading.Thread(target=mission,args=(lock1,lock2))
# b=threading.Thread(target=mission,args=(lock2,lock1))
# a.start()
# b.start()


# 七、通知和等待
# 抢票，一个资源（生产者），多个线程共享。
# 生产者和消费者。
# 使用from threading import  Condition 的锁，不仅有获取和释放的方法
# 还有
# wait     :等待， 会释放当前线程占用的锁（跟time.sleep不一样，sleep，不释放锁）
# notifyall：通知所有等待的线程加入cpu执行列表
# notify方法：任选一个等待线程，加入cpu执行列表

# 需求
# 生产者：生产商品，让商品+1，定义一个列表仓库，每次列表中加入一个元素，当做生产一个商品
# 消费者：消费商品，让商品-1，让列表中元素被删除
# 条件：仓库只能容纳3件商品。
# 当供过于求：生产者生产太快，商品在仓库中达到3件之后，生产者不能再生产，需要被阻塞
             # 被唤醒的时机：只有要商品被消费了
# 求大于供：消费者消费太快，商品在仓库中0个，消费者就不能再消费，需要被阻塞
#            # 被唤醒的时机：只要有商品被生产了

from threading import Condition
# lock=threading.Condition()
#
# def produce(li):
#     i=0
#     while  True:
#         try:
#             lock.acquire()
#             if len(li)==3:
#                 print("仓库已满，生产阻塞")
#                 lock.wait()
#             else:
#                 li.append("商品{}".format(i))
#                 i+=1
#                 print("生产了{}商品".format(i))
#                 lock.notify_all()
#         finally:
#             lock.release()
#
# def consume(li):
#     while True:
#         try:
#             lock.acquire()
#             if  len(li)==0:
#                 print("仓库已空，消费阻塞")
#                 lock.wait()
#             else:
#                 print("消费了{}商品".format(li.pop(0)))
#                 lock.notify_all()
#         finally:
#             lock.release()
#
# li=[]
# t1=threading.Thread(target=produce,args=(li,))
# t2=threading.Thread(target=consume,args=(li,))
# t1.start()
# t2.start()


# 八、队列（线程）
# 队列数据类型，内部实现了锁的机制，队列多用于多线程的并发
# 队列分为三种：
"""
先进先出队列：队列
先进后出队列：堆栈
优先队列：按照优先级出队列
"""
# import queue
# #（1）先进先出队列
# #queue.Queue(size):size=0或者负数，表示无限容量，如果size有值，代表最大容量
# q=queue.Queue(3)
# # 通过q.qsize() 返回队列中元素的格式
# print(q.qsize())
# # q.empty队列是否为空
# print(q.empty())
# # q.full() 判断队列是否已满
# print(q.full())
# # q.put向队列中添加元素
# # item:要添加的元素
# # block：继续向队列中添加元素的时候，如果队列已满，put方法是否是处于阻塞状态（默认True）
# # block如果=False，当队列已满的时候 ，再继续添加元素，则会报错。
# # timeout：队列已满，如果在指定的时间内（单位：秒），仍然无法添加元素，则会产生异常
# q.put("hello")
# q.put("world",block=False)
#
# #put_nowait 代表只要队列已满，put函数执行的时候会报错。
# # q.put_nowait(item)  # 等价于put(item,block=False)
#
# # q.get() 向外取元素（规则就是先进先出）
# q.put("python")
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

# 如果队列是空队列，继续向外get元素，get方法是默认的阻塞函数。用法跟put中一样。
# q.get(block=False)
# q.get_nowait()====q.get(block=False)


# （2）先进后出，堆栈
# lq=queue.LifoQueue()
# lq.put(1)
# lq.put(2)
# lq.put(3)
# # print(lq.get())
# # print(lq.get())
# # print(lq.get())
# # print(lq.get())
# while not q.empty():
#     print(q.get())

# （3）优先队列
# 不是按照传统队列的先进先出，或者后进先出，而是根据队列的优先级别进行排列
# 进的时候，正常进入 ，出的时候是按照优先级别出
# 优先级队列中的元素必须支持元素之间的比较。
# print("abc"<"bcd")
# print((1,2,4)<(3,4))
# q=queue.PriorityQueue()
# q.put("clock")
# q.put("banana")
# q.put("egg")
# q.put("apple")
# while not q.empty():
#     print(q.get())
#
# q.put((1,2,3))
# q.put((2,2,3))
# q.put((3,2,3))
# q.put((-1,2,3))
# while not q.empty():
#     print(q.get())
#
#
# q=queue.PriorityQueue()
# q.put((2,"clock"))
# q.put((1,"banana"))
# q.put((3,"egg"))
# q.put((4,"apple"))
# # q.put("a") #
# while not q.empty():
#     print(q.get())


# 应用队列实现生产者和消费者的例子
import queue
import threading
def produce(q):
    i=1
    while True:
        q.put(i)
        print("生产商品{}".format(i))
        i+=1
        time.sleep(0.5)

def consume(q,name):
    while True:
        print("{}消费了{}".format(name,q.get()))
        time.sleep(0.1)
# 队列本身创建的时候就有容量的设置
q=queue.Queue(3)
t1=threading.Thread(target=produce,args=(q,))
t2=threading.Thread(target=consume,args=(q,"tom"))
t3=threading.Thread(target=consume,args=(q,"jerry"))
t1.start()
t2.start()
t3.start()