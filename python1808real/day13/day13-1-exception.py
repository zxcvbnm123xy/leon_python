"""
第十二章  错误和异常
"""
# 问题归结为两种：
# （1）错误：出现在编译期的问题
# （2）异常：出现在执行期的问题

# 在python中对错误和异常都使用异常对象来进行处理。

# 一、异常的相关概念
# 当python解释器遇见异常的时候，会出现异常的位置产生一个【异常类型】的对象.
# 当发生异常之后，程序不会马上停止，而是“暂停”，程序会从上下文中查找有没有【异常处理的程序】
# 如果有异常处理的程序，则会走异常处理
# 如果没有异常处理的程序，异常会【向上传播】，一直到走到Python解释器都没有处理，程序才会真正的终止
#  在控制台抛出异常。
# 【异常类型】：处理异常的异常类。
# 【异常处理的程序】：对于程序发生异常之后的处理
# 【向上传播】：
# 函数的调用：采用堆栈（落井下石）的模式
# 异常的向上传播：把异常传播给调用者。
def  A():
    B()

def  B():
    C()

def  C():
    D()

def  D():
    E()
def  E():
    print(1/0)
# A()


# 二、异常的常见类型
# BaseException（爷爷）：是所有异常最根的类：定义了最基础的功能，很多都没有做实现。只是框架的作用。
# Exception（父亲）: 继承BaseException，实现了异常的一些常用的功能
# ValueError
# ZeroDivisionError
# NameError
# AttributeError
# 为什么必须有【父类】：因为父类对BaseException做了一些基础功能的实现，所有的子类对于基础
#                    功能就不用再实现了。
# 为什么还要有【爷爷类】：为了有一些设计，认为父类无法满足需求，可以去自己扩展爷爷类进行重写。
# 1. ZeroDivisionError 除数为0的异常
# print(1/0)

# 2.nameError 名字错误，名字不存在的时候，出现的异常。
# a=1
# def a():
#     pass
# class a:
#     pass
# print(a)

# 3.typeError 类型不匹配
# print("aaa"+1)
# class P:
#     pass
# p=P()
# print(p+1)

# 4.AttributeError: 属性不存在（就是在类的下面报nameError的错）
#类属性，实例属性
# class A:
#     pass
# print(A.a)

#5.IndentationError 缩进错误
# class A:
# print()

# 6.IndexError索引异常，索引越界
li=[1,2,3]
# print(li[4])
# print(li.pop(4))

#7.UnboundLocalError 对局部变量访问异常
# 当使用一个局部变量的时候，没有进行赋值，直接访问会报错
# def hello():
#     print(a)
#     a=1
# hello()

# 8.AssertionError 断言异常
# assert  5>50,"出现错误"


# 9.ModuleNotFoundError: 模块不存在异常
# import a

# 10.KeyError 字典中key不存在的异常
# d={}
# print(d[1])

# 11.RecursionError 递归异常
# def a():
#     a()
# import sys
# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())

# 12.StopIteration 迭代终止异常，当迭代器中没有内容之后，就会出现异常
li=[1,2,3]
# 获得li对象的迭代器  # 迭代器是一次性的
# it=li.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# for i in li:
#     print(i)
# for i in li:
#     print(i)

#13.ValueError 当对值处理错误的时候，会出现异常
# int("a")
# dict(1,2,3)

# 14.SyntaxError 语法错误异常
# print(

# 三、捕获异常
# 【异常的处理程序】
# 1. try except 语法
# 一个程序应该具有异常处理能力，关乎到程序的稳定性和健壮性。
"""
语法：
try:
   可能产生异常的程序
except 异常类型1  :
    处理异常
except 异常类型2：
    处理异常
"""
#执行try语句会三种情况
"""
1. try语句全部执行完毕，没有产生异常
2. try中产生了异常，被其中一个except捕获
3. try中产生了异常，没有被任何一个except捕获
"""
# 1.try语句全部执行完毕，没有产生异常：执行try中所有的代码，不执行任何一个except
# a=1
# b=5
# try:
#    print("try执行开始")
#    a/b
#    print("try执行结束")
# except ZeroDivisionError:
#     print("产生了除数为0的异常")
# print("其他的代码段")

