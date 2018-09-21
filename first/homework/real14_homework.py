from collections.abc import Iterable
from datetime import datetime
import time
import math
# 1.是否所有的可迭代对象都是Iterable的实例呢？ __getitem__
def q1():
    class I:
        def __getitem__(self, item):
            return item
    i = I()
    print(isinstance(i, Iterable))
    for j in i:
        time.sleep(5)
        print(j)

# 2.使用生成器，生成2 ~ 100内所有的质数。
def q2_1():
    def gen():
        for i in range(2,100):
            for j in range(2,int(math.sqrt(i))+1):
                if i%j==0:
                    break
            else:
                yield i
    g=gen()
    for  item in g:
        print(item)
#s 生成器
def q2_2():
    def gen():
        msg=""
        while True:
            i=yield msg
            for j in range(2,int(math.sqrt(i))+1):
                if i%j==0:
                    msg="n"
                    break
            else:
                msg="y"
    g=gen()
    g.send(None)
    for i  in range(2,100):
        msg=g.send(i)
        if msg=="y":
            print(i)

# 3.为现有函数增加一个执行时间的功能，前提是不能修改函数体，也不能修改函数的调用方式。（使用两种方式实现）
# 日志中：执行的时间点，函数的执行时间，函数的参数，返回值
def q3():
    def log(funname):
        def inner(*args,**kwargs):
            start=time.time()
            r=funname(*args,**kwargs)
            end=time.time()
            fn=funname.__name__
            opertime=datetime.now()
            a=b=None
            if args:
                a="; ".join([str(i) for i in args])
            if kwargs:
                b=" ; ".join(["{}={}".format(k,v) for k,v in kwargs.items()])
            text="""
            当前方法的名字{}
            当前方法传入的参数是{}和{}
            当前方法操作的时间{}
            当前方法执行的时间{}
            当前方法的返回值{}
            """
            print(text.format(fn,a,b,opertime,end-start,r))
            return r
        return inner
    @log
    def add(user):
        print("执行添加方法")
        time.sleep(1)
        return "添加成功"
    @log
    def modify(user):
        print("执行修改方法")
        time.sleep(0.5)
        return "修改成功"
    add("张三")
    modify("李四")

# 4.在课堂案例基础上，当我做增删改的时候，我必须是登录后才能做，目前登录验证可以不到数据库中验证，只要验证用户名是admin，密码是123就可以看成是登录成功。使用装饰器函数实现即可。
#
#
def q4():
    login_status=False
    def login(funname):
        _username="admin"
        _password="123"
        def inner(*args, **kwargs):
            r=None
            global login_status
            if login_status==False:
                username = input("请输入一个用户名：")
                password = input("请输入一个密码：")
                if username==_username and password==_password:
                    print("您好，登录成功")
                    r=funname(*args, **kwargs)
                    login_status=True
                else:
                    print("对不起，用户名或者密码错误")
            else:
                print("您已登录， 请继续执行操作")
                r = funname(*args, **kwargs)
            return r
        return inner

    def log(funname):
        def inner(*args,**kwargs):
            print("这是日志的start")
            start=time.time()
            r=funname(*args,**kwargs)
            end=time.time()

            fn=funname.__name__

            opertime=datetime.now()

            #参数
            a=b=None
            if args:
                a="; ".join([str(i) for i in args])
            if kwargs:
                b=" ; ".join(["{}={}".format(k,v) for k,v in kwargs.items()])
            text="""
            当前方法的名字{}
            当前方法传入的参数是{}和{}
            当前方法操作的时间{}
            当前方法执行的时间{}
            当前方法的返回值{}
            """
            print(text.format(fn,a,b,opertime,end-start,r))
            return r
        return inner
    @login
    @log
    def add(user):
        print("执行添加方法")
        time.sleep(1)
        return "添加成功"

    @login
    @log
    def modify(user):
        print("执行修改方法")
        time.sleep(0.5)
        return "修改成功"

    add("张三")
    modify("李四")

# 5.编写一个程序，初始为传入一个点的坐标，然后可以对该点进行移动。在多次移动时，能够保留上一次移动的结果。（使用两种方式实现）
# 闭包函数，闭包类
# 闭包，用上一次的变量
#
# x,y
# (1,1)
# (2,3)---3,4
# (-1,-1)--2,3
#
def move(x,y):
    def inner(run_x,run_y):
        nonlocal x,y
        x+=run_x
        y+=run_y
        print("移动了位置{}，{}".format(x,y))
    return inner
m=move(0,0)
m(12,-15)
m(10,9)

# 6.课堂的大一点小一点的例子重新用另一种思路实现
def gen():
    x=1
    while True:
        msg =yield x
        print(x)
        if msg=="too big,小一点":
            x-=1
        else:
            x+=1
g=gen()
next(g)
msg=""
while True:
    x=g.send(msg)
    if x==5:
        msg="too big,小一点"
    else:
        msg="too small,大一点"
