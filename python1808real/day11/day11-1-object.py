"""

第十章  面向对象的特征

二、封装、继承和多态
1、封装
"""


# 2）. propery
# 为了调用者方便调用私有成员
# 两种方式：
# （1）property函数
# （2）property装饰器


# （1）property函数
class Computer:
    def __init__(self):
        self.__memory="128g"
        self.cpu="intel5"

    def setmemory(self,memory):
        self.__memory=memory
    def getmemory(self):
        return self.__memory
    def delmemory(self):
        del self.__memory
    # 加入property函数，将私有成员使用property改名字
    #语法： 对外名字 = property(获得私有成员的方法，设置私有成员的方法，删除私有成员的方法，注释)
    # memory是 被property过的：memory是私有属性，但是已经使用propery提供了方便的调用方式
    memory= property(getmemory,setmemory,delmemory,"内存大小")
    memory= property(getmemory,setmemory,None,"注释")

c=Computer()
# print(c.getmemory())
# c.setmemory("256g")

# 使用property的变量来访问
c.memory="256g"
print(c.memory)
# del c.memory

c.cpu="intel7"
print(c.cpu)

# （2）property装饰器
# @property
# 注意：当使用 @property就要定义好要对外提供的名字是什么。
class Computer:
    def __init__(self):
        self.__memory="128g"

    # 对外提供的属性名 就是get、set、del方法的名字
    # 一般先写get方法:例如 对外提供的属性名字memory，就将get获取方法写成memory
    # 在对应get和set、del方法上加装饰器
    # 在get方法上加的装饰器： @property
    # 在set方法上加的装饰器： @对外属性名字.setter
    # 在del方法上加的装饰器： @对外属性名字.deleter
    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self,memory):
        self.__memory=memory

    @memory.deleter
    def memory(self):
        del self.__memory

    def __a(self):
        print("执行__a方法")
    def exec_a(self):
        self.__a()

c=Computer()
print(c.memory)
c.memory="256g"
print(c.memory)

# 练习：
# 1.Computer中的cpu设置成私有属性，使用property函数和装饰器提供对外的接口。
# 2.私有实例方法，在类的外部调用
# c.__a() # 不能调用
c.exec_a()


# 2.继承
# 元类是用来产生类的。
# 继承是用来继承代码（成员）的。
# （1）背景
# 需求
# java讲师  python讲师
class JavaTeacher:
    def __init__(self,name,gender,group,age):
        self.name=name
        self.gender=gender
        self.group=group
    def introduce(self):
        print("我是{}，所在的小组{}".format(self.name,self.group))

    def teach(self):
        print("打开电脑")
        print("打开eclipse")
        print("知识点讲解,java。。。。")
    def homework(self):
        pass
class PythonTeacher:
    def __init__(self, name, gender, group,age):
        self.name = name
        self.gender = gender
        self.group = group

    def introduce(self):
        print("我是{}，所在的小组{}".format(self.name, self.group))

    def teach(self):
        print("打开电脑")
        print("打开pycharm")
        print("知识点讲解,python。。。。")

# 代码冗余问题：
# 1. 写的时候冗余，读的时候不易懂
# 2. 代码的扩展性不强

# 解决方式：使用继承解决类和类之间的相似问题。

# （2）继承实现
"""
继承描述关系：
继承实现是一种【一般】与【特殊】的关系。
水果类---一般性-----父类----父类
苹果类---特殊性-----子类----扩展类、衍生类

子类应该继承父类

子类继承父类之后，父类中有的成员（属性、方法等等），子类中也有。（子承父业）
就像直接定义在子类中一样。
"""

#继承方式分为两种：显式继承、隐式继承
# 第一种范式：显式继承：
"""
语法：
class 类名(父类):
   类体
"""
class Fruit:
    def show(self):
        print("我是水果")
class Apple(Fruit):
    pass
a=Apple()
f=Fruit()
a.show()

# 第二种：隐式继承：专门指如果不写明继承父类，则默认继承object类
# A偷偷的继承object
class A:
    pass
# 新式类  经典类
# object


# (3) 继承意义
# 通过继承，可以实现代码的重用性，把公共功能或者属性提取出来方法父类中，每一个子类
# 继承父类，子类中就会具有父类的所有方法和属性，子类还可以在此基础上进行扩展。

# (4) 两个内建函数
# isintance(对象，类)：第一个参数是否属于第二个参数(包含父类)产生的
# issubclass（子类，父类）：第一个参数是否是第二个参数的子类(自己也是自己的子类)
print(isinstance(a,Apple))
print(isinstance(a,Fruit))
print(isinstance(a,object))
print(isinstance(f,object))
print(isinstance(f,Apple))

