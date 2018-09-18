# 1.	研究一下min，max、sum函数，看看传入一个列表是否可以使用？传入多个参数形式是否可以使用？自己写一个函数，使得sum也能跟max和min一样，可以传入多个参数
print(min(1,2,3,-2))
print(min((1,2,3,-2))) # iterable可迭代对象：可以使用for遍历
print(max(1,2,3,-2))
print(max((1,2,3,-2))) # iterable可迭代对象：可以使用for遍历
print(sum((1,2,3,4)))
# print(sum(1,2,3,4)) # sum函数不能直接传入序列
def sum_2(*n):
    return sum(n)
sum_2(1,2,3,4)


# 2.	编写程序，练习其他序列类型的拆包。
# 拆包：在调用函数的时候，在实际参数前面加*
print(1,2,3)
print(* (1,2,3))
print("a","b","c")
print(* "abc")
print(b"a",b"b",b"c")
print(* b"abc")  # 拆包之后，字节类型使用的是ascii码

#
# 3.	编写函数，第一个参数指定今天是星期几（1 ~ 7），第二个参数指定天数n，返回n天后是星期几。
def which_day(t,n):
    d=(t + n) % 7
    if d==0:
        return 7
    return (t+n)%7
print(which_day(6,2))
print(which_day(6,1))


#
# 4.	证明运算符优先级高会影响结合性，但不会像数学上那样，先进行计算。
# 例如：a + b * c，会首先计算a（使用函数来证明）。
#3+4*5
def a():
    print("a函数执行")
    return 3
def b():
    print("b函数执行")
    return 4
def c():
    print("c函数执行")
    return 5
a()+b()*c()


#
# 5.	3 <= x <=4 与x >=3 and x <=4完全等价吗？
# 从结果上来说是等价的
# 但是从执行的访问效果上来说，不一样
# 3 <= x <=4只访问一次x的内存，x >=3 and x <=4需要访问两次
x=2
print(3<=x<=4)
print(x >=3 and x <=4)

def d():
    print("d函数执行")
    return 3
3<=d()<=4
d() >=3 and d()<=4
#
# 6.	给定含有字典的列表，实现对列表的排序。（根据字典中指定键的值排序）
x=[{"a":100,"b":50},{"a":12,"b":30},{"a":32,"b":30}]
# x.sort()
# print(x)

# 列表中的元素，如果是字典，不能直接排序，如果希望排序，需要指定key
# key代表一个规则，将列表中的每一个元素都应用到key上，获得返回值，排序会根据返回值进行排序
# 排序的结果不是只有返回值， 而是原列表根据返回值排序
x=[{"a":100,"b":50},{"a":32,"b":30},{"a":12,"b":30}]

# 目前题目中的key要求：得到字典中key=a 的键值对对应的 值（返回值）。
def s(k):
    # k.get("a")
    return  k["a"]
x.sort(key=s)
print(x)


#
# 7.	写函数，检查用户传入的序列的每一个元素是否含有空内容
# （传入的序列元素只考虑都是字符串，使用isspace方法即可），
# 如果有告诉调用者是哪个元素，如果没有则告诉调用者没有空格。
def checkspace(seq):
    for index,i in enumerate(seq):
        if i.isspace():
            print("第{}元素是空格".format(index))
            break
    else:
        print("没有空格元素")
checkspace("abddjfkld djfks")
checkspace("abddjfklddjfks")

#
# 8.	写函数，检查传入列表的长度，如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者，否则返回“不符合要求”提示
def myfun(li):
    n=len(li)
    if n>2:
        return li[:2]
    return "不符合要求"
print(myfun([1,2,3]))
print(myfun([1,2]))

#
# 9.	编写函数，接收一个字符串，分别统计大写字母、小写字母、数字、其他字符的个数，
# 并以元组的形式返回结果。
import string
def que9(str):
    capital=little=digit=other=0
    for i in str:
        # 字符串的比较可以通过ascii码
        # if "A"<=i<="Z":
        if i in string.ascii_uppercase:
            capital+=1
        # elif "a"<=i<="z":
        elif i in string.ascii_lowercase:
            little+=1
        # elif "0"<=i<="9":
        elif i in string.digits:
            digit+=1
        else:
            other+=1
    return capital,little,digit,other
print(que9("Ajldjlsjafkljlksfj=djflasdjf6561dfdjsklf"))
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)


