# 1.	部署Python开发环境，并练习环境变量的使用。
# 2.	计算机语言发展和按执行方式分类。
"""
    机器语言，汇编语言，高级语言
    编译型和解释型
"""
    
# 3.	Python属于什么语言
"""
解释型，动态，强类型的高级语言
"""
# 4.	Python的版本
"""
2x 2.7(不再升级维护)  3x 3.7
"""
# 5.	Python的执行方式，阐述区别和优缺点
"""
交互执行：一句一句的执行，执行完毕，当前的命令就结束。
脚本执行：将py文件从头执行完，执行完毕之后，才将内存清空
"""
# 6.	在c盘下写一个py文件，分别使用交互式和文件式访问执行。

# 7.	X=“abc”，y=”def”,y=x ，z=y   输出x和y、z的结果，画出内存图。
def q1():
    x="abc"
    y="def"
    y=x
    z=y
    print(x,y,z)

# 8.	删除一个变量后，内存中是如何操作的？是否连同变量值也删除了？
"""
删除了变量名，内存中没有删除变量值
"""

# 9.	输入a,b,c,d4个整数，计算a+b-c*d的结果
def q2():
    """
    输入四个数，计算a+b-c*d的结果
    :return:
    """
    a=int(input("请输入第一个数："))
    b=int(input("请输入第二个数："))
    c=int(input("请输入第三个数："))
    d=int(input("请输入第四个数："))
    print(a+b-c*d)

# 10.	输入2个数，输入一个操作符，实现运算。
def q3():
    """
    输入2个数，输入一个操作符，实现运算
    :return:
    """
    x=int(input("请输入第一个数："))
    y=int(input("请输入第二个数："))
    c=input("请输入一个操作符：")
    if c=="+":
        print("{}+{}=".format(x,y),x+y)
    elif c=="-":
        print("{}-{}=".format(x,y),x-y)
    elif c == "*":
        print("{}*{}=".format(x,y),x * y)
    elif c == "/":
        if y==0:
            print("除数不能为0！")                                            
        else:
            print("{}/{}=".format(x,y),x/y)

# 11.	输出10/3的结果
"""
 两个操作数进行运算的时候，结果取高级别的数值类型，
 但是注意，如果结果是浮点数，那么浮点数来
"""
# 12.	标识符的要求
"""
1. 名字  字母，数字，_  组合，不是以数字开头
2. 不是能关键字
3. * $ @不能有类似的字符
"""
# 13.	关键字区分大小写吗？  区分

# 14.	请打印出以下变量的值：
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
#
def q4():
    n = 123
    f = 456.789
    s1 = 'Hello, world'
    s2 = 'Hello, \'Adam\''
    s3 = r'Hello, "Bart"'
    s4 = r'''Hello,
    Lisa!'''
    print(n,f,s1,s2,s3,s4,sep="\n")
    #
# 15.	查看“Python之禅”，并翻译（import this）。
#
# import this
"""
Beautiful is better than ugly.         优美胜于丑陋（Python以编写优美的代码为目标）
Explicit is better than implicit.      明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似） 
Simple is better than complex.         简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现） 
Complex is better than complicated.    复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
Flat is better than nested.            扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套） 
Sparse is better than dense.           间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
Readability counts.                    可读性很重要（优美的代码是可读的） 
Special cases aren't special enough to break the rules.
Although practicality beats purity.  
即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）   
Errors should never pass silently.
Unless explicitly silenced.  
不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写except:pass风格的代码）           
In the face of ambiguity, refuse the temptation to guess.
当存在多种可能，不要尝试去猜测 
There should be one-- and preferably only one --obvious way to do it.
而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法） 
Although that way may not be obvious at first unless you're Dutch.
虽然这并不容易，因为你不是 Python 之父（这里的Dutch是指Guido）
Now is better than never.
Although never is often better than *right* now.
做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准） 
Namespaces are one honking great idea -- let's do more of those!
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
"""
# 16.	数值类型分为哪些？
"""
 整数类型，浮点，复数  布尔
"""
# 17.	编写程序，从键盘输入某个分钟数，将其转换成小时和分钟表示。
def q5():
    minute=int(input("请输入一个分钟数："))
    hour=minute//60
    s_minute=minute%60
    print("输入的时间是：{}分钟，您输入的是{}小时{}分钟".format(minute,hour,s_minute))

# 18.	将十进制的17转换成2进制，8进制和16进制，使用手工计算，并使用数值的方法验证。
def q6():
    """
    二进制：0b10001
    八进制：0o21
    十六进制：0x11
    :return:
    """
    s=17
    print(bin(s),oct(s),hex(s))

# 19.	将二进制100110101转换成10进制，8进制和16进制，使用手工计算，并使用数值方法验证。
def q7():
    """
    100110101=1 * 2 ** 8 + 1 * 2 ** 5 + 1 * 2 ** 4 + 1 * 2 ** 2 + 1

    :return:
    """
    y = 0b100110101
    print(1 * 2 ** 8 + 1 * 2 ** 5 + 1 * 2 ** 4 + 1 * 2 ** 2 + 1)
    print(oct(y))
    print(hex(y))
q7()
# 20.	使用Decimal类计算，输入两个浮点类型，再输入需要保留的有效数字，计算相加结果
def q8():
    f1=0.1
    import decimal
    print(decimal.Decimal(f1))
    x=decimal.Decimal("0.1")
    y=decimal.Decimal("0.2")
    print(x+y==0.3)