print(issubclass(Apple,Fruit))
print(issubclass(Apple,object))
print(issubclass(Fruit,object))
print(issubclass(Fruit,Fruit))

# type(a)==Apple
# type(a)==Fruit
# Apple==Fruit  错误

# 应用
class Student:
    pass
class LittleStudent(Student):
    pass
class MiddleStudnet(Student):
    pass
class BigStudent(Student):
    pass

# 判断如果是学生Student就可以去上学。
# if type(l)==LittleStudent or type(l)==MiddleStudnet or type(l)==BigStudent:
# if isinstance(l,Student)  方便
# if issubclass(type(l),Studnet)

# (5)成员的继承
# 类属性、类方法、实例属性、实例方法、静态方法 五个成员
# ① 类属性、类方法、实例方法、静态方法 的继承
# class Bike:
#     brand="飞鸽"
#     @classmethod
#     def cm(cls):
#         print("类方法")
#
#     def bybike(self):
#         print("双手扶把")
#         print("骑上自行车")
#         print("蹬....")
#
#     @staticmethod
#     def sm():
#         print("静态方法")
# class CvBike(Bike):
#     pass
# cvbike=CvBike()
# print(CvBike.brand)
# CvBike.cm()
# cvbike.bybike()
# CvBike.sm()

# ② 方法的重写（常用的是实例方法）
# 当子类继承了父类 ，子类对于父类方法不是完全适用，可以对父类方法进行重新定义
# 上述方式叫做：重写
# 重写的方式：【方法名字和参数一定都是跟父类的方法相同的】。
# 一旦子类重写了父类方法，执行子类方法的时候，就不会执行父类的相关方法，而是执行子类自己的方法。
class Bike:
    brand="飞鸽"
    @classmethod
    def cm(cls):
        print("类方法")

    def bybike(self):
        print("双手扶把")
        print("骑上自行车")
        print("蹬....")
        a="变量的赋值"

    @staticmethod
    def sm():
        print("静态方法")
# class CvBike(Bike):
#     def bybike(self):
#         print("骑上自行车")
#         print("不扶把，")
#         print("蹬....")
# cvbike=CvBike()
# print(CvBike.brand)
# CvBike.cm()
# cvbike.bybike()
# CvBike.sm()


# 重写时，在子类中调用父类的方法，语法：super().父类的方法
# super().父类方法，进行继承的时候，会将方法全部引用过来，不能只继承一部分
class CvBike(Bike):
    # 重写父类的bybike
    def bybike(self):
        print("骑上自行车")
        print("不扶把，")
        print("蹬....")
        super().bybike() # 就像使用复制，粘贴将父类的代码粘贴过来一样。
        a="变量的赋值_new"  # 将父类中定义的变量继承过来之后，可以进行修改。
        print(a)
    def go_to_school(self):
        print("上课")

cvbike=CvBike()
cvbike.bybike()
cvbike.go_to_school()

# ③实例属性的继承
# 实例属性是在__init__方法中定义
# 实际上，实例属性的继承，就相当于重写父类中的__init__方法
# class Bike:
#     def __init__(self):
#         self.color="白色"
#         self.size=28
# class CvBike(Bike):
#     def __init__(self):
#         super().__init__()  # 属性继承的时候，建议将super放在第一行
#         self.color="蓝色"  # 修改父类的属性
#         self.cv="变速器"   # 扩展父类的属性
#
# cvBike=CvBike()
# print(cvBike.color)
# print(cvBike.size)
# print(cvBike.cv)

# ④ 私有成员的继承
# 子类是允许访问父类的私有成员。
class Bike:
    def __init__(self):
        self.color="白色"
        self.__size=28
class CvBike(Bike):
    def __init__(self):
        super().__init__()  # 属性继承的时候，建议将super放在第一行
        self.color="蓝色"  # 修改父类的属性
        self.cv="变速器"   # 扩展父类的属性


cvBike=CvBike()
print(cvBike.color)
# print(cvBike._Bike__size)# 如果访问真实名字，也可以访问到，但是不建议这样写。
print(cvBike.cv)

# （6） 多重继承
# 一个子类可以继承多个父类
# 多个父类使用,分隔
# 正方形是特殊的矩形，特殊菱形
class Rectangle:
    def area(self):
        print("矩形求面积")
    def a(self):
        pass
