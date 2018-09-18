"""
第八章 函数
"""
#一、 背景
# 代码中有多个模块都要使用到打星星功能？
print("功能模块1")
for i in  range(5):
    for j in range(5):
        print("*" ,end="")
    print()
print("功能模块2")
for i in  range(5):
    for j in range(5):
        print("*" ,end="")
    print()
print("功能模块3")

# 函数：可以实现单一功能或者多个功能模块的代码段    划分函数使用的“功能模块”

# 函数的类型：内置函数、自定义函数

# 内置函数(存在内置功能模块中)
# print()
# print(abs(-100,-200))
#问题：函数调用时，需要知道函数的个数
#      abs？ 函数名，定义好函数之后，调用需要使用函数名
#     函数的返回值

li=[1,2,3,-1]
# li.sort()
sorted(li)
print(li)


# 二、自的定义
"""
语法：
def 函数名([参数,]):
    函数体
    return 返回值
"""

# 2. pass关键字的使用
import keyword
print(keyword.kwlist)
# 是用来占位
# def a():
#     pass
# print("其他的代码段")
#
# if 3<2:
#     pass
# else:
#     pass
#
# for i in range(10):
#     pass
# while True:
#     pass

#3. 函数的调用
# 函数定义好之后不会自动执行，必须通过函数的调用才能够执行（魔法方法除外）。
# 格式：函数名([参数])
def add():
    # pass
    print("add函数执行")
add()

#解决星星问题
# def p():
#     for i in range(5):
#         for j in range(5):
#             print("*", end="")
#         print()
#
# print("功能模块1")
# p()
# print("功能模块2")
# p()
# print("功能模块3")


# 三、函数的参数类型
def p():
    for i in range(5):
        for j in range(5):
            print("*", end="")
        print()
def p_new(a):
    for i in range(a):
        for j in range(5):
            print("*", end="")
        print()
print("功能模块1")
p()
print("功能模块2")
p()
print("功能模块3")
b=11
p_new(b)

# 函数定义时候的参数：形式参数：在调用函数的时候，使用形式参数绑定实际参数。
# 函数调用时候的参数：实际参数：在函数调用的时候，向函数中传递对象。


# 函数类型： 位置参数（必须参数）、默认参数、命名关键字参数、可变参数、关键字参数
# 1. 位置参数：根据定义的参数的位置去绑定传入参数值的参数。
# 要求： （1）如果定义的了位置参数就必须传入
#        （2）传入参数的顺序跟定义时候的顺序一致

# line:打印几行
# x：  每行多少个星星
def p_new(line,x):
    for i in range(line):
        for j in range(x):
            print("*", end="")
        print()
# p_new(1,10)
p_new(10,1)

# 2. 默认参数: 当函数定义的时候，给参数一个默认值
# 位置参数、命名关键字参数都可以给定默认值
# 使用场景：
# （1）为方便调用者调用（减少参数的传入）
# （2）作为函数的升级和扩展，方便曾经的调用者不出错误。
"""
默认参数要求
（1）当函数调用的时候，如果没有给定参数的值，函数会使用默认值给参数赋值；
     如果给定了参数的值，就会使用给定的参数值。
（2）位置参数要放在默认参数的前面
（3）默认参数一般要绑定不可变类型。不要使用可变类型当做默认值
     原因：当不给默认值参数传值的时候，参数只能使用同一个默认值对象（可变），来对参数进行赋值，
           如果是可变对象，则参数是一直改变。
"""
# def p_new(x,line=5):
#     for i in range(line):
#         for j in range(x):
#             print("*", end="")
#         print()
# p_new(10)
# p_new(1,1)
def f(a=[]):
    a.append(10)
    print(a)
# 调用
f([1,2,3])
f([4,5,6])
f()
f()
f()
f([1,2,3])


# 解决方式
def f(a=[]):
    if len(a)==0:
        a=[]
    a.append(10)
    print(a)
# 调用
f([1,2,3])
f([4,5,6])
f()
f()
f()
f([1,2,3])


