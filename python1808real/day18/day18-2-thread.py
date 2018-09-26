"""
第十七章 线程
"""
# 一、相关概念
# 1. 同步和异步
# 同步和异步关注的是消息的通信机制，描述的是一种行为方式，多个任务之间的关系
# 同步：调用者主动等待被调用方，返回结果，在没有返回结果之前，就一直专职等待。
#       千万不要把计算机中“同步”理解成“同时执行”
# 异步：调用者发送请求请求，不会专职等待被调用方返回结果，当被调用方有结果之后，
#       再通知调用者，再继续执行刚才的任务。

# 2. 阻塞和非阻塞
# 描述的是一个任务的某一种状态
# 阻塞：调用者当调用了被调用者时，被调用者没有返回结果之前，调用者就一直等待，
        # 描述等待的这个状态，为阻塞状态。
# 非阻塞：调用者再没有得到被调用者返回结果之前，会去执行其他的任务，描述不会等待
        # 这个状态，为非阻塞。

# 概念的区分
"""
同步异步和阻塞与非阻塞

阻塞与非阻塞和同步与异步之间没有必然的联系，是两个概念 ，两个角度
阻塞是使用了同步机制的结果
非阻塞是使用了异步机制的结果。

非阻塞是不是一定就意味着异步？
# 不是，非阻塞只能决定当前任务的状态（可以不等着），是不是要去做其他的任务，不是由
#       非阻塞决定的，是由异步决定的。

阻塞是不是一定意味着任务之间一定不是异步关系？
# 是

# 异步是不是意味着当前的任务处于非阻塞状态？
# 是

# 同步一定也意味着某一个时刻，某一个任务处于阻塞状态。


3. 串行和并行
# 任务的执行方式
# 串行：多个任务时，各个任务按照顺序执行，执行完一个任务之后，才能执行下一个任务。
#      可以理解成同步的概念，两个任务是串行执行的===两个任务之间的关系是同步机制

# 并行：多个任务同时执行，意味着多个任务之间是异步机制。


4. 并行和并发
# 同时处理的含义，只有【并行】是真正意义上同时处理。
时间上：
  并行指的是多个时间同一个时刻发生。
  并发是多个事件在同一个时间间隔执行。其实是切换时间片轮流执行。微观的角度（串行）

作用点上：
  并行作用在多个实体上多个事件
  并发作用在一个实体上的多个事件

处理个数：
   并行，多个处理器处理多个任务
   并发，一个处理器处理多个任务
  
"""
#
# 5. IO密集型和计算密集型
# 程序（任务）的类型
# IO密集型：cpu占用率比较低，IO占用率比较高。
# Cpu密集型：cpu占用率高，IO占用率低。

# IO密集型更适合做并发处理。IO执行速度慢

# 6. 并发的三个层次
# 低阶：操作系统层面实现并发，一般是针对于一门语言的库编写，不是给程序员用，python不支持
# 中阶：几乎所有语言都支持中阶并发。
# 高阶：第三方模块执行并发操作。

# 7. 线程和进程
# 程序：程序可以看成一些列的指令集。静态的。
# 进程：当程序运行起来之后，创建一个（也可以是多个）进程。
# 线程：进程的基本执行单元，一个进程至少要一个线程。
# 进程可以看成是任务，比如洒水，扫地
# 线程就是基本的执行单元，执行任务的人。

# 一个线程只能属于一个进程
# 关于进程独立，线程共享的问题（重要）：
"""
进程具有独立的空间和系统资源，
线程没有独立的系统资源，
处于同一个进程下的线程共享该进程下的资源
一定要避免多线程（同一个进程下）资源出现的并发修改问题————————线程不安全。
"""


# 8. 多线程
# 【同时】：并发
# 多进程：多个任务同时执行
# 多线程：在同一个任务中，多个线程同时执行
# 处理：单核cpu处理IO密集型才有效果

# 多线程的缺点：
# （1）线程也是程序，也需要占用内存，设置的线程越多，占用内存就越多。
# （2）多线程需要协调管理，需要cpu时间跟踪，cpu也会被占用一部分。
# （3）最重要：多线程的共享资源不安全。导致数据不一致。


# 二、线程的创建
# 1. 使用threading模块创建线程（中阶的并发编程）（本章使用的方法）
# 2. 利用第三方模块（高阶并发编程）

