# 1.	手工计算-27的二进制原码、使用程序输出-27的二进制码，验证是否正确
#         显示-27的原码，显示-27的补码 ， 想一种办法-27& 数=-27
# （1）27的原码  手工 下除法 00011011
print(bin(27))
# (2)-27 原码 10011011
# （3）反码   11100100
# （4）补码   11100101
print(bin(-27))   #python中已与显示识别复数，所以-
print(bin(-27&0b11111111))   #实际值并不是-27的补码，只是显示的是-27补码的样子

# 2.	给出将-27 << 3与-27 >> 3的过程。并在程序上验证是否正确
"""
-27补码          10000000  01100101
-27补码          11111111  11100101
<<3 右侧以1填充  111111111  00101000
反码            1      00  11010111
原码            1      00  11011000    -216
"""
print(2**7+2**6+2**4+2**3)
""""
>>3
-27补码                    11100101
>>3 左侧以1填充
补码                       11111100
反码                       10000011
原码                       10000100   -4
"""
print(-27>>3)
print(-27<<3)

# 3.	输入一个三位正整数，输出该数值的百位，十位与个位。
def q1():
    #方法一
    a=input("请输入一个三位数的正整数：")
    print(a[0], a[1], a[2])
    for i in a:
        print(i, end=" ")

    #方法二
    a=input("请输入一个三位数的正整数：")
    for i in range(len(a)):
        print(int(a)//10**i%10,end=" ")


# 4.	编写程序，证明and的优先级高于or。

print(1 or 5 and 4)
print((1 or 5) and 4)

"""
对于, 1 or 5 and 4: 先算5 and 4, 5为真, 值为4. 再算1 or 4, 1 为真,值为1 
对于, (1 or 5) and 4: 先算1 or 5, 1为真, 值为1. 再算1 and 4, 1为真,值为4
"""

# 5.	编写程序，证明and与or短路现象的存在。
1 or print("阿萨斯大所多")
0 and print("asdasdasd")

1 or print("2") and print("3")
"""
And：如果第一个表达式False，则第二个表达式不执行
Or:  如果第一个表达式为True，则第二个表达式不执行
从结果看，并没有打印，and和or 有短路现象
"""
# 6.	输入一个数，输出该数*7的结果。（不允许使用*，也不允许连续累加）
def q0():
    a=int(input("请输入一个整数："))
    print((a<<3)-a)

"""
2作为查询权限，4具有修改权限， 8有 删除权限
16 审核权限
都是要用 2**？这种方式
"""

# 7.	输出如下内容：分别使用双引号，和三引号
def q2():
    a="hello"
    "hello"  # 匿名字符串 也创建的内存，只不过没有名字，用起来不太方便
    print("A：are you \"tom\"\nB：no")

    print("""
    A：are you "tom"
    B：no
    """)

# 8.	定义两个字符串，a=“hello”  b=”hello”，令c=a，
# 思考：是否能对a中的h进行修改
# 输出abc三个变量的值
# 使用is和==判断abc之间的关系，并画出内存图
def q3():
    a="hello"
    b="hello"
    c=a
    a="6"+a[1:]
    print(a)
    print(id(a),id(b),id(c))

# 9.	输入一个16位学号如，1001010220170101，其中100是学校代号101是院系代号
# 02专业代号2017年级01班级01学号，请使用切片获取出各个代码。
#
def q4():
    a=input("请输入您的学号：")
    print("您的学校代码:{}".format(a[:3]))
    print("您的院系代码:{}".format(a[3:6]))
    print("您的专业代码:{}".format(a[6:8]))
    print("您的年级代码:{}".format(a[8:12]))
    print("您的班级代码:{}".format(a[12:14]))
    print("您的学号代码:{}".format(a[14:]))

# 10.	这是一个地址，
# http://news.gzcc.cn/html/2017/xiaoyuanxinwen_1027/8443.html
# 其中1027/8443是新闻编号，想办法获得新闻编号。
#
def q5():
     # 去掉内部的空格
    s="http: // news.gzcc.cn / html / 2017 / xiaoyuanxinwen_1027 / 8443. html"
    # http://news.gzcc.cn/html/2017/xiaoyuanxinwen_1027/8443.html
    print(s.replace(" ",""))
    s=s.replace(" ","")
    # 方式一：切片
    print(s[-14:-5])
    # 方式二：切片+index
    print(s[s.index("_")+1:s.index(".html")])
    # 方式三：
    print(s.strip("http://news.gzcc.cn/html/")[-9:])
    # 方式四：
    print(s.split("_")[1].rstrip(".html"))

# 11.	这是一个网址，但是前面有错误的空格字符
# "  http://news.gzcc.cn/html/xiaoyuanxinwen/4.html"
# （1）	去掉前面的空格
# （2）	删除http://前缀
# （3）	去掉后缀.html并输出数字4
# （4）	显示这段文字中有多少个n
# （5）	使用/分隔成多个单词
#
def q6():
    s="  http://news.gzcc.cn/html/xiaoyuanxinwen/4.html"
    print(s.strip())
    s=s.strip()
    print(s.lstrip("http://"))
    print(s.rstrip(".html"))
    print(s.rstrip(".html")[-1:])
    print(s.count("n"))
    print(s.split("/"))

# 12.	分别输入3个爱好，打印出来“我的爱好是**、**、**”
#
def q5():
    h1=input("请输入第一个爱好：")
    h2=input("请输入第二个爱好：")
    h3=input("请输入第三个爱好：")
    # print("我的爱好是%s,%s,%s" % (h1,h2,h3))
    print("我的爱好是{}、{}、{}".format(h1,h2,h3))
    print(f"我的爱好是{h1}、{h2}、{h3}")

# 13.	定义一个字符串a，里面有字符，有数字，请将a字符串的数字取出，
# 并输出成一个新的字符串
#
def q7():
    x="adasdasdafasfa32f4f43gf54"
    x_new=""
    for i in x:
        if i.isdigit():
            x_new+=i
    x=x_new
    print(x)

# 14.	查资料，或者自己试一下str中的方法，将小写转大写，大写转小写  aDdFDdddFD
#
#
str = "ahskSHLKHDLJKHWHDdhskahdHSLHd"
print(str.swapcase())