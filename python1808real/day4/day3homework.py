# 1.定义一个字符串“我爱python”，将他采用gb2312编码，然后在解码
# 编码：字符串--字节   解码：字节---字符串
s="我爱python"
print(s.encode("gb2312"))
print(b'\xce\xd2\xb0\xaepython'.decode("gb2312"))



# 2.	小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
# 并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# # -*- coding: utf-8 -*-
s1 = 72
s2 = 85

r = (s2-s1)/s1
print('小明的成绩提高了%.1f%%' % (r*100))
print('小明的成绩提高了{:.1f}%'.format( r*100))
#
# 3.请输入星期几的第一个字母来判断一下是星期几，
# 如果第一个字母一样，则继续判断第二个字母。
# (1)input
# (2)m  w f s s t t
# (3)需要处理input的大小写
def que3():
    letter=input("请输入星期几的首字母：").upper()
    if letter=="M":
        print("Monday")
    elif letter=="W":
        print("Wednesday")
    elif letter=="F":
        print("Friday")
    elif letter=="T":
        letter=input("请输入星期几的第二个字母：").lower()
        if letter=="u":
            print("Tuesday")
        elif letter=="h":
            print("Thursday")
        else:
            print("input error")
    elif letter=="S":
        letter = input("请输入星期几的第二个字母：").lower()
        if letter=="a":
            print("Saturday")
        elif letter=="u":
            print("Sunday")
        else:
            print("input error")
    else:
        print("input error")


# 4.编写程序实现如下数学表达式。
# X<1000的时候，y=x
# 1000≤X<2000  y=0.9x
# 2000≤X<3000  y=0.8x
# X≥3000        y=0.7x
# if ..elif..else使用的时候一定注意大小顺序
def que4():
    x=int(input("输入x的值："))
    if x<1000:
        y=x
    elif x<2000:
        y=0.9*x
    elif x<3000:
        y=0.8*x
    else:
        y=0.7*x



#
# 5.输入一个数字，如果输入的是数字，可以输出他的平方。如果输入exit，
# 跳出程序，如果输入的既不是数字也不是exit，提示错误信息之后可以再次输入。
"""
 (1)  x=input
（2）判断x =="exit" 退出break
     x.isdigit()   得到平方
（3）else print提示
（4）需要使用while True
"""
def que5():
    while True:
        x=input("请输入一个数字：")
        if x=="exit":
            break
        elif x.isdigit():
            print("运算的结果是：%d " % (int(x)**2))
        else:
            print("输入有误")


#
# 6.一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
"""
(1)两个input  age  gender
(2) 10<=age<=12  and gender="f"  :符合
    否认不符合
(3)使用循环 for  while  最高次数10
(4) 向(2) 符合条件时进行计数
"""
def que6():
    s=0
    # for i in range(3):
    time=0
    while time<3:
        age=int(input("输入年龄："))
        gender=input("输入性别：")
        if 10<=age<=12 and gender=="f":
            print("恭喜你，可以 加入球队")
            s+=1
        else:
            print("不能加入球队")
        time+=1
    print("符合条件人数是{}".format(s))


#
#
# 7.输入3个数，找到最大值和最小值输出
"""
(1)input 3个数
(2) 随机找两个数进行比较，找到max和min，再跟第三个数比较。得到max和min
    先假设其中一个数就max或者min
    
（3）如果使用for循环考虑有多个值的情况
   max
   跟循环体中其他的值进行逐个比较。每一次比较都找到最大值。
"""
def que7_1():
    a=int(input("第一个数："))
    b=int(input("第二个数："))
    c=int(input("第三个数："))
    max=min=a
    # if a<b
    if max<b:
        max=b
    else:
        min=b
    if max<c:
        max=c
    if min>c:
        min=c
    print("最大值是{}".format(max))
    print("最小值是{}".format(min))

def que7_2():
    max=min=0
    for i in range(3):
        num=input("输入一个数")
        if i==0:
            max=min=num
        else:
            if num>max:
                max=num
            if num<min:
                min=num
    print("最大值是{}".format(max))
    print("最小值是{}".format(min))

