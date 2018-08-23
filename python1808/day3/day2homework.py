# 1.数值类型分为哪些？
# 数值类型：整数、浮点数、复数
# 布尔类型属于整数类型的子类型


# 2.计算二进制数1001和二进制101手工计算，程序验证
#  1001
#+  101
#  1110
def que1():
    x=0b1001
    y=0b101
    print(bin(x+y))
# que1()
# 3.将十进制的17转换成2进制，8进制和16进制，使用手工计算，并使用数值的方法验证。
def que3():
    z=17
    print(bin(z))
    print(oct(z))
    print(hex(z))

# 4.将二进制100110101转换成10进制，8进制和16进制，使用手工计算，
# 并使用数值方法验证。
# 乘幂
# 底数：2
def que4():
    a=0b100110101
    print(1*2**8+1*2**5+1*2**4+1*2**2+1)
    print(oct(a))
    print(hex(a))


# 5.输入a,b,c,d 4个整数，计算a+b-c*d的结果，输出。
# 先4个input ，1个print
def que5():
    a=int(input("请输入a："))
    b=int(input("请输入b："))
    c=int(input("请输入c："))
    d=int(input("请输入d："))
    print("结果是=",a+b-c*d)

# que5()

# 6.定义变量a="123"  b="456"  c="789",
# 现将d绑定到a，a绑定到b，b绑定到c。
# 输出abcd四个值，画出内存图变化。
def que6():
    a=123
    b=456
    c=789
    d=a
    a=b
    b=c
    print(a,b,c,d)