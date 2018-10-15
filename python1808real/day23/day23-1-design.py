"""
面向对象
"""
# 一、OOD和五个原则
# 编程范式：编程规范，面向过程、面向对象、函数式编程
# 面向过程：大量函数，按顺序的调用，怎么办
# 面向对象：对象为单位，谁？谁应该有什么属性、什么行为，调用对象下的属性、行为完成需求

# OOA面向对象的分析法
# 抽象、封装、继承、分类、聚合、关联.....

# OOD面向对象的设计
# 遵从的原则达到的设计目标：可扩展、可修改、可替代

# 面向对象的设计要遵从五项原则：SOLID
# S--单一职责原则
# O--开放关闭原则
# L--里氏转换原则
# I--接口隔离原则
# D--依赖倒置原则
#（1）  S--单一职责原则
# 一个类只做一件事情。
# ATM  Card:
# Card:取钱、查询、存钱
# ATM:取钱（调用card取钱）
# class Card:
#     def __init__(self,cardid,name,balance):
#         self.id=cardid
#         self.name=name
#         self.balance=balance
#     def withdraw(self,money):
#         self.balance-=money
# class ATM:
#     def insertCard(self,card):
#         self.card=card
#     def withdraw(self,money):
#         # self.card.withdraw(money)

#（2） O--开放关闭原则
# 类、模块、函数对外扩展开放，而对于修改是关闭的。
# class Milk:
#     def __init__(self,milk):
# class MilkTea(Milk):
#     ....
# 装饰器：对函数进行扩展，但是对函数内部不进行修改

#（3）L--里氏转换原则
# 继承关系原则
# 所有引用父类（基类）地方必须能能够透明的使用其子类对象
# 子类尽量不去重写父类的方法。
# （主要属性和方法不去覆盖父类的。如果彻底违反了里氏转换原则，只能说明父子继承关系有问题）
# 父类相当于是接口规范，子类不应该去破坏父类接口规范。
# class Card:
#     pass
# class CreditCard(Card):
#     pass
# class SaveCard(Card):
#     pass
# class Teacher:
#     def __init(self,name,age):
#         pass
#     def introduce:
#         pass
#     def teach:
#         pass

# （4）I--接口隔离原则
# 最小继承原则
# 不能强迫用户去依赖那些他们不使用的接口。
# 所有子类都有的方法或者属性应该放在父类中，否则就不应该放在父类中。
# 自行车，父类自行车：ride()  GPS定位，那么所有的自行车（普通自行）都会带有GPS定位，不合理

#（5）D--依赖倒置原则
# 高层次模块不应该依赖低层次模块，两者都应该依赖抽象。
# 当有一些类作为参数传递给另一个类的时候，可以使用父类，这样子类对象也可以当做参数传入。
# class Iread:
#     def getConetent(self):
#         pass
# class Book(Iread):
#     def getContent(self):
#         print("很久很久以前....")
# class Ipad(Iread):
#     def getConetent(self):
#         print("从pad中将故事....")
# class Mag(Iread):
#     def getConetent(self):
#         print("从杂志中将故事....")
# class Mother:
#     def tellStory(self, i):
#         print("妈妈开始讲故事....")
#         i.getContent()

# m=Mother()
# b=Book()
# ma=Mag()
# m.tellStory(b)
# m.tellStory(ma)

# 二、设计模式
# 一套 被反复使用，多人知晓的代码经验的总结
# GOF四人帮 四个博士根据五个原则，在框架设计中总结出来23种设计模式。
# 大话设计模式，c++

# 分为三种类型：创建型模式、结构型模式、行为型模式
# 创建型：工厂模式、抽象工厂、单例模式、原型设计模式、建造者模式
# 结构型：适配器模式，组合模式，桥接模式、装饰模式，外观、代理模式，享元模式
# 行为型：迭代器模式，观察者模式，策略模式，访问者模式。。。。。

# 1. 创建型模式：创建者对类的实例化进行了抽象。能够把模块中的对象和创建对象进行分离，
#    对于需要创建对象他们只需要获得接口，不需要具体创建的内细节。
# （1）工厂模式
class A:
    pass
class B:
    pass
class C:
    def __init__(self,a,b):
       pass

# 调用者
a=A()
b=B()
c=C(a,b)

# 工厂模式
class A:
    pass
class B:
    pass
class C:
    def __init__(self,a,b):
       pass
class Cfactory:
    def creatC(self):
        a=A()
        b=B()
        c=C(a,b)
        return c
# 调用者
c=Cfactory()