class Diamond:
    def area(self):
        print("菱形求面积")
        # super().area()  # 当前方法找不到的时候，也会按照mro原则找到矩形的area方法
    def b(self):
        pass
class Square(Rectangle,Diamond):
    def t(self):
        # self.area()
        Diamond.area(self)
s=Square()
s.t()


# 继承原则 MRO原则：继承的顺序
# 如果多个父类中的方法和属性都不同名，一般不需要查看MRO原则
# 如果多个父类中出现重名的方法或者属性，才需要按MRO搜索具体继承的是那个属性或者方法。

# 对于树形结构的两种遍历方法：
# 深度优先
# 广度优先

"""
python2.2 之前的版本，经典类方式实现类。
class A(object):
MRO：深度优先

python2.3--python2.7 : 经典类和新式类并存
2.3
新式类： MRO广度优先
经典类： MRO深度优先

2.3-2.7，C3算法
C3分为两种情况：一种有统一父类的情况，另一种无统一父类的情况


python3 ,类只有新式类：不写(object)也默认继承object
使用C3算法：
分为：
有统一父类（环状结构）：一直深度优先到查看到有统一父类，变为广度优先。
没有统一父类（非环状结构）：深度优先
# 练习一
"""
# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
# class D(A,B):
#     pass
# class E(C,D):
#     pass
# print(E.mro())


# 练习二
# class F:
#     pass
# class E:
#     pass
# class D:
#     pass
# class C(D,F):
#     pass
# class B(E,D):
#     pass
# class A(B,C):
#     pass
# print(A.mro())

# 如果有多个父类，多个父类又有相同的方法，比如area方法，
# 如果非要想继承菱形的area，这么办？
# 1. 菱形写在继承的第一个位置  (推荐)
# 2. 可以使用   父类.实例方法  （可以做到，但是属于 类.实例方法  ----并不好）

# 实现之前背景
class Teacher:
    def __init__(self,name,gender,group):
        self.name=name
        self.gender=gender
        self.group=group
    def introduce(self):
        print("我是{}，所在的小组{}".format(self.name,self.group))

    #告诉其他的继承子类，需要实现teach方法。属于定义的一种规范。
    def teach(self):
        pass

# class PythonTeacher(Teacher):
#     def teach(self):
#         print("打开电脑")
#         print("打开pycharm")
#         print("python")
# class JavaTeacher(Teacher):
#     def teach(self):
#         print("打开电脑")
#         print("打开Eclipse")
#         print("java")
#
# class PHPTeacher(Teacher):
#     def TEACH(self):
#         print("打开电脑")
#         print("打开Eclipse")
#         print("java")


# 3.多态
# 在运行和编译的时候，参数或者对象的多种形态。
# python是鸭子类型的 语言   动态  强类型，多态体现的特别不明显。
# 体现明显的java语言
class Father:
    pass
class Son(Father):
    pass

# 多态对象
# Father f=Father()
# Son s=Son()
# Son s_new=Father()

# 多态参数
# class A:
#     def talk(self,Father father):
#         pass
# a=A()
# a.talk(s)


# 对于已有内置方法len
len("str")
len([1,2,3])
len((1,2,3))
# f=Father()
# len(f)


# 自定义Animal类，有run方法
# 子类Cat  Dog
class Animal:
    def run(self):
        pass
class Cat(Animal):
    def run(self):
        print("猫在跑步")
class Dog(Animal):
    def run(self):
        print("狗在跑步")
class Bug:
    def run(self):
        print("虫子在跑步")
def run(a):
    a.run()
cat=Cat()
dog=Dog()
bug=Bug()
run(cat)
run(dog)
run(bug)



#追击敌人的狗，查毒品的狗
# 假如没有多态的时候：
class ArmyDog:
    def bit_enmey(self):
        print("袭击敌人")
class DrugDog:
    def track_dugs(self):
        print("追查毒品")
class Person:
    def work_with_army(self,dog):
        dog.bit_enmey()
    def work_with_drug(self,dog):
        dog.track_dugs()
p=Person()
p.work_with_army(ArmyDog())
p.work_with_drug(DrugDog())


#
class Dog:
    def work(self):
        pass
class ArmyDog(Dog):
    def work(self):
        print("袭击敌人")
class DrugDog(Dog):
    def work(self):
        print("追查毒品")

class Person:
    def work_with_dog(self,dog):
        dog.work()
p=Person()
p.work_with_dog(ArmyDog())
p.work_with_dog(DrugDog())

