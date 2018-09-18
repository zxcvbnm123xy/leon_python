"""
第九章 类和对象
"""
# 一 、基本概念
# 1. 对象
# 对象（实例）：万物皆对象。对象具有属性和行为。
# 属性： 名词
# 行为： 动词
# 行为和属性都是用来描述对象的。

# 学生管理系统：查看成绩功能
# 学生1、学生2，成绩1，成绩2，课程1，课程2.。。
# 学生类、成绩类、课程类
# Student:id, name ,class,gender ,birday  ,  findScore()
# Score: id, stuid, courseid, score
# Course: id, name ,credit


# 2. 类
# 一个类别：按照需求划分，将具有相同属性（名）和行为的对象划分成一个类别。
# 学生：张三（名字，2个眼睛，睡觉）、李四（名字，眼睛，睡觉）、王五（名字，眼睛，睡觉）
# 编码的时候一个类别就是一个class

# 学生类别---统招学生、定向学生
# 注意：划分的时候，相同类别的对象之间总是比不同类别的对象之间更相似。

# 3. 类和对象之间的关系
# 类是对象的抽象，对象是类的具体表现
# 类----模板、蓝图
# 对象--根据模板和蓝图设计出来的具体实例

# 二、类的定义
# 1. 语法：
"""
class 类名:  
   类体(类的成员)
类名是标识符：字母数字下划线组成，不能用数字开头。习惯上说首字母大写。
"""
# 定义一个人的类
class Person:
    '注释'
    pass

# 使用类产生对象
# 语法：对象名=类名([参数])  # [参数]取决于init方法中的参数
p1=Person()
print(p1)
print(p1.__doc__)
print(Person(),"匿名对象")

a="hello"  # 相当于调用了str()
print(type(a))
li=[1,2,3]
print(type(list()))

# 自定义的类跟已有的数据类型之间的关系：
# 已有的数据类型（int,str,list,tuple,set,dict）也是由类产生的，只不过创建对象的方式不太一样。
# 自定义类解决问题：复杂的数据类型



# 2. 动态属性和方法
# 类是产生对象，对象是由类产生
# 属性和行为必须存在在类中。
# 属性：变量赋值的形式 例如：a=1  name="张三"
# 行为：函数定义的方式 例如：def run():pass
# 函数--方法
# 一般把类中的函数称为方法、行为

# （1）动态的属性
# 语法：对象名.属性名=属性值
class Person:
    '注释'
    pass
p1=Person()
p1.name="张三"
#调用属性：对象名.属性名（属性名必须存在，如果不存在会报错）
print(p1.name)
# print(p1.name1)

# 动态创建的属性只对当前的对象有效，对其他的对象无效。
# p2=Person()
# print(p2.name)

# (2) 定义动态的行为
# 行为是以函数的模式存在的
# 要求：函数有self参数。
# self:代表当前对象
def run(self):
    print("正在跑步")
# 调用动态方法：对象名.方法名=函数名
p1.run1=run
p1.run1(p1)
# 动态创建的方法也只对当前的对象有效，对其他的对象无效。
p2=Person()
# p2.run1(p2)



# 动态属性和方法的局限：
# 每个对象都要单独赋予才可以，其他对象不赋予就没有对应属性和方法。

# 3.在类中定义属性和行为（实例属性和实例方法）
# 位置：在类的内部

# 属性：变量赋值的方式：需要通过__init__方法实现。
# 行为：通过函数定义的方式：实例方法中必须要有self参数，而且位置是第一个

# （1）在类中定义方法（实例方法）
class Person:
    def run(self):
        print("正在跑步")
    def walk(self):
        pass
#调用实例方法：
# 第一步：先有对象
# 第二步：对象.方法名（参数除了self以外的其他参数需要传递）
p1=Person()
p1.run()
print("====")
p2=Person()
p2.run()

#（2）在类中定义属性（实例属性）
# 语法：
"""
定义：
在init方法中
self.属性名=属性值

调用：
对象名.属性名

#说明：一般实例属性都在init方法中进行创建，目的是让代码的可读性增加
"""
class Person:
    def __init__(self,name,age): # 对于每个类创建之后都自带的方法，当创建对象的时候，会被调用
        print("执行init方法")
        self.name=name
        self.age=age

    def run(self):
        print("正在跑步")

p1=Person("张三",20)
print("Person类产生的对象p1的属性name={}".format(p1.name))
print("Person类产生的对象p1的属性age={}".format(p1.age))

p2=Person("李四",30)
print("Person类产生的对象p2的属性name={}".format(p2.name))
print("Person类产生的对象p2的属性age={}".format(p2.age))

"""
练习：
1.定义个学生类
2. 学生的属性：名字，生日，性别
3. 学生的行为：上课、下课、玩
"""


