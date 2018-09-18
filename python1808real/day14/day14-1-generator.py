"""
第十三章  迭代器、生成器、装饰器
"""
# 迭代器回顾
# 迭代器和迭代对象是两个类。
# 迭代对象：所有可以经历for的对象就是迭代对象。
# 迭代对象实现Iterable类中__iter__方法。（个别实现__getitem__()）
# 迭代对象中的iter方法：用来返回一个迭代器。

# 迭代器：是迭代对象的子类，专门用来产生迭代对象中的元素的。
# 迭代器实现了Iterator中 __iter__\ __next__
class A:
    def __init__(self):
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        # 产生迭代对象/迭代器中的每一个元素
        # 理解成产生元素的规则
        if self.count<=10:
            self.count+=1
            return "新元素"
        else:
            raise StopIteration()

a=A()
print(next(a)) #a.__next__()
print(next(a))
print(next(a))
for i in a:
    print(i)

# 迭代器只能被遍历一次。
# 迭代对象：在迭代对象中可以返回一个迭代器


"""
迭代器的缺点：
（1）必须要实现iter方法和next
（2）如果不是使用for循环（底层捕捉了StopIteration的异常），当调用next无返回结果的时候，会报异常
（3）一次性全部迭代，结果未必一下子全部使用，很可能只是一个一个使用。
"""
# 解决方案：生成器


# 二、生成器
# 1. 生成器产生的背景
"""
python2.5之后才出现的生成器
生成器：返回的是一个可迭代对象。 生成器的顶层就是使用迭代器实现的。

# 可迭代对象（生成器的）访问方式：
（1）next(迭代器)
（2）for循环

懒加载：按需加载，延迟加载
"""

# 需求：实现列表中:1,2,3...100，每个元素的平方
li=[]
for i in range(1,101):
    li.append(i**2)
# 列表推导式
print([i**2 for i in range(1,101)])

#2. 生成器的实现
# （1）生成器表达式---产生生成器对象
print((i**2 for i in range(1,101)))
gen=(i**2 for i in range(1,101))
print(next(gen))
print(next(gen))
print(next(gen))

# （2）生成器函数
# 生成器函数：也是一个函数，是一个带有特殊关键字yield 的函数
# yield产生一个i，会让程序暂停到yield的位置
# 1. 当生成器函数被调用的时候，不会理解执行函数，只是会产生一个生成器对象（迭代器对象），
#    生成器底层是迭代器。
# 2. 当第一次调用next的时候，相当于激活生成器函数，函数开始执行，执行到yield暂停
#    等待调用者再次执行next
# 3. 当程序运行到yield的时候，相当于将程序的执行权交给主调用方。
# 4. 当生成器函数终止时，StopIteration会在调用方报异常。生成器函数中如果是有限循环，调用者
#   循环的次数需要跟生成器函数保持一致，调用者的循环次数需要小于生成器的循环次数。
#   当调用者调用next的时候，如果生成器中没有yield就会报错。
def f():
    print("开始执行f函数")
    for i in range(1,101):
        # print(i)
        print("产生i之前")
        yield i  # yield产生一个i，作用跟return很像（但是不是return）
        print("产生i之后")

g=f()  # 不是真正执行了生成器函数 ，只是产生了生成器对象
print(g)
# 采用next获得元素 获得生成器中yield的产出值i
print("yield的产出值i=",next(g))  #开始执行函数一直到yield暂停，会产出一个i
print("主程序中其他的代码段1")
print("主程序中其他的代码段2")
print("主程序中其他的代码段3")
print("yield的产出值i=",next( g))  # 当再次调用next的时候，会从上次暂停的位置继续走
print("主程序中其他的代码段4")
print("主程序中其他的代码段5")
print("主程序中其他的代码段6")
# print("yield的产出值i=",next( g))  # 当再次调用next的时候，会从上次暂停的位置继续走


# 练习：斐波那切数列，使用生成器函数实现
# （1）先使用普通函数实现
# （2）再向普通函数中加yield
# （3）调用生成器函数获得每一个值
# def fib():
#     print("开始执行")
#     a=0
#     b=1
#     for i in range(5):
#         print("yield产生b之前")
#         yield b
#         print("yield产生b之后")
#         a,b=b,a+b
# g=fib()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  # for循环中只有5次机会，for循环结束之后，程序中（生成器函数）没有yield


# （3）yield表达式
#yield  程序到yield的时候，就会暂停，执行程序的调用者，一直到下一次执行next，继续刚才停止的位置继续执行。
# 生成器 中包含一个特殊的函数
# 【生成器对象.send（参数）】:这个函数是获得生成器对象的产出值的，同next

# 生成器函数中的产出值获得方式：
# （1）next(生成器对象)  （2）生成器对象.send(参数)  （3）for循环


# yield表达式的内容：在调用者端，使用send方法的send参数的内容

# 生成器函数中：
# 生成器表达的值（send传递的参数）= yield 产出值

# 调用者：
# 生成器对象.send(参数)


# 第一次调用生成器中的next----激活生成器
# next(生成器对象)  ----------生成器对象.send(None)  效果一样。

def gen():
    for i in range(1,101):
        print("产生i之前")
        value = yield i  # value是生成器yield表达式的内容
        print("生成器yield表达式的内容=", value)
        print("产生i之后")
g=gen()
# print(next(g))
print(g.send(None))
print("其他的代码块1")
# print(next(g))
print(g.send("第二次调用"))
# # # value生成器yield表达式的内容，要通过调用者的send(参数)
print(g.send("第三次调用"))
print(g.send("第四次调用"))

# 生成器编程
# 例子： 1,2,3,4,5,4,3,2,1,2,3,4.....
# 思路：
"""
1. 先写主程序
2. 生成器函数
"""

import time

def gen():
    msg=""
    while True:
        x= yield msg
        if x==5:
            msg="too big,小一点"
        elif x==1:
            msg="too small，大一点"

g=gen()
g.send(None)
x=1
while True:
    print(x)
    time.sleep(1)
    msg=g.send(x)
    if msg=="too big,小一点":
        x-=1
    else:
        x+=1