# 3. 命名关键字参数：必须使用名字传入的参数
# # 语法：需要使用*,作为分隔符，在* 后面的参数都是命名关键字参数。
# 注意：(1)调用的时候，必须传入 名字=值
#       (2)命名关键字参数，只要定义了，（除了有默认值以外）一定要传入。
#      （3）位置参数应该在命名关键字参数的前面
"""
命名关键字参数的作用：
（1）增加程序可读性
（2）调用的时候，参数可以忽略顺序
（3）当形式参数有默认值的时候，可以简化传递。
"""


def p_new(line,*,x,y=8):
    for i in range(line):
        for j in range(x):
            print("*", end="")
        print()
p_new(line=10,y=2,x=1)
p_new(line=10,x=2,y=2)  # 位置参数也可以通过 名字=值传入，但是意义上来说，仍然是位置参数。
p_new(10,x=2)


# 4.可变参数
# 参数传入的时候，个数不限制
# 会将所有的位置参数打包成元组的形式
# 语法：* args
def s(a,b,c=0):
    return a**2+b**2+c**2
s(2,3)

def s(* args):
    s=0
    for i in args:
        s+=i**2
    return s
print(s(1,2,3))  # (1,2,3)
print(s(1,2))
print(s(1))
print(s())
a=(1,2,3)
# print(s(a))  # s((1,2,3))    ((1,2,3),)

 # 序列的打包
"""
当定义函数的时候，在函数参数的前面加 *，打包，将元素打包成元组的形式
"""

# 序列的拆包
# 当函数执行的时候，在实际参数前面加 * ，拆包，将序列进行拆包  [1,2,4]----1,2,4
print(s( * a))
print(s(* [3,4,5]))


# 5. 关键字参数（** kwargs）
# 能够将所有的命名关键字参数打包成字典传递给函数（参数名：key    参数值：value）
def regist(name,age,** kwargs):
    print(name)
    print(age)
    print(kwargs)
    print("注册成功")

regist("张三",20)
regist("张三",20,city="北京",gender="男")
# 打包：  ** 定义的时候，将命名关键字参数打包成字典
d=dict(city="北京",gender="男")

# 拆包： 在函数调用的时候，使用** 对参数进行拆包
regist("张三",20,** d)


#参数的组合
# 注意：可变参数跟命名关键字参数不能混合
# def a(*,x, *args):
#     pass
# 如果将命名关键字参数放前面， *, 后面参数都被认为是需要使用名字 = 值传入，
# 可变参数连个数都无法确定，所以更没有办法确定自己的名字

# def a(* args,*,x):
# 如果将可变参数放在命名关键字前面。
# 当函数调用传入参数的时候，位置参数都会被* args吸收，
# 后面应该都是带名字的参数（两个选择，*，命名关键字参数，**kwargs）

#顺序
# 位置参数  >默认参数 >命名关键字参数/可变参数  >关键字参数
def f1(a,b,c=0,* args,**kwargs):
    print("a={}  b={}  c={}  args={}  kwargs={}".format(a,b,c,args,kwargs))
f1(1,2)
f1(1,2,3)
f1(1,2,3,4,5)
f1(1,2,3,4,5,6,x=1)

def f2(a,b,c=0,*,d,**kwargs):
    print("a={}  b={}  c={}  d={}  kwargs={}".format(a, b, c, d, kwargs))
f2(1,2,3,d=99)
f2(1,2,3,d=99,f=100)
f2(1,2,3,f=100,d=99)

# 万能参数：当传入参数的时候，符合没有名字的参数放前面，有名字的参数放后面
def f3(* args,**kwargs):
    print("args={}  kwargs={}".format(args,kwargs))
f3()
f3(1,2,3,x=1,y=2)
f3(1,2,3,x=1,y=2)

def t(*args,b):
    pass
# 当可变参数后定义位置参数，会自动转换成命名关键字参数。
t(1,2,3,4,b=5)


