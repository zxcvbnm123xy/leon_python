"""
第十四章 文件
"""
# 一.文件
# 操作系统中，word文档，图片，音乐，视频，txt
# 文件划分成两个类别：
# （1）文本文件：.txt    .bat
# （2）二进制文件：除了文本文件以外都是二进制文件。 .doc

# 无论文本文件还是二进制文件在计算机中真正的存储方式都是二进制。

# 二、python文件操作
# 1. 获取文件对象
# 在python中通过open函数来获取文件对象
# open(file,mode)
# 【参数】
# file: 文件的路径。
#        相对路径：从当前的路径开始的路径     /a/b/c
#        绝对路径: 以盘符开头的就是绝对路径   c:/abc/def/....
# mode:模式
# 同组的模式不能一起使用。
# 读写方式
# r  : 以读模式打开，文件一定要事先存在，如果文件不存在会报错
# w  ：以覆盖写的模式打开，如果文件不存在，会新创建文件
# a  ：以追加写的模式打开，如果文件不存在，会创建新文件

# 文本、二进制：
# t:  以字符串模式打开
# b:  以二进制的模式打开

# +： 升级，原来如果是只读的 ，就会升级为可读可写
#          原来如果是只能写的，就会升级为可读可写。

# 例子
# rb  读模式二进制模式打开，只能读
# wt  写模式的文本模式打开，只能写

# 都是可读可写
# r+: 文件必须存在，可读可覆盖写。
# w+: 文件可以不存在，如果不存在会新创建文件，可读可覆盖写。
# a+: 文件可以不存在，如果不存在会新创建文件，可读可追加写。

# 打开一个文件
# 模式默认是rt：文本只读
# 【返回值】open的返回值是文件对象（本质是迭代对象）
# 注意权限是绝对权限。
# f=open("c:/a.txt","wt")
# f.write("aaaaaaaaaaaaaaaaaaaaaa")
# f.read()

# 2.关闭
# 文件属于占用内存比较大对象，一定要在使用之后关闭，同时注意，即使没有成功打开 ，也要关闭。
# 文件对象.close()
# 关闭文件的方式：
"""
(1)直接关闭：问题，如果文件没有被成功打开 ，或者文件操作的过程中出现了异常，都会导致文件不能被关闭
(2)使用try...finally关闭
(3)使用with语句体打开，关闭，关闭的时候，直接在with语句体中自动关闭。
"""
# f=None
# try:
#     f = open("c:/a.txt", "rt")
#     # 其他操作文件的代码
# finally:
#     f.close()

#with语句体打开、关闭文件
# 语法  with open(路径，模式) as  文件的变量名:
#            对于文件的操作
# with open("c:/a.txt", "wt") as f:
#     f.write("bbbbbb")

# 3.文件的读取
# 文件对象是一个迭代对象
# 使用文件的内部函数访问文件
# （1）read(size)  :size参数读取出的数据的大小，
# 如果以文本模式读取，单位是字符
# 如果以二进制模式读取，单位是字节
# -1或者不写，会按照全部读取
# 一般的window操作系统txt文档都是以gbk的模式存储
# with open("c:/a.txt", "rt") as f: # 以t模式读取，返回值是字符串
#     print(f.read(1))
#     print(f.read(1))
#     print(f.read())

# b.txt被另存为utf-8 模式，所以打开的时候，需要指定encoding="utf-8"
# with open("c:/b.txt", "rt",encoding="utf-8") as f: # 以t模式读取，返回值是字符串
#     print(f.read(1))
#     print(f.read(1))
#     print(f.read())
# with open("c:/a.txt", "rb") as f: # 以b模式读取，返回值字节
#     print(f.read(1))
#     print(f.read(1))
#     print(f.read())

# （2）readline() 返回文件的一行
#readline 读取文本内容的时候，保留原文本末尾的换行符。
# 如果没有内容可读（读完了），会返回空串
# with open("c:/a.txt","rt") as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())

# (3)readlines()，返回一个列表，列表中的每一个元素是文件的一行内容，每行会保留末尾的换行符
# with open("c:/a.txt","rt") as f:
#     print(f.readlines())

# 文件作为迭代器，当访问比较大的文件时，都使用for循环进行迭代。
# with open("c:/a.txt","rt") as f:
#     for line in f:
#         print(line,end="") # 去掉print中的\n，使用文本中自带\n

# 4.文件的写入
# （1）write（content），返回写入的长度
# w模式下，write方法是从当前指针的位置进行写入。
# with open("c:/b.txt","wt") as f:
#     f.write("happy new year")
# with open("c:/b.txt","at") as f:
#     f.write("!!!!!!!!!!")

