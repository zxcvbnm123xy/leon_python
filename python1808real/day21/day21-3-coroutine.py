"""
三、协程
1. 相关概念
coroutine ：微线程
比线程还要小的执行单元

协程底层实现使用生成器 yield

协程的优势：
1. 协程具有极高的执行效率。子程序切换不是线程的切换，而是我们程序自己通过yield控制
   协程在执行上，几乎没有开销，并发数越多。

2. 协程没有线程的不安全问题。一个进程可以同时存在多个协程，但是只有一个协程是被激活。


协程缺点：
1. 无法利用多核资源，协程的本质仍然是单线程
2. 进行阻塞操作时，会阻塞掉整个程序（yield）

"""
# 2.协程的实现
# 生成器
# 生成器函数执行跟普通函数执行区别：
"""
(1) 调用的时候，不是执行函数，而是创建一个生成器对象
（2）程序执行到yield就会把执行权利交给调用者
（3）调用send或者next会继续从刚才暂停的位置继续执行
（4）生成器函数执行完毕之后，如果调用者仍然调用生成器函数的send或者next，会产生StopIteration
"""
# 大一点，小一点
# 主程序，生成器函数给主程序传递信息。
# send的参数===生成器yield表达式的内容
# send的返回值===生成器yield的产出值
# import time
# def gen():
#     msg=""
#     while True:
#         x=yield msg
#         if x==5:
#             msg="too big ,小一点"
#         elif x==1:
#             msg="too small ,大一点"
# g=gen()
# next(g)
# x=1
# while True:
#    time.sleep(0.5)
#    print(x)
#    msg=g.send(x)
#    if msg=="too small ,大一点":
#         x+=1
#    else:
#        x-=1

# 3. 协程的四个状态
# 新建  GEN_CREATED  : 协程等待开始执行，未激活
# 执行  GEN_RUNNING  : 协程正在运行，执行协程函数时
# 暂停  GEN_SUSPENDED :协程遇到yield暂停，在主程序中显示协程
# 关闭  GEN_CLOSED   :协程执行结束
# import inspect
# def simple_coroutine():
#     while True:
#         print("协程开始")
#         print("在simple_coroutine中协程的状态是{}".format(inspect.getgeneratorstate(my_coro)))
#         x=yield
#         print("协程获得x={}".format(x))
#
# my_coro=simple_coroutine()
# print("协程的状态是{}".format(inspect.getgeneratorstate(my_coro)))
#
# next(my_coro)
# print("协程的状态是{}".format(inspect.getgeneratorstate(my_coro)))
#
# my_coro.send(40)
# print("协程的状态是{}".format(inspect.getgeneratorstate(my_coro)))
# my_coro.close()
# print("协程的状态是{}".format(inspect.getgeneratorstate(my_coro)))

# 利用协程完成生产者、消费者。
# 生产骨头，消费者小狗吃骨头
"""
(1) 主程序一直生产骨头。。。。过程中有小狗过来吃骨头
（2）骨头数量>5，可以调用小狗send
"""
# import time
# li=[]
# def consume(name):
#     print("{}要开始啃骨头...".format(name))
#     while True :
#         n = yield
#         time.sleep(0.2)
#         print("{}正在啃{}".format(name,n))
#
# dog1=consume("tom")
# dog2=consume("jerry")
# dog1.send(None)
# dog2.send(None)
# if __name__=="__main__":
#     n=0
#     while True:
#         n+=1
#         li.append("骨头{}".format(n))
#         print("正在生产骨头{}".format(n))
#         time.sleep(1)
#         if len(li)>2:
#             dog1.send(li.pop())
#             dog2.send(li.pop())


# 关于yield
# def gen(a):
#     while True:
#         print("开始执行..")
#         b= yield a
#         print("a={},b={}".format(a,b))
#         c= yield a+b
#         print("a={},b={}，c={}".format(a, b,c))
#
# g=gen(5)
# next(g)
# g.send(6)
# g.send(7)


# 4. 协程的异常和关闭
# 协程对象.throw()抛出异常
# 协程对象.close() 关闭