# 在实例方法中访问实例属性：
class Person:
    def __init__(self,name,age): # 对于每个类创建之后都自带的方法，当创建对象的时候，会被调用
        print("执行init方法")
        self.name=name
        self.age=age

    def run(self,place):
        print("{}-{}正在{}跑步".format(self.name,self.age,place))
        # place是参数  self.name是属性
p1=Person("张三",20)
p1.run("操场")
p1.run("公路")



# 三、类的成员
# 包含：实例属性、实例方法、类属性、类方法、静态方法
# 1.类属性
# 类属性和实例属性的区别：
#   类属性：在类中定义的属性，类属性跟具体的实例无关，只跟当前类有关系
#   实例属性：跟具体实例相关。每个实例的实例属性值都不同。

# 类属性的定义：在类的内部定义，以变量赋值的形式定义。
class Person:
    # 类属性
    desc="人的描述"
    def __init__(self,name,age):
        # 实例属性
        self.name=name
        self.age=age
    def run(self,place):
        print("{}-{}正在{}跑步".format(self.name,self.age,place))

# 类属性的访问： 有两种形式：
# 可以通过对象访问：对象名.类属性名（是只读的）
# 可以通过类名访问：类名.类属性名(推荐使用)
p1=Person("张三",20)
print(p1.desc)
p1.desc="人的描述_new"  # 不通过【对象.类属性名】对类属性进行修改，只能给对象新创建一个动态属性
print(p1.desc,Person.desc)
p2=Person("李四",30)
print(p2.desc)

# 2.类方法
# 类方法和实例方法的区别：
# 类方法：类的方法，跟具体的实例没有关系
# 实例方法：每个实例的方法
# 类方法的定义: 在类的内部定义函数，在函数的上方@classmethod，使用固定的参数cls（当前类）
class Person:
    # 类属性
    desc="人的描述"
    def __init__(self,name):
        # 实例属性
        self.name=name
    def run(self):
        print("{}正在跑步".format(self.name))

    # 类方法
    @classmethod
    def copy(cls,p):
        print("这是类方法")
        return Person(p.name)
# 类方法的调用：
# 可以通过对象:对象名.类方法名
# 类调用      ：类名.类方法名(推荐)
p1=Person("张三")
# p1.copy()
p2=Person.copy(p1)
print(p2.name,"通过copy方法复制的p2")


# 实例方法的调用：
# 对象名.实例方法
p1.run()  #self不需要传入

# 类名调用实例方法 # 基本不使用。显示的传入p1对象
Person.run(p1)

# 3.静态方法
# 静态方法跟类没关系，跟实例也没有关系
# 定义静态方法 @staticmethod
class Person:
    # 类属性
    desc="人的描述"
    def __init__(self,name):
        # 实例属性
        self.name=name
    # 实例方法
    def run(self):
        print("{}正在跑步".format(self.name))
    # 类方法
    @classmethod
    def copy(cls):
        print("这是类方法")
    #静态方法
    @staticmethod
    def sm():
        print("这是静态方法")
    @staticmethod
    def makefriend(p1,p2):
        print("{}和{}交朋友".format(p1.name,p2.name))
# 静态方法的调用 使用类名调用静态方法
# 对象名.静态方法名
# 类名. 静态方法名 （推荐）
p1=Person("张三")
p2=Person("李四")
p1.sm()
Person.sm()
Person.makefriend(p1,p2)

# 类和实例的选择
# 类属性：当属性跟具体的实例没有关系，所有的实例共享同一个属性。
# 实例属性：当属性值跟具体的实例相关。是每个实例独有的属性。

# 类方法、实例方法、静态方法：
# 如果定义的方法是对实例进行操作的，那么设计成实例方法，参数self
# 如果定义的方法跟具体的对象没什么关系，操作的是类属性，那么定义成类方法，参数cls
# 既不操作类属性、也不操作实例属性，选择使用静态方法。不指定固定参数

# 所有的方法都是为属性服务

# 四、在方法中访问属性
# 1.实例方法中访问类属性
class Person1:
    # 类属性
    descc="人的描述"
    def __init__(self,name):
        # 实例属性
        self.name=name
    # 实例方法
    def run(self):
        print("{}正在跑步".format(self.name))
        #实例方法中访问类属性
        # 对象名.类属性名，类名.类属性名
        print("实例方法中访问类属性:",self.descc) # 不推荐使用
        # print("实例方法中访问类属性:",Person.descc) # 会硬编码的影响
        #self.__class__当前对象所属的类
        print("实例方法中访问类属性:",self.__class__.descc) # 推荐

    # 类方法
    @classmethod
    def copy(cls):
        print("这是类方法")
p1=Person1("张三")
p1.run()



