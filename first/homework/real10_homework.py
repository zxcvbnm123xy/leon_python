# 1.元编程产生一个类，将所有实例方法名，都转成大写调用，如
# class A:
#     def aaa(self):
#         pass
# a = A()
# a.aaa()
# a.AAA()
# 目前会返回true，现在改成必须大写调用，应返回false。
#
class A(type):
    def __new__(cls, name,bases,attrs):
        d={}
        for k,v in attrs.items():
            if not (k.startswith("__") and k.endswith("__")):
                d[k.upper()]=v
        return super().__new__(cls, name,bases,d)

class AA(metaclass=A):
    def aaa(self):
        print("aaa-AAA大写调用")
a=AA()
a.AAA()
#
# 2.创建元类，用来检测类中定义的属性，
# 如果任何attr属性名中包含“x”字母，则输出错误信息。
# def __new__(cls, name, bases, attr)  attr就是属性名
# 自己尝试一下这个属性名到底能对谁起作用？类方法名，实例方法名，类属性，实例属性，静态属性？
#
# class A:
#     bx = 1
#     def ax(self):
#         pass
#     def __init__(self):
#         self.cx = 122
# a = A()
#


