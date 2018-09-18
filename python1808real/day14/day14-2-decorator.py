"""
第十三章 迭代器、生成器、装饰器
三、装饰器
#使用装饰器来扩展已有函数或者已有类的功能。
"""
# 1. 闭包
# 嵌套函数
def outer():
    def inner():
        print("innner函数执行")
    return inner()
# a=outer()
# print(a.__closure__) # 因为嵌套函数中没有形成闭包__closure__没有这个属性

# 闭包
def outer():# 在outer中有参数，参数 也算外围变量
    x=1 # 外围变量
    def inner():
        # x=2# 不能加
        print("innner函数执行,x={}".format(x))
    return inner
a=outer()
a()
print(a.__closure__)  # __closure__显示当前对象的闭包结构

# 闭包结构要素：
# （1）嵌套函数，外部函数的返回内部函数的名字
# （2）在内部函数中必须要访问外围变量。

"""
闭包的作用：
（1）当函数被调用后，依然希望使用函数中的变量。
（2）一个函数需要被扩展功能
"""
# 案例一：当函数被调用后，依然希望使用函数中的变量。
# 实现bill第几天上班的问题
# 不能成功
# def on_duty(name):
#     times=0
#     times+=1
#     print("{}第{}次上班".format(name,times))
# on_duty("bill")
# on_duty("bill")

# 使用闭包解决
# def on_duty(name):
#     times=0
#     def inner():
#         nonlocal times
#         times+=1
#         print("{}第{}次上班".format(name, times))
#     return inner
# duty=on_duty("bill")
# duty()
# duty()
# duty()

# 案例二：一个函数需要被扩展功能
# from datetime import datetime
# def on_duty(name):
#     print("{}上班了".format(name))
#     print(datetime.now())
#
# def off_duty(name):
#     print("{}下班了".format(name))
#     print(datetime.now())
# on_duty("bill")
# off_duty("bill")

# 需要在上下班的时候打卡，显示时间
# 将显示时间抽取成函数
# from datetime import datetime
# def check_in():
#     print(datetime.now())
# def on_duty(name):
#     print("{}上班了".format(name))
#
#
# def off_duty(name):
#     print("{}下班了".format(name))
#
# on_duty("bill")
# off_duty("bill")

# 新定义函数解决
from datetime import  datetime
# def check_in():
#     print(datetime.now())
# def on_duty(name):
#     print("{}上班了".format(name))
# def off_duty(name):
#     print("{}下班了".format(name))
# def new_on_duty(name):
#     check_in()
#     on_duty(name)
# def new_off_duty(name):
#     check_in()
#     off_duty(name)
# new_on_duty("bill")
# new_off_duty("bill")

# 使用闭包解决
# def on_duty(name):
#     print("{}上班了".format(name))
# def off_duty(name):
#     print("{}下班了".format(name))
# 下面程序也是闭包，但是会出现递归问题。在调用on_duty会继续在内部调用on_duty
# def check_in():
#     def inner(name):
#         on_duty(name)
#         print(datetime.now())
#     return inner
# on_duty=check_in()
# on_duty("bill")


# 闭包：
# 定义闭包函数，闭包函数的参数是原函数的名字func
# 在内部函数调用的时候，直接调用func（参数） 相当于调用原函数
# def on_duty(name):
#     print("{}上班了".format(name))
# def off_duty(name):
#     print("{}下班了".format(name))
# def check_in(func):
#     def inner(name):
#         func(name) # 原函数的功能调用
#         print(datetime.now())  # 新功能的扩展
#     return inner
# on_duty=check_in(on_duty)
# off_duty=check_in(off_duty)
# on_duty("bill")
# off_duty("bill")

# 遗留问题：所有曾经调用on_duty的调用者，必须要在代码前面加
# on_duty=check_in(on_duty)
# off_duty=check_in(off_duty)
# 否则on_duty、off_duty就不是新功能的


# 解决：使用装饰器解决
# 2. 装饰器
# 装饰器的底层其实就是闭包结构实现的。
# 装饰器：用来处理被装饰函数的，扩展被装饰函数的功能。
"""
装饰器语法：
（1）定义装饰器
def decorator(原函数名):
    def inner(参数):
      函数体
    return inner
 (2) 调用装饰器
 @装饰器的名字
 def 原函数():
    pass
    
 当再次调用  原函数()  的时候，相当于fun=decorator(原函数)
"""
# def check_in(func):
#     def inner(name):
#         func(name) # 原函数的功能调用
#         print(datetime.now())  # 新功能的扩展
#     return inner
# @check_in
# def on_duty(name):
#     print("{}上班了".format(name))
# @check_in
# def off_duty(name):
#     print("{}下班了".format(name))
#
# # on_duty=check_in(on_duty)
# # off_duty=check_in(off_duty)
# on_duty("bill")
# off_duty("bill")
# 装饰器改进之前的问题：直接在函数定义的上方加装饰器。不需要在函数调用的时候，重新命名
# 语法糖：在python中所有提供的便捷使用的方式都叫做语法糖。

