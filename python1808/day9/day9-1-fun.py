"""
第八章 函数
"""
# 背景：问题 ，控制台上打印每行5个星星，五行
# print("其他的代码块")
# for i in range(5):
#     print("*"*6)
# print("其他的代码块")
# for i in range(5):
#     print("*"*6)
# print("其他的代码块")
# 问题：（1）代码重复，可读性差  （2）可扩展或可修改性差
#函数的的定义：实现单一或者多个“功能”的代码段，当前的功能一定具有通用性。

#函数的分类：内建函数和自定义函数

# 一、内建函数
#abs()# 求数字的绝对值
# print("ddd","ccc")
# print(abs(-100,-200))
# print(abs("a"))


# li=[1,3,54,2]
# print(li.sort())
# print(li)
"""
1.函数名：abs  print
2.函数的参数，个数有要求，对类型也有要求（函数体决定）
3.函数有返回值
"""

# 二、自定义函数
# 1.函数的定义
"""
def 函数名(【参数1,参数2,】):
    函数体
    【return 返回值】
"""
# 函数名：规则
# 变量名、函数名、类名。。。。都属于标识符
# 标识符：
# （1）数字、字母、下划线，不能以数字开头
# （2）不能使用关键字

#2. pass关键字
# pass 是用来占位，当定义了选择、循环、函数、类，可以使用pass进行占位
def add():
    # pass
    print("执行加法")

#3.函数调用：函数的定义并不代表执行，只有当真正调用的时候，函数才执行。
# 函数名([参数])
add()

#解决背景中的问题
# def pstar():
#     for i in range(5):
#         print("*" * 4)
#
# print("其他的代码块")
# pstar()
# print("其他的代码块")
# pstar()
# print("其他的代码块")



#三、函数的参数
#需求：需求变更，需要有打印3个星星， 还要有打印4个星星
# def pstar():
#     for i in range(5):
#         print("*" * 4)
# def pstar3():
#     for i in range(5):
#         print("*" * 3)
# def pstar2():
#     for i in range(5):
#         print("*" * 2)
# print("其他的代码块")
# pstar()
# print("其他的代码块")
# pstar()
# print("其他的代码块")
# pstar3()


# 将星星数设置成参数q，函数调用者就可以根据传入的参数来打印星星
# def pstar(q):
#     for i in range(5):
#         print("*" * q)
# a=2
# pstar(a)
# pstar(3)

# 函数定义时候参数叫做：形式参数
# 函数调用时传入的参数叫做：实际参数

# 参数的类型：函数定义的时候，python的参数类型
# 位置参数、默认参数、命名关键字参数、可变参数、关键字参数

# 1.位置参数 (必须参数)
# 调用函数时参数传入的值必须跟定义函数时的参数数量、位置保持一致。
# 要求：（1）位置参数，必须要传入（除了有默认值参数）  （2）传入的顺序必须按照定义的时候的顺序
# def pstar(q,line):
#     for i in range(line):
#         print("*" * q)
# pstar(2,4)# 调用函数时，会将q绑定到2上，将line绑定到4


# 2.默认参数
# 当函数定义的时候，给参数一个默认值
# 格式：定义的时候，参数名=默认值
# 要求：
# （1）对于所有参数都可以设置默认值
# （2）如果调用函数时，给了默认参数对应的参数值，就会使用给定的参数值给参数赋值。
     # 如果调用函数时，没有个默认参数对应的参数值，就会使用默认值来参数赋值。
# （3）位置参数要放在默认值参数的前面
# （4）默认值一般要使用不可变类型，如果使用可变类型 ，程序会出现问题。
# def pstar(q,line=5):
#     for i in range(line):
#         print("*" * q)
# pstar(4,1)
# a=2
# pstar(a)
# pstar(3)

# 将默认值设置成可变类型。
def f(a=[]):
    a.append(1)
    print(a)
f(["a","b"])
f(["c","d"])
f()
f()


# 练习：自己写一个abs函数。
def abs_new(x):
    if x>=0:
        print(x)
    else:
        print(-x)
abs_new(-100)
abs_new(100)


# 3. 命名关键字参数
# def pstar(x,y=5):
#     for i in range(y):
#         print("*" * x)
# pstar(4,1)
# a=2
# pstar(a)
# pstar(3)
# 函数定义的时候使用*作为分隔符，*后面是,
# 函数调用的时候，【必须】要指定参数的名字
"""
def a(*, 命名关键字参数1,命名关键字参数2...):
    pass
"""
# 调用
# a(参数名=参数值,参数名=参数值...)
# def pstar(*,x,line):
#     for i in range(line):
#         print("*" * x)
# pstar(x=5,line=2)
# pstar(line=2,x=5)
# pstar(x=1,line=3)
"""
命名关键字参数的作用：
（1）增强程序的可读性
（2）可以忽略参数的顺序
（3）命名关键字参数如果有默认值时，可以一样可以简化调用。
"""

"""
命名关键字参数注意：
（1）命名关键字参数只要定义了，就必须传入（除了有默认值参数）
（2）命名关键字传入参数必须使用 :名字=值
（3）命名关键字参数需要放在位置参数之后
"""

# 位置参数也可以使用：名字=值 传入参数
# 可以解决多个参数都有默认值的问题。
def pstar(x=2,line=1):
    for i in range(line):
        print("*" * x)
# pstar(x=3,line=1)
# pstar(2,10)
pstar(line=10)


