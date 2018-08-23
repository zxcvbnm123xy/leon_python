"""
二、循环
1. for
for 循环：依据任意序列中的子项，按其在序列中的顺序进行迭代
"""
# 背景：
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

"""
for循环的语法
# 变量名：是序列中的每一个元素
迭代对象：序列（字符串、字节、列表、元组）和其他可迭代对象
遍历：指将一个可迭代的对象每个元素都查看一遍。

for 变量名 in 序列（字符串、字节、列表、元组）和其他可迭代对象:
   循环体
"""
# 使用for循环输出5次hello world
# for i in "11111":
#     print("hello world")

# 可迭代对象可以换成其他的，只要满足可迭代对象是五次就可以。
# for i in "12345":
#     print("开始：")
#     print("hello world")

# 将可迭代对象中的每一个元素都加1
for i in "11111":
    # print(i,type(i))
    n=int(i)
    n+=1
    print(n)

# 1+2+3+4+5
s=0
for i in "12345":
    n=int(i)
    s=s+n
print(s)

#1+2+3+...100
# range(start,end,step)函数：能够产生一个列表
# 包含start不包含end
# step：默认1：方向是从左到右
# print(range(1,5))  # [1,2,3,4]  python2x
# print(list(range(1,5)))         python3x
a=range(1,5)
print(type(a))
for i in a:
    print(i)

print(list(range(1,101)))

# 1+...+100累加和
s=0
for  i  in range(1,101):
    # s=s+i
    s+=i
print(s)

# 练习
"""
1. 定义字符串、定义字节，使用for循环对其进行遍历，计算长度

"""
s="hello world python"
l=0
for i in s:
    print(i)
    l=l+1
print("通过for循环计算出的l={}".format(l))
# 0 1 2 3  ... len(s)-1
# for i in range(0,len(s)):
for i in range(len(s)):# 简化
    print("通过索引访问每一个元素",s[i])


# 字节的遍历是ascii
# 通过索引访问的也是ascii
l1=0
b=b"helloworldpython"
for i in b:
    l1+=1
    # print(i)
print("通过for循环计算出的l1={}".format(l1))
for i in range(len(b)):
    print("通过索引的方式访问字节元素",b[i])


#2. 输出1-100以内所有的奇数 使用两种办法
# print(list(range(1,101,2)))
for i in range(1,101):
    if i%2!=0:
        print(i,end=" ")
print()
#3.输出1-100以内所有的偶数
for i in range(1,101):
    if i%2==0:
        print(i,end=" ")

print()
#4.有一些列的温度数 30  50  66  99  58  20代表华氏温度
   #希望将这些温度变成摄氏温度: 摄氏温度=（华氏温度-32）/1.8
# (1)需要将每个温度变成摄氏温度
#（2）希望得到的结果仍然是字符串
"""
思路：
（1）如何将字符串处理成单个元素（温度），split(",")
 (2) 使用for循环处理每一个温度
    处理之前需要将温度转换float
（3）+可以拼接字符串
    format也能组装字符串
"""
s="30,50,66,99,58,20"
print(s.split(","))
t=s.split(",")
a=""
for  i in t:
    # print(i)摄氏温度=（华氏温度-32）/1.8
    x=(float(i)-32)/1.8
    # print(x)
    # a+=str(x)+","
    a+="{},".format(x)
s=a.rstrip(",")
print(s)
s="1.2,1.5,1.65892......."


# 2.循环的嵌套
"""
语法：
for  i  in 外循环对象：
   for j in 内循环对象:
      循环体
外循环每执行一次，内循环都会完整的执行一轮。
"""
#打印星星*
# print("******")
# print("*"*6)
#
# for i in  range(6):
#     print("*",end="")

# 需要打印10行，每行6个星星
for j in range(10):
    for i in range(6):
        print("*", end="")
    print()
# 写代码，通常先写内循环，再写外循环


#3. 跳出循环
# break：终止当前循环
# 希望在字符中检测有没有*
for i in "hel*djlkgdljgklgdjdkgj":
    if "*"==i:
        print("找到*")
        break

#输入一个数，判断是不是质数
# 质数：只能被自己和1整除
# 判断不是质数更容易
# num%(2...n-1) ！=0 是质数
# num%(2...n-1) ==0 不是质数 break
import math
num=int(input("请输入一个数"))
tag=True
# print(math.sqrt(7))
for i in range(2,int(math.sqrt(num))+1):
    if num%i==0:
        print("不是质数")
        tag=False
        break
    # else:
    #     print("是质数")
# if tag==True:
if tag:#（简化）
    print("是质数")

# 因式分解
# 8=2*4
# 8=4*2
# 16=2*8
# 16=4*4
# 16=8*2