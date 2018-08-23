#1.一个足球队在寻找年龄在10岁到12岁的小女孩（包括#10岁和12岁）加入。
"""
编写程序，询问用户的性别（m表示男性，f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，
询问10次后，输出满足条件的总人数。
"""
def q1():
    e = 0
    for num in range(0, 10):
        sex = str(input("请输入您的性别，m代表男性，f代表女性: "))
        age = int(input("请输入您的年龄 : "))
        if sex == "f" and 10 <= age <= 12:
             e = e + 1
             print("恭喜您成功加入球队！")
        else:
            print("抱歉，您不符合条件！ ")
    print("一共有 ", e, "名成员加入球队")

#2.input输入3个数，找到最大值
def q2():
    print("请输入三个数：")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    max = n1
    if n2 > max:
        max = n2
    if n3 > max:
        max = n3
    print("最大的数是：", max)

#3.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
def q3():
    n=int(input("请输入一个整数："))
    n=str(n)
    m=n[::-1] #正切片倒过来，[start：end：step] step 代表方向 -1 倒过来
    if(n==m):
        print("这个整数是回文数")
    else:
        print("这个整数不是回文数")


#4.输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号…（直角三角形）；
#在此基础上，输出一个空心的直角三角形。

def q4():
    #直角三角形
    for i in range(1,11):
        print('*'*i)

    #空心直角三角形
    rows = 5
    for i in range(0, rows + 1):
     for j in range(0, rows - i):
      print(" ")
     for k in range(0, 2 * i - 1):
      if k == 0 or k == 2 * i - 2 or i == rows:
        print("*")
      else:
        print(" ")
     print("\n")


#5.输出9 * 9乘法表。
"""
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
"""
def q5():
    for i in range(1, 10):
        for j in range(1,i+1):
            print("%s * %s = %s" %(i, j , i*j), end=" ")
        print("")

#6.玩游戏，玩3次。
import random
realvalue=random.randint(1,10)
print(realvalue)
print("游戏开始")
# guess=input("请输入猜测的数字：")
# "8"   8
# ==代表判断内容是否一致
# if else 语句体，要注意缩进
# int()能够将字符串转换成数值
for i in range(3):
    guess = int(input("请输入猜测的数字:"))
    if guess == realvalue:
        print("猜对了")
        print("猜对了也没有奖励")
        break
    else:
        print("猜错了")
        print("小笨蛋")