# 2. try中产生了异常，被其中一个except捕获:
# try抛出异常之后的语句不再执行，
# 执行符合except类型异常处理程序
# try模块后面的其他代码段正常执行

# 对于except分支，至多只会执行一个最先匹配成功的分支。
# a=1
# b=0
# try:
#    print("try执行开始")
#    a/b
#    print(c)
#    print("try执行结束")
# except ZeroDivisionError:
#     print("产生了除数为0的异常")
# except NameError:
#     print("产生了除数为0的异常")
# print("其他的代码段")

# 合并多个异常：当认为异常情况的处理可以一致的时候，可以对异常进行合并
# 合并异常语法：except (异常类型1，异常类型2，..)
# a=1
# b=0
# try:
#    print("try执行开始")
#    # a/b
#    print(c)
#    print("try执行结束")
# except (ZeroDivisionError,NameError):
#     print("出错了！！！！！")
# print("其他的代码段")

#3. try中产生了异常，没有被任何一个except捕获
#  会将异常向上抛出。如果调用者的程序中有异常的处理，则进入异常处理程序，否则会一直抛出异常
#  给python解释器，控制台报错。
# a=1
# b=0
# try:
#    print("try执行开始")
#    a/b
#    print("try执行结束")
# except NameError:
#     print("name不存在的异常")
# print("其他的代码段")

# 程序开发的时候，有的时候不可能所有的异常都能够被想到
# 如果try中抛出的异常不符合任何一个【except 异常类型】，
# 在所有except的最后，可以使用空except来处理所有的异常
# 慎用：因为会捕获所有的异常，也就会漏掉所有的错误
# a=1
# b=0
# try:
#    print("try执行开始")
#    a/b
#    print("try执行结束")
# except NameError:
#     print("name不存在的异常")
# except :
#     print("出错了~~~~~~")
# print("其他的代码段")


# 多个异常的except处理顺序：
# 如果异常类型之间没有继承关系，可以任意放置
# 如果异常类型之间有偶继承关系，必须要将子类异常放前面，父类异常放后面。
# a=1
# b=0
# try:
#    print("try执行开始")
#    a/b
#    print("try执行结束")
# except ZeroDivisionError:
#     print("除数为0的异常")
# except Exception:
#     print("Exception异常")
#
# print("其他的代码段")

# 思考：以下哪种异常抛出的方式比较好
a=1
b=0
# 方式一：
def div1(a,b):
    try:
       print("try执行开始")
       a/b
       print("try执行结束")
    except ZeroDivisionError:
        print("除数为0的异常")
    except Exception:
        print("Exception异常")

    print("其他的代码段")
# div1(a,b)


# 方式二：
def div(a,b):
    a/b
try:
    div(a,b)
except ZeroDivisionError:
    print("除数为0的异常")
except Exception:
    print("Exception异常")
print("其他的代码段")


try:
    div(a,b)
except ZeroDivisionError:
    print("出错了，滚蛋")
except Exception:
    print("Exception异常")
print("其他的代码段")

# 练习：自己写一段程序，抛出异常，捕获异常，IndentationError和TypeError有什么不同。
#错误是编译期产生的，所以不能用try except捕获异常
# try:
#     print(
# except SyntaxError:
#     print("语法错误")
# print("其他的代码段")


# 应用场景：
# 1. 异常可以用来捕获错误，抛出错误，同时使得程序继续执行，不中断
# 2. 使用异常处理程序来处理，错误无法预测的场景
#例1：
# d={"tom":100,"jerry":80}
# # 希望能够通过输入一个人的名字，来获得他的程序
# name=input("请输入一个名字：")
# # 相当于访问了两次d
# if name in d.keys():
#     print(d[name])
# else:
#     print("不存在这个人")
#
# # 异常
# try :
#     print(d[name])
# except KeyError:
#     print("不存在这个人")

