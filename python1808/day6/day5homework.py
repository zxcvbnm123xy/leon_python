# 1.一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
"""
思路：
（1）两个input，（int）age gender
（2）if 10<=age<=12 and gender=="f"  成功
（3）for  i in range(10)
（4）成功的时候sum+1
"""
def que1():
    s=0
    for  i in range(10):
        age=int(input("请输入年龄"))
        gender=input("请输入性别")
        if 10<=age<=12 and gender=="f":
            print("恭喜你，可以加入球队")
            s+=1
        else:
            print("对不起，不符合条件")
    print("球队已经有{}人".format(s))



# 2.input输入3个数，找到最大值
"""
思路：
（1）3个input  int
（2）比较的时候俩俩比较
假设一个值max，跟另外一个值相比，得到最大值，max跟真实的最大值绑定
再继续将max跟第三个值比较，得到最大的值，max跟真事最大值绑定。
"""
# 2  9  4

# a=int(input("请输入第一个值："))
# b=int(input("请输入第二个值："))
# c=int(input("请输入第三个值："))
# 找最大值最小值的程序
# max=a
# if max<b:
#     max=b
# if max<c:
#     max=c
# print("最大值是{}".format(max))
#
# min=a
# if min>b:
#     min=b
# if min>c:
#     min=c
# print("最小值是{}".format(min))


# 升级版
# max=min=a
# if max<b:
#     max=b
# else:
#     min=b
# if max<c:
#     max=c
# if min>c:
#     min=c
# print("最大值是{}".format(max))
# print("最小值是{}".format(min))


# 继续使用for循环
"""
思路跟上面一样
input是通过for循环input进来的。
"""
def que2():
    max=0
    for i in range(3):
        num=int(input("请输入一个数："))
        if i==0:
            max=num
        else:
            if num>max:
                max=num
    print("最大值是{}".format(max))


# 3.一个5位数，判断它是不是回文数。即6123216是回文数，个位与万位相同，十位与千位相同。

# 思路
# i   len(num)-i     -i-1
# num[0]==num[6]  num[-1]
# num[1]==num[5]  num[-2]
# num[2]==num[4]  num[-3]
# range(0,int(len(num)/2))
#方式一：
# num=input("请输入一个数")
# tag=True
# for i  in range(int(len(num)/2)):
#     if num[i]!=num[-i-1]:
#         tag=False
#         break
# if tag:
#     print("是回文数")
# else:
#     print("不是回文数")

# 方式二：
# [start:end :step]
# num="abc"
# print(num[::-1])
# if num==num[::-1]:
#     print("是回文数")
# else:
#     print("不是回文数")




# 4.输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号…（直角三角形）；
# 在此基础上，输出一个空心的直角三角形。
# 实心的
# for i in range(1,11):
#     print("*"*i)
# 实心的
for i in range(10):
    for j in range(i+1):
        print("*",end="")
    print()


# 空心
for i in range(10):
    for j in range(i+1):
        if j==0 or i==j or i==9:
            print("*",end="")
        else:
            print(" ",end="")
    print()


#
# 5.输出9 * 9乘法表。
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6  3*3=9
# 思路：
# 第三行
# for i in range(1,4):
#     print("{}*3={}".format(i,i*3),end="\t")

for j in range(1,10):
    for i in range(1, j+1):
        print("{}*{}={}".format(i, j,i * j), end="\t")
    print()

#
#
# 6.玩游戏，玩3次。
import random
realvalue=random.randint(1,5)
print(realvalue)
c=0
for i in range(3):
    guess=int(input("请输入猜测的数字："))
    if guess==realvalue:
        print("猜对了！")
        print("猜对了也没有奖励！")
        break
    else:
        c+=1
        print("猜错了")
if c==3:
    print("小笨蛋")