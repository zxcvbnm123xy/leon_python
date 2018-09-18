
# l=["1","2","3"]
# print(sum(("a","b"),"e"))
# sum(打包好的序列,初始值) 初始值默认0
# 先将打包好的序列拆包，将元素进行+
# 再跟初始值进行+操作
print(sum([1,2,3,4,5],5))



L = [ ['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa'] ]
# 将L拆包，形成一个序列  是包含了3个列表的序列
# 将序列中元素+
print(['Apple', 'Google', 'Microsoft']+['Java', 'Python', 'Ruby', 'PHP']+['Adam', 'Bart', 'Lisa'])
# print(['Apple', 'Google', 'Microsoft']+['Java', 'Python', 'Ruby', 'PHP']+['Adam', 'Bart', 'Lisa']+0)
# ['Apple', 'Google', 'Microsoft']+['Java', 'Python', 'Ruby', 'PHP']+['Adam', 'Bart', 'Lisa']+0
print(sum(L,[]))


# 对于字符串和字节就不可以这样操作
# print(sum(["a","b"],""))
# print(sum([b"a",b"b"],b""))
# 拆包  "a" 、 "b"
# print("a"+"b")


# 1.	请用索引取出下面list的指定元素：
# # -*- coding: utf-8 -*-
L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]
print(L[1][1])
for i in L:
    for j in i:
        print(j,end=" ")
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j],end=" ")
print()

def que1():
    # 希望输入一个字符串，查看字符是否在列表中的元素，如果属于，则显示一下对应的位置
    a=input("输入一个单词").lower().capitalize()
    for index,i in enumerate(L):
        if a in i:
            print("存在，位置{}-{}".format(index,i.index(a)))
            break
    else:
        print("没有找到")
    L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    ]
    # 第二种方式 ，双层for循环
    for in1,i in enumerate(L):
        for in2,j in enumerate(i):
            if a==j:
                print("存在，位置{}-{}".format(in1,in2))
                break
        else:
           continue
        break
    else:
        print("没找到")
#
#
# 2.	定义一个字符串a，里面有字符，有数字，请将a字符串的数字取出，
# 并输出成一个新的字符串
# 使用列表推导式。
a="adjklgfj1jkjd565kjkfdj4ll"
print([i for i in a if i.isdigit()])
# 将列表拼回字符串 join
# a.join(b) 将b序列中的元素使用a字符串拼接
print("".join([i for i in a if i.isdigit()]))
#
#
# 3.	有一个已经排好序的升序列表。现输入一个数，要求按排序将它插入列表中。
li=[1,40,45,48,90]
def que3_1():
    insertnum=int(input("请输入一个数字："))
    for index,i in enumerate(li):
        if insertnum<=i:
            # li[index:index]=[insertnum]
            li.insert(index,insertnum)
            break
    else:
       li.append(insertnum)
    print(li)
def que3_2():
    li=[1,40,45,48,90]
    insertnum=int(input("请输入一个数字："))  #46
    if insertnum>li[-1]:
        li.append(insertnum)
    else:
        for index in range(len(li)):
            if insertnum<=li[index]:
                #先将列表扩充一个位置
                li.append("占位")
                temp=li[index]
                li[index]=insertnum
                for j  in range(index+1,len(li)):
                    temp,li[j]=li[j],temp
                break
        print(li)

# a)	除使用切片、insert或者append以外，自己尝试想一下不用现成方法，只使用索引的原始方式是否可以实现。
#
# 4.	将列表逆序输出，使用三种方式。
a=[3,4,5,77,88,1]
# (1)切片
# print(a[::-1])
#(2)reverse
# a.reverse()
# print(a)
#(3)reversed
# print(list(reversed(a)))
#(4) append
li=[]
a=[3,4,5,77,88,1]
for i in range(len(a)-1,-1,-1):  #右到左
      li.append(a[i])
print([a[i] for i in range(len(a)-1,-1,-1)])
print(li,"range(len(a)-1,-1,-1):  #右到左")
# for i in range(len(a)):
#     li.append(a[-1-i])
# print(li)
a=[3,4,5,77,88,1]
#(5)insert
# li=[]
# for i in a:
#     li.insert(0,i)
# print(li)

#(6)pop 和append
# a=[3,4,5,77,88,1]
# li=[]
# for i in range(len(a)):
#     li.append(a.pop())
# print(li)

#(7)直接使用算法
a=[3,4,5,77,88,1,2]
for i in range(int(len(a)/2)):
    # 0   -1
#     1   -2
#    i    -1-i
    a[i],a[-1-i]=a[-1-i],a[i]
