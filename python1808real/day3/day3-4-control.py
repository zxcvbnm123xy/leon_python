"""
第五章 流程控制
"""
"""
顺序结构：按部就班执行
选择结构：根据条件不同执行
循环结构：重复执行
"""
# 缩进：python使用缩进的方式来决定当前的代码层次（通常情况下使用四个空格tabs），
# 同一个层次的缩进应该一致

# 一、选择判断
# 1. if  ：当条件成立的时候，执行的代码段
# a=89
# if a<=90:# 条件必须返回布尔类型
#     print("我很瘦")
#     print("我可以继续胡吃海塞")
# print("if模块外的语句")

# 2. else: 当if条件不成立的时候执行代码段（else下没有条件）
# 代码中有if 和else-----二选一，只有两个分支
a=91
if a<=90:# 条件必须返回布尔类型
    print("我很瘦")
    print("我可以继续胡吃海塞")
else:
    print("我需要去健身房锻炼")
print("if模块外的语句")

# 3. elif 多个分支，后面有条件，可以有多个elif
"""
if  表达式:
  if成立的语句体
elif 表达式:
  elif成立的语句体
elif 表达式:
  elif成立的语句体
elif 表达式:
  elif成立的语句体
else :
   以上所有的条件都不成立时执行的代码段
"""
a=91
if a<=90:# 条件必须返回布尔类型
    print("我很瘦")
    print("我可以继续胡吃海塞")
elif a<=100:
    print("不能吃太多")
else:
    print("我需要去健身房锻炼")
print("if模块外的语句")

#在同一个if语句体中， 多个条件都符合时，只按照一个条件执行，按照先遇到的条件成立执行。
a=89
if a<=100:# 条件必须返回布尔类型
    print("不能吃太多")
elif a<=90:
    print("我很瘦")
    print("我可以继续胡吃海塞")
else:
    print("我需要去健身房锻炼")
print("if模块外的语句")
# 一般安排if和elif的条件时，要按照固定的大小顺序。
# 如果不能按照大小顺序：需要两侧都加入限制
# 最好将条件发生可能性大的放在前面
a=89
if 90<a<=100:# 条件必须返回布尔类型
    print("不能吃太多")
elif a<=90:
    print("我很瘦")
    print("我可以继续胡吃海塞")
else:
    print("我需要去健身房锻炼")
print("if模块外的语句")


# 猜数字
# realvalue=8
# temp=int(input("输入一个数字"))
# if temp==realvalue:
#     print("猜对了")
# else:
#     print("猜错了")
#     if temp>realvalue:
#         print("猜大了")
#     else:
#         print("猜小了")

# 4. 布尔类型的转换
"""
          True     False
int       非0         0  
float     非0.0       0.0
complex   非0j        0j 
str       非""        "" 
bytes     非b""       b""

None---False
"""
s="hello world"
# if len(s)>0:
if s:
    print("不是空串")
else:
    print("是空串")

# 5. 三元表达式
# 适合条件判断比较简单的情况
# 格式： 条件成立时的返回值  if 条件 else if条件不成立时候的返回值
x=1
y=10
if x<y:
    min =x
else:
    min=y
print("min={}".format(min))
print("min={}".format(x if x<y else y))

# 练习：
# 1-5工作日  6和7休息日
day=9
print("工作日" if 1<=day<=5 else ("休息日" if day==6 or day==7 else "输入错误") )

# x代表性别 x==0输出男，否则输出女
x=0
print("男" if x==0 else "女")

# 6. 断言： 断定某些语句是否正确
# 语法： 一旦表达式返回False，程序会报AssertionError，程序被停止，无法继续
"""
assert 表达式, 错误信息
"""
# assert 1>5,"谁告诉你的？"

#比if else好的地方在于：调试时候代码行数少，能够阻止代码的继续执行。if else没有办法让程序抛异常。
# if 1>5:
#     print("谁告诉你的？")
# else:
#     print("继续执行")


# 二、循环
# 问题：输出5次helloworld
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

# 1. while 循环
"""
# 当条件成立的时候就会进入循环体
while 条件:
   循环体
"""
# 适合使用while：需要执行循环的次数非常明确的时候，当条件永远为真的时候————一般使用while
# 使用while的好处在于，次数容易明确
# 需要注意的地方在于：一定要注意条件中的变量在while迭代中的变化，设置程序的出口，
# 如果程序没有出口，会变成死循环
# time=1
# while time<=5:
#     print("hello world")
#     # time +=1

# 1+2+...+100
# a=1
# s=0
# while a<=100:
#     s+=a
#     a+=1
# print(s)


# 2. for循环
#（1） 语法：
"""
for 变量名 in 迭代对象:
   迭代体
"""
# 在for循环中要注意构建好迭代对象。迭代对象意味着迭代的次数
for i in "abcde":
    print("hello world")

#1+2+3...+100
s=0
for i in "123":
    a=int(i)
    s+=a
# （2）
# range函数：返回一个列表
# range(start,end,step)
# step默认1：从左往右方向
# 包含start，不包含end
# start不写，默认0
print(list(range(1,5)))
print(list(range(1,101)))
print(list(range(1,101,2)))
# print(list(range(1,101,-2))) #step方向跟start和end不 一致，得到的是空列表
s=0
for i in range(1,101):
    s+=i
print(s)


# （3）循环的嵌套：
# 一般先写内循环，再写外循环。
# 外循环每执行一次，内循环都会完整的执行一轮
# 打星星 打印10行星星，每行5个
# for i in range(5):
#     print("*",end="")
# print()

for j in range(10):
    for i in range(5):
        print("*", end="")
    print()


# （4）跳出循环
# 一般情况下都是在if条件语句中才有意义
# break    ：跳出当前循环，终止循环
# for i in range(100):
#     if i == 3:
#         print("存在3")
#         break

# continue ：跳出当前本次循环，会继续执行下一次循环的内容。
# for i in range(100):
#     if i==3:
#         print("存在3")
#         continue
#     print("显示当前的数字是{}".format(i))

# 希望输出1-19之间的所有数，标注所有偶数
for i in range(20):
    if i%2==0:
        print("当前的数是偶数{}".format(i))
        continue
        # break
    print("当前的数是{}".format(i))


# (5) 在循环中使用else
# 在循环迭代正常完成之后执行。
# 当循环迭代不正常完成的时候（break，或者异常中断），不会执行的语句。
# tag=True
# for i in range(4,100):
#     if i==3:
#         print("3找到了")
#         tag=False
#         break
# if tag:
#     print("没找到3")

# 当循环迭代不正常完成的时候（break，或者异常中断），不会执行的语句。

# 执行循环中else，有两种情况：
# 1. 当没有走循环中的break（没有异常中断）
# 2. 当for循环迭代体为空
for i in range(4,4):
    if  i==3:
        print("3找到了")
        break
else:
    print("没找到3")

#（6）枚举
li=["a","b","c"]
for i in li:
    print(i)
for index in range(len(li)):
    print(index,li[index])
#enumerate(li)会将迭代对象每个元素形成一个元组(index,当前的元素)
# 使用的时候要注意的：第一个元素就是index
for index,i in enumerate(li):
    print(index,i)