# def t(*args,b,**kwargs):
def t(*args,**kwargs):
    print(args)
    print(b)
    print(kwargs)
t(1,2,3,4,5,b=3,c=5,d=6)


# 四、函数的返回值
li=[1,2,3]
li.sort()
sorted(li)
# 返回值：函数调用之后的结果
def a():
    return "返回值"
b=a()
print(b)

#加法
def add(a,b):
    c=a+b
    # return c
    print(a+b)
    # return a+b
    # return None
    # return

x=add(5,9)
print(x)

"""
return 返回None：
（1）return None
（2）return
（3）不写返回值
"""

# return  函数的返回值，可以是变量，也可以是表达式。
# 当程序执行到return之后，后面的语句不再执行。
# 程序中只要有return，return之后的语句就不再执行。（错误）
# return是可以返回多个返回值（以元组的形式存在）
# 可以使用平行赋值对结果进行变量的绑定（变量数量要跟结果的数量一致）
def compute(a,b):
    # return a+b
    # return a-b
    # return a/b
    # return a*b
    return a+b,a-b,a*b,a/b
c=compute(3,4)
c1,c2,c3,c4=compute(3,4)
print(c)
print(c1,c2,c3,c4)

# 练习：计算一元二次方程的解。


# 五、函数的传递方式
# 1. 不可变类型的值传递
# 数值、字符串、字节、布尔
def myfun(x):
    x=x+2
    print("在myfun里面x的值是{}".format(x))
x=100
myfun(x)
print("在myfun函数的外面a的值是{}".format(x))

# 结论：对于不可变类型的参数来说，在参数传递的过程中，不会改变函数调用之前的参数值。


# 2.可变类型的值传递
def myfun(x):
    x[0]="new"
    print("在myfun里面x的值是{}".format(x))
x=[1,2,3]
myfun(x)
print("在myfun函数的外面a的值是{}".format(x))
# 结论：对于可变类型的参数来说，在参数传递的过程中，会改变函数调用之前的参数值。


# 六、命名空间和作用域
# 命名空间：在python中可以认为命名空间是一个保存命名的容器。
# 容器：装名字的容器
# 名字：变量的定义、函数名、类名、模块名。。。。
# 名字存储的时候，以字典的形式存储：key-value
# 名字key：引用的内存对象地址value
li=[1,2,3]
print(id(a))
def f():
    pass

# 名字是在什么时候定义？定义的位置在哪？
# 对于变量来说：当第一次赋值的时候，就决定了在哪个命名空间。
# 对于函数来说：def出现的时刻，就决定过了函数在哪个命名空间。

#具体变量或者函数的名字在哪个命名空间，取决于定义的“区域”
# 1. 命名空间划分成以下几类：
# 1). 内建命名空间：在python解释器启动的时候，就创建好了。
# 2). 全局命名空间：在读取模块定义的时候，创建的，直到程序运行结束。
# 3). 局部命名空间：函数执行的时候创建，在函数执行之后销毁。
# def a(xx):
#     xx=xx+1
#     bb=1
#       print(xx,bb)
# print(bb)
# print(xx)
#  注意：命名空间千万不要理解成包含的关系。

# 2. 作用域：名字在自己的命名空间中的作用范围。
#  比如定义了一个变量，在哪能用？
# 1）内建命名空间的作用域： 所有模块。最大。
# 2）全局命名空间的作用域：在整个py文件中都有效。如果其他的模块（文件）
#    希望访问到某一个模块的全局命名空间下的名字，需要使用import
# 3) 局部命名空间的作用域：最小，只在当前函数内部有效。
# 注意：虽然作用域也有大小，但是也不要理解成包含关系。
# yy=1
#
# def a(xx):
#     xx=xx+1
#     bb=1
#     print(xx,bb)
# print(bb)
# print(xx)
# print(yy)
#
# def outer():
#     p=1
#     def inner():
#        print(p)

