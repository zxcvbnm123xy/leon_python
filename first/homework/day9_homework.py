# 1.
# 研究一下min，max、sum函数，看看传入一个列表是否可以使用？
# 传入多个参数形式是否可以使用？
# 自己写一个函数，使得sum也能跟max和min一样，可以传入多个参数
# sum((1, 2, 3))
#
print(min(1,2,3))
print(max(1,2,3))
def sum_s(x,*y):
    sum=x
    for i in y:
        sum+=i
    return sum
print(sum_s(1,2,3))

# 2.
# 编写函数，第一个参数指定今天是星期几（1
# ~ 7），第二个参数指定天数n，返回n天后是星期几。
#
def week(x,n):
    """
    x:指定今天是周几
    n：指定n天后是周几
    """
    for i in range(7):
        if i==x:
            i=x
    n = (x + n) % 7
    return x,n
x=3
n=6
a=(str(week(x,n)))
print("今天是周"+a[1]+","+str(n)+"天后是周"+a[4])

#
# 3.
# 证明运算符优先级高会影响结合性，但不会像数学上那样，
# 先进行计算。例如：a + b * c，会首先计算a（使用函数来证明）。
#
#
#a+b*c
def compute(*args):
    """
    sn：放入数字
    on:放入运算符
    :param args:
    :return:
    """
    sn = []  # 数字栈
    on = []  # 操作符栈
    for item in args:
        if isinstance(item, int) or isinstance(item, float):
            if len(on) == 0 or on[-1] == '+' or on[-1] == '-':
                sn.append(item)
                print(item)
            else:
                sn.append(item)
                if isinstance(sn[-2], int) or isinstance(sn[-2], float):
                    if len(on) == 0 or on[-1] == '+' or on[-1] == '-':
                        on.append(item)
        else:
            on.append(item)
    """
    程序先打印的是a，证明计算机先打印的是a
    """
# 4.
# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者，否则返回“不符合要求”提示
#
def a2(arg):
    """
    定义一个新的列表，把符合条件的放入新的列表中
    :param arg:
    :return:
    """
    if len(arg) > 2:
        li_new=[]
        li_new=arg[0:2]
    else:
        return "不符合要求！"
    return li_new

li = [12,13,14,15]
print(a2(li))

# 5.
# 将之前写过的列表的排序，写成函数，实现传入一个列表能够进行排序的功能。
#
def sortedtest(x):
    list_new=[]
    list_new=sorted(x)
    return list_new
x=[111,2,343,56,1]
print(sortedtest(x))


#练习，创建一个狗的类，
#狗有属性，name，age，type
#狗有行为，吃饭，睡觉，洗澡，咬人，叫（显示狗的名字，年龄）
#吃饭显示某一个牌子狗粮（参数）
#小狗交朋友的方法，两只小狗交朋友

class Dog:
    def __init__(self,name,age,type):
        """

        :param name: 狗的名字
        :param age: 年龄
        :param type: 品种
        """
        self.name=name
        self.age=age
        self.type=type
        self.tb = None

    def eat(self,tb):
        self.tb=tb
        print("{}，{}岁的{}在吃{}的狗粮".format(self.name,self.age,self.type,self.tb))

    def sleep(self):
        print("{}，{}岁的{}在睡觉".format(self.name,self.type,self.age))

    def shout(self):
        print("{}，{}岁的{}在啊呜啊呜的叫".format(self.name,self.type,self.age))

    def makeFriend(self,p2):
        print("{}岁的{}{}和{}岁的{}{}交朋友".format(self.age,self.type,self.name,p2.age,p2.type,p2.name))




p1=Dog("tony",3,"京巴")
p2=Dog("linda",2,"泰迪")
p1.shout()
p2.eat("肉骨头牌")
p1.makeFriend(p2)

class Student:
    def __init__(self,name,age,id):
        """

        :param name: 学生的名字
        :param age: 年龄
        :param id: 学号
        """
        self.name=name
        self.age=age
        self.id=id

    def startClass(self):
        print("学号为{}的学生{}，正在上课".format(self.id,self.name))

    def chooseClass(self,lesson):
        self.lesson=lesson
        print("{}岁的学生{}，正在选课,选的是{}".format(self.age,self.name,self.lesson))

s1=Student("tony",18,"0001")
s2=Student("linda",20,"0002")
s1.startClass()
s2.chooseClass("数学")