# 1.	请用索引取出下面list的指定元素：
# # -*- coding: utf-8 -*-
# L = [
# ['Apple', 'Google', 'Microsoft'],
# ['Java', 'Python', 'Ruby', 'PHP'],
# ['Adam', 'Bart', 'Lisa']
# ]
#
l=[
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]
# print(l[0][1])
def q1():
    #遍历每一个成员
    for i in l:
        for j in i:
            print(j)
def q1_1():
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j])

#
# 2.	定义一个字符串a，里面有字符，有数字，请将a字符串的数字取出，
# 并输出成一个新的字符串,使用列表推导式。
#
def q2():
    a="jgj231jk2gh343kjgg4jk5gjk2"
    a_new=[]
    [a_new.append(i) for i in list(a) if i.isdigit()]
    print("".join(a_new))
# q2()

# 3.	有一个已经排好序的升序列表。现输入一个数，要求按排序将它插入数组中。
# a)	除使用切片、insert或者append以外，自己尝试想一下不用现成方法，只使用索引的原始方式是否可以实现。
#
def q3():
    # 切片 定位到位置，插入
    li=[1,2,3,44,55,66,77]
    li[6:]=[99]
    print(li)

def q3_1():
    #append 方法
    li = [1, 2, 3, 44, 55, 66, 77]
    li.append(99)
    print(li)

def q3_2():
    li = [1, 2, 3, 44, 55, 66, 77]
    a=int(input("请输入一个数："))
    for index,i in enumerate(li):
        if a<i:
            li.insert(index,a)
            break
    else:
            li.append(a)

    print(li)

# q3_2()

# 4.	将列表逆序输出，使用三种方式。
#
def q4():
    li=[1,2,3,4,5,656]
    print(li[::-1])

def q4_1():
    li = [1, 2, 3, 4, 5, 656]
    li.reverse()
    print(li)

def q4_2():
    li = [1, 2, 3, 4, 5, 656]
    for i in range(int(len(li)/2)):
        li[i],li[-1-i]=li[-1-i],li[i]
    print(li)

def q4_3():
    li = [1, 2, 3, 4, 5, 656]
    li_new=sorted(li,reverse=True)
    print(li_new)

q4_3()

# 5.	列表：实现字符串的反序输出，两种方式
#
#
def q5():
    str="asjdasjdsfhaklh"
    str=str[::-1]
    print(str)

def q5_1():
    str = "asjdasjdsfhaklh"
    li=[]
    for i in str:
        li.append(i)
    li.reverse()
    print("".join(li))
# q5_1()

# 6.	输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：
#
#
def q6():
    year,months,date=int(input("请输入年份：")),int(input("请输入月份：")),int(input("请输入日期："))
    months=[0,31,30,30,30,31,30,31,31,30,31,30,31]
    day=0
    if 0<months<=12:
        for i in range(months):
            day+=months[i]
    if (year%4==0 and year%100!=0 or year%400==0) and months>2:
        day+=1
    print(day+date)
# q6()
# 7.	将二维列表转换成一维列表。
#

def q7():
    li=[[1,2,3],
        [4,5,6]]
    li_new=[]
    for i in li:
        for j in i:
            li_new.append(j)
    print(li_new)

from numpy import *
def q7_1():
    li = array([[1,2,3],
                [4,5,6]])
    li_new = li.flatten()
    print(li_new)

def q7_2():
    li = [[1, 2, 3],
          [4, 5, 6]]
    li_new=[y for x in li for y in x]
    print(li_new)

q7_2()

# 8.	将上面二维列表中每个元素格式扩大十倍，列表维度不变。
#
def q8():
    li = [[1, 2, 3], [4, 5, 6]]
    print([[j*10 for j in i] for i in li])
# q8()

# 9.	实现二维列表（矩阵）的转置（m * n）。

