# 1.	编写一个函数，参数为一个列表（或元组）类型，能够遍历输出列表中的元素。
# 列表中的元素可能还是列表，嵌套列表要求能够单个元素输出，并且可能会出现多层嵌套。
li=[1,2,3,[4,5,[6,7,[8,9]]]]
# 突破点：当元素是不可变类型的时候 ，append到新列表中
#         如果当前元素是列表， 使用递归调用自己
li_new=[]
def showli(li):
    for i in li:
        if type(i)!=list:
            li_new.append(i)
        else:
            showli(i)
showli(li)
print(li_new)

#
# 2.	打印菲波那切数列的前n项。使用两种循环和递归两种方式
# 递归解决
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
# print(fib(10))
for i in range(1,11):
    print(fib(i))


# 迭代解决
a=b=1
# x=a+b
# 1 1 2
for i in range(10):
    print(a)
    # x=a+b
    # a=b
    # b=x
    a,b=b,a+b

#
#
# 3.	猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想吃时，
# 只剩下一个桃子了。求第一天共摘多少个桃子。（迭代法）
# 递归
# 第10天  1
# 第9天   （1+1）*2=4
# 第8天   （4+1）*2
def a(n):
    if n==10:
        return 1
    else:
        return (a(n+1)+1) *2
print(a(1))

day=10
x=1
while day>1:
    x=(x+1)*2
    day-=1
print(x)


#
# 4.	求平方和，有列表[1,……9]，把每一个元素都取一下平方，然后累加求和
# 使用普通函数和面向过程思维解决问题
# 使用高阶函数解决问题
li=list(range(1,10))
print(li)
s=0
for i in li:
    s+=i**2
print(s)

print(sum([i**2 for i in li]))

print(list(map(lambda x:x**2,li)))
print(sum(list(map(lambda x:x**2,li))))

from functools import reduce
# reduce(函数，迭代对象)
print(reduce(lambda x,y:x+y,map(lambda x:x**2,li)))
import operator
print(reduce(operator.add,map(lambda x:x**2,li)))

#
# 5.	自己实现一下map函数，然后再自己调用一下。
# map(func,迭代对象)
# 将迭代对象中的每一个元素调用一次func
def m(func,seq):
    result=[]
    for i in seq:
        result.append(func(i))
    return result

print(list(m(lambda x:x**2,li)))

#
# 6.	编写“计算机类”，属性包括CPU型号，内存大小，硬盘大小。
# 行为包括介绍CPU型号，展示内存大小，展示硬盘大小，综合介绍。
class Computer:
    def __init__(self,cpu):
        self.cpu=cpu
        self.disk=None
        self.memory=None
    def showcpu(self):
        print("cpu的型号{}".format(self.cpu))
    def showdisk(self):
        print("硬盘的大小{}".format(self.disk))
    def showmemeory(self):
        print("内存的大小{}".format(self.memory))
    def introduce(self):
        print("""
        cpu的型号{}、
        硬盘的大小{}、
        内存的大小{}
        """.format(self.cpu,self.disk,self.memory))
        self.showcpu()
        self.showdisk()
        self.showmemeory()
c=Computer("Intel7")
c.showcpu()
c.memory="128G"
c.disk="100T"
c.showmemeory()
c.showdisk()
c.introduce()

#
# 7.	编写一个银行卡类，具有账号，人名与余额属性。编写提款机类，接收一张银行卡，并且具有存款，提款，查询余额，转账功能。
