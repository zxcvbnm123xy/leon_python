"""
第三章 数据类型  字节bytes
"""
# 一、字节的定义
# 字节是由一些列的单个字节组成的序列。
# 单个字节：占用8个数据位（二进制）2**8-1=255

# 创建字节：跟创建字符串类似，加前缀b
b=b"hello world"
print(type(b))

# 字节的操作
# 索引、切片、运算符、遍历
print(b[0]) # 对于字节的索引，显示的是ascii
print(b[1:5])
print(b"hello"+b"world")  # 与字符串类似，都是新创建字节进行合并
print(b"h" in b)
c=b"hello world"
print(b is c)

d=b"abc"

# 字节的字符集是ascii码

# 遍历和索引得到的都是ascii码
for i in b:
    print(i)


# 相关方法
# 同字符串