# 10.	设计一个函数，判断输入的abc三个边是否能够成三角形，如果是的话计算出面积
# （海伦公式）（p=(a+b+c)/2）
# S=sqrt[p(p-a)(p-b)(p-c)]
import math
def que10(a,b,c):
    #判断是否是一个三角形
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        s=math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s
    else:
        return "不是三角形"
print(que10(3,4,5))
print(que10(3,4,9))

#
# 11.	统计考试成绩，给定一个字典，里面包含学生成绩，
# 使用函数，实现求平均成绩，最高成绩的学生，最低成绩的学生，全班成绩排名
ss={"tom":60,"kate":100,"jerry":80,"lily":89,"luly":100}
scores=ss.values()
def avgScore(ss):
    # print(sum(ss.values()))
    # print(len(ss))
    return sum(scores)/len(ss)
print(avgScore(ss))

# 求最高最低成绩，只能先找到成绩，再找到对应的人。
def maxScore(ss):
    # print(max(scores))
    maxscore=max(scores)
    # d_new={}
    # for k,v in ss.items():
    #     if v==maxscore:
    #         d_new[k]=v
    # return d_new

    #字典推导式
    return {k:v for k,v in ss.items() if v==maxscore}
print(maxScore(ss))

#最低成绩
def minScore(ss):
    minscore=min(scores)
    return {k:v for k,v in ss.items() if v==minscore}
print(minScore(ss))

def sortScore(ss):
    # print([(v,k) for k,v in ss.items()])
    s1=[(v, k) for k, v in ss.items()]
    s1.sort(reverse=True)
    # print(s1)
    return [(i[1],i[0]) for i in s1]
print(sortScore(ss))


#
#
# 12.	写一个lambda表达式，实现两个数的相加
# 回忆lambda表达式：是一个函数，如果将结果赋予一个变量，调用变量()就可以执行函数。
# 语法： lambda 参数:返回值表达式
# 一般lambda可以起到简化函数定义的目的。如果有高阶函数使用key，会使用lambda表达式为key赋值。
# sort(key=函数名)  函数名可以直接使用lambda表达式代替。相当于lambda表达式是一个匿名函数。
def a(x,y):
    return x+y
print(a(8,9))
b=lambda x,y:x+y
print(b(8,9))



#
# 13.	不使用nonlocal与global，能不能来修改外围函数中的变量与全局变量？
#能。
# nonlocal与global专门对待不可变数据类型的参数。
x=[1,2,3]
y=1
def test():
    x[0]="new"
    global y
    y=2
    z=[4,5,6]
    def inner():
        z[0]="new"
    inner()
    print(z)
test()
print(x)
print(y)

#
# 14.	在其他语言中，函数名称相同，但是参数列表不同的函数，成为函数重载。
# Python中支持函数重载吗？如果在程序定义了同名的函数，会出现什么情况？
# 对于其他语言来说：定义同名的函数，但是参数个数和参数类型不同，叫做重载，
#                  调用函数的时候会自动根据函数的参数，调用对应的函数。
# def add(int x,int y):
#     pass
# def add(float x,float y):
#     pass
# def add(int x,int y,int z):
#     pass
# add(4,5)
# add(4,5,6)
# add(4.1,5.1)

# 在python本身的语言开发包中是没有重载的概念的。
# 原因：参数类型可以是任意的类型
# 如果函数出现了重复定义，后面定义的函数名字会覆盖前面定义的函数名字。
# def add(* args):
#     s=None
#     for i in args:
#         s+=i
# def add(x,y):
#     x+y
# def add(x,y,z):
#     pass
# add(1,2)

#
# 15.	d={"tom":90,"jerry":100,"kate":77}，分别按姓名和成绩排序
d={"tom":90,"jerry":100,"kate":77}
def sortScore(ss):
    # print([(v,k) for k,v in ss.items()])
    s1=[(v, k) for k, v in ss.items()]
    s2=[(k, v) for k, v in ss.items()]
    s1.sort(reverse=True)
    s2.sort()
    # print(s1)
    # return [(i[1],i[0]) for i in s1]
    return s2
print(sortScore(d))

print(sorted(d,reverse=True))
def s(k):
    return k[1]
print(sorted(d.items(),reverse=True,key=s))
print(sorted(d.items(),reverse=True,key=lambda k:k[1]))





