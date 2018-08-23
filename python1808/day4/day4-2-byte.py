"""
字节 （序列）bytes
字节：由一些列的单字节组成
单字节：占用8个数据位： 数字 特殊的符号  英文字母等。。。不能存储汉字
"""
# 00000000
# 00000001
# 11111111
# 最多存储255种不同内容

# 一、字节创建
s="hello"
print(type(s))
# 定义字节跟字符串类似，但是需要在定义的单引号或者双引号前面加b
b=b"hello"
print(type(b))
# b=b"中国"

# 二、字节的操作:参看字符串
# 运算符、索引、切片
print(b"abc"+b"bcd")
print(b"abc"<b"bc")
# is ==
b=b"hello"
b1=b"hello"
b2=b1
print(b == b1)
print(b is b1)
print(b2 is b1)
print(id(b),id(b1),id(b2))

# 索引输出的是ascii
print(b[0])
# 切片不是ascii码
print(b[0:2])


# 相关方法
b=b"hello"
print(b.count(b"h"))
print(b.split(b"e"))


