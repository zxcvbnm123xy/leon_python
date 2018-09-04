#
# 1.定义一个字符串“我爱python”，将他采用gb2312编码，然后在解码
def q1():
    s="我爱python"
    b=s.encode("gb2312")
    print(b)
    s_new=b.decode("gb2312")
    print(s_new)

# 2.	小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
# 并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# # -*- coding: utf-8 -*-
# s1 = 72
# s2 = 85
# ----
# r = ???
# print('???' % r)
#
def q2():
    s1=72
    s2=85
    r=(s2-s1)/s1
    print("小明提高了%.1f%%"%(r*100))
    print("小明提高了{:.1f}%" .format(r * 100))

# 3.	请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#
def q3():
    """
    (1)input 输入
    （2）m，t ，t，w，f，s，s
    （3）可能会有大小写，需要处理一下input的大小写问题
    :return:
    """
    day=input("请输入星期几的第一个字母:").lower()
    # day=day.lower()
    # if day==M or day==m:
    if day=="m":
        print("今天是周一！")
    elif day=="w":
        print("今天是周三！")
    elif day=="f":
        print("今天是周五！")
    elif day=="t":
        day=input("请输入第二个字母：").lower()
        if day=="u":
            print("今天是周二！")
        elif day=="h":
            print("今天是周四")
        else:
            print("输入有误，请重新输入！")
    elif day=="s":
        day=input("请输入第二个字母：").lower()
        if day=="a":
            print("今天是周六！")
        elif day=="u":
            print("今天是周日！")
        else:
            print("输入有误，请重新输入！")
    else :
        print("输入有误，请重新输入！")

# 4.编写程序实现如下数学表达式。
# X<1000的时候，y=x
# 1000≤X<2000  y=0.9x
# 2000≤X<3000  y=0.8x
# X≥3000        y=0.7x
#
def q4():
    x=int(input("请输入一个数："))
    y=0
    if x<1000:
        y = x
        print(y)
    elif x<200:
        y=0.9*x
    elif x<3000:
        y = 0.8 * x
        print(y)
    else :
        y = 0.7 * x
        print(y)


# 5.输入一个数字，如果输入的是数字，可以输出他的平方。如果输入exit，跳出程序，
# 如果输入的既不是数字也不是exit，提示错误信息之后可以再次输入。
#
def q5():
    while True:
        """
        (1)input
        (2)判断传入的x == “exit” 退出
            x.isdigit() 得到平反
        （3）else 提示错误信息
        （2）需要使用while循环
        """
        while True:
            num=input("请输入数字：")
            if num.isdigit():
                print("您的结果是{}".format(int(num)**2))
                print("您的结果是：d%"%(int(num)**2))
            elif num=="exit":
                print("您已退出计算！")
                break
            else:
                print("您输入有误！请再次输入")

# 6.一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写程序，询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
#
#
def q6():
    """
    (1)两个input age gender
    （2）10<=age<=12 and gender="f":符合
        否则不符合
    （3）使用循环 for while 最高次数十次
    （4）向（2）符合条件是进行计数
    :return:
    """
    i = 0
    s = 0
    # for  i in range(3):
    while i < 3:
        sex = input("请输入性别：")
        age = int(input("请输入年龄："))
        if 10 <= age <= 12 and sex == "f":
            print("恭喜你，能够加入球队")
            s += 1
        else:
            print("对不起，你不符合要求")
        i += 1
    print("球队的人数是{}".format(s))

# 7.输入3个数，找到最大值和最小值输出
def q7():
    """
    (1)input 三个数
    (2)随机找两个数进行比较，找到max，min 再跟第三个数比，得到里面的max和min
        先假设其中一个数就是max或者min
    (3)如果使用for循环考虑有多个值的情况
    max跟循环体中其他的值进行逐个比较，每次比较都找到最大值进行比较
    :return:
    """
    a=int(input("请输入第一个数："))
    b=int(input("请输入第二个数："))
    c=int(input("请输入第三个数："))
    max=min=a
    if max<b:
        max=b
    else:
        min=b
    if max<c:
        max=c
    else:
        min=c
    print("三个数中最大值是：{}".format(max))
    print("三个数中最小值是：{}".format(min))

def q7_1():
    for i in range(3):
        num=int(input("请输入一个数："))
        if i==0:
            max=min=num
        if num>max:
            max=num
        if num<min:
            min=num
    print("三个数中最大值是：{}".format(max))
    print("三个数中最小值是：{}".format(min))

# 8.输入一系列成绩，每次输入一个成绩之后都询问是否还要继续输入y/n，输入n后可以计算这些成绩的平均值，
# 并且统计优良中及格、不及格的人数
# 优>=90
# 良>=80
# 中>=70
# 及格>=60
# 不及格<60
#
def q8():
    """
    （1）input成绩
    （2）需要循环 while
    （2）循环同时计算sum的值
        需要记录人数 平均数=sum/count
    （4）需要进行成绩的判断，给对应的分级人数加一
    :return:
    """
    # i="y"
    # while i=="y":
    sum = 0
    count = 0
    count_bj = count_j=count_z=count_l=count_y=0
    while True:
        score=int(input("请输入您的成绩："))
        sum+=score
        count+=1
        i = input("您是否还要继续输入？y/n：")
        if score<60:
            count_bj += 1
        elif 60<=score<70:
            count_j += 1
        elif 70<=score<80:
            count_z += 1
        elif 80<=score<90:
            count_l += 1
        elif score>=90:
            count_y += 1
        while i!="y" and i!="n":
            print("您的输入有误")
        if i=="n":
                break
    print("平均值是{:.2f}".format(sum/count))
    print("不及格人数是{}，及格人数是{}，中等人数是{}，良好人数是{}，优秀人数是{}"
         .format(count_bj,count_j,count_z,count_l,count_y))

