"""
第十九章  线程

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
lock=threading.Condition()

def produce(li):
    i=0
    while  True:
        try:
            lock.acquire()
            if len(li)==3:
                print("仓库已满，生产阻塞")
                lock.wait()
            else:
                li.append("商品{}".format(i))
                i+=1
                print("生产了{}商品".format(i))
                lock.notify_all()
        finally:
            lock.release()

def consume(li):
    while True:
        try:
            lock.acquire()
            if  len(li)==0:
                print("仓库已空，消费阻塞")
                lock.wait()
            else:
                print("消费了{}商品".format(li.pop(0)))
                lock.notify_all()
        finally:
            lock.release()

li=[]
t1=threading.Thread(target=produce,args=(li,))
t2=threading.Thread(target=consume,args=(li,))
t1.start()
t2.start()