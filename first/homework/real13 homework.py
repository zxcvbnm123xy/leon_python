from datetime import datetime
# 1. 编写程序，验证AttributeError的产生场合。下面两个都可以。
# class A:
#     c=3
#     __m=3
# try:
#     print(A.__m)
# except AttributeError:
#     print(A._A__m,"私有属性")

# 2.输入一个日期，格式为年 / 月 / 日，如果格式正确，则返回该日期是当年的第几天，
# 否则日期默认为今天，返回今天是当年的第几天。
#
def que2():

    a=input("请输入一个日期")
    try:
       dt= datetime.strptime(a,"%Y/%m/%d")
    except ValueError:
       dt= datetime.today()
    print(dt.timetuple().tm_yday)

#
# 3. 修改之前的银行提款程序，并自定义一个异常类InsufficientFundsError。当余额不足时，产生该错误。并且调用端能够处理捕获该错误。
def que3():
    class Card:
        def __init__(self,id,name,balance=0):
            self.id=id
            self.name=name
            self.balance=balance
    class InsufficientFundsError(Exception):
        def __init__(self,value):
            self.value=value
    class ATM:
        def __init__(self):
            self.card=None
        def insertCard(self,card):
            self.card=card
        def despsit(self,money):
            self.card.balance+=money
            print("已存入{}，余额是{}".format(money,self.query()))
        def withdraw(self,money):
            if money>self.card.balance:
                raise InsufficientFundsError("当前的余额{}，提取的额度{}，余额不足".format(self.card.balance,money))
            self.card.balance-=money
            print("已提取{},余额是{}".format(money,self.query()))

        def query(self):
            return self.card.balance
    c=Card(62200000,"张三")
    atm=ATM()
    atm.insertCard(c)
    atm.despsit(100)
    try:
        atm.withdraw(60)
    except InsufficientFundsError  as e:
        print(e.value)

    try:
        atm.withdraw(60)
    except InsufficientFundsError  as e:
        print(e.value)

    atm.despsit(100)


# 4.将一个列表中所有元素转换成浮点类型，如果不能转换，则丢弃该元素。
#
float()
li=[1,{2,3},{1:"a"},2,3,"a","b",1+2j,["new","cccc"]]
b=li[:]
for i in b:
    try:
        li.append(float(i))
        # li.remove(i)
    except (ValueError ,TypeError):
        # li.remove(i)
        pass
    finally:
        li.remove(i)
print(li)
# 5. 异常，自己写一个len方法，能够获得序列的长度
s="abcd3333"
def len_1(s):
    l=0
    for i in s:
        l+=1
    return l
print(len_1(s))

# 6.作业：
# # 斐波那切数列，使用迭代器实现斐波那切数列
# class Fib:
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         pass
# f = Fib()
# print(f.__next__)
# print(f.__next__)
# print(f.__next__)
#
# # __next__魔法方法
# # next(f) <======> f.__next__()
#
class Fibo:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b

        return self.a

    def __iter__(self):
        return self

# 7. 将课堂的自定义迭代器，实现逆序输出
# next(myIterable) - --最后一个值。
# next(myIterable) - --倒数第二个值。

li=[1,2,3] # list的__iter__方法一定是返回了list的迭代器。
# 将MyIterable下的实例属性设置成li
class MyIterable:
    def __iter__(self): # 返回的是迭代器
        self.li=li
        # return li.__iter__() # 返回的是list下的迭代器
        return MyIterator(self.li) # 返回自定义的迭代器
class MyIterator:
    def __init__(self,data):
        self.li=data
        # 索引
        self.index=0
    # 返回迭代器中下一个元素
    def __next__(self):
        if self.index<len(self.li):
            r=self.len(li[self.index])
            self.index+=1
            return r
        else:
            raise StopIteration
    def __iter__(self):
        return self

myIterable=MyIterable()
for i in myIterable:
    print(i)
myit=myIterable.__iter__()
for i in myit:
    print(i)