from numpy import *
def q9():
    li=[[1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    li_new=transpose(li)

    print(li_new)

# def q9_1():
#     li = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]
#           ]
#     li_1=[]
#     li_2=[]
#     li_3=[]
#     for i in li:
#         for j in i:
#             li_1.append(li[i][j])
#     print(li_1)
# q9_1()
# 10.	输入若干数值，然后实现摄氏度与华氏度的相互转换。摄氏度 = (华氏度 - 32) / 1.8。
#
# def q10():
    """
    输入若干数值，进行温度转换
    摄氏度=(华氏度 - 32) / 1.8
    华氏度=摄氏度*1.8+32
    :return:
    """
    t=input("请输入带温度的符号的温度值（例如32C）：").lower()
    if t[-1] in ['f']:
        C = (eval(t[0:-1]) - 32) / 1.8
        print("转换后的温度是{:.2f}C".format(C))
    elif t[-1] in ['c']:
        F = 1.8 * eval(t[0:-1]) + 32
        print("转换后的温度是{:.2f}F".format(F))
    else:
        print("输入格式错误")
# q10()

# 11.	输入一些数值，以stop作为输入的结束。求列表的最大值与最小值，和与平均值。
#
def q11():
    li=[]
    while True:
        s=input("请输入一些数值：")
        if s=="stop":
            break
        else:
            li.append(int(s))
    print(li)
    max=min=li[0]
    sum=0
    for i in li:
        sum+=i
        if max<i:
            max=i
        else:
            min=i
    print("这些数值的总和为{}，最大值为{}，最小值为{},平均值为{:.2f}".format(sum,max,min,sum/len(li)))
# q11()

# 12.	编写程序，输入一个字符，判断是否为关键字。
# keyword.kwlist
#
def q12():
    import keyword
    print(keyword.kwlist)
    while True:
        k=input("请输入字符：")
        if k=="stop":
            break
        elif k in keyword.kwlist:
            print("是关键字！")
        else:
            print("不是关键字")
# q12()

# 13.分别对一维列表与二维列表重复2次，然后修改列表中的元素。总结一维列表与二维列表表现的差异性，并总结原因，
# 画出内存图。
# # * 重复运算符 是浅拷贝
#
def q13():
    a=[1,2,3,4,5,6]
    b=[[1,2,3],[4,5,6]]
    a2=a*2
    b2=b*2
    print(a,a2,b,b2,sep="\n")
    a[0]="new"
    b[0]="new"
    print(a,b)

# q13()
#
# 14.	比较[[“_”]*3 for I in range(3)]和[[“_”] *3]*3有什么不同
#
def q14():
    a=[["_"]*3 for I in range(3)]
    b=[["_"] *3]*3
    print(a,b,sep="\n")
q14()
# 15.	题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：列表有sort方法，所以把他们组成列表即可。
#
def q15():
    li=[]
    for i in  range(3):
        x=int(input("请输入一个数："))
        li.append(x)
    li.sort()
    print(li)

def q15_1():
    x ,y,z= int(input("请输入第一个数：")),int(input("请输入第二个数：")),int(input("请输入第三个数："))
    if x>y:
      x,y=y,x
    if x>z:
        x,z=z,x
    if y>z:
        y,z=z,y
    print(x,y,z)

def q15_2():
    x ,y,z= int(input("请输入第一个数：")),int(input("请输入第二个数：")),int(input("请输入第三个数："))
    m=[x, y, z]
    m.sort()
    print(m)

# q15_2()
#
# 16.	时间：暂停一秒输出，并格式化当前时间
#
#
import time
def q16():
        ls=time.localtime()
        print(ls)
        time.sleep(1)
        print(time.s.strftime("%Y-%m-%d %H:%M:%S",ls))
# q16()
#
# 17.	 题目：求s=a+aa+aaa+aaaa+aa...a的值
# 其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#
def q17():
    a=int(input("请输入a的值："))
    n=int(input("请输入位数："))
    s=0
    sum=0
    for i in range(n):
        s+=a*(10**i)
        sum+=s
    print(sum)
# q17()

# 18.	一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，
# 共经过多少米？第10次反弹多高
#
def q18():
    hight=100
    time=10
    s=0
    for i in range(1,time+1):
        if i==1:
            s=hight
        else:
            s+=hight*2
        hight/=2
        if i==10:
            print(hight)
    print(s)
# q18()

# 19.	二维数组。输出两个矩阵的元素相加和
# X = [[12, 7, 3],
# [4, 5, 6],
# [7, 8, 9]]
#
# Y = [[5, 8, 1],
# [6, 7, 3],
# [4, 5, 9]]
#
def q19():
    x = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
    y = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]]
    li=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
           li[i][j]=x[i][j]+y[i][j]
    print(li)
# q19()
# 20.	企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，
# 可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
#
#
def q20():
    I=float(input("请输入当月利润，单位为万元："))
    bns=0
    cat=[100,60,40,20,10,0]
    pct=[0.01,0.015,0.03,0.05,0.075,0.1]
    for i in range(6):
        if I >cat[i]:
            I=I-cat[i]
            bns=bns+I*pct[i]
            I=cat[i]
    print("当月应发放奖金数为{}万元".format(bns))

# q20()

# 21.	假设一年期定期利率为3.25%，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番？
#
def q21():
    money=10000
    year=0
    while money<20000:
        money*=1.14
        year+=1
    print(year)

q21()


# 22.	以列表，元组类型分别测试，x += y与x = x + y是否存在差异性，并总结其原因。
#
def q22():
    x=[1,2,3]
    y=[1,2,3]
    # x+=y
    print(x,id(x))
    x = x + y
    print(x,id(x))
    x1=(1,)
    y1=(1,)
    # x1+=y1
    print(x1,id(x1))
    x1=x1+y1
    print(x1,id(y1))
    """
    列表:x+=y 比x=x+y更省内存，前者x的id不变，后者id改变了，说明是新建的列表
    元组:x+=y ，x=x+y，对于内存来说一致，x的id都是新的，说明新创建元组，因为元组的元素不可变
    """
# q22()
# 23.	对元组进行复制，会发生什么情况？总结。
# 三种复制方式，赋值、切片浅拷贝、深拷贝
#
#
import copy
def q23():
    a=(1,2,3,[4, 5])
    b=a
    c=a[:]
    d=copy.copy(a)
    e=copy.deepcopy(a)
    print(a,b,c,d,e)
"""
赋值： 赋值操作(包括对象作为参数、返回值),
不会开辟新的内存空间,他只是赋值了对象的引用.
也就是除了b这个名字之外,没有其他的内存开销,修改了a也就影响了b,修改了b,也就影响了a.
浅拷贝：浅拷贝会创建新的对象,其内容非原对象本身的引用,而是原对象内第一层对象的引用,
修改嵌套列表中的元素,地址未发生变化,指向的都是用一个位置
深拷贝：深拷贝会创建新对象，并一直复制到不可变类型
"""

# 24.	del是否可以应用于元组，字符串与字节类型，为什么？
#
#
a=(1,2,3)
b="1asdasd"
c=b"asdasdasd"
# del a[0]
# del a[1]
# del b
# del c
# del a
print(a,b,c)
"""
del 元组名，删除元组，当访问被删除的元组时会报错
"""