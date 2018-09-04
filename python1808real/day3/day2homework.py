# 1.	手工计算-27的二进制原码、使用程序输出-27的二进制码，验证是否正确
#         显示-27的原码，显示-27的补码 ， 想一种办法-27& 数=-27
# （1）正数的原码  0b11011  27
#  (2)负数的原码  10011011  -27
# （3）反码       11100100
# （4）补码        11100101 -27补码
print(bin(-27)) # python中易于显示识别负数，所以带-
print(-27&-1)
print(bin(-1))

print(bin(-27&0b11111111))   # 实际值并不是-27的补码，只是显示的样子是-27的补码的样子

# -1在任何的操作系统中，存储的形式都是全部位是1
# print(bin(27))

# 2.	给出将-27 << 3与-27 >> 3的过程。并在程序上验证是否正确
# （1）估计一下结果的值 必须使用16位计算
# （2）0000000000011011
# （3）1000000000011011
# （4）1111111111100101  -27 补码
# （5）1111111100101000  左移
# （6）1000000011011000  结果的原码  -216
print(2**7+2**6+2**4+2**3)

# （4）1111111111100101  -27 补码
# （7）1111111111111100  右移
# （6）1000000000000100  结果的原码  -4
print(2**2)
print(-27>>3)
print(-27<<3)



# 3.	输入一个三位正整数，输出该数值的百位，十位与个位。
def que3_1():
    x=input("请输入三位正整数数字：")
    # for i in range(len(x)):
    #     print(x[i])
    print(x[0])
    print(x[1])
    print(x[2])

# 方式二：
def que3_2():
    x=345
    print(x//100%10)
    print(x//10%10)
    print(x//1%10)

def que3_3():
    #扩展，可以任何一个数的所有位上的数字：
    x=input("请输入整数数字：")
    for i in reversed(range(len(x))):
       print( int(x)//10**i%10,end=" ")
# que3_3()


# 4.	编写程序，证明and的优先级高于or。
# 应该or在前and在后。
# print(1 or 2 and 3)
# print(1 or (2 and 3))
# print( (1 or 2) and 3)

1 or print("2") and print("3")
# 因为1 将or后面的所有表达式都短路掉。所以证明了and左右两侧的表达式是结合好的
# 否则（如果没有and的优先级比or高的说法）
# or 只能将一个表达式给短路掉。1 or print("2") 得到1
# 1 and print("3"): 至少应该执行一个print(3)
# 但是实际的结果，既没有执行print（"2"），也没有执行print("3")

# 5.	编写程序，证明and与or短路现象的存在。
1 or print("dddddddddddd")
0 and print("dddddddddddd")

1 or input()
0 and input()

1 or 2/0
0 and 2/0
# 2/0



# 6.	输入一个数，输出该数*7的结果。（不允许使用*，也不允许连续累加）
# x *7=x*(4+2+1)
# x*4 + x*2 + x*1
# x<<2+ x<<1 +x<<0
# x<<3-x
print((5<<2)+(5<<1)+(5<<0))
print(5*7)
print((5<<3)-5)

# 15   7
# 2**3+2**2+2**1+2**0


# 7.	输出如下内容：分别使用双引号，和三引号
# # A：are you "tom"
# # B：no

print("A：are you \"tom\"\nB：no")
print("""
A：are you "tom"
B：no
""")

# 8.	定义两个字符串，a=“hello”  b=”hello”，令c=a，
# 思考：是否能对a中的h进行修改
# 输出abc三个变量的值
# 使用is和==判断abc之间的关系，并画出内存图
a="hello"
b="hello"
c=a
# a[0]="p"
a="p"+a[1:]
print(a)

print(a is b)
print(a is c)
print(b is c)

#
#
# 9.	输入一个16位学号如，1001010220170101，其中100是学校代号101是院系代号
# 02专业代号2017年级01班级01学号，请使用切片获取出各个代码。
def que9():
    stuno=input("请输入一个学号：")
    print("学校代码：",stuno[:3])
    print("院系代码：",stuno[3:6])
    print("专业代码：",stuno[6:8])
    print("年级代码：",stuno[8:12])
    print("班级代码：",stuno[12:14])
    print("学号代码：",stuno[14:])

# 11.	这是一个地址，
# http://news.gzcc.cn/html/2017/xiaoyuanxinwen_1027/8443.html
# 其中1027/8443是新闻编号，想办法获得新闻编号。
s="http://news.gzcc.cn/html/2017/xiaoyuanxinwen_1027/8443.html"
#方式一：使用切片
print(s[-14:-5])
#方式二：
print(s.rstrip(".html")[-9:])
#方式三：
print(s.split("_")[1].rstrip(".html"))

#
# 12.	这是一个网址，但是前面有错误的空格字符
s= "  http://news.gzcc.cn/html/xiaoyuanxinwen/4.html"
# （1）	去掉前面的空格
ss=s.strip()
print(s)

# （2）	删除http://前缀
print(ss.lstrip("http://"))

# （3）	去掉后缀.html并输出数字4
print(ss.rstrip(".html")[-1])
# （4）	显示这段文字中有多少个n
print(ss.count("n"))

# （5）	使用/分隔成多个单词
print(ss.split("/"))
#
#
# 13.	分别输入3个爱好，打印出来“我的爱好是**、**、**”
def que13():
    h1=input("输入一个爱好：")
    h2=input("输入一个爱好：")
    h3=input("输入一个爱好：")
    print("我的爱好是",h1,"、",h2,"、",h3)
#
#
# 14.	定义一个字符串a，里面有字符，有数字，请将a字符串的数字取出，并输出成一个新的字符串
def que14():
    a="dodgidga155ddsj255"
    a_new=""
    for i in a:
        if i.isdigit():
            a_new+=i
    print(a_new)

#
# 15.	查资料，或者自己试一下str中的方法，将小写转大写，大写转小写  aDdFDdddFD
a="aDdFDdddFD"
print(a.swapcase())
#
#
#
#