# 2.实例方法中访问实例属性
# 对象名.实例属性名，
# 类名.实例属性（错误）
class Person:
    # 类属性
    descc="人的描述"
    def __init__(self,name):
        # 实例属性
        self.name=name
    # 实例方法
    def run(self):
        print("{}正在跑步".format(self.name))
        #实例方法中访问实例属性
        # 对象名.实例属性名，   类名.实例属性（错误）
        print("实例方法中访问实例属性:",self.name)
    # 类方法
    @classmethod
    def copy(cls):
        print("这是类方法")
# print(Person.name)
p1=Person("张三")
p1.run()



# 3.类方法中访问类属性
# cls.类属性名
class Person:
    # 类属性
    descc="人的描述"
    def __init__(self,name):
        # 实例属性
        self.name=name
    # 类方法
    @classmethod
    def copy(cls):
        print("这是类方法")
        print("类方法中访问类属性：",cls.descc)
        print("类方法中访问类属性：",Person.descc)
Person.copy()


# 4.类方法中访问实例属性
# cls.类属性名
# 类方法跟具体实例无关。
# 不合理
class Person:
    # 类属性
    descc="人的描述"
    def __init__(self,name):
        # 实例属性
        self.name=name
    # 类方法
    @classmethod
    def copy(cls,p1):
        print("这是类方法")
        print("类方法中访问实例属性：",p1.name)
p1=Person("张三")
Person.copy(p1)


# 五、魔法方法
# 在python中定义了一些列的特殊方法，格式__xx__ 命名——魔法方法
# 普通的方法都需要函数的调用 函数名(参数)，函数才能执行
# 魔法方法：不需要主动调用，当符合一定条件的时候，会自动调用。
# 1. __new__
# 在创建对象的时候，用来创建对象的方法
# 是一个静态方法。
# 必须要有return，才可能够执行init方法
# object
# class Person:
#     def __new__(cls, *args, **kwargs):
#         print("new方法执行")
#         #super()是用来调用父类下的方法
#         return super().__new__(cls) # 真正创建的方法
#
#     def __init__(self,name):
#         self.name=name
#         print("执行init方法")
#
# p1=Person("张三")

# 2. __init__: 实例方法
# 是在使用__new__创建对象之后，调用__init__进行初始化的方法

# 3.__del__(self): 当销毁对象的时候，会调用这个方法
# class Person:
#     def __new__(cls, *args, **kwargs):
#         print("new方法执行")
#         # super()是用来调用父类下的方法
#         return super().__new__(cls)  # 真正创建的方法
#
#     def __init__(self, name):
#         self.name = name
#         print("执行init方法")
#     def __del__(self):  # 在垃圾回收机制的时候，对对象进行销毁
#         print("执行了del方法")
# p1 = Person("张三")
# p2=p1
# del p1 # 只是删除了p1的名字
# print("没有被销毁")
#


# 4.__str__(self)
# 当调用了内建函数str   format  print时候，会自动调用的方法
# 返回值就是字符串
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         print("执行了str方法")
#         # return "当前对象来源于{}类，id={}".format(self.__class__,id(self))
#         return "当前对象来源于{}类，id={},name={}".format(self.__class__,id(self),self.name)
#     def __repr__(self):
#         return "success"
# p=Person("张三")
# print(p)
# <main.Person  内存>

# 5. repr(self)
# 是针对解释器：当__str__方法不存在的时候，会自动调用repr方法


# 6.__bytes__(self):
# 当bytes()方法会自动调用的方法，方法返回值是字节类型
class Person:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        print("执行了str方法")
        # return "当前对象来源于{}类，id={}".format(self.__class__,id(self))
        return "当前对象来源于{}类，id={},name={}".format(self.__class__,id(self),self.name)
    def __bytes__(self):
        print("执行了bytes方法")
        return b"success"
p=Person("张三")
print(bytes(p))

# 7. __call__(self):
# 将对象当函数一样调用
# 对象名()
class   Person:
    def  __call__(self, *args, **kwargs):
        print("执行了call方法")
p=Person()
p()



# 六、动态属性操作
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
p=Person("张三",20,"man")
# 当创建一个属性的时候，不知道名字————动态属性
# 1.hasattr(obj,name): 判断对象obj中是否存在name指定的属性名。有True 否则False
p.a="aaaa"
print(hasattr(p,"age"))
print(hasattr(p,"a"))

# 2.setattr(obj,name,value)
# 将object对象的name属性设置为value
setattr(p,"bbb","bbbbbbbbbbbbbbbbbb")
print(p.bbb)
p.dog="小狗"
n=input("请输入一个属性名")
v=input("请输入一个属性值")
setattr(p,n,v)
print(hasattr(p,n))

# 3.getattr(obj,name)
#返回obj对象中name的属性值
print(getattr(p,n))
print(getattr(p,"name"))
print(getattr(p,"age"))

# 4.delattr(obj,name)
# 删除obj对象中name的属性
delattr(p,n)
# print(getattr(p,n))


