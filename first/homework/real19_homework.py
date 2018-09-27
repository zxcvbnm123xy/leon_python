# 1.使用两个进程，对同一个全局变量进行修改多次，会出现什么情况。
import multiprocessing,os
a=0
def mission():
    global a
    for i in range(100000):
        a+=1
    print("{}进程中的a={}".format(os.getppid(),a))

if __name__=="__main__":
    p1=multiprocessing.Process(target=mission)
    p2=multiprocessing.Process(target=mission)
    p1.start()
    p2.start()
    print("在进程外侧的a={}".format(a))
# 在进程下，对于系统资源都不是共享。

# 2.使用进程队列完成生产者消费者的例子 multiprocess下queues
from multiprocessing import Process,Queue
import random,time
def produce(q):
    fruits = ("三明治", "蛋糕", "饮料")
    while True:
        a=random.choices(fruits)
        q.put(a)
        print("生产了{}".format(a))
        time.sleep(0.1)
def consume(q):
    while True:
        print("消费了{}".format(q.get()))
        time.sleep(0.5)
if __name__=="__main__":
    q=Queue(3)
    q1=Process(target=produce,args=(q,))
    q2=Process(target=consume,args=(q,))
    q1.start()
    q2.start()
    
#   3.自己实现tcp的scoket编程。在with语句体中，使用open打开要传送的文件，
#     使用socket对象下的sendfile函数发送文件。读取的时候，使用recv读取即可。