# 1.	部署Python开发环境，并练习环境变量的使用。
# 注意add path

# 2.	计算机语言发展和按执行方式分类。
# 机器语言  汇编语言  高级语言
# 执行方式：编译型语言  解释型语言


# 3.	Python属于什么语言
# 解释型、动态、强类型的语言

# 4.	Python的版本
# 2x ---2.7
# 3x  目前到3.7


# 5.	Python的执行方式，阐述区别和优缺点
"""
交互式和脚本式（文件）
交互式：直接输入马上可以看到运行结果
脚本式：相当于把py文件全部加载，在中间过程中不能达到人机交互的目的。

"""

# 6.	在c盘下写一个py文件，分别使用交互式和文件式访问执行。


# 7.	X=“abc”，y=”def”,y=x ，z=y   输出x和y、z的结果，画出内存图。

x="abc"
y="def"
y=x
z=y
print(x,y,z)

# 8.	删除一个变量后，内存中是如何操作的？是否连同变量值也删除了？
# python del变量名，只能删除变量名，不能删除变量值
x=1
# del x
x=2
# 垃圾回收机制 ：最近最少使用

# 9.	输入a,b,c,d4个整数，计算a+b-c*d的结果
def que5():
    a=int(input("请输入一个数："))
    b=int(input("请输入一个数："))
    c=int(input("请输入一个数："))
    d=int(input("请输入一个数："))
    print(a+b-c*d)

    a,b,c,d=int(input("请输入一个数：")),int(input("请输入一个数：")),int(input("请输入一个数：")),int(input("请输入一个数："))


# 10.	输入2个数，输入一个操作符，实现运算。
def que10():
    a=int(input("请输入一个数："))
    b=int(input("请输入一个数："))
    c=input("输入一个操作符")
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    else:
        print(a/b)


# 11.	输出10/3的结果
print(10/3)
print(10/2)

# 12.	标识符的要求
# 字符、数字、_，不能用数字开头
# 区分大小写
# 不能是关键字


# 13.	关键字区分大小写吗？
# 区分

# 14.	请打印出以下变量的值：
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

#
#
# 15.	查看“Python之禅”，并翻译（import this）。
# 16.	数值类型分为哪些？
# 整数、浮点、复数

# 17.	编写程序，从键盘输入某个分钟数，将其转换成小时和分钟表示。
def que17():
    num=int(input("请输入分钟数："))# 121
    hour=num//60
    min=num%60
    print(hour,"小时",min,"分钟")

# 18.	将十进制的17转换成2进制，8进制和16进制，使用手工计算，并使用数值的方法验证。
# 10001
print(bin(17))
print(oct(17))
print(hex(17))


# 19.	将二进制100110101转换成10进制，8进制和16进制，使用手工计算，并使用数值方法验证。
# 转换成十进制，使用乘幂
print(1*2**8+1*2**5+1*2**4+1*2**2+1*2**0)
# 转换成八进制有两种方式：直接将十进制转换8/16进制，下除法
# 309除以8==465

# 对应二进制的三位获得 八进制的一位,
# 十六进制对应四位一取
# 100  110  101
# 4    6     5

# 20.	使用Decimal类计算，输入两个浮点类型，再输入需要保留的有效数字，计算相加结果
f1=3.0
f2=0.2
import decimal
print(decimal.Decimal(f1))
print(decimal.Decimal(0.5))
print(decimal.Decimal(0.25))


print(decimal.Decimal(f1)+decimal.Decimal(f2))
context=decimal.getcontext()
context.prec=3
print(decimal.Decimal(f1)+decimal.Decimal(f2))
print(decimal.Decimal(f1))