# 8.输入一系列成绩，每次输入一个成绩之后都询问是否还要继续输入y/n，
# 输入n后可以计算这些成绩的平均值，并且统计优良中及格、不及格的人数
# 优>=90
# 良>=80
# 中>=70
# 及格>=60
# 不及格<60
"""
 (1)input成绩
（2）需要循环 while
(3)循环同时需要计算sum的值
   需要记录人数count
   平均值=sum/count
(4)需要进行成绩的判断，对应分级人数+1
"""
def que8():
    # c="y"
    # while c=="y":
    s=count=perfect=good=normal=pas=bad=0
    while True:
        score=int(input("输入一个成绩："))
        s+=score
        count+=1
        if score>=90:
            perfect+=1
        elif score>=80:
            good+=1
        elif score>=70:
            normal+=1
        elif score>=60:
            pas+=1
        else:
            bad+=1

        c=input("是否还要继续输入y/n")
        while  c!="y" and c!="n":  # not(c=="y" or c=="n" )
            print("你输入命令有误")
            c = input("请重新输入y/n")
        if c=="n":
            break
    print("平均值是{:.2f}".format(s/count))
    print("优{}、良{}、 中{}、及格{}、不及格{}".format(perfect,good,normal,pas,bad))
# que8()
#
#
# 9.题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
(1)三层循环
(2) 循环中的变量互不相等 才输出
    i !=j  j!=k  k！=i
"""
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and k!=i:
#                 print(i,j,k)

# while 循环要注意变量的+1 或者-1
def qu9_2():
    i=j=k=0
    while i< 4:
        i+=1
        while j<4:
            j+=1
            while k<4:
                k+=1
                if i!=j and j!=k and k!=i:
                    print(i,j,k)
            k=0
        j=0


#  程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
#
# 10.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
(1) 字符串的切片逆序==原来的字符串相等
(2) 判断第0个位置-1
         1      -2
         2      -3
         i      -1-i
"""
def que10_1():
    a=input("请输入一个数：")
    # print(id(a[::-1]),id(a))
    if a==a[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

def que10_2():
    a=input("请输入一个数：")
    # i     - 1 - i
    # 比较到中间的位置  12321  int(len(a)/2)
    for i in  range(int(len(a)/2)):
        if a[i]!=a[-i-1]:
            print("不是回文数")
            break
    else:
        print("是回文数")
#
# 11..输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号…
for i in range(10):
    print("*"*i)

for i in range(10):
    for j in range(i):
        print("*",end="")
    print()


# 12.在上面题基础上，打印一个圣诞树
"""
   *
  ***
 *****
*******

*
**
***
****
"""
def que12_1():
    for i in range(1,11):
        for k in range(1,11-i):
            print(" ",end="")
        # for j in range(1,i+1):  # 实际i
        #     print("*",end="")
        # for j in range(1, i ):  # 实际到i-1  2*i    2-1    2*i+1-1
        #     print("*", end="")
        for j in range(1, 2*i ): #2*i
            print("*", end="")
        print()

def que12_2():
    for i in range(1,11):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1,i+1):  # 实际i
            print("* ",end="")
        print()


# 13.在上面题基础上，打印一个菱形
def que13_1():
    for i in range(1,11):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1, 2*i ):
            print("*", end="")
        print()
    # for i in range(10,1,-1):
    for i in reversed(range(1,10)):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1, 2*i ):
            print("*", end="")
        print()
def que13_2():
    for i in range(1,11):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1,i+1):  # 实际i
            print("* ",end="")
        print()
    for i in reversed(range(1,10)):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1,i+1):  # 实际i
            print("* ",end="")
        print()

# 14.在上面题基础上，打印一个空心菱形
def que14_1():
    for i in range(1,11):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1, 2*i ):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ",end="")
        print()
    # for i in range(10,1,-1):
    for i in reversed(range(1,10)):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1, 2*i ):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ",end="")
        print()

