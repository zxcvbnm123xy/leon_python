# s = "abcdefg"
# x = 0
# print("a" + "b")
# print('abc'> 'xyz')
# # x = 3
# # print("ab" in "abcd")
# # x += 6
# # print(int(4**0.5))
#
# #练习 将下面列表在中tom和jerry元素位置对调
# names=["tom","jerry","kate",1,3,[4,5]]
# names[0]=names[1]
# names[1]="tom"
# print(names)
#
# #新定义一个names_new ,画出内存图
# names=["tom","jerry","kate",1,3,[4,5]]
# names_new = names
# print(names_new)
#
# li=["a","b","c","d","e"]
# #1.添加
# #+合并：新创建列表进行合并
# #append对列表中的元素进行追加
# li.append("z") #注意使用的时候append的返回值是none
# print(li)
#
# #字符串的相关方法都不是原地修改，都是新创建字符串
# # s="abc"
# # print(s.replace("a","d"))
# # print(s)
# print(li+["z"])
# print(li)
#
# #插入元素，可以向列表中的index位置插入object参数
# #li.insert(index,object),insert之后的返回值也是none
# li=["a","b","c","d","e"]
# li.insert(2,"z")
# print(li)
#
# #练习，使用insert能不能达到append的效果
# li.append("happy")
# print(len(li))
# li.insert(len(li),"happy")
# print(li)
#
# #2.删除
# #（1）pop
# # li.pop(index) 可以删除index指定位置的元素 一次只能删除一个
# #pop的返回值是删除元素的内容
# #index如果省略 会默认删除列表中的最后元素
# li.pop(-1)
# print(li)
# print(li.pop(1))
# li.pop()
# print(li)
#
# #(2) remove 根据传入参数的内容删除指定元素
# # li.remove("c")
# # print(li)
# # li.remove()
# #删除的内容不存在，会报错
# #一次删一个 只删除第一次见到的元素
# li=["a","b","c","d","e","a"]
# li.remove("a")
# print(li)
#
# #3.检索
# # li.index("要检索的内容"，起始位置，终止位置)
# #包含起始，不包含终止
# print(li.index("d"))
# #内容不存在，会报错
#
# #4.统计
# li=["a","b","y","f","e","t"]
# print(li.count("a"))
#
# #5.反向:原地反向
# li.reverse()
# print(li)
#
# #6.排序sort
# #reverse参数:默认升序F，
# #降序reverse=True
# li.sort()
# print(li)
# li.sort(reverse=True)
# print(li)
#
# #降序可以通过先调用sort升序排序，在调用reverse反向
#
# #7.列表的复制
# #（1）赋值
# #（2）copy方法
# #（3）切片
# #（4）copy包下的copy和deepcopy
# #（5）*
# li=[1,2,3,[4,5]]
# li1=li
# print(id(li),id(li1))
# li[0]="new"
# print(li,li1)
#
# #使用列表的copy方法进行复制
# #只负责复制当前的列表对象（只复制第一层）
# li=[1,2,3,[4,5]]
# li2=li.copy()
# print(id(li),id(2))
#
#
# #一，元组的创建
# #定义元组:元组名（元素，）
# #元组的元素不能进行修改
# a=(1,2,3)
# print(type(a),a)
# b=1,2,3
# print(type(b),b)
#
# #二，元组的操作
# #1.运算符
# #跟列表一样 + * in not in is is not
# a=(1,2)
# b=(3,4)
# print(a+b)
#
# print(a*3)
#
# #元素的合并和重复
#
# print(1 in a)
# print(1 in ((1,2),3,4))
#
# #is ==
# a=(1,2,3)
# b=(1,2,3,)
# c=a
# print(id(a),id(b),id(c))
#
# #2.索引、切片
# a=(1,2,3)
# print(a[1])
# print(a[1:3])
#
# #如果元组中的元素是可变类型，对于可变类型是可以修改的
# a=([1,2,3],4,5,6)
# a[0][0]="new"
# print(a)
#
# #三、相关方法
# a=(1,2,3,1,2,3,4,1,2,1)
# #统计
# print(a.count(1))
# #返回某一个元素的位置
# print(a.index(1))
#
# print(4%10)
#
# # 常用字符
# # ascii
# #  gb2312
# #  big5 繁体
# # GBK：亚洲的支持比如中文，韩文，日文，大字符集
# # UNicode字符集（定长存储）：将所有的语言统一到一套编码中，2-4个自己写
# # 包括ascii也用两个字节，所以很浪费空间
# #  utf-8 字符集（变长储存），英文使用一个字节表示，汉字一般用三个字节
# #
# # 因为字节和字符串使用的编码集不一样：
# # 字节 ascii
# #字符串 Unicode 字符集
#
# print(ord("a"))
#
# #二、Unicode和utf-8
# #1.Unicode
# print(ord("中")) #计算机内部其实存的就是20013对应的二进制
# print(chr(20013))  #ord 和 chr是可逆的 一个是汉字 一个是二进制
#
# #0x4e2d 20013对应的16进制
# print(hex(20013))
#
# #对应的Unicode字符集， \u4e2d 取对应的十进制找到十六进制，就是对应的Unicode字符集
# print("\u4e2d")
#
# #2.utf-8字符集
# print("中".encode())  #可以直接将字符转换成utf-8的编码集
# # b'\xe4\xb8\xad'
# print(bin(0xe4),bin(0xb8),bin(0xad))
#
# # 0b11100100 0b10111000 0b10101101
# # unicode      100111000101101
#
# # 3.在计算机中两个字符集之间的合作关系
# # （1）.计算机内存中，统一使用unicode编码（因为unicode的速度快），
# # 当需要保存到硬盘或者内存的时候，需要转成utf-8（因为utf-8省资源）
# # 五个组成部分 硬盘存储，内存，控制器，计算中心，io
# # （2）.浏览网页的时候，服务器也是把动态生成的unicode内容转成utf-8，再传到服务器
# #       所以网页看到的编码应该都是utf-8
#
# # 三、Python中的字节和字符之间的转换
# # 在python 中 字节：utf-8  字符串：unicode
#
# # 字符串（unicode）---->字节（utf-8） 编码encode
# s="中国"
# print(s.encode())  #encoding 参数不设置，默认utf-8
# print(s.encode(encoding="gb2312"))
#
# # 字节（utf-8）------>字符串（unicode） 解码decode
# b=b'\xe4\xb8\xad\xe5\x9b\xbd'
# print(b.decode())
# b1=b'\xd6\xd0\xb9\xfa'
# print(b1.decode(encoding="gb2312"))
#
# # day=int(input("请输入星期几："))
# # print("今天是周{}".format(day if 1<=day<=5 else "末"))
# #
# # x=int(input("请输入0或1："))
# # print("男的" if x==0 else "女的")
#
# # 断言：断定某些语句是都正确
# # 语法：一旦表达式返回False，程序回报AssertionError，程序被停止，无法继续
# """
# assert 表达式，错误信息
# """
# # assert 1>6,"谁告诉你的？"
#
# # 1+2+...+100
# x=1
# s=0
# # while x<=100:
# #     s+=x
# #     x+=1
# # print(s)
# for x in  range(1,101,2):
#     s+=x
#
# print(s)
#
# #练习：使用索引实现列表中元素的对调
# #  使用索引替换所有元素为new
li=["a","b","c",[1,2]]
li[0],li[1],li[2],li[3]=li[1],li[0],li[3],li[2]
print(li)

for i in range(len(li)):
    li[i]="new"
print(li)

#练习，希望删除或者插入元素使用切片完成
a=["aaa","bbb","ccc","ddd","eee"]
a[1:1]=["fff"]
a[1:1]=[]
print(a)

# 练习：
import copy
a=["aaa","bbb","ccc","ddd","eee"]
b=a
c=a[:]
d=copy.deepcopy(a)
a.sort()
#
print(a,b,c,d)



li=[10,20,80,77,55,7,8]

min=0
for i in range(len(li)):
    if i<li[min]:
        min=i
    li[0],li[min]=li[min],li[0]
print(li)

"""
第七章 字典和集合
"""
#字典
#映射类型数据：根据"键" 映射到“值”
names=["tom","jerry","kate"]
scores=[100,80,77]
#使用字典，形成，名字-成绩的对照表
#名字---key
#成绩--value值

#字典的原理：
#哈希表（散列表）：这种表能够根据键值对直接进行访问的数据结构
#通过吧key和value映射到表一个位置记录上，相当于使用哈希函数
#将key值映射成唯一的哈希code
#将哈希code跟value关联。

#如果key在映射成hashcode的时候，
# 结果是重复的，会采用链接法或开放寻址法（python）
#一直找到没有重复的唯一值

#一、字典的定义
#格式：{kay：value，key2：value...}
#格式：dict（kay=value，key2=value...）
# 如果定义字典时出现重复的值，使用后面的value覆盖前面的value值
"""
#字典的特点
1，字典中的键值对是无序存储
2，字典中的key值是不可变数据类型，value不限制
3，字典中的key不能重复
"""
s={"tom":100,"jerry":90,"kate":89,"tom":99}
print(s)
s1=dict(tom=100,jerry=90,kate=80)
print(s1,type(s1))