# 3.装饰器的优化
# 参数、返回值
# 对于装饰器参数的优化，采用万能参数。这样可以支持更多的原函数扩展。
# def check_in(func):
#     def inner(*args,**kwargs):
#         func(*args,**kwargs)
#         print(datetime.now())
#     return inner
# @check_in
# def on_duty(name):
#     print("{}上班了".format(name))
# @check_in
# def off_duty(name):
#     print("{}下班了".format(name))
# def outwork(name,place):
#     print("{}去{}出差".format(name,place))
# on_duty("bill")
# off_duty("bill")
# outwork("bill","北京")

# 返回值
# def check_in(func):
#     def inner(*args,**kwargs):
#         result=func(*args,**kwargs)
#         print(datetime.now())
#         return result # 可以在这里篡改返回值
#     return inner
# @check_in
# def on_duty(name):
#     print("{}上班了".format(name))
#     return "success"
# @check_in
# def off_duty(name):
#     print("{}下班了".format(name))
# def outwork(name,place):
#     print("{}去{}出差".format(name,place))
# print(on_duty("bill"))
# off_duty("bill")
# outwork("bill","北京")

# 4.叠加装饰器

# 开发的是，功能可能不断的扩充，需要对装饰器进行叠加
"""
# 没扩展一个功能都定义一个新的装饰器就可以实现
# 调用的时候，在原函数定义的位置，需要进行装饰器的累加
@dacorator2
@dacorator1
def fun():
    pass
fun1=dacorator1(fun) # fun1 是被 dacorator1修饰过的fun
fun2=dacorator2（fun1） # fun2是被dacorator2修饰过的fun1
"""
# def check_in(func):
#     def inner(*args,**kwargs):
#         result=func(*args,**kwargs)
#         print(datetime.now())
#         return result # 可以在这里篡改返回值
#     return inner
# # 加一个向领导汇报工作的功能
# def record(func):
#     def inner(*args,**kwargs):
#         result = func(*args, **kwargs)
#         print("向领导汇报工作")
#         return result
#     return inner
# @record
# @check_in
# def on_duty(name):
#     print("{}上班了".format(name))
#     return "success"
#
# print(on_duty("bill"))

# 装饰器嵌套时执行的顺序
def dec1(func):
    print("dec1的方法start")
    def inner():
        print("dec1---inner---start")
        func()
        print("dec1---inner---end")
    return inner
def dec2(func):
    print("dec2的方法start")
    def inner():
        print("dec2---inner---start")
        func()
        print("dec2---inner---end")
    return inner
@dec1
@dec2
def test():
    print("测试test执行")
a=dec2(test)  # a是dec2的inner
b=dec1(a)     #b是dec1的inner
b()

# 5.含有参数的装饰器
# 装饰器的蚕食只能是被装饰的方法名，不能加其他的参数。
# 定义的时候如果希望加入参数，可以在双时期外侧继续定义外部函数
# 使用的时候：在@装饰器（传入参数）
# def check_in(func,format): 错误
from functools import wraps
def check_in(format,a):
    def check_in_inner(func):
        @wraps(func)
        def inner(*args,**kwargs):
            print(a)
            result=func(*args,**kwargs)
            print(datetime.now().strftime(format))
        return inner
    return check_in_inner
@check_in("%Y/%m/%d %H:%M:%S","a")
def on_duty(name:str)->None:
    """
    bill 上班的方法
    :param name:
    :return:
    """
    print("{}上班了".format(name))
on_duty("bill")

# 6.保留函数的元信息
# 元信息：函数名字，函数文档，函数的注释
# 需要使用functools.wraps解决

print(on_duty.__name__)
print(on_duty.__doc__)
print(on_duty.__annotations__)

# 7.类装饰器
# 实现装饰器可以通过定义装饰器函数（闭包）
# 也可以通过类装饰器解决

# 使用类解决闭包的问题
def on_duty(name):
    times=0
    times+=1
    print("{}第{}次上班".format(name,times))
# 使用类解决闭包
class OnDuty:
    def __init__(self,name):
        self.times=0
        self.name=name
    def __call__(self):
        self.times+=1
        print("{}第{}次上班".format(self.name,self.times))
duty=OnDuty("bill")
duty()
duty()
duty()

# 使用类装饰器解决bill打卡的问题
# @类装饰器
# 对象=类装饰器（原函数名）
# 对象（）

# 装饰器函数
# 新的函数名=装饰器函数名（原函数名）
# 新函数名（）
class CheckIn:
    def __init__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
        print(datetime.now())
        return self.func(*args, **kwargs)

@CheckIn
def on_duty(name):
    print("{}上班了".format(name))
on_duty("bill")

# 练习
# 对程序的日志进行记录
"""
思路：
（1）实现一个记录日志的装饰器，闭包函数
（2）在原函数定义上使用@ 装饰器
"""
import time
def log(func):
    def inner(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print("当前发方法操作的时间{}".format(end-start))
        print("当前发方法执行的时间{}".format(datetime.now()))
        print("当前发方法的返回值{}".format(result))
        print("当前发方法的参数{}{}".format(*args,**kwargs))
        return result
    return inner
@log
def add(user):
    print("正在执行添加。。。")
    time.sleep(0.5)
@log
def modify(user):
    print("正在执行修改...")
add("张三")
modify("李四")