def que14_2():
    for i in range(1,11):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1,i+1):  # 实际i
            # print("* ",end="")
            if j==1 or j==i:
                print("* ", end="")
            else:
                print("  ",end="")
        print()
    for i in reversed(range(1,10)):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1,i+1):  # 实际i
            if j==1 or j==i:
                print("* ", end="")
            else:
                print("  ",end="")
        print()

# 使用center打印菱形
"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""
def que14_3():
    s="*"
    for i in range(1,8,2):
        print((s*i).center(7))
    for i in reversed(range(1,6,2)):
        print((s*i).center(7))


# 15.输入年份，判断该年是否为闰年。
def que5():
    year=int(input("请输入年份"))
    if year%4==0 and year%100!=0 or year%400==0:
        print("是闰年")
    else:
        print("不是闰年")



# 16.输出所有的水仙花数（三位数，各位数字的立方和等于自身）。
"""
(1) for range(100,1000)
(2)各个位数  
    num//10**i%10
"""
def que16():
    for i in range(100,1000):
        a=i//100
        b=i//10%10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)

# 使用循环的方式取各个位数
def ques16_2():
    for i in range(100,1000):
        s=0
        for j  in range(3):
            num= i // 10**j % 10
            s+=num**3
        if s==i:
            print(i)


# 17.输出9 * 9乘法表。（str函数）要求使用for和while两种方法解决。
"""
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
"""
def que17_1():
    for i in range(1,10):
        for j in range(1,i+1):
            print("{}*{}={}".format(j,i,i*j),end="\t")
        print()
def que17_2():
    i=j=1
    while i<=9:
        while j<=i:
            print("{}*{}={}".format(j, i, i * j), end="\t")
            j+=1
        j=1
        i+=1
        print()


# 18.输入一个整数，如果该值不为0，则将该值赋值给x，否则将10赋值给变量x。（不允许使用任何选择判断语句）
def  que18():
    value=int(input("请输入一个数"))
    x=value or 10
    print(x)

# 19.记录猜错的次数，如果错误超过3次，则退出，并输出“小笨蛋。。。”，如果3次之内猜对了，则输出“真聪明”4
import random
def que19():
    realvalue=random.randint(1,5)
    print("realvalue={}".format(realvalue))
    times=3
    while True:
        if times==0:
            print("小笨蛋，3次都没猜出来")
            break
        guess=int(input("请输入猜测数字："))
        if guess==realvalue:
            print("猜对了")
            print("真聪明")
            break
        else:
            times-=1
            if guess>realvalue:
                print("猜大了，小一点")
            else:
                print("猜小了，大一点")

def que19_2():
    realvalue=random.randint(1,5)
    print("realvalue={}".format(realvalue))
    times=3
    while times>0:
        guess=int(input("请输入猜测数字："))
        if guess==realvalue:
            print("猜对了")
            print("真聪明")
            break
        else:
            times-=1
            if guess>realvalue:
                print("猜大了，小一点")
            else:
                print("猜小了，大一点")
    else:
        print("3次都没猜出来 ，小笨蛋")

#
# 20.定义一个用户名admin，密码123，写一个登录程序，
# 每次输入错误时，给予提示，还有几次机会，如果用户名或者密码输入错误超过三次，则锁定用户（不允许再输入用户名密码了）。
def que20():
    username="admin"
    password="123"
    times=3
    while times>0:
        in_username=input("请输入用户名")
        in_password=input("请输入用密码")
        if username==in_username and password==in_password:
            print("登录成功")
            break
        else:
            times-=1
            if username!=in_username:
                print("用户不存在")
            elif password!=in_password:
                print("用户名存在，但是密码错误")
    else:
        print("您已经输错超过三次，账户已锁定")




# 21.输入一个数，判断是否是素数

import math
def que21():
    num=int(input("请输入一个数"))
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            print("不是质数")
            break
    else:
        print("是质数")


# 22.输出100以内的素数
for i in range(2,101):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i)
