"""
第十章： 面向对象的特征
"""
# 一、 面向对象和面向过程
"""
面向过程：将程序按部就班的执行，为了实现代码的复用性，通过设计函数来实现，堆积大量的函数。
          遇见问题之后，直接按部就班解决
          
面向对象：根据需求，分析出对象，根据需求将对象划分成类，类中属性、行为，将类和类之间进行关联。
          遇见问题之后，谁？对象下的属性和方法。
"""
# 比如 员工请假:  员工提出请假申请、撤销----》领导审批————》人事记录
# 面向过程
"""
请假(员工，领导)
撤销（员工，领导）
审批（员工，领导）
记录（员工，人事）
d1
d2
d3
...


调用：
请假
审批
记录
"""

"""
面向对象解决：
分析：员工、领导、人事
# 属性和方法:
员工：请假、撤销
领导：审批
人事：记录

class Worker:
    def 请假(self,领导)：
      pass
    def 撤回（self,领导）：
      pass
    def 写请假单（self）:
      pass
      
class manager:
    def 同意（self，员工）:
       pass
    def 驳回（self,员工）：
       pass
       
class HR:
    def record(self,员工)：
      pass
      
w=Worker()
m=Manager()
hr=HR()
w.请假(m)
m.同意（w）
hr.record(w)
    

"""
"""
对比面向过程的缺陷：
1. 员工不能审批，领导也不用请假，主谓宾分的不清晰
2. 复杂的数据不能存储，当需求发生改动的时候，改动量极大，方法太多，无法分清方法功能

# 面向过程适合解决：一成不变的需求。操作系统，纯函数
打(武松，老虎)
吃(狗，屎)

# 面向对象适合解决：需求经常变动场景。
武松.打（老虎）
狗.吃(屎)
"""

# 二、面向对象的三个特征
# 封装、继承、多态
# 1. 封装： 信息的隐藏
# 作用：
# （1）数据的安全性
# （2）（重要）方便调用者调用: 内部功能如何修改，不影响调用者的调用者调用方式。
# cls  self
# Person1.desc
# self.__class__.desc

# 1.成员私有化
# 类属性、类方法、实例属性、实例方法、静态方法
# 将类中定义的变量进行私有化，使得变量只能在当前类中访问，不能在外部访问，如果访问需要指定接口。
# 如果需要将一个属性名或者方法名私有化
# 命名格式：   __开头（不能以两个__结尾）
class Computer:
    def __init__(self):
        self.cpu1="intel7"
        self.__memory1="128G"  # 是私有属性
    def fun(self):
        print("在类的内部是可以访问私有成员的",self.__memory1)
    def getMemory(self):
        return self.__memory1
    def setMemory(self,memory):
        self.__memory1=memory
c=Computer()
print(c.cpu1)
c.fun()
# print(c.__memory) # 在类的外部是不能直接访问到私有成员

#如果希望在类的外部访问私有成员，需要提供接口（方法get\set）
print("在类的外部访问私有成员",c.getMemory())
c.setMemory("256G") # 在类的外部修改私有成员
print(c.getMemory())

"""
# 封装性中方便调用者调用的体现
将属性进行封装之后，如果在类的内容修改了属性的名字，外部接口不会修改，对于访问者
来说，调用接口方式还是保持不变
c.setMemory("256G") print(c.getMemory())
"""

# 在python中，私有变量是个假的私有变量
# 通过将私有变量名字: __变量名
# 内部其实将名字封装成： _类名+私有成员的名字
# print(c._Computer__memory1)
# c._Computer__memory1=111111
# print(c._Computer__memory1)

#2.propery
# 为调用者方便调用私有成员
# 两种方式：
# （1）property函数
# （2）property装饰器

# （1）property函数
class Computer:
    def __init__(self):
        self.__memory="128G"
    def setMemory(self,memory):
        self.__memory=memory
    def gatmemory(self):
        return self.setMemory()
    def delmemory(self):
        del self.__memory
    # 加入property函数，将私有成员使用property改名字
    # 语法：对外名字=property（获得私有成员的方法，设置私有成员的方法，删除私有成员的方法）
    memory=property(gatmemory,setMemory,delmemory,"电脑的内存大小")

c=Computer()
# print((c.gatmemory()))

# 使用property的变量来访问
c.memory="256G"