# 本章涉及到threading模块创建线程分为两种模式：
# （1）threading.Thread创建线程对象，指定两个参数 target，args。
#  (2) 继承threading.Thread，重写run方法创建线程对象。
import threading,time
# 方式一：
# threading.Thread(target=,args=)
# target=要执行的函数名（要使用多线程实现执行函数）
# args=要执行函数的参数(以元组的形式传入)
# time.sleep算是IO程序
# def mission(end):
#     for i in range(end):
#         print(i)
#         time.sleep(0.5)
#
#
# t1=threading.Thread(target=mission,args=(10,))
# t2=threading.Thread(target=mission,args=(10,))
# 希望线程执行，需要将线程对象放到cpu的执行计划（执行列表）
# 对象.start
# start并不代表执行，只能代表将任务交给了cpu，cpu什么时候执行，由cpu说了算
# t1.start()
# t2.start()


# 方式二：继承threading.Thread
# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(10):
#             print(i)
#             # time.sleep(0.5)
#             # print(threading.current_thread())
#             # print(threading.get_ident())
#             # print(threading.main_thread())
#
# t1=MyThread()
# t2=MyThread()
# t1.start()
# t2.start()

# run方法才是真正执行线程中任务的方法。如果直接调用run方法，那么相当于让当前任务
# 串行执行。
# t1.run()
# t2.run()


# 三、线程的生命周期
# 1.新建：当新创建一个线程对象时，线程处于新建状态
# 2.就绪：执行start方法之后，线程处于就绪状态
# 3.运行：cpu将时间片分配给当前的线程对象，执行线程对应任务。
# 4.阻塞：因为某些条件没有满足，处于等待的过程中，cpu会将时间片分给其他的线程。
#         比如sleep(1)，当睡1s之后，只能代表当前线程被重新加入到cpu的执行列表中。
#         并不代表会马上执行。
# 5.死亡：当线程run方法执行完毕，或者run方法中抛出了异常没有被捕获，程序意外终止。

# 四、线程的相关操作
# 1 threading.active_count()  当前活跃线程数量，（处于就绪之后，死亡之前）
# print("当前活跃线程的数量",threading.active_count())

# 2.threading.enumerate() 返回一个列表，包含活跃的线程
# li=threading.enumerate()
# for i in li:
#     print(i)

# 3.threading.current_thread() 当前执行的线程
# print(threading.current_thread())

#4.threading.get_ident() 线程标志，一个序号，独一无二的序号

#5.threading.main_thread() 返回执行解释器的线程（主线程）
# 对于一个进程来说，只有一个主线程。 if __name__=="__main__":
# print(threading.main_thread())


#6. start 就绪，加入到cpu的执行列表中，等待执行
#7. run方法，当线程获得时间片之后，会执行的方法

#8. 线程对象.join(参数)
# 线程抢占。
# B.join（参数）  在A 线程中，如果调用了B线程的join方法，B线程抢占时间片
# 参数：抢占的时间，不写一直抢占时间片到B执行结束
# def mission():
#     print("休眠开始")
#     time.sleep(2)
#     print("休眠结束")
#
# t=threading.Thread(target=mission)
# t.start()
# t.join()
# print("主线程执行")

# 例子：修路的例子
# def mission():
#     print("修路开始")
#     print("修路过程中....")
#     time.sleep(2)
#     print("修路结束")
#
# t=threading.Thread(target=mission)
# print("start之前ident=",t.ident)
# t.start()
# print(t.is_alive())
# print("start之后ident=",t.ident)
# t.name="过马路的线程"
# print("想要过马路")
# t.join()
# print("路修好了，可以过马路。。。。")
# print(t.name)
# print(t.is_alive())

# 9.name 线程中的一个私有属性，线程名字
# get和set ，被property化

# 10.ident 线程标志  属性，get_ident  ===ident
# 被propery化 。没有提供set方法
# 只有线程start启动之后，才有ident标志

# 11. is_alive 判断是否存活

