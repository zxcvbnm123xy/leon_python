"""
字符集
"""
# 定义字节和定义字符串
a="hello"
b=b"hello"
# 在计算机中存储的，无论是字节还是字符串都是以二进制模式存储的。
# 字符集：是一堆字符组成的集合，用来指定字节或者字符串映射成二进制的规则

#一、常用的字符集：
# 1. ascii码：只包含字母，数字，还有一些符号，127个。

# 2.gb2312编码：简体汉字编码规范。 2个字节16个数据位
#     big5(了解)：支持汉字繁体编码规范
#   GBK：亚洲的比如中文、韩文、日文，大字符集。

# 3.unicode字符集（定长存储）：将所有的语言都统一到一套编码中。2-4个字节来表示一个字符
#   包括ascii也需要使用2个字节表示，所以很浪费空间

# 4.utf-8 字符集（变长存储）：英文使用1个字节表示，汉字一般使用3个字节表示。

# 因为字节和字符串使用的编码集不同：
# 字节    ascii
# 字符串  unicode字符集

print(ord("a"))


#二、 unicode和utf-8
# 1.unicode
print(ord("中"))  # 计算机内部其实存储的是20013对应的二进制。
print(chr(20013))

#0x4e2d 20013对应的16进制
print(hex(20013))
print(bin(20013))

# 对应的unicode字符集  \u4e2d
print("\u4e2d")

#2. utf-8字符集
print("中".encode())  #可以直接将字符转换成utf-8的编码集
# b'\xe4\xb8\xad'
print(bin(0xe4),bin(0xb8),bin(0xad))


# 中
# utf-8    111001001011100010101101  24数据位    3个字节
# unicode       100  111000101  101  16个数据位  2个字节
# utf-8 编码可以看成是unicode编码的一部分


# 3. 在计算机中两个字符集之间的合作关系
# (1). 计算机内存中，统一使用unicode编码(因为unicode的速度快)，
#      当需要保存到硬盘或者传输的时候，需要转换成utf-8（因为utf-8存储省资源）
#（2）.浏览网页的时候，服务器也是把动态生成的unicode内容转换成utf-8再传输到服务器，
# 所以在网页上看到的编码都是utf-8编码。



# 三 、python中的字节和字符之间的转换
# 在python中
# 字节：  utf-8
# 字符串：unicode

# 字符串（unicode）---->字节（utf-8）  编码  encode（字符串下的方法）
s="中国"
print(s.encode() )# encoding参数不设置，默认是转换成utf-8
print(s.encode(encoding="gb2312"))  #b'\xd6\xd0\xb9\xfa'

# 字节（utf-8）----->字符串（unicode） 解码 decode（字节下的方法）
b=b'\xe4\xb8\xad\xe5\x9b\xbd'
print(b.decode())
b1=b'\xd6\xd0\xb9\xfa'
print(b1.decode(encoding="gb2312"))






