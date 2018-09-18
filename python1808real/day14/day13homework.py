# 1.
# 编写程序，验证AttributeError的产生场合。下面两个都可以。
# 方式一：
# class A:
#     pass

# 类属性
# A.a
# 实例属性，实例方法
# a=A()
# a.b
# a.c()

# 方式二：
# li=[1,2,3]
# li.a

# 当访问一个对象的时候，对象下没有指定的属性名
# （类属性、实例属性、类方法名、实例方法名、静态方法）

# 2.# 输入一个日期，格式为年 / 月 / 日，如果格式正确，
# 则返回该日期是当年的第几天，否则日期默认为今天，返回今天是当年的第几天。
def que2():
    from datetime import  datetime
    s=input("请输入一个日期：")
    try:
        # print(datetime.strptime(s,"%Y/%m/%d"))
        dt=datetime.strptime(s,"%Y/%m/%d")
    except:
        # print(datetime.today())
        dt=datetime.today()
        raise ValueError("输入的日期有误")
    timetuple=dt.timetuple()# 将datetime类型的对象变成时间元组
    print(timetuple.tm_yday)




#
# 3.
# 修改之前的银行提款程序，并自定义一个异常类InsufficientFundsError。
# 当余额不足时，产生该错误。并且调用端能够处理捕获该错误。
class InsufficientFundsError(Exception):
    def __init__(self):
        self.message="余额不足"


class Card:
    def __init__(self,id,name,balance=0):
        self.id=id
        self.name=name
        self.balance=balance
class ATM:
    def __init__(self):
        self.card=None
    def insert(self,card):
        self.card=card
    def desposit(self,money):
        self.card.balance+=money
        print("存入了{}".format(money))
        self.query()
    def query(self):
        print("当前余额是{}".format(self.card.balance))
    def withdraw(self,money):
        if money>self.card.balance:
            raise InsufficientFundsError()
        self.card.balance-=money
        print("已取款{}".format(money))
        self.query()

card=Card(1001,"张三",500)
atm=ATM()
atm.insert(card)
atm.desposit(100)

atm.withdraw(300)
try:
    atm.withdraw(400)
except InsufficientFundsError as err:
    print(err.message)
atm.desposit(1000)
atm.withdraw(100)

# 4.
# 将一个列表中所有元素转换成浮点类型，如果不能转换，则丢弃该元素。
li=[1,2,3,"a","b",1+2j,4,[1,2]]
li_new=[]
for i in li[:]:
    try:
        li_new.append(float(i))
    except(ValueError,TypeError):
        li.remove(i)
print(li)
print(li_new)

# 如果不想新创建li_new存储数据，希望直接把数据存储到li
li=[1,2,3,"a","b",1+2j,4,[1,2]]
for i in li[:]:
    try:
        li.append(float(i))
        # li.remove(i)
    except(ValueError,TypeError):
        pass
    finally:
        li.remove(i)
print(li)


#
# 5.# 异常，自己写一个len方法，能够获得序列的长度
# 方式一：
# def len1(s):
#     l=0
#     for i in s:
#         l+=1
#     return l
# print(len1("abc"))
#
# def que5(value):
#     try:
#         print(len1(value))
#     except TypeError:
#         print("不能获得非迭代对象的长度")
# que5("abc")
# que5(1)


# 方式二：通过捕获IndexValue来获得长度
def len2(s):
    index=0
    while True:
        try:
            s[index]
            index+=1
        except IndexError:
            break
        except :
            print("非迭代对象")
            break
    return index
print(len2("abc"))


#
# 6.作业：
# # 斐波那切数列，使用迭代器实现斐波那切数列
class Fib:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a

    def __iter__(self):
        return self
f=Fib()
print(next(f))
print(next(f))
print(next(f))
for i in f:
    if i<100000:
        print(i)
    else:
        break

# 方式二
class Fib:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        if self.a < 100000:
            self.a,self.b=self.b,self.a+self.b
            return self.a
        else:
            raise ValueError("当前Fib只能产生<100000的斐波那切数列")


    def __iter__(self):
        return self
f=Fib()
try:
    print(next(f))
    print(next(f))
    print(next(f))
    for i in f:
        print(i)
except ValueError:
    print("执行完毕")

# 7.
# 将课堂的自定义迭代器，实现逆序输出
# next(myIterable) - --最后一个值。
# next(myIterable) - --倒数第二个值。
class MyIterable:
    def __iter__(self):
        self.li=[1,2,3]
        return MyIterator(self.li)
class MyIterator:
    def __init__(self,data):
        self.li=data
        self.index=len(self.li)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>-1:
            r=self.li[self.index]
            self.index-=1
            return r
        else:
            raise StopIteration
myIterable=MyIterable()
myIterator=myIterable.__iter__()
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# 掌握：迭代器和迭代对象 父类、关系
#       自定义迭代器或者迭代对象时，实现哪些方法。
#       迭代器的特性