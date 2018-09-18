"""
第八章函数

八、递归函数

一个函数的递归包含两种情况
1. 直接递归：A函数---A函数
2. 间接递归：A函数--B函数---A函数

递归一定会确定一个条件，当某一个条件成立的时候，递归终止。

递归：递推和回归

循环和递归是有一定相似度的，能够通过循环解决的问题，一般使用递归也能过实现。
循环：思考问题角度比较复杂，速度快
递归：思考角度比较简单，速度慢
"""
# 1. 1+2+...+100
s=0
for i in range(1,101):
    s+=i
print(s)

# 递归解决（懒）
# 1. 累加和
"""
1+2+...+100   前99个数相加的和+100
1+...99       前98个数相加的和+99
1+..98        前97个数相加的和+98
...
1+2+3         前2 个数相加和+3
1+2           1+2
1             1  

突破点：找好分界点  
1------1
>1  
"""
#定义函数：求前n项和
def s(n):
    if n==1:
        return 1
    else:
        return  s(n-1)+n
print(s(100))


# 2. N的阶乘
# n!=1*2*3*4*....*n
# (1)找好分界点   （2）做一个前n项阶乘函数
# 分界点1
def s2(n):
    if n==1:
        return 1
    else:
        return s2(n-1)*n
print(s2(4))

# 3.斐波那切数列
# 每一项都是前两项的和
# 1 1 2 3 5 8 13 21 34 .....
# 使用递归解决
# 突破点：n==1 和n==2 都返回1
#        n>2         前两项的和
def s3(n):
    if n==1 or n==2:
        return 1
    else:
        return s3(n-1)+s3(n-2)
print(s3(7))

# li=[1,[[[1,2],2],2,3],[4,5]]
# 定义一个函数：将列表中的元素转换成一维列表。
# 分界点：不是列表的时候，直接new.append(i)
        # 是列表的时候，直接调用自己。

#4. 汉诺塔问题
def hano(n,A,B,C):
    if n==1:
        print("{}--{}".format(A,C))
    else:
        hano(n-1,A,C,B)
        print("{}--{}".format(A,C))
        hano(n-1,B,A,C)

hano(3,"A","B","C")
def b():
    pass
def a():
    b()
    print()
# RecursionError:递归错误，但是不仅仅是自己调用自己次数太多的时候，出的问题。


# 九、高阶函数
# 高阶函数：能够接受一个函数或者多个函数作为输入，同时还能够输出一个函数
# 1.sort 可以传入key
li=[1,2,3,-8]
li.sort()
print(li)
# 如果指定了key，那么会根据key指定函数名，对每个元素使用函数，得到返回值，再根据返回值排序
li.sort(key=lambda k:abs(k)+1)
print(li)

#2. map 将元素按照函数的规则进行改变
# 语法：map(func,iterable)
# 将迭代对象中的每一个元素都应用一下func，得到返回值，形成新的迭代对象
li=[1,2,3,4,5]
# 将li中的每个元素求平方，形成新的列表
def s(k):
    return k**2
print(list(map(s,li)))
# 优化一下
print(list(map(lambda k:k**2,[1,2,3,4,5])))


#3.filter函数：过滤
# 语法：filter(func,iterable)
# 按照函数将迭代对象中符合条件的留下来，不符合条件的去除掉
# func方法返回布尔类型值
# 当对所有的元素，每一个元素都调用一次func方法之后，会得到True/False，如果True，留下
li=[1,2,3,4,5]
li_new=[]
for i in li:
    if i>3:
        li_new.append(i)
print(li_new)

print(list(filter(lambda k:k>3,li)))

#4.reduce  按照函数二变一
import functools
# functools.reduce(func,iterable,init)
"""
第一个参数：func： 函数名，需要一个两个参数的函数
第二个参数：可迭代对象
"""
li=list(range(1,11))
print(li)

# 求累加和、最大值、最小值
"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x=1
y=2

x=3
y=3

x=6
y=4

x=10
y=5
"""
print(functools.reduce(lambda x,y:x+y,li))
print(functools.reduce(lambda x,y:x if x>y else y,[-1,5,2,6,7,3]))
"""
x=-1
y=5

x=5
y=2

x=5
y=6

x=6
y=7

x=7
y=3

7
"""


#5.max
max([1,2,3,4,-5])
year_c=[(2000,30),(2001,31.2),(2002,34.6),(2005,30.5)]
print(max(year_c,key=lambda x:x[1]))


# 十、柯里化函数
# 局部函数
# def a(x,y):
#     pass
# a(10,1)
# 希望能够有一种方法能够调用函数的时候将参数分步传入
# a(10)
# a(1)
# 柯里化函数：值传递给函数一部分参数，调用之后，让他返回另一个函数去处理剩下的参数。
# 一个函数：x的n倍
# def multifun(x,n):
#     return x*n
# print(multifun(10,2))
# 需求：希望能够得到2倍乘的方法

# 方式一：通过functools中的partial函数
# functools中的partial函数，可以解决函数的柯里化问题
# 新函数=partial(原函数名,一个参数)
#  如果不是以【名字=值】，会默认按照参数的顺序从左到右赋值
# 新函数(另一个参数)
# times3=functools.partial(multifun,n=3)  # 3倍乘的函数
# print(times3(6))
# print(times3(10))

# 方式二：通过柯里化装饰器
#在定义好的方法上面 @装饰器
from toolz import curry
@curry
def multifun(x,n):
    return x*n
times3=multifun(n=3)
print(times3(8))
print(times3(9))

# 练习：
# power(2,3)函数进行柯里化，使用局部 函数的方式调用
@curry
def power(x,y):
    return x**y
y5=functools.partial(lambda x,y:x**y,y=5)
print(y5(10))

y5=power(y=5)
print(y5(10))


#
# pip install toolz


# 十一、函数的文档
# 一般函数的说明文档在函数定义的下一行使用三引号
def fun():
    """
    对函数的基本功能进行介绍
    参数
    :return: 返回值的说明
    """
    pass
# 调用说明文档
print(fun.__doc__)
help(fun)

# 十二、函数的注释
# 参数的类型    参数:类型(基础数据类型和自定义的类)
# 返回值的类型  在冒号的前面-> 返回值类型
class Person:
    pass
def add(a:int,b:Person)->int:
    pass
# 显示函数的注释
print(add.__annotations__)