# 12.daemon 设置是否是守护线程（后台线程）
# 守护线程
# 有一个唱歌，乐队伴奏
# 两种情况
"""
(1)将乐队伴奏设置为非守护线程（默认，前台线程）谁也不谁（cpu采用异步模式对待每个线程）
唱歌的人唱完了，乐队伴奏如果还没有伴奏完毕，会继续伴奏


（2）将乐队线程设置为守护线程
唱歌的人唱完了，乐队伴奏不管有没有演奏完毕，都不会继续伴奏

如果将一个线程设置成守护线程：意味着告诉处理器，
不用顾及当前的这个线程，当其他的非守护线程 退出的时候，守护线程也会跟着退出。
python中垃圾回收机制，使用守护线程
"""
# def music():
#     print("乐队线程开始执行")
#     time.sleep(1)
#     print("乐队持续在伴奏")
#     print("乐队持续在伴奏")
#     print("乐队持续在伴奏")
#     print("乐队持续在伴奏")
#     print("乐队持续在伴奏")
#     print("乐队结束")
# if __name__=="__main__":
#     mt=threading.Thread(target=music)
#     # 守护线程需要在start之前设置
#     mt.setDaemon(True)
#     mt.start()
#     print("开始唱歌")
#     print("唱歌中...")
#     print("唱歌结束")


# 五、线程同步
# 解决：多线程中出现的资源共享问题。
# 1. 并发修改出现问题
# 票就是共享资源
# ticket=100
# def buy_ticket():
#     global ticket
#     while ticket>0:
#         time.sleep(0.5)
#         print("{}抢到了第{}票".format( threading.current_thread().name,ticket))
#         ticket-=1
#
# t1=threading.Thread(target=buy_ticket)
# t1.name="张三"
# t2=threading.Thread(target=buy_ticket)
# t2.name="李四"
# t3=threading.Thread(target=buy_ticket)
# t3.name="王五"
# t1.start()
# t2.start()
# t3.start()



#2. 线程锁
# 希望在同一个时间点内，一片共享资源只希望被一个线程访问。
# 方式
# lock=threading.Lock()
# 加锁
# lock.acquire()
# 解锁
# lock.release()

#第一次解决: while循环可能同时进入了其他两个线程
# ticket=100
# lock=threading.Lock()
# def buy_ticket():
#     global ticket
#     while ticket>0:
#         lock.acquire()
#         # time.sleep(0.5)
#         print("{}抢到了第{}票".format( threading.current_thread().name,ticket))
#         ticket-=1
#         lock.release()
#
# t1=threading.Thread(target=buy_ticket)
# t1.name="张三"
# t2=threading.Thread(target=buy_ticket)
# t2.name="李四"
# t3=threading.Thread(target=buy_ticket)
# t3.name="王五"
# t1.start()
# t2.start()
# t3.start()

# 第二次  问题原因：张三进入之后加锁，循环将所有的排票都抢完毕
# ticket=100
# lock=threading.Lock()
# def buy_ticket():
#     global ticket
#     lock.acquire()
#     while ticket>0:
#         # time.sleep(0.5)
#         print("{}抢到了第{}票".format( threading.current_thread().name,ticket))
#         ticket-=1
#     lock.release()
#
# t1=threading.Thread(target=buy_ticket)
# t1.name="张三"
# t2=threading.Thread(target=buy_ticket)
# t2.name="李四"
# t3=threading.Thread(target=buy_ticket)
# t3.name="王五"
# t1.start()
# t2.start()
# t3.start()

# 第三次： 没有人解最后锁
# ticket=100
# lock=threading.Lock()
# def buy_ticket():
#     global ticket
#     while True:
#         lock.acquire()
#         if ticket>0:
#             # time.sleep(1)
#             print("{}抢到了第{}票".format( threading.current_thread().name,ticket))
#             ticket-=1
#         else:
#             break
#         lock.release()
#
# t1=threading.Thread(target=buy_ticket)
# t1.name="张三"
# t2=threading.Thread(target=buy_ticket)
# t2.name="李四"
# t3=threading.Thread(target=buy_ticket)
# t3.name="王五"
# t1.start()
# t2.start()
# t3.start()

# 第四次
ticket=100
lock=threading.Lock()
def buy_ticket():
    global ticket
    while True:
        try:
            lock.acquire()
            if ticket>0:
                time.sleep(0.2)
                print("{}抢到了第{}票".format( threading.current_thread().name,ticket))
                ticket-=1
            else:
                break
        finally:
            lock.release()

t1=threading.Thread(target=buy_ticket)
t1.name="张三"
t2=threading.Thread(target=buy_ticket)
t2.name="李四"
t3=threading.Thread(target=buy_ticket)
t3.name="王五"
t1.start()
t2.start()
t3.start()