# 9.题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#  程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
#
def q9():
    """
    (1)三层循环
    （2）循环中的变量，互不相等 才输出
        i!=j  j！=k  k！=i
    :return:
    """
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i!=j and j!=k and i!=k:
                    print(i,j,k)

def q9_1():
    #while 循环要注意变量的+1 或者-1
    i=k=j=0
    while i<4:
        i+=1
        while j<4:
            j+=1
            while k<4:
                k+=1
                if i!=j and j!=k and i!=k:
                        print(i,j,k)
            k=0
        j=0

# 10.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#
def q10():
    """
    (1):字符串的切片逆序==原来的字符串相等
    （2）判断第0个位置-1
               1     -2
               2     -3
               i     -1-i
    :return:
    """
    a=input("输入一个数")
    print(id(a[::-1],id(a)))
    if a==a[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

def q10_1():
    num=input("输入一个数")
    for i in range(int(len(num)/2)):
        if num[i]!=num[-1-i]:
            print("不是回文数")
            # tag=False
            break
    else:
        print("是回文数")

# 11..输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号…
def q11():
    for i in range(1,11):
        print("*"*i)
    for i in range (1,11):
        for j in range(1,i+1):
            print("*",end="")
        print()

# 12.在上面题基础上，打印一个圣诞树
def q12():
    """
       *
      ***
     *****
    *******
       *
       *
       *
    :return:
    """
    for i in range (1,11):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
        print()

# 13.在上面题基础上，打印一个菱形
def q13():
    for i in range(1, 11):
        for k in range(1, 11 - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            print("*", end="")
        print()
    #reversed 翻转函数 反转
    for i in reversed(range(1, 10)):
        for k in range(1, 11 - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            print("*", end="")
        print()
def q13_1():
    for i in range(1, 11):
        for k in range(1, 11 - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            print("*", end="")
        print()
    for i in reversed(range(1, 10)):
        for k in range(1, 11 - i):
            print(" ", end="")
        for j in range(1, 2 * i):
            print("*", end="")
        print()
# 14.在上面题基础上，打印一个空心菱形
def q14():
    for i in range (1,11):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1,2*i):
            if j==1 or j==2*i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    #for i in range(10,1,-1)
    for i in reversed(range (1,10)):
        for k in range(1,11-i):
            print(" ",end="")
        for j in range(1,2*i):
            if j==1 or j==2*i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
def q14_1():
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
    s="*"
    for i in range(1,8,2):
        print((s*i).center(7))
    for i in reversed(range(1,6,2)):
        print((s*i).center(7))

# 15.输入年份，判断该年是否为闰年。
def que15():
    year=int(input("请输入年份"))
    if year%400==0 or year%4==0 and year%100!=0   :
        print("是闰年")
    else:
        print("不是闰年")

# 16.输出所有的水仙花数（三位数，各位数字的立方和等于自身）。
def q16():
    """
    (1)for range(100,1000)
    (2)各个位数
    (3)num//10**i%10
    :return:
    """
    for i in range(100,1000):
        a=i//100
        b=i//10%10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)

#使用循环的方式取各个位数
def q16_1():
    for i in range(100,1000):
        s=0
        for j in range(3):
            num=i // 10**j % 10
            s+=num**3
        if s==i:
            print(i)

# 17.输出9 * 9乘法表。（str函数）要求使用for和while两种方法解决。
def q17():
    #for
    for i in range(1,10):
        for j in range(1,i+1):
            print("{}*{}={}".format(j,i,i*j),end="\t")
        print()

    #while
def q17_1():
    i = j = 1
    while i <= 9:
        while j <= i:
            print("{}*{}={}".format(j, i, i * j), end="\t")
            j += 1
        i += 1
        j = 1
        print()


# 18.输入一个整数，如果该值不为0，则将该值赋值给x，否则将10赋值给变量x。（不允许使用任何选择判断语句）
#
def q18():
    num=int(input("输入一个值:"))or 10
    print(num)

# 19.记录猜错的次数，如果错误超过3次，则退出，并输出“小笨蛋。。。”，如果3次之内猜对了，则输出“真聪明”
def q19():
    import random
    realvalue = random.randint(1, 5)
    print(realvalue)
    c = 0
    for i in range(3):
        guess = int(input("请输入猜测的数字："))
        if guess == realvalue:
            print("猜对了！")
            print("猜对了也没有奖励！")
            break
        else:
            c += 1
            print("猜错了")
    if c == 3:
        print("小笨蛋")
# q19()
# 20.定义一个用户名admin，密码123，写一个登录程序，每次输入错误时，给予提示，还有几次机会，如果用户名或者密码输入错误超过三次，则锁定用户（不允许再输入用户名密码了）。
def q20():
    username="admin"
    password="123"
    times=3
    while times<=3:
        if times==0:
            print("输入超过3次，锁定用户")
            break
        in_username=input("请输入用户名:")
        in_password=input("请输入密码:")
        if username==in_username and password==in_password:
            print("登录成功")
            break
        else:
            times-=1
            if username!=in_username:
                print("对不起用户不存在")
            elif password!=in_password:
                print("用户名存在，但是密码不正确")
# q20()
# 21.输入一个数，判断是否是素数
def q21():
    import math
    num = int(input("请输入一个数"))
    for i in range(2, int(math.sqrt(num)) + 1):
        if  num % i == 0:
            print("不是质数")
            break
        else:
            print("是质数")

# 22.输出100以内的素数
def q22():
    for i in range(2,101):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
q22()