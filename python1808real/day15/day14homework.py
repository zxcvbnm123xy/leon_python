# 1.是否所有的可迭代对象都是Iterable的实例呢？ __getitem__
# from collections.abc import Iterable
# import time
# class I:
#     def __getitem__(self, item):# __getitem__跟目前使用__iter__和__next__放在一起使用很像
#         # return item  # item就是迭代对象的索引
#         if item<100:
#             return item
#         else:
#             raise StopIteration()
# i=I()
# print(isinstance(i,Iterable))

# for j in i:
#     # time.sleep(1)
#     print(j)


# 2.使用生成器，生成2 ~ 100内所有的质数。
# 方式一：
import math
def gen():
    for i in range(2,101):
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                break
        else:
            # print(i)
            yield i
g=gen()
for i in g:
    print(i)

# 方式二
# （1）主思路：从2-100输出这些数
# （2）生成器：判断是否是质数的生成器对象
# （3）产出值：msg信息（判断是否是质数的标志）
      #yield表达式的值（send的传入参数）：从2到100的所有数

# def gen():
#     msg=""
#     while True:
#         i= yield msg
#         for j in range(2,int(math.sqrt(i))+1):
#             if i%j==0:
#                 msg="n"
#                 break
#         else:
#             msg="y"
#
# g=gen()
# g.send(None)
# for i in range(2,101):
#     msg=g.send(i)
#     if msg=="y":
#         print(i)

#
# 3.为现有函数增加一个执行时间的功能，前提是不能修改函数体，也不能修改函数的调用方式。
# （使用两种方式实现）日志中：执行的时间点，函数的执行时间，函数的参数，返回值
# 使用装饰器去扩展已有功能
"""
实现装饰器的步骤：
1. 实现装饰器的功能，使用闭包函数实现。外围函数的参数一定是被装饰函数的名字（形式参数）
2. 将装饰器装饰在原函数上 @ 装饰器名
"""
# from datetime import datetime
# import time
# def log(funcname):
#     def inner(*args,**kwargs):
#         print("这是程序的日志：")
#         # 传入的参数 *args,**kwargs ，处理成字符串
#         a=b=""
#         if args:
#             # map(func,可迭代对象)  map(str,args)  "张三;20；
#             a=";".join([str(i) for i in args])
#         if kwargs:
#             b=";".join(["{}:{}".format(k,v) for k,v in kwargs.items()])
#
#         # 操作时间
#         opertime=datetime.now()
#         # 执行时间
#         start=time.time()
#         result=funcname( *args,**kwargs)
#         time.sleep(0.5)
#         end=time.time()
#
#         # 函数名
#         fn=funcname.__name__
#
#         text="""
#         当前方法的名字{}，
#         当前方法传入的参数{},{}，
#         当前方法操作的时间{}，
#         当前方法的执行时间{}，
#         当前方法的返回值是{}
#         """.format(fn,a,b,opertime,end-start,result)
#         print(text)
#         return result
#     return inner
#
# @log
# def add(user):
#     print("正在添加{}".format(user))
#     return "add success"
#
# @log
# def modify(user):
#     print("正在修改{}".format(user))
#     return "modify success"
#
# @log
# def delete(user,department):
#     print("正在删除{}-{}".format(user,department))
#     return "delete success"
#
# add("张三")
# modify("李四")
# delete("王五","人事部")



#
#
# 4.在课堂案例基础上，当我做增删改的时候，我必须是登录后才能做，
# 目前登录验证可以不到数据库中验证，只要验证用户名是admin，密码是123就可以看成是登录成功。
# 使用装饰器函数实现即可。
# from datetime import datetime
# import time
# # 实现装饰器，实现登录验证
# _username="admin"
# _password="123"
# login_status=False
# def login(funcame):
#     def inner(*args,**kwargs):
#         global login_status
#         if not login_status:
#             username=input("请输入用户名：")
#             password=input("请输入密码：")
#             result=None
#             if username==_username and password==_password:
#                 print("您好，登录成功！！")
#                 result=funcame(*args,**kwargs)
#                 login_status = True
#             else:
#                 if username!=_username:
#                     print("对不起，用户不存在")
#                 else:
#                     print("密码错误")
#         else:
#             print("您已登录，请继续执行操作")
#             result = funcame(*args, **kwargs)
#         return result
#     return inner
#
#
# def log(funcname):
#     def inner(*args,**kwargs):
#         print("这是程序的日志：")
#         # 传入的参数 *args,**kwargs ，处理成字符串
#         a=b=""
#         if args:
#             # map(func,可迭代对象)  map(str,args)  "张三;20；
#             a=";".join([str(i) for i in args])
#         if kwargs:
#             b=";".join(["{}:{}".format(k,v) for k,v in kwargs.items()])
#
#         # 操作时间
#         opertime=datetime.now()
#         # 执行时间
#         start=time.time()
#         result=funcname( *args,**kwargs)
#         time.sleep(0.5)
#         end=time.time()
#
#         # 函数名
#         fn=funcname.__name__
#
#         text="""
#         当前方法的名字{}，
#         当前方法传入的参数{},{}，
#         当前方法操作的时间{}，
#         当前方法的执行时间{}，
#         当前方法的返回值是{}
#         """.format(fn,a,b,opertime,end-start,result)
#         print(text)
#         return result
#     return inner
#
# @login
# @log
# def add(user):
#     print("正在添加{}".format(user))
#     return "add success"
# @login
# @log
# def modify(user):
#     print("正在修改{}".format(user))
#     return "modify success"
# @login
# @log
# def delete(user,department):
#     print("正在删除{}-{}".format(user,department))
#     return "delete success"
#
# add("张三")
# modify("李四")
# delete("王五","人事部")


#
#
# 5.编写一个程序，初始为传入一个点的坐标，然后可以对该点进行移动。
# 在多次移动时，能够保留上一次移动的结果。（使用两种方式实现）
#
# x,y
# (1,1)
# a(2,3)---3,4
# a(-1,-1)--2,3

# 闭包的实现方式两种：闭包函数、闭包类
def move(x,y):
    def inner(offset_x,offset_y):
        nonlocal x,y
        x+=offset_x
        y+=offset_y
        print(x,y)
    return inner
m=move(0,0)
m(2,3)
m(3,4)

class Move:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __call__(self, offset_x,offset_y):
        self.x+=offset_x
        self.y+=offset_y
        print(self.x,self.y)

m1=Move(0,0)
m1(-2,-3)
m1(10,10)


#
# 6.课堂的大一点小一点的例子重新用另一种思路实现
# 主思路：给msg赋值
# 生成器：产出具体的x值
import time
def gen():
    x=1
    while True:
        msg= yield x
        print(x)
        if msg=="too big,小一点":
            x-=1
        else:
            x+=1
g=gen()
next(g)
msg=""
while True:
    time.sleep(1)
    x=g.send(msg)
    if x==5:
        msg="too big,小一点"
    elif x==1:
        msg="too small,大一点"