print(a)


#
# 5.	实现字符串的反序输出，两种方式
s="abcdfdlkfdy"
#方式一：
print(s[::-1])

# 方式二：
L=list(s)
print(L)
L.reverse()
print("".join(L))

#
# 6.	输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：
def que6():
    year=int(input("请输入年："))
    month=int(input("请输入月："))
    day=int(input("请输入日："))
    months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    sums=0
    if 0<=month<=12:
        for i in  range(month):
            sums+=months[i]
    if (year%4==0 and year!=100 or year%400==0 ) and month>2:
        sums+=1
    sums+=day
    print(sums)


#
#
# 7.	将二维列表转换成一维列表。
li=[[1,2,3,4,5],[6,7]]
l=[]
for i in li:
    for j in i:
        l.append(j)
print(l)

#
# 8.	将上面二维列表中每个元素格式扩大十倍，列表维度不变。
# 使用列表推导式将二维列表转换成一维列表
print([10*j for i in li for j in i])
print([[ 10*i for i in item] for item in li])



#
# 9.	实现二维列表（矩阵）的转置（m * n）。
li=[[1,2,3],
    [4,5,6],
    [7,8,9]]
# li=[[1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]]
# 转置之后的第0个元素，应该是原来的每个元素的第0个元素的集合
# 转置之后的第1个元素，应该是原来的每个元素的第1个元素的集合
# 转置之后的第2个元素，应该是原来的每个元素的第2个元素的集合
# 思路：遍历原来的li，将每个元素中的第0个元素形成一个小列表，
#  最终形成3个小列表
# 将3个列表形成最大的列表
li_new=[]
for index in range(len(li)):
    one=[]
    for j in li:
        one.append(j[index])
    # print(one)
    li_new.append(one)
print(li_new)

li=[[1,2,3],
    [4,5,6],
    [7,8,9]]
print([[item[index] for item in li] for index in range(len(li))])



#
# 10.	输入若干数值，然后实现摄氏度与华氏度的相互转换。
# 摄氏度 = (华氏度 - 32) / 1.8。
def que10():
    h=[]
    while True:
        a=input("请输入一个华氏温度：")
        if a=="exit":
            break
        x=float(a)
        h.append("{:.2f}℃".format((x-32)/1.8))
    print(h)


#
# 11.	输入一些数值，以stop作为输入的结束。求列表的最大值与最小值，和与平均值。

def que11():
    li=[]
    while True:
        x=input("输入一个数值：")
        if x=="stop":
            break
        elif x.isdigit():
            li.append(int(x))
        else:
            print("输入不合法")
    print(li)
    min=max=li[0]
    s=0
    for item in li:
        s+=item
        if min>item:
            min=item
        if max<item:
            max=item
    print("最大值{}，最小值{}，平均值{:.2f}".format(max,min,s/len(li)))


#
# 12.	编写程序，输入一个字符，判断是否为关键字。
def que12():
    import keyword
    x=input("请输入字符")
    print(True if x in keyword.kwlist else False)


#
# 13.	分别对一维列表与二维列表重复2次，然后修改列表中的元素。
# 总结一维列表与二维列表表现的差异性，并总结原因，画出内存图。
# # * 重复运算符 是浅拷贝

li1=[1,2]
a=li1*2
print(a)
li1[0]="new"
print(a)

li2=[[1],[2]]
b=li2*2
print(b)
li2[0][0]="new"
print(b)
# * 相当于浅拷贝
# 因为对于不可变类型的元素来说，修改复制之前列表中元素，对于复制之后的列表没有影响
# 对于可变类型的元素来说，修改复制之前列表中元素，对于复制之后的列表有影响


#
#
# 14.	比较[[“_”]*3 for I in range(3)]和[[“_”] *3]*3有什么不同
c=["_"]
a=[c*3 for I in range(3)]
b=[c *3]*3
print(a)
print(b)
a[0][0]="new"
print(a)
b[0][0]="new"
print(b)

# 对于* 重复 来说，无论是可变类型还是不可变类型，都没有复制原来的对象
# 产生的是一个新对象，根据* 次数来指向原来的对象

#
# 15.	题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：列表有sort方法，所以把他们组成列表即可。
# li=[]
# for i in range(3):
#     m=int(input("请输入一个数字"))
#     li.append(m)
# li.sort()
# print(li)