#(2) writelines(lines)
# 参数lines是列表类型，将列表中的所有元素写入文件
# with open("c:/b.txt","wt") as f:
#     f.writelines(["第1行数据\n","第2行数据\n","第3行数据\n","第4行数据\n"])
#
# with open("c:/b.txt","wb") as f:
#     f.write(b"abcde1456")
# 练习：
"""
1. 创建一个txt文件，
写入有志者事竟成，破釜沉舟，百二秦关终属楚，
苦心人 ，天不负，卧薪尝胆三千越甲可吞吴

2.追加，我要学python
3.读取一下文件。

"""
# with open("test.txt","wt") as f:
#     f.write("有志者事竟成，破釜沉舟，百二秦关终属楚，\n苦心人 ，天不负，卧薪尝胆三千越甲可吞吴.")
#
# with open("test.txt","a+") as f:
#     f.write("我要学python")
#     # print(f.read()) # 读不出来内容，因为文件指针定位

# 实现文件的复制
# with 语句体支持同时open，可以使用,分隔
# with open("test.txt") as f1,open("copy.txt","wt") as f2:
#     # 方式一：适合文件小的情况
#     # f2.writelines(f1.readlines())
#
#     # 方式二：
#     for line in f1:
#         f2.write(line)
#
# with open("c:/c.mp3","rb") as f1,open("c:/c_copy.mp3","wb") as f2:
#     for line in f1:
#         f2.write(line)


# 5. 文件的定位
# 文件的指针：是下一次要读取或者写入的字节（字符）的位置，随着读取或者写入的进行，
#            指针也会随之移动
# 文件指针的初始位置，分为两种情况
#（1）r或者w打开文件，指针在初始位置，0，开头的位置
#（2）a模式打开的文件，指针在文件的末尾位置，文件末尾最后一个字符的下一个位置。

# 文件定位的相关方法
# （1）tell() 返回文件指针的位置
# print()
# with open ("c:/d.txt","wt") as f:
#     print(f.tell())
#     f.write("0123456789")
#     print(f.tell())
#
# with open ("c:/d.txt","rt") as f:
#     print(f.tell())
#     f.read(5)
#     print(f.tell())

#（2）seek(offset,whence)：改变文件指针的位置。
# offset偏移量 正数：从左向右移动，负数：从右向左移动
# whence指定偏移量的参照位置：
# 0（从文件头开始计算   os.SEEK_SET）
# 1（从当前位置开始计算 os.SEEK_CUR ）
# 2（从文件末尾开始计算 os.SEEK_END ）
# 使用时的注意事项：
"""
对于0起始位置来说可以指定r模式和t模式
对于1和2来说，必须指定b模式
# 如果指定的是t模式，
当whence=1或者2，offset只能取0：将指针指向当前位置，将指针指向文末
"""
# import os
# with open ("c:/d.txt","r+b") as f:
#     print(f.tell())
#     f.read(1)
#     print(f.tell())
#     # whence=0 从文件头开始移动3个
#     f.seek(3,os.SEEK_SET)
#     print(f.tell())
#     # 移动回起始位置
#     f.seek(0,0)
#     print(f.tell())
#
#     # whence=1 从文件当前位置开始移动
#     f.read(2)
#     print(f.tell())
#     f.seek(3,os.SEEK_CUR)
#     print(f.tell())
#
#     # whence=2 从文件末尾开始移动
#     f.seek(-1,os.SEEK_END)
#     print(f.tell())
#     f.seek(3,os.SEEK_END)
#     print(f.tell())
#     f.write(b"abc")
#
# with open ("c:/e.txt","r+t") as f:
#     print(f.tell())
#     f.read(1)
#     print(f.tell())
#     # whence=0 从文件头开始移动3个
#     f.seek(3,os.SEEK_SET)
#     print(f.tell())
#     # 移动回起始位置
#     f.seek(0,0)
#     print(f.tell())
#
#     # # whence=1 从文件当前位置开始移动
#     f.read(2)
#     print(f.tell())
#
#     # 对于字符来说，不支持从当前位置和末尾，移动非0的位置
#     # f.seek(1,os.SEEK_CUR) 错误
#     f.seek(0,os.SEEK_CUR)
#     print(f.tell())
#
#     # f.seek(1,os.SEEK_END)  # 错误
#     f.seek(0, os.SEEK_END)
#     print(f.tell())

"""
对于b模式来说，whence=0、1、2 都可以
对于t模式来说，whence=0 可以
              whence=1、2  offest=0才可以
"""


# 三、 文件与路径的操作
# 使用os、os.path模块对文件或者文件夹的操作
# 1.os模块
import os
# （1）mkdir创建目录，父目录必须存在，创建的目录必须不存在，否则报错
# os.mkdir("c:/abc/def")

# (2) os.makedirs()创建路径，如果父路径不存在，也会创建
# os.makedirs("c:/abc/def/ghi")
# exist_ok 默认值是False 意味着如果创建的目录存在，则报错
# os.makedirs("c:/abc/d ef/ghi",exist_ok=True)

#(3)os.rmdir()删除空目录，如果路径不存在会 报错
# os.rmdir("c:/abc/def/ghi")

#(4)os.removedirs() 删除空目录，删完还会看父目录是不是空，如果是，也一并删除，直到不为空为止
# os.removedirs("c:/abc/def/ghi")

# (5)os.remove() 删除文件 如果不存在也会报错
# os.remove("c:/a.txt")

#(6)rename重命名文件或者目录
# 源文件所在的路径跟重命名之后的路径要保持一致
# os.rename("c:/abc/1.txt","c:/abc/2.txt")

#(7)os.renames() 相当于移动文件
# 可以将重命名的文件移动到不同的路径
# 移动之后，会判断文件夹是否为空目录，如果是空目录，直接删除。
# os.renames("c:/abc/2.txt","c:/edf/2_new.txt")

# （8）getcwd 返回当前工作的目录
# print(os.getcwd())

#(9)walk（path） 遍历路径下的文件
# 返回值：元组，每一层的情况
#（起始路径，起始路径下的文件夹，起始路径下的文件）
# t=os.walk("c:/abc")
# print(t)
# for i in t:
#     print(i)

# (10) 返回路径下的文件目录
# print(os.listdir("c:/"))


# 2. os.path
# (1) 返回绝对路径
# 如果参数是.则返回当前文件所在的绝对路径
# print(os.path.abspath("."))

# （2）basename返回路径中最后的部分
# print(os.path.basename("c:/abc/def/ghi/1024.html"))

# (3)返回多个路径中最长公共路径
# print(os.path.commonpath(["c:/abc/def/ghi","c:/abc/def","c:/abc/def/ghi1"]))

# (4)os.path.exists(path) 判断路径是否存在
# 联合os模块下的文件和文件夹一起判断
# print(os.path.exists("c:/abc1"))

#（5） 返回目录的创建时间，访问时间和修改时间（同操作系统保持一致）
# print(os.path.getatime("c:/abc/other.txt"))
# print(os.path.getctime("c:/abc/other.txt"))
# print(os.path.getmtime("c:/abc/other.txt"))

# （6）返回文件的大小，单位：字节
# print(os.path.getsize("c:/abc/other.txt"))

# (7)os.path.isdir判断路径是否存在一个文件、目录
# print(os.path.isdir("c:/abc1"))

# （8）拼接路径，将参数全部拼接成路径
# print(os.path.join("abc","def","ghi"))
# 如果参数中存在绝对路径，那么绝对路径之前的参数全部丢掉
# print(os.path.join("abc","c:/def","ghi"))
# print(os.path.join("abc","c:/def","","","","ghi"))

# (9)将路径拆分成dirname和basename
# print(os.path.split("c:/abc/def/ghi"))

# 3.shutil模块
# （1）copy复制文件，不会赋值文件的时间
import shutil
# shutil.copy(源文件所在位置,拷贝到的新路径)
# 拷贝到的新路径 存在，则直接拷贝,方法会返回目标文件所在的路径
#              不存在，报错。
# print(shutil.copy("c:/abc/other.txt","c:/abc/def/other_new.txt"))
# print(shutil.copy("c:/abc/other.txt","c:/aaa/other_new.txt"))

# （2）shutil.copy2() 将源文件的时间都复制过去
# print(shutil.copy2("c:/abc/other.txt","c:/abc/def/other_new1.txt"))

# （3） copytree 赋值目录，连同子目录一起复制
# 第一个参数：原路径
# 第二个参数：目标路径（要求目标路径不能存在，如果存在会报错）
# shutil.copytree("c:/abc","d:/abc")

#(4)删除目标路径，包括路径下的子路径，文件都会删除
# shutil.rmtree("d:/abc")

# (5)连同当前的目录以及目录下子目录、文件，一起移动到目标路径
shutil.move("c:/abc","d:/abc")