#
#
# 16.	可逆素数：指有一些素数，它的各个位逆序之后，仍然是素数。
# 输出100以内的所有可逆素数。提示：可以将判断是否是素数、可逆素数作为函数提取出来。
def isPrime(num):
    if num>1:
        for i in range(2,int(math.sqrt(num)+1)):
            if num%i==0:
                break
        else:
            return True
    return False
print(isPrime(55))
for i in range(10,101):
    if isPrime(i):
        if isPrime(int(str(i)[::-1])):
            print(i)

#
#
# 17.	假设市面上有4种面值 硬币，20元、10元、5元、1元。输入一个钱数，
# 能够使用最少的硬币凑成这个钱数。

def q17():
    v=[20,10,5,1]
    m=int(input("请输入一个钱数："))
    # 44
    li=[]
    while m>=1:
        for i in v:
            if i<=m:
                li.append(i)
                m-=i
                break
    print(li)



# 类属性的访问：
# 有两种形式：
# 可以通过对象访问：对象名.类属性名
# 可以通过类访问名：类名.类属性名（推荐）
class Person:
    #类属性
    desc="人的描述"

    def __init__(self,name):
        self.name=name
        # self.age=age
        # self.sex=sex

    def run(self,place):
        print("{}在{}跑步".format(self.name,place))

p1=Person("张三")
print(p1.desc)
p1.desc="人的描述_new" #不通过【对象.类属性名】调用
print(p1.desc,Person.desc)
p2=Person("李四")
print(p2.desc)

#2.类方法
# 类方法和实例方法的区别
# 类方法：类的方法，跟具体的实例无关
# 实例方法：属于每个实例的方法
#类方法的定义：在类的内部定义函数，
# 在函数的上方@classmethod,使用固定参数cls（当前类）

class Person:
    #类属性
    desc="人的描述"

    def __init__(self,name):
        self.name=name
        # self.age=age
        # self.sex=sex

    # 实例方法
    def run(self,place):
        print("{}在{}跑步".format(self.name,place))

    # 类方法
    @classmethod
    def copy(cls,p):
        print("这是类方法")
        return Person(p.name)

    # 静态方法
    @staticmethod
    def sm():
        print("这是静态方法")
# 类方法的调用：
# 可以用过对象和类调用,对象名.类方法名
# 类调用                 类名.类方法名（推荐）
p1=Person("张三")
# p1.copy()
p2=Person.copy(p1)
print("=============")
print(p2.name)

# 实例方法的调用：
# 对象名.实例方法
p1.run("陆地") #s不需要传入

#类名调用实例方法 # 基本不使用，显示的传入p1当前对象
Person.run(p1,"空中")

# 3.静态方法
# 静态方法跟类没关系，跟实例也没有关系
class Person:
    #类属性
    desc="人的描述"

    def __init__(self,name):
        self.name=name
        # self.age=age
        # self.sex=sex

    # 实例方法
    def run(self,place):
        print("{}在{}跑步".format(self.name,place))

    # 类方法
    @classmethod
    def copy(cls):
        print("这是类方法")

    # 静态方法
    @staticmethod
    def sm():
        print("这是静态方法")

    @staticmethod
    def makefriend(p1,p2):
         print("{}和{}交朋友".format(p1.name,p2.name))

# 静态方法调用 使用类名调用静态方法
# 对象名.静态方法
# 类名.静态方法（推荐）
p1=Person("张三")
p2=Person("李四")
p1.sm()
Person.sm()
Person.makefriend(p1,p2)

# 类和实例的选择
# 类属性：当属性跟具体的实例没有关系，跟所有的实例有共享同一属性
# 实例属性：当属性值跟具体的实例相关，是每个实例独有的属性

# 类方法，实例方法，静态方法：
# 如果定义的方法是对实例进行操作的，那么设计长实例方法
# 如果定义的方法跟具体的对象没什么关系，操作的是类属性，
# 那么定义成实例方法
# 既不操作类属性，也不操作实力属性，选择使用静态方法。静态方法没有参数，不指定固定参数

# 所有的方法 都是为属性服务的

# 四、在方法中访问属性
# 实例方法中访问类属性
# 实例方法中访问实力属性
# 类方法中访问类属性
# 类方法中访问实例属性


# 动态属性才做
# 1.hasatter(obj,name)