# 每次找到一个最小值
# 默认的最小值是第一个元素
#
li=[10,20,80,77,55,67,68,8]
# min=0
# for i in range(1,len(li)):
#     if li[i] <li[min]:
#         min=i
# li[0],li[min]=li[min],li[0]
# print(li)
#
# min=1
# for i in range(1,len(li)):
#     if li[i] <li[min]:
#         min=i
# li[1],li[min]=li[min],li[1]
# print(li)


for j in range(len(li)):
    min = j
    for i in range(j+1, len(li)):
        if li[i] < li[min]:
            min = i
    li[j], li[min] = li[min], li[j]
    print(li)


#
#
# 16.	时间：暂停一秒输出，并格式化当前时间
# import time
# time.time  毫秒数
def que16():
    import time
    # print(time.time())
    print(time.localtime())
    print(time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()))
    time.sleep(1)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#
#
#
#
#
# 17.	 题目：求s=a+aa+aaa+aaaa+aa...a的值
# 其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
def que17_1():
    a=input("请输入每一位是什么")
    n=int(input("请输入最多有多少位"))
    sums=0
    for i  in range(1,n+1):
        # print(a*i)
        sums+=int(a*i)
    print(sums)

"""
0
2=0+2*10**0
22=2+2*10**1
222=22+2*10**2
2222=222+2*10**3
"""
def que17_2():
    a=int(input("请输入每一位是什么"))
    n=int(input("请输入最多有多少位"))
    num=0
    sums=0
    for i in range(n):
        num+=a*(10**i)
        sums+=num
    print(sums)





# 18.	一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
# 求它在第10次落地时，共经过多少米？第10次反弹多高？
h=100
s=0
for i in range(10):
    if i==0:
        s=h
    else:
        s+=h*2
    h/=2
print(s,h)

#
#
#
# 19.	二维数组。输出两个矩阵的元素相加和
X = [[12, 7, 3],
[4, 5, 6],
[7, 8, 9]]

Y = [[5, 8, 1],
[6, 7, 3],
[4, 5, 9]]

r= [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[i])):
         r[i][j]= X[i][j]+Y[i][j]
print(r)
#
#
# 20.	企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，
# 高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，
# 可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
# 超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
L=120
c=0
if 0<=L<=10:
    c=0.1*L
elif 10<L<=20:
    c=0.075*(L-10)+0.1*10
elif 20<L<=40:
    c=0.05*(L-20)+0.075*(20-10)+0.1*10
elif 40<L<=60:
    c=0.03*(L-40)+ 0.05*(40-20)+0.075*(20-10)+0.1*10
elif 60<L<=100:
    c=0.015*(L-60)+0.03*(60-40)+ 0.05*(40-20)+0.075*(20-10)+0.1*10
elif 100<L:
    c=0.01*(L-100)+0.015*(100-60)+0.03*(60-40)+ 0.05*(40-20)+0.075*(20-10)+0.1*10
print(c)
li=[100,60,40,20,10,0]
rates=[0.01,0.015,0.03,0.05,0.075,0.1]
c=0
for i in range(6):
    if L>li[i]:
        c+=(L-li[i])*rates[i]
        L=li[i]
print(c)


#
#
#
# 21.	假设一年期定期利率为3.25%，计算一下需要过多少年，
# 一万元的一年定期存款连本带息能翻番？
c=10000
year=0
while c<20000:
    year+=1
    # c=c*(1+0.0325)
    c*=1.0325
print(year)
#
#
# 22.	以列表，元组类型分别测试，x += y与x = x + y是否存在差异性，并总结其原因。
x=(1,)
y=(2,)
print(id(x))
x+=y
# x=x+y
print(x,id(x))
# 对于列表来说
#  x += y 对于x只创建一片内存（只创建一个对象）
#  x = x + y 会将结果重新创建一个新对象。

# 对于元组来说 ， x += y 和x = x + y都是新创建对象。
# 原因：元组是不可变类型


#
# 23.	对元组进行复制，会发生什么情况？总结。
# 三种复制方式，赋值、切片浅拷贝、深拷贝
# 赋值、切片、copy包下的copy都是指向原来的元组对象。
# 深拷贝会一直拷贝到不可变的数据类型为止
import copy
a=(1,2,3,[4,5])
b=a
c=a[:]
d=copy.copy(a)
e=copy.deepcopy(a)

print(id(a),id(b),id(c),id(d),id(e))
a[3][0]="new"
print(a,e)


#
#
# 24.	del是否可以应用于元组，字符串与字节类型，为什么？
t=(1,2,3)
s="abc"
b=b"abc"
# del t[0]
# del s[0]
# del b[0]
# 不能能够删除元组，字符串，或者字节中的元素，因为他们都是不可变的数据类型。
