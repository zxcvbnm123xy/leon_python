# 1.编写一个银行卡类，具有账号，人名与余额属性。
# 编写提款机类，接收一张银行卡，并且具有存款，提款，查询余额，转账功能。
"""
1. 类的创建，对象的创建，实例属性和实例方法的调用
2. 类和类之间的沟通： 类和其他的数据类型之间可以用参数，和其他类之间依然可以使用参数沟通
有三种方式：A类 和B类
（1）通过参数的传递（适合 B类跟A 类的方法没有太多联系，只使用一次 ）
（2）通过实例方法，将B类设置成A 类的属性  （适合B类跟A类有一定的关系，但是不是强依赖）
（3）通过__init__方法，将B类设置成A类的属性（适合A类必须由B类产生。）
"""
# 比如字符串已经不能满足【地点】数据的复杂度
# 操场1000米草地
# 操场22000米塑胶
# 操场10000千米塑胶
class Place:
    def __init__(self,name,len,type):
        self.name=name
        self.len=len
        self.type=type
    def __str__(self):
        return "{}-{}-{}".format(self.name,self.len,self.type)
p1=Place("操场","1000米","草地")
p2=Place("操场2","2000米","塑胶")
p3=Place("操场","10000千米","塑胶")
class Person:
    def __init__(self,name):
        self.name=name
    def run(self,place):
        print("{}正在{}跑步".format(self.name,place))

person1=Person("张三")

# 在调用run方法的时候，传入字符串类型 str
person1.run("操场")
person1.run(p1)
# 方式一，都写在Card一个类中：
# class Card:
#     def __init__(self,id,name,balance=0):
#         self.id=id
#         self.name=name
#         self.balance=balance
#     def deposit(self,money):
#         print("您可以执行存款操作：",end="")
#         self.balance+=money
#         print("已经存入了{}".format(money))
#         self.query()
#     def withdraw(self,money):
#         print("您可以执行取款操作：",end="")
#         if money<=self.balance:
#             self.balance-=money
#             print("已取款{}".format(money))
#             self.query()
#         else:
#             print("余额不足")
#     def query(self):
#         print("{}，您好，您当前余额是{}元".format(self.name,self.balance))
#     def transfer(self,otherCard,money):
#         #编程语言里：无法通过某个属性值，查找到对应对象
#         # 转出：
#         if money <= self.balance:
#             self.balance-=money
#             # 转入
#             otherCard.balance+=money
#         else:
#             print("余额不足")
#         print("已成功向（{}）{}转账{}".format(otherCard.id,otherCard.name,money))
#         self.query()
#
# # 创建对象
# card1=Card(10001,"张三")
# card1.query()
# card1.deposit(1000)
# card1.withdraw(100)
# card1.withdraw(1000)
#
# card2=Card(10002,"李四",20)
# card1.transfer(card2,100)
# card2.query()


# 方式二，提取出存款，取款、查询、转账都在ATM类中
class ATM:
    def __init__(self):
        self.card=None
    def insertCard(self,card):
        self.card=card
        print("您已插入卡片！")
    def deposit(self, money):
        print("您可以执行存款操作：", end="")
        self.card.balance += money
        print("已经存入了{}".format(money))
        print("{}，您好，您当前余额是{}元".format(self.card.name ,self.card.balance))

    def withdraw(self, money):
        print("您可以执行取款操作：",end="")
        if money<=self.card.balance:
            self.card.balance-=money
            print("已取款{}".format(money))
            self.query()
        else:
            print("余额不足")

    def query(self):
        print("{}，您好，您当前余额是{}元".format(self.card.name,self.card.balance))

    def transfer(self, otherCard, money):
        # 转出：
        if money <= self.card.balance:
            self.card.balance-=money
            # 转入
            otherCard.balance+=money
        else:
            print("余额不足")
        print("已成功向（{}）{}转账{}".format(otherCard.id,otherCard.name,money))
        self.query()


class Card:
    def __init__(self,id,name,balance=0):
        self.id=id
        self.name=name
        self.balance=balance

card1=Card(10001,"张三")
card2=Card(10002,"李四",10)
atm=ATM()
atm.insertCard(card1)
atm.deposit(1000)
atm.withdraw(50)
atm.transfer(card2,500)

atm.insertCard(card2)
atm.query()





#
#
# 2.编写一个计数器，能够记录一个类创建了多少个对象。
# 创建对象的数字记录在哪里？类属性、实例属性——类属性，是所有对象共享数字
# 创建对象的时候调用的方法： __new__   __init
class Counter:
    count=0
    # 方式一
    # def __new__(cls, *args, **kwargs):
    #     # 修改类属性
    #     # print(cls is Counter)
    #     cls.count+=1
    #     print("创建了第{}个对象".format(cls.count))
    #     return super().__new__(cls)

    # 方式二：
    def __init__(self):
        # Counter.count+=1
        self.__class__.count+=1
        print("创建了第{}个对象".format(self.__class__.count))

c1=Counter()
c2=Counter()
c3=Counter()
print(Counter.count)



#
# 3.编写程序，设计单张扑克牌类Card，具有花色，牌面与具体值。
# 同时设计整副扑克牌类Cards，具有52张牌。
import random
class Card:
     def __init__(self,type,value,real_value):
         self.type=type
         self.value=value
         self.real_value=real_value
     def __str__(self):
         return "{}{}".format(self.type,self.value)
# [card1,card2,...card52]
class Cards:
    def __init__(self):
        self.cards_list=[]
        self.li=[]
        # ♠♥♦♣
        # 2345678910JQKA
        li_value=list(range(2,11))+list("JQKA")
        # print(li_value)
        for i in "♠♥♦♣":
            for index,j in enumerate(li_value):
                self.cards_list.append(Card(i,j,index))
        # print(self.cards_list)
        # for i in self.cards_list:
        #     print(i)
    def sample(self):
        # li=[card1,card2,card3]
        for i in range(3):
            index=random.randint(0,len(self.cards_list)-1)
            self.li.append(self.cards_list.pop(index))
            # 删除刚刚抽取的牌
            # del self.cards_list[index]
    def compare(self):
        self.li.sort(key=lambda k:k.real_value)
        for i in self.li:
            print(i,end="")
        print()
        if self.li[0].value==self.li[1].value==self.li[2].value:
            print("三条")
        elif self.li[0].value==self.li[1].value or self.li[1].value==self.li[2].value :
            print("一对")
        elif self.li[0].type==self.li[1].type==self.li[2].type and \
            self.li[0].real_value+2==self.li[1].real_value+1==self.li[2].real_value:
            print("同花顺")
        elif self.li[0].type==self.li[1].type==self.li[2].type :
            print("同花")
        elif self.li[0].real_value+2==self.li[1].real_value+1==self.li[2].real_value:
            print("顺子")
        else:
            print("散牌")




cards=Cards()
cards.sample()
cards.compare()


# ????  A2345678910JQK
#
# 设计一个发牌的函数，可以任意发出三张牌。
# 对任意三张牌断定牌的类型。
# 类型包括：
# 三条：三张牌value一样
# 一对：两张value一样
# 顺子：三张牌挨着
# 同花：三张牌type一样
# 同花顺：挨着，类型一样
# 其余都是散牌
