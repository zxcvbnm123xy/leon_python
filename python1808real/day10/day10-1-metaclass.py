"""
第九章
七、元编程
# 编写程序，能够操纵或者改变其他程序

元类  ---- 类-----对象
"""
# 一、元类
# 类可以创建对象
# 类算不算对象？ 被赋值？被传递？被返回？
# 答案：可以
# 类也是对象
# 赋值
class Person:
    pass
P=Person
print(P())

# 当参数
def fun(person):
    pass
fun(Person)

# 返回值
def fun():
    return Person
fun()

# list是列表的类
# 显示一个对象类？type（object）
print(type(list()))  #list
print(type(list)) # type
print(type(str))
print(type(Person))# type

# 对象是由类产生，类是由元类产生的
# type产生的类，type就是元类：元类就是创建类的类。
print(type(type))  #type 是一切的基础，用来产生类，产生type，包括自己


# 1. type
# type有两种用法
# (1)type(object):返回当前对象的类型
li=[1,2,3]
print(type(li))  #list
# (2)充当元类，创建一个类
class Person:
    desc="人的描述"
    def __init__(self,name):
        self.name=name
    def run(self):
        pass
# 直接使用type创建类的语法：
# type(类名（字符串），继承的父类（元组）,类关联的属性和方法（字典）)
#实例方法
def a(self,name):
    self.name=name
#类方法
@classmethod
def cm(cls):
    return "类方法的返回值"
def sm():
    return "静态方法的返回值"
Person1=type("Person2",(),{"desc":"人的描述","__init__":a,"cm1":cm,"sm1":sm})
print(type(Person1))
p1=Person1("张三")
print(p1)
print(Person1.desc)
print(Person1.cm1())
print(p1.name)
print(Person1.sm1())

# 2.自定义元类
# 继承：借助原来type的内容，扩充自己的内容
# （1）继承type
# class 元类名(继承的类type):
#     pass
#  (2) 怎么调用自定义元类来创建自己的类？
# class 类名(metaclass=元类名)：
#    PASS
##metaclass的默认值是type
# class Person(继承的类,metaclass=type):
#     pass
# 元类是用来创建类的
# __new__方法是用来创建对象（类）
# 实例：自定义元类
# class ModelMetaClass(type):
#     def __new__(cls, *args, **kwargs):
#         print("我是新的元类！！！！")
#         return super().__new__(cls, *args, **kwargs)
# class A(metaclass=ModelMetaClass):
#     pass

# 3.三个特殊的魔法方法
# 1). __new__: 创建对象，静态方法
# 2). __init__：在new执行之后，用来初始化
# 3). __call__：把对象当函数一样调用
# class Person:
#     def __call__(self, *args, **kwargs):
#         print("调用Person的call方法")
# p1=Person()  # 调用的是谁的call方法？type的__call__方法
# p1()#  调用的是Person的call方法

class ModelMetaClass(type):
    def __new__(cls, *args, **kwargs):
        print("元类的new方法执行")
        return super().__new__(cls, *args, **kwargs)
    def __init__(self,*args,**kwargs):
        print("元类的init方法执行")
        super().__init__(*args,**kwargs)
    def __call__(self, *args, **kwargs):
        print("元类的call方法")
        return super().__call__(*args, **kwargs)
class A(metaclass=ModelMetaClass):
    def __new__(cls, *args, **kwargs):
        print("A类的new方法")
        return super().__new__(cls)
    def __init__(self, *args, **kwargs):
        print("A类的init方法")
        super().__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        print("A类下的call方法")
    def fun(self):
        print("fun方法执行")

"""
ModelMetaClass 爷爷
A    父亲
a    儿子
1. 当定义了元类ModelMetaClass之后，只要定义一个类A使用了这个元类创建，就会调用元类下
  的new方法和init方法（无论这个A类有没有产生对象）
2. 当使用这个A类创建对象a的时候，会先调用元类ModelMetaClass下的call来进行对象的创建A()，
  接着调用A类下new方法和init方法
3. 当调用a()，会调用A类下的call方法
4. 当调用a下的实例方法时，不会调用任何new init 或者call，只调用自己的实例方法。

# 一个对象（A类下的a）的需要有哪些方法执行？
（1）元类下的call
（2）类下的new方法
（3）类下的init方法
"""
a=A()
a()
a.fun()

# object（继承，只是为了减少代码冗余）      type(真正用来创建对象（类）)
# type是object的子n类，但是object是type创建的。
# issubclass(子类，父类)#
print(issubclass(type,object))
print(type(object))


# 二、元类的应用
# 元编程都是设计层面的知识
# 所有的类总是会直接或者间接的继承object
from datetime import datetime
class ModelMetaclass(type):
    """
    name:  使用元类ModelMetaclass创建的类类名
    bases：使用元类ModelMetaclass创建的类需要继承哪些父类（元组）
    attrs: 使用元类ModelMetaclass创建的类下的属性和方法（字典）
    """
    def __new__(cls, name,bases,attrs):
        attrs["a"]=123456
        attrs["time"]=datetime.now()
        for k,v in attrs.items():
            print(k,v)
        return super().__new__(cls,name,bases,attrs)
class A(metaclass=ModelMetaclass):
    pass
class B(metaclass=ModelMetaclass):
    pass

# 1. 创建元类，使得使用这个元类创建的类不能够实例化对象：抽象类(只能用来被继承，不能用来实例化对象)。
# class Card:
#     pass
# class CreditCard(Card):
#     pass
# class SaveCard(Card):
#     pass
class NoIntance(type):
    def __call__(self, *args, **kwargs):
        # # assert 1>2,"不能创建对象"
        raise ValueError("不能创建对象")  # 专门用来主动抛出异常


# class Card(metaclass=NoIntance):
#     pass
# c=Card()


# 2. 创建一个元类，使得使用这个元类创建的类不能够被继承  final类
class Final(type):
    def __new__(cls,name,bases,attrs):
        for k in bases:
            # isinstance(对象a，类A)：对象a是不是A产生的对象
            if isinstance(k,Final):
                raise TypeError("不能够继承当前类{}".format(k.__name__))
        return super().__new__(cls,name,bases,attrs)

# object是type产生的类
# class Father(object,metaclass=Final):
#     pass
# class Son(Father):
#     pass
# son=Son()


#3. 使用元编程完成单例模式
# 原本一个类可以创建无数个不同的对象，
# 单例模式：一个类只能创建一个对象
# 在类中创建一个实例属性=None
# 在call中判断，如果实例属性是None，那么就可以创建新对象
# 如果实例属性不是None，直接返回原来的实例对象
class Singleton(type):
    def __init__(self,*args,**kwargs):
        self.instance=None
        super().__init__(*args,**kwargs)
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance=super().__call__( *args, **kwargs)
            return self.instance
        else:
            return self.instance

# 元类下的new和init是class A的时候执行的
class A(metaclass=Singleton):
    pass
a=A()
b=A()
c=A()
print(id(a),id(b))

# 利用new或者init：会执行A的new和init
class B:
    _instance=None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance= super().__new__(cls, *args, **kwargs)
            return cls._instance
        else:
            return cls._instance

b1=B()
b2=B()
print(id(b1),id(b2))