# 协程对象.throw()抛出异常  能够让生成器在暂停的yield表达式处抛出指定的异常
#     如果生成器自己处理了异常，那么代码会向下继续执行到下一个yield。如果没有捕获，则
#    将异常向上抛出
# 如果没有在调用端抛出异常，则send的返回值是yield的产出值。
# 如果在调用端throw方法抛出异常，异常的返回值就是yield的产出值。

class MyException(Exception):
    pass
def gen_exp():
    print("开始执行")
    while True:
        try:
            x = yield 1
        except MyException:
            print("捕获了异常")
        else:
            print("send的传入参数是x={}".format(x))

g=gen_exp()
next(g)
g.send(10)
g.send(20)
print(g.throw(MyException))
g.send(30)


# 5. 协程返回值
"""
生成器的return返回值可以在生成器出现StopIteration的异常时，
调用者捕获异常时，通过异常对象可以获得
返回值：只有在生成器内部产生异常StopIteration的时候才有效果
# """
# def gen_return():
#     print("协程开始")
#     while True:
#        x=yield 1
#        if x==40:
#            break
#        print("传入的参数{}".format(x))
#     return "success"
# g=gen_return()
# next(g)
# g.send(10)
# try:
#     g.send(40)
# except StopIteration as err:
#     print(err)


#6. yield from
# yield from 相当于使用try ..except捕获了StopIteration的异常，获得生成器的return值
# 带有yieldfrom的生成器：委派生成器

# 两个作用
#（1） 代替for循环，代替在for循环中再次调用生成器，产出值。（简化）
# def gen():
#     for i in range(1,3):
#         yield i
#
# def gen_new():
#     # 使用for循环调用生成器
#     # for i in gen():
#     #     yield i
#
#     # 使用yield from调用生成器
#     yield from gen()
# # g=gen()
# # g.send(None)
# # print(next(g))
# # print(next(g))
# # print(list(gen()))
# print(list(gen_new()))


#（2） 带有yield from的生成器可以看是委托方。
#      调用另外一个子生成器，获得子生成器抛出异常时的返回值
# 需求：使用生成器求移动平均值。
# def averager():
#     total=0.0
#     count=0
#     avgvalue=None
#     while True:
#         i = yield avgvalue
#         total+=i
#         count+=1
#         avgvalue=total/count
#
# ag=averager()
# next(ag)
# li=[10,20,30,40,50,60]
# for i in li:
#     avgvalue=ag.send(i)
#     print(avgvalue)

# 如果需要求多组数据的移动平均值。只求每个班的平均成绩即可
"""
客户端      委托生成器     子生成器（一定要有return）

委托生成器可以获得子生成器的return返回值。（yield from内部处理了StopIteration的异常，获得了return值）
"""
# 子生成器
def averager():
    total=0.0
    count=0
    avgvalue=None
    while True:
        # i = yield avgvalue
        # 如果希望使用return值，那么必须在while循环内部设置break
        # 当所有人的成绩都计算完毕的时候(假定，如果传入的参数None，则代表计算完成)
        i = yield
        if i is None:
            break
        total+=i
        count+=1
        avgvalue=total/count
    return avgvalue

# yield from能够获得子生成器 return的值。
# 委派生成器(带有yield from的生成器)
# 传入一个字典，用来存储【班级：平均成绩】
def grouper(results,key):
    while True:
        results[key]=yield from averager()

#客户端
def client():
    data={"class_1":[70,80,90,100,100,55,67,88],
          "class_2":[76,84,93,100,50,56,91,88]}
    results={}
    for k,v in data.items():
        # 创建委派生成器对象
        coroutine=grouper(results,k)

        # 激活协程（一次性可以激活委派生成器和子生成器）
        next(coroutine)

        # 调用生成器send(成绩) 给委派生成器（由委派生成器再将i传给子生成器）传入每个成绩
        for i in v:
            coroutine.send(i)
        coroutine.send(None) # 通过传入None来让子生成器中执行break
    print(results)
client()

"""
使用yield from的注意事项：
（1） 方便调用其他生成器，一次性产出多个结果代替for
（2）客户端通过调用委派生成器来触发子生成器， 传入参数，得到return返回值
（3）子生成器接到参数后，一定要执行break，才能够return返回值。
     调用者一定要注意，最后一次调用send，一定是能够使得子生成器执行break条件的值。
"""
















