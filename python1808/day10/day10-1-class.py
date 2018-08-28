"""
第九章 类和对象
背景：我们原来学是基础数据类型无法存储复杂类型的数据
比如，一个学生，姓名，年龄，班级，性别。。。 跑步、上课。。。
"""
score=90.0       # float
name="tom"       # str
scores=[100,50]  # list
d={"tom":100}    # dict

print(type(score))




# 一、基本概念
# 1. 什么是对象
# 万物皆对象，对象是具有行为和属性的。
# 桌子：4个腿，颜色，大小——属性
# 小猫：颜色，类型——属性，叫、吃饭、睡觉——行为


# 不同的对象具有不同的属性

# 2. 什么是类？
# 一个类别，按照需求划分，把具有相同属性和行为的对象划分成一类。
# 学籍管理系统：Student  Teacher
# 公交管理系统:Person Bus....

# 划分的是，一般来说相同类别的对象之间总是比不同类别之间的对象更加相似。

# 3. 类和对象之间的关系
# 类是对象的抽象，对象是类的具体表现
# 类——模板、蓝图
# 对象--模板或者蓝图设计出来的实例。
# 对象==实例

# 汽车管理系统：车---宝马、奥迪——————对象
# Car：属性brand，color————————————类

# 宏观，大：
# 动物园：Animal类
# 狮子、老虎  对象

# 微观，小：
#Lion：非洲狮、亚洲狮子。。。。



# 二、类的定义
# 1. 语法
"""
class 类名:
   类体（属性、行为）# 一共有5个成员，今天讲的是实例属性和实例方法
"""
class Person:
    '注释'
    pass

# 类产生（创建）（new）对象——object
# 语法：类名()
p1=Person()
print(p1)
print(p1.__doc__)
print(type(p1))

# 2. 在类中定义对象的属性和行为
# 在实际的开发中，需求分析会先从对象开始，会按照业务需求将对象划分成类。
# 实际编码中，会创建类（类是用来创建对象）
# 类中要具有对象的关键元素（属性、行为）

"""
属性：使用变量赋值   名词
行为：使用函数来进行行为的实现  动词
"""
# （1） 在类中定义行为（类中的方法，类中的函数）
class Person:
    '注释'
    # 在类下定义的实例方法有一个特点：每一个实例方法的第一个参数必须是self（python）
    # self:代表当前的对象
    def run(self):
        print("正在跑步~~~")
# className  class_name
# 调用类中定义的实例方法（行为）、属性：必须通过实例（对象）来调用（self）
# p1=Person()
# # 调用的时候不需要给self参数赋值
# p1.run()
#
# p2=Person()
# p2.run()

# 建议不要这样做
# p1=Person()
# Person.run(p1)

# 需求：有很多的学生对象，学生都可以选课 ，学生都可以上课
class Student:
    def choose_course(self):
        print("正在选课")
    def classing(self):
        print("正在上课")

#访问实例方法和实例属性都需要先有实例（对象）
s1=Student()
s1.choose_course()
s1.classing()



# （2）.在类下定义实例属性
# 实例属性需要通过__init__方法来进行赋值。 __init__方法会在对象创建的时候被自动调用。
# 为什么在方法中进行赋值？ 因为在方法下赋值才是实例属性

# 尽量不要使用自定义的实例方法初始化实例属性：
# 原因：1.需要通过手工调用自定一定方法才可以对属性赋值
#       2.将属性分散到其他的方法，不直接定义在init中，代码的可读性差
class Person:
    def __init__(self,name,age): # name和age强依赖关系
        print("__init__方法执行")
        # 对实例属性进行赋值 ：格式   self.名字=值
        # 如果当前的属性是变化的，需要使用参数赋值的形式来对属性赋值
        # 如果当前的属性一成不变，可以直接赋予具体的值。
        # self.name="张三"
        # self.age=20
        self.name=name
        self.age=age
        self.city=None  #弱依赖关系
        self.place=None

    # 自己写实例方法实例化属性
    def setGender(self,gender):
        self.gender=gender

    # def run(self,place):
    def run(self):
        # print("正在跑步")
        # 在实例行为（方法）中访问实例属性。通过self
        # place是普通的参数
        # self.name和self.age都是实例属性
        print("{}-{}正在{}跑步".format(self.name,self.age,self.place))
    def on_duty(self):
        print("正{}在上班....".format(self.place))

p1=Person("张三",20)
# p1.setGender("男")
# p1.city="北京"
# #访问实例下的属性
# # print(p1.name,p1.age)
# print(p1.gender,p1.city)
# p1.run("操场上")
p1.place="操场上"
p1.run()
p1.place="立水桥"
p1.on_duty()



p2=Person("李四",30)
# print(p2.name,p2.age)
# p2.run("公路上")



# 练习：
"""
1. 创建一个狗的类
2. 狗的属性：name，age，type
3. 狗的行为：吃饭（可以显示某一个牌子的狗粮）、睡觉、叫（能够显示狗的名字狗的年龄）
4. 小狗交朋友的方法 两只小狗交朋友
"""
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.type=None
        self.dog3=None
    def setDog2(self,dog2):
        self.dog3=dog2
    def eating(self,brand):
        print("正在吃{}的狗粮".format(brand))
    def sleep(self,type):
        self.type=type
        print("{}类型的小狗正在睡觉".format(type))
        print("{}类型的小狗正在睡觉".format(self.type))
    def spark(self):
        print("{}-{}正在汪汪叫".format(self.name,self.age))
    def makefriend(self,dog2):
        print("{}-{}和{}-{}交朋友".format(self.name,self.age,dog2.name,dog2.age))
    # def makefriend(self,dog2name,dog2age):
    #     print("{}-{}和{}-{}交朋友".format(self.name,self.age,dog2name,dog2age))
    def bb(self):
        print()

dog1=Dog("中华小神犬",5)
dog1.eating("A牌子")
dog1.sleep("金毛")
dog1.spark()

print(dog1.type)
dog1.type="金毛"
print("这只小狗的类型{}".format(dog1.type))

dog2=Dog("旺财",2)
dog1.makefriend(dog2)
# dog1.makefriend(dog2.name,dog2.age)
# 无论是大对象（自定义的对象）还是小对象（字符串、列表、数值），都可以当做参数传递。