# 例子2：
s="2018-10-01"
# import time
# # print(time.strptime(s,"%Y-%m-%d"))
#
# try:
#     print(time.strptime(s, "%Y-%m-%d"))
# except ValueError:
#     print("无法处理时间类型")

# 四、获取异常对象
# 当异常抛出的时候，会产生一个异常对象。
# 获得异常对象的方法有两种
#1. 在sys包下
# import sys
# a=1
# b=0
# try:
#    a/b
# except ZeroDivisionError:
#     print(sys.exc_info())
#2. 在【except 异常类型  as 变量】：
# 变量会绑定异常类型的对象
a=1
b=0
try:
   a/b
except ZeroDivisionError as e:
    print(e.args)
    print(e)

# 五、finally  else
# finally: 在任何情况下都会执行的代码段（异常出现、异常捕获、异常没有吧诶成功捕获，正常执行...）
# else:  当try语句没有抛出异常的时候，会执行的代码段。不走except，就会走else
"""
语法：
try :
   可能出现异常的代码段
except 类型 变量:
    异常的处理
except 类型 变量:
    异常的处理
...
else:
    try没有抛出异常的是，会执行的代码
finally：
    所有情况始终执行的代码段
"""

# class Test:
#     def divide(self,x,y):
#         r=x/y
#         print("try:result={}".format(r))
#
# t=  Test()
# try:
#     t.divide(6,0)
# except ZeroDivisionError:
#     print("except:除数为0的异常")
# else:
#     print("else:当try正常执行，没有异常的时候执行的代码段")
# finally:
#     print("finally:始终执行的代码段")

# 使用场景：
# finally：资源使用的时候，会使用finally关闭资源。无论有没有成功连接、成功打开，都需要关闭资源
# else: 区分代码块

# def fun():
#     try:
#         return 1
#     finally:
#         return 2
# print(fun())
#
# def fun():
#     x=1
#     try:
#         return x
#     finally:
#         x=2
# print(fun())

# 六、强制抛出异常
# raise，可以让程序员强制主动抛出异常
# 格式: raise 类型("错误信息")
# 用法有两种
# 1. 直接在程序中主动抛出异常
def register(age):
    if age>0:
        print("正常执行注册操作")
    else:
        print("不能执行注册")
        raise ValueError("年龄不能为负数")

    print("其他注册成功的程序")
# register(-10)

# 2. 在except抛出异常： 目的是在出异常的位置，保留异常的抛出，防止异常的疏漏
class Test:
    def divide(self,x,y):
        try:
            r=x/y
            print("try:result={}".format(r))
        except ZeroDivisionError:
            print("except:除数为0的异常")
        except:
            print("出错了")
            raise ValueError("ValueError")
#
# t=  Test()
# try:
#     t.divide(6,"0")
# except ValueError:
#     print("暂时不做处理")
# print("其他代码段")
#


# 七、自定义异常
"""
自定义异常的语法：
class MyError (Exception):
    def __init__(self,message)
        self.message=message
调用
MyError("错误信息")  -----产生异常类型的对象
"""
class MyException(Exception):
    def __init__(self,message):
        self.message=message
try:
    raise MyException("自定义的异常")
except MyException as e:
    print(e.message)
print("其他的代码段")


# 需求：定义一个方法regist(age)，age>0可以注册成功
# 如果输入age<=0则重新注册，有提示信息。需要自定义一个异常类age<=0的异常。
# （1） 自定一一个异常类
# （2） 注册def regist(age)
#     当age<=0 则可以raise抛出自定义的异常类型
class AgeError(Exception):
    def __init__(self,message):
        self.message=message
def reg(age):
    if age<=0:
        raise AgeError("输入年龄<=0")
    else:
        return True
while True:
    try:
        a=int(input("输入一个年龄信息"))
        if reg(a):
            break
    except ValueError:
        print("请输入一个数字，您输入的不合法")
    except AgeError as e:
        print(e.message)