#命名关键字参数在sort函数和sorted函数中的应用
li=[11,-33,555,88]
# li.sort(reverse=True)
# key:函数名
# 会将列表中的每一个元素都应用key，使用key函数的返回值进行排序
# sort是列表下的函数，原地修改
li.sort(key=abs)
print(li)


# 去掉列表中的重复元素
list1 = [1, 2, 5, 4, 1, 5, 6, 8, 0, 2]
print(list1)
print(sorted(set(list1),key=list1.index))

#sorted是内置函数 ，新建列表进行修改
print(sorted((1,44,2,3)))


# 4.可变参数（收集参数）
# 将位置参数以元组的形式存储传递给函数。
# 需求：实现两个数的平方和
# def s(a,b):
#     print(a**2+b**2)
# def s(a,b,c=0):
#     print(a**2+b**2+c**2)
# s(3,4)

# 语法：* args  (args约定俗称)
def s(* args):
    sums=0
    for i in args:
        sums+=i**2
    print(sums)
s(1,2,3,4,5)
s()

# 序列的打包：在函数定义的时候，前面* ，就代表将参数进行打包，打包后将参数放到元组中。
li=[3,4,5]
# s(li)  不可以这样传，因为li已经打包好了
# 注意：如果定义参数的时候，参数使用* 进行打包，
# 函数调用时一定不要使用打包好的数据（列表、元组、字典、集合）

# 序列的拆包：在函数调用的时候，前面*， 就代表对传入的参数进行拆包。
s(* li)
# a=1
# s(* a)  拆包的时候，参数必须是可迭代对象


# 5. 关键字参数（收集参数）
#  将所有命名关键字参数收集成字典存储传递给函数。
# 格式：**kwargs (约定俗称)
#  需求
def regster(name,age,**kwargs):
    print(name)
    print(age)
    print(kwargs)
    print("成功注册")

# regster("张三",20)
# regster("张三",20,"北京","java工程师","男")  # 如果只有可变参数，不能记录key的信息
# regster("张三",20,city="北京",job="java工程师",gender="男")

# 序列的打包： 定义的时候使用** 将所有的命名关键字参数，打包成字典
d={"city":"广州","job":"python工程师","gender":"女"}
# regster("李四",25,di=d)  #会将d重新打包成字典 di是key  d的对象是value

# 序列的拆包： 调用的时候 ** 进行拆包
regster("李四",25,**d)

#  需求
def regster(*args,**kwargs):
    print(args)
    print(kwargs)
    print("成功注册")
regster()
regster("张三")

# 位置参数放在最前面，可变参数、关键字参数
# 说明：可变参数和命名关键字参数不能一起使用。
# 参数的顺序：
# 位置参数> 默认参数> 命名关键字参数/可变参数  > 关键字参数



# 四、函数的返回值
# 使用return关键字来定义返回
# 当调用函数之后，程序执行到return，就会跳出函数，return后面的语句不再执行。
# 一个函数中，在return后面语句一定不执行(不对)
# 一个函数中，只要执行了return，那么后面的语句一定不执行（对）
#
# def add(a,b):
#     sum=a+b
#     return sum
#     print("这句话还可以执行吗")
# def add(a,b):
#     if a==2:
#         sum=a+b
#         return sum
#     print("这句话还可以执行吗")
# s1=add(2,2)
# print("add方法的返回值",s1)

# 返回None的情况：
# （1）没有return
# （2）return None
#  (3) return
def a():
    print("a方法执行")
    # return None
    return

# print中如果有函数调用，其实是在调用函数的返回值
print(a())


# return的返回值可以是表达式。
def add(a,b):
    # return sum  #变量指向的对象
    return a+b
add(2,3)


#返回多个返回值，以元组的形式存在
# 可以使用跟元组一样数量的变量去接返回值，可以对于返回值一一赋值。数量上必须一一赋值。
def compute(a,b):
    # return a+b
    # return a-b
    # return a*b
    # return a/b
    return a+b,a-b,a*b,a/b
print(compute(10,3))
x,y,z,k=compute(10,3)
print(x)
print(y)
print(z)
# print(k)

# x,y=y,x

# 一般在函数中都使用return返回值去返回结果，而不使用print
def a():
    # print("a函数开始执行")
    # print(1+2+3)
    return 1+2+3
temp=a()
print("当前的返回值是{}".format(temp))

# 练习：
# 1.求一元二次方程两个解(只做d判断是否有解)
# ax^2+bx+c=0
import math
def q(a,b,c):
    d=b**2-4*a*c
    if d>=0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
    else:
        return "无解"
    return x1,x2
print(q(1,6,2))

#2. 写一个函数计算x的n次方
def p(x,n):
    if x==0 and n<0:
        return "不存在"
    return x**n
print(p(2,5))
print(p(2,-5))

def p1(x,n):
    s=1
    if n>0:
        for i in range(n):
            s*=x
    else:
        for i in range(-n):
            s*=x
        return 1/s
    return s
print(p1(2,5))
print(p1(2,-5))


# 五、函数的文档
# 函数对于功能的描述
# 功能描述以"""定义的字符串存在，定义在函数定义的下方
def fun():
    """
    参数：
    功能：
    :return:返回值
    """
    pass

# 查看注释，函数名.__doc__
print(fun.__doc__)
print(print.__doc__)
help(fun)
help(print)

# 六、参数注释
def fun(a,b)->int:
    pass
print(fun.__annotations__)