# 工厂模式的实现：简单工厂，抽象工厂
# ①简单工厂
# class Shape:
#     def __init__(self):
#         self.brand=None
# class Circle(Shape):
#     def draw(self):
#         print("画圆形")
# class Rectangle(Shape):
#     def draw(self):
#         print("画矩形")
# class Square(Shape):
#     def draw(self):
#         print("画正方形")
#
# # circle=Circle()
# # circle.draw()
#
# # 简单工厂实现的思路：不指定某一个特定的类创建对象，而直接找工厂创建
# # 从工厂加工出来的商品可以做定制模式
# class ShapeFactory:
#     def create(self,shape_name):
#         r=None
#         if shape_name=="circle":
#             r = Circle()
#             r.brand="圆形工厂加工出来的"
#         elif shape_name=="rectangle":
#             r=Rectangle()
#         elif shape_name=="square":
#             r=Square()
#         return r
#
# # fac=ShapeFactory()
# # obj=fac.create("circle")
# # # obj=fac.create("square")
# # obj.draw()
# # print(obj.brand)
# c=Circle()
#
# print(c.brand)

# ② 工厂方法模式
# 给每一个形状都加一个工厂，大的工厂ShapeFactory下还有子工厂（圆形工厂、长方形工厂、正方形工厂）
class Shape:
    def __init__(self):
        self.brand=None
class A:
    pass
class Circle(Shape):
    def __init__(self,a):
        super().__init__()
        self.a=a

    def draw(self):
        print("画圆形")
class Rectangle(Shape):
    def draw(self):
        print("画矩形")
class Square(Shape):
    def draw(self):
        print("画正方形")


class ShapeFactory:
    def create(self):
       pass
class CircleFactory(ShapeFactory):
    def create(self):
        a=A()
        c=Circle(a)
        return c
class RectangleFacory(ShapeFactory):
    def create(self):
        c = Rectangle()
        return c
class SquareFacory(ShapeFactory):
    def create(self):
        c = Square()
        return c

cf=CircleFactory()
c=cf.create()
c.draw()

# 使用的场景：
# （1）一个类不知道创建他的对象时需要哪些其他类或者一起来创建。
# （2）一个类希望由它的子类 来指定它创建的对象。


# 2. 单例模式
# 背景：当一个类只希望有一个实例存在。比如，数据库的连接。每个库都有自己的用户名和密码
# user表
# username   password...
# yinda        123
# zhangsan     111
# select * from user where username=? and password=?
# 单例模式的特点：单例类只能有一个实例
# 单例模式的实现方式：
# python有四种模式实现单例：

# 方式一、自带的模块就单例模式
# from python1808real/day23/my   # 无论有多少个线程同时访问，都只能执行一次。
# aobj就只有一个


# 方式二、使用new方法 ，创建对象，调用类下的__new__
class Singleton:
    _instance=None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance=super().__new__(cls, *args, **kwargs)
        return cls._instance

s1=Singleton()
s2=Singleton()
print(s1 is s2)


# 方式二、使用元类
# 创建类：元类下的new 和init
# 创建对象：元类下的call，类下的new和init
class Singleton(type):
    _instance=None
    def __call__(self, *args, **kwargs):
        if not self.__class__._instance :
            self.__class__._instance=super().__call__(*args, **kwargs)
        return self.__class__._instance
class M(metaclass=Singleton):
    pass
m1=M()
m2=M()
print(m1 is m2)


# 方式四、装饰器
from functools import wraps
def Singleton(cls):
    _instance=None
    @wraps(cls)
    def inner(*args,**kwargs):
        nonlocal _instance
        if not _instance :
            _instance=cls(*args,**kwargs)
        return _instance
    return inner

@Singleton
class A:
    pass
a1=A()
a2=A()
print(a1 is a2)


# 2. 结构模式
# 解决创建对象之后，对象和对象之间的依赖关系。
# （1）适配器模式
# 解决问题：当已有功能可以使用，但是接口与调用者不匹配，需要使用适配器模式。
# 例子：5个人（类） 打篮球，其中一个人需要调用外籍球员（攻击、防卫方法跟前面4个人不一样）
class Player:
    def __init__(self,name):
        self.name=name
    def attack(self):
        print("{}进攻".format(self.name))
    def defense(self):
        print("{}防御".format(self.name))
class Forwads(Player):
    pass
class Center(Player):
    pass
class Guards(Player):
    pass

class Foreign:
    def __init__(self,name):
        self.name=name
    def foreignAttack(self):
        print("{}外籍球员进攻".format(self.name))
    def foreignDefense(self):
        print("{}外籍球员防御".format(self.name))

class Translator(Player):
    def __init__(self,name):
        super().__init__(name)
        self.foreignCenter = Foreign(self.name)

    def attack(self):
        self.foreignCenter.foreignAttack()
    def defense(self):
        self.foreignCenter.foreignDefense()


f1=Forwads("张三丰")
f2=Forwads("张四丰")
c=Center("李四")
# c=Translator("tom")
g1=Guards("王五")
g2=Guards("王六")
c.attack()
c.defense()

# 适合的场景：
# 如果希望使用一方，现存）的类，但是接口不符合需求的时候个已存在（第三