# 3. 访问的顺序原则
# 在命名空间下的名字，能否被访问到，能在哪被访问到，顺序。
# （1） 定义一个全局变量，然后在函数内去修改全局变量
x=1
def fun():
    # print(x,"在fun函数中")
    global x  # 解决，需要声明global
    x=2
    print(x,"在fun函数中")
fun()
print(x,"在fun函数的外侧")

# （2） 在函数内，先输出变量，然后尝试修改该变量的值
# 命名空间中有哪些名称，不是在执行的时候，才一点一点加的变量，
# 而是在程序解析编译的时候，就决定了有哪些名字
x=1
# def fun2():
#     print(x)
#     # 原因是因为在当前的fun2局部空间作用域中到到了x，
#     # 代码认为声明在后，使用在前。
#     x=2
# fun2()

# （3） 在函数内部，将全局变量参数+1
# x=1
# def fun3():
#     # x=x+1  # 在fun3的内部找到了x，但是是在赋值之前x+1
# fun3()

# （4） 定义一个全局 变量id，定义一个li=[1,2,3],再打印列表所在的内存地址。
# id=2
# li=[1,2,3]
# print(id(li))
# 结论：变量名、函数名、类名，都不要使用内建命名空间的名字。


# LEGB原则
#  当python解析器遇到一个名字的时候，一定要到内存中查找对应的对象，要有查找顺序
# （1） 先到局部命名空间去找（本身是在局部命名空间中），如果没找到 ，会继续到外围
#       命名空间中查找
# （2） 如果在外围命名空间中没有找到，会到全局命名空间中查找
# （3） 如果在全局命名空间中没有找到，会到内建命名空间中查找
# （4） 如果在内建命名空间中没有找到，则会 报错。
# L--local  ------局部
# E--enclosing----外围
# G--global-------全局
# B--bulidins-----内建

# 对于名称有两种操作：访问、修改和删除
# （1）访问：读取，会严格按照LEGB的顺序
# （2）修改和删除：（不遵循LEGB原则）
#      修改：先从最小的作用域开始查找，如果找到则修改，如果找不到，
#           不会再继续往上查找，而是直接在当前最小的最用于中新建一个。
#           （为了避免不小心起了一个跟全局变量名一样的变量，污染全局变量）
#      删除：只能删除自己当前命名空间中的名字，不能删除其他命名空间的名字。

# 对于在局部命名空间中希望修改全局变量或者外围变量：使用global和nonlocal关键字
# 在局部命名空间中修改全局变量，global
# y=2
# def g():
#     # print(y)
#     global y
#     y=3
#     print(y)
# g()
# print(y)
#
# # 在局部命名空间中修改外围变量，nolocal
# def  out():
#     x=1
#     def inner():
#        nonlocal x
#        x=2
#     inner()
#     print(x)
# out()


# 七、 lambda表达式 （入）
# python的函数属于头等函数
# 头等函数：变量跟函数类似，函数名也可以像变量那样操作，被赋值、被传递、作为返回值。
# （1）赋值
def x():
    print("执行x函数")
y=x
# x()
y()

# (2) 传递
li=[1,3,-2]
abs(-1)
li.sort(key=abs)
print(li)

#(3) 函数还以作为返回值
#嵌套函数：函数中再定义函数
# 闭包
def outer():
    def inner():
        print("inner函数执行")
    return inner  # 返回的是内部函数的名字
a=outer()
a()

# (4) 当函数体非常简单，可以lambda表达式表达函数
# 格式：lambda 参数 : 返回值表达式
#lambda代表函数，但是是匿名函数（没有名字的函数）
# 对参数进行+1的功能
def s(k):
    return  k+1
print(s(10))
aaa=lambda k:k+1
print(aaa(20))

li=[1,2,-5,-6]
# 排序的规则：每个元素+1之后的结果再排序
# li.sort(key=s)
# print(li)

# key可以直接指向匿名的lambda表达式
li.sort(key=lambda k:k+1)
print(li)

def add(a,b):
    pass
def add(a,b,c):
    pass