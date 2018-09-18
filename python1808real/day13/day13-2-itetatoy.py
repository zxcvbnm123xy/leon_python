"""
第十三章：生成器，迭代器，装饰器
"""
# 迭代器
# 1.可迭代对象与迭代器
# 字符串，列表，元组，字典，集合
# 可以进行for循环遍历的对象，就是可迭代对象
s="abc"               #str
b=b"abc"              #bytes
li=[1,2,3,4]          #list
tu=(1,2,3,4)          #touple
d={1:"one",2:"two"}  #dict
se={1,2,3}            #set
for i in s:
    pass
for i in b:
    pass
for i in li:
    pass
for i in tu:
    pass
for i in d:
    pass
for i in se:
    pass

# 可迭代对象的类型时Iterable类型
from collections.abc import Iterable
print(issubclass(str,Iterable))
print(issubclass(bytes,Iterable))
print(issubclass(list,Iterable))
print(issubclass(tuple,Iterable))
print(issubclass(dict,Iterable))
print(issubclass(set,Iterable))

# 3 一般可迭代对象都是事先了Iterable中 __init__方法，来成为可迭代对象
#  有的是实现了__getiterm__方法，也可以是可迭代对象（历史原因）
# 任何的可迭代对象，都有迭代器
# 迭代器：是一个一次性容器，里面的元素只要被next调用过，就呗pop掉了
from collections.abc import Iterator
print(issubclass(Iterator,Iterable))

# 迭代对象：实现__iter__方法，返回一个迭代器
# 迭代器：__iter__:返回一个迭代器
#         __next__:返回迭代对象的下一个元素
li=[1,2,3]
it=li.__iter__() #获得迭代器
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it)
# print(it.__next__())

# for 循环
# for i in li:
#     print(i,end="")
# print()
for i in it:
    print(i,end="")
print()
for i in it:
    print(i,end="")
print()

# 为什么迭代对象可以遍历多次？迭代器只能遍历一次？
# 迭代器只能够遍历一次——底层
# 为什么迭代对象遍历多次：模拟for循环
# 迭代对象可以通过__iter__方法产生一个迭代器
li=[1,2,3] #迭代对象下，有__iter__方法，能够产生迭代器
it=li.__iter__()
while True:
    try:
        item=it.__next__()
        print(item)
    except StopIteration:
        del it
        break

# 3. 自定义一个迭代类型
# 自定义迭代对象：不需要显示的继承ITerable，只要实现iter方法，返回一个迭代器，
#                这样就可以形成一个迭代对象，就是Iterable的子类
# 自定义迭代器： 不需要显示的继承Iterator，只要实现iter方法，__next__
#                 这样就可以形成一个迭代器，就二十iterator的子类
# class MyIterable:
#     def __iter__(self):
#         pass
# class MyIterator:
#     def __iter__(self):
#         pass
#     def __next__(self):
#         pass
# m=MyIterable()
# print(isinstance(m,MyIterable))
# print(isinstance(m,Iterable))
# print(issubclass(MyIterable,Iterable))
#
# n=MyIterator()
# print(isinstance(m,Iterator))
# print(issubclass(MyIterator,Iterator))
# print(issubclass())

# 模拟列表自定义迭代对象和迭代器
li=[1,2,3]
# 将MyIterable下的实例属性设置成li
class MyIterable:
    def __iter__(self):
       self.li=li
       # return li.__iter__() # 返回的是list下的迭代器
       return MyIterator(self.li) # 返回自定义的迭代器
class MyIterator:
    def __init__(self,data):
        self.li=data
        # 索引
        self.index=0
    def __iter__(self):
        return self
    # 返回迭代器中下一个元素
    def __next__(self):
        if self.index<len(self.li):
            r=self.li[self.index]
            self.index+=1
            return r
        else:
            raise StopIteration
m=MyIterable()
for i in MyIterable:
    print(i)

# 为什么list，或者touple，str 都被设计成可迭代对象，而不直接设计成迭代器
# 迭代器是一次性的，当时用过一次__next__迭代器中的元素就没有了
# 使用迭代对象中的__iter__方法，返回一个新的迭代器

# 作业：
# 斐波那契数列，使用迭代器实现菲波那切数列
# 实例属性  __init__
# a=0
# b=1
class Fib:
    def __iter__(self):
        return self
    def __next__(self):
        pass
f=Fib()
print(f.__next__())
print(f.__next__())
print(f.__next__())

# __next__ 魔法方法
# next(f)<======>f.__next__()