#定义空字典
d={}
print(len(s),print(len(d)))

# 二，字典中key和value的访问和修改
#字典不能通过索引访问键值对，因为无序的数据类型
#只能通过kay访问值
#格式：字典[key](key必须存在)
s={"tom":100,"jerry":90,"kate":89}
print(s["tom"])

#通过key修改值
# 格式： 字典[key] (key可以不存在)
# 如果key存在：会修改key对应的value
# 如果key不存在：会创建key，value键值怼
s["tom"]=99
print(s)

s["tim"]=59
print(s)


#练习
#（1）定义一个全局变量，# 然后在函数内去修改全局变量
#（2）在函数内先输出全局变量，输出对应的变量，然后尝试去修改该变量的值
#（3）在函数内部将全局变量函数+1
#（4） 定义一个全局变量 id 定义一个li=[1,2,3]
# 在打印列表所在的内存地址

a=100
li=[1,2,3]
id(li)
print(id(li))
def q(x,y):
    # a+=1
    x+=1
    li[0]+=1

q(a,li)
print(a,li)
print(id(li))

# L---local 局部
# E---enclosing-----外围
# G---global-----全局
# B---bulidins-----内检

#访问：读取，会严格按照LEGB的顺序
#修改和删除：
    #修改:先从最小的域开始查找， 如果找到则修改，如果找不到不会继续往上找
            # 如果找不到不会继续往上找，而是直接在当前最小的域新建一个
#           为了避免不小心污染全局变量，起了一个跟全局变量名一样的变量
#    删除：只能删除自己变量空间的，不能删除其他变量空间的
#

#对于再聚不命名空间中希望修改全局变量或者外围变量:使用global和noglobal关键字
#在局不命名空间中修改全局变量：global
y=2
def g():
    # print(y)
    global y #解决需要声明global
    y=3
    print(y)
g()

#在局不命名空间中修改外围变量：nolocal
def out():
    x=1
    def inner():
        nonlocal x
        x=2
    inner()
    print(x)

out()

# n的阶乘
def s(n):
    if n==1:
        return 1
    else:
        return s(n-1)*n

from toolz import curry
@curry
def power(x,y):
    return x**y
times=power(3)
print(times(9))

import functools
c=functools.partial(power,y=3)
print(c(10))

import random

stu = ""
stu = "".join(str(i) for i in random.sample(range(0, 9), 6))
print(stu)