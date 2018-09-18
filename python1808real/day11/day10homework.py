# 1.
# 元编程产生一个类，将所有实例方法名，都转成大写调用，如
# class A:
#     def aaa(self):
#         pass
# a = A()
# a.aaa()
# a.AAA()
class Upper(type):
    def __new__(cls,name,bases,attr):
        d={}
        for k,v in attr.items():
            # print(k,v)
            if not (k.startswith("__") and k.endswith("__")):
                #^__.+__$ 正则表达式
                d[k.upper()]=v
        return super().__new__(cls,name,bases,d)

class A(metaclass=Upper):
    def aaa(self):
        print("执行aaa方法")
a=A()
# a.aaa()
a.AAA()
# 实例方法
# 实例.方法  def 方法的名字：
# 创建类的时候走的方法：元类的new和init方法

#
# 目前会返回true，现在改成必须大写调用，应返回false。
#
# 2.
# 创建元类，用来检测类中定义的属性，如果任何attr属性名中包含“x”字母，则输出错误信息。
# def __new__(cls, name, bases, attr)  attr就是属性名 。
# 自己尝试一下这个属性名到底能对谁起作用？类方法名，实例方法名，类属性，实例属性，静态属性？
# class A:
#     bx = 1
#
#     def ax(self):
#         pass
#
#     def __init__(self):
#         # self.cx = 122
# a = A()
class NoXAttrs(type):
    def __new__(cls, name,bases,attrs):
        for k,v in attrs.items():
            if "x" in k:
                # message=f"{k}属性命名错误，不能使用x命名"
                raise ValueError("{}命名错误".format(k))
        return super().__new__(cls, name, bases, attrs)

class B(metaclass=NoXAttrs):
    # x1="类属性"

    # @classmethod
    # def xcm(cls):
    #     pass

    # @staticmethod
    # def xsm():
    #     pass

    # def runx(self):
    #     pass

#   元类在创建类的时候，new方法中的attr，不能包含实例属性
    def __init__(self,name):
        self.xname=name

# B.x1
# B.xcm()
# B.xsm()
b=B("张三")
print(b.xname)
# b.runx()
#
