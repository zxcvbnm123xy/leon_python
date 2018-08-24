# 1.请用索引取出下面list的指定元素，遍历所有元素
# # -*- coding: utf-8 -*-
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
def q1():
    # 直接遍历
    print(L[1][1])
    for i in L:
        print(i)
        for j in i:
            print(j)

    # 位置遍历
    for i in range(len(L)):
        # print(L[i])
        for j in range(len(i)):
            print(L[i][j])


# 2.将数组逆序输出（不是按大小，就是元素顺序逆序），使用两种方式。
a=[1,3,4,5,6,-1]
#方式一
a.reverse()
print(a)

#方式二
print(a[::-1])

#方式三
a_new = []
for i in range(len(a)): #遍历所有的元素
    a_new.append(a[-1-i])
print(a_new)

for i in range(len(a)):
    a_new.append(a.pop())
print(a_new)

#方式四 insert
for i in a:
    a_new.insert(0,i)
print(a_new)

#方式五
a=[1,3,4,5,6,-1]
for i in range(int(len(a)/2)):
    a[i],a[-1-i]=a[-1-i],a[i] #平行赋值
print(a)

# 内置方法，原地逆序
for i in reversed(a):
    a_new.append(i)
print(a_new)

# 3.输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
# 思路
# 2018-8-23
# days=7月之前一共有多少天
# days+23
# 闰年：能够被4整除同时不能被100整除的年份，或者是能够被400整除

year = int(input("请输入年："))
month = int(input("请输入月："))
day = int(input("请输入日："))
months=[0,31,28,31,30,31,30,31,31,30,31,30,31]

s=0
if 0<month<=12:
    for i in range(month):
        s+=month[i]
    s+=day

#判断闰年
if month>2 and (year%4==0 and year%100!=0 or year %400==0):
    s=+1
print("当年是今日的第几天：")

# 4.求列表li=[1,4,-5,9,-6]
# 的最大值与最小值，和与平均值。
li=[1,4,-5,9,-6]
#思路：先取出一个值，假设成最大值最小值，遍历所有元素
max=min=li[0]
sums=0
for i in li:
    if i>max:
        max=i
    if i<min:
        min=i
    sums+=i
print("max=",max)
print("min=",min)
print("maxarg=",sums/len(i))
print("sums=",sums)

# 5.编写程序，输入一个字符，判断是否为关键字。
# keyword.kwlist
# import keyword
# x=input("请输入一个字符：")
# print(keyword.kwlist)
# if x in keyword.kwlist:
#     print("是关键字")
# else：
#     print("不是关键字")

# 6.输入三个整数x,y,z，形成一个列表，请把这三个数由小到大输出。
# 程序分析：列表有sort方法，所以把他们组成列表即可。
l=[]
for i in range(3):
    m=int(input("请输入一个数字："))
    l.append(m)
l.sort()
print(l)

# 在题6的基础上，如果有余力的同学可以不用sort方法，自己写排序方法做，
# 提示，获得列表中每次获得的最小值，使用索引。
# li=[1,4,-5,9,-6]
"""
思路：每一次都获取当前列表的最小值
"""
li=[1,4,-5,9,-6]
L=[]
min=li[i]
for i in li:
    if i<min:
        min=i
        L.append(min)
        li.remove(min)

# 7. 题目：求s=a+aa+aaa+aaaa+aa...a的值
# 其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 输入两个值，一个是当前的数字，一个是最大的位数
# a = input("请输入每一位是什么：")
# n = input("请输入最大数字数是多少位？")
# s=0
# for i in range(1,n+1):
#     # print(a*i)
#     num=int(a*i)
#     s+=num
# print(s)
def que():
    a = input("请输入每一位是什么：")
    n = input("请输入最大数字数是多少位？")
    #生成每一个数字
    # 2=           2+0*10
    # 22=          2+2*10
    # 222=         22+20*10
    # 2222=        222+200*10
    # L=[]
    # num=0
    # for i in range(n):
    #     num=num+a
    #     a=a*10
    #     # L.append(num)
    #     s+=num
    # print(s)

# 8. 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
# 求它在第10次落地时，共经过多少米？第10次反弹多高？

hight=100
times=10
s=0
for i in range(1,times+1):
    if i==1:
        s=hight
    else:
        s+=hight*2
    hight=hight/2
print(s)

# 9.列表通过copy方法复制、切片方法复制、
# 变量赋值方式复制，修改内部元素，画出内存图
a=[1,2,3,[4,5]]
a1 =a[:]
print(id(a1),id(a))
print(id(a1[3]),id(a[3]))

# 10.看一下列表、元组、字符串的整切片指向的对象是什么？
a = ["1", "2", "3", "4", "5"]
b = "1,2,3,4,5"
c = (1, 2, 3, 4, 5)
print(id(a), id(b), id(c))
print(id(a[:]), id(b[:]), id(c[:]))
