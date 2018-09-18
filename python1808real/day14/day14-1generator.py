"""
第十三章 迭代器，生成器，装饰器
"""
# 迭代器回顾
# 迭代器和迭代对象是两个类。
# 迭代对象：所有可以经历for循环的对象就是迭代对象。
# 迭代对象实现了ieterable类中__iter__方法。（个别实现了__getitem__）
# 迭代对象中的iter方法：用来返回一个迭代器

# 迭代器：是迭代对象的子类，专用来产生迭代对象的元素的。
# 迭代器实现了Iterator中__iter__\__next__
class A:
    def __init__(self):
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        # 产生迭代对象/迭代器中的每一个元素
        if self.count<=10:
            self.count+=1
            return "新元素"
        else:
            raise StopIteration()
a=A()
print(next(a)) # a.__next__
for i in a:
    print(i)

# 迭代器只能被遍历一次
# 迭代对象：在迭代对象中可以返回一个迭代器


"""
迭代器的缺点：
（1）必须要实现iter方法和next
（2）如果不是使用for循环（底层捕捉了StopIterration的异常），当调用next无返回结果的时候，报异常
（3）一次性全部迭代，结果未必一下子全部使用，很可能是一个一个使用
"""
# 解决方案：生成器
#
# 二、生成器
# 1.生成器的背景
"""
python 2.5之后才出现的生成器
生成器：返回的是一个可迭代对象。生成器的顶层就是用迭代器实现的。

# 可迭代对象（生成器的）访问方式：
（1）next（迭代器）
（2）for循环

懒加载：按需加载，延迟加载
"""

# 需求：实现列表中：1,2,3...100中每个元素的平方
li=[]
for i in range(1,101):
    li.append(i**2)
# 列表推导式
print([i**2 for i in range(1,101)])

# 2.生成器的实现
# （1）生成器表达式
print((i**2 for i in range(1,101)))
gen=((i**2 for i in range(1,101)))
print(next(gen))
print(next(gen))
print(next(gen))

# （2）生成器函数
# 生成器函数：也是一个函数，是一个带有特殊关键字yield的函数
# yield 产生一个i，会让程序暂停到yield的位置
# 1.当生成器函数被调用的时候，不会立即执行函数，只会产生一个生成器对象
#   生成器底层是迭代器。
# 2.当第一次调用next的时候，相当于激活了生成器函数，函数执行，执行到yield暂停
#   等待调用者再次执行next
#4.当生成器函数终止时，Stop会终止
#5.当调用者调用next的时候，如果生成器中没有yield就会报错

def  f():
    print("开始执行f函数")
    for i in range(1,101):
        # print(i)
        print("产生i之前")
        yield i # yield 产生一个i，作用跟return很像，但是不是return
        print("产生i之后")
g=f() # 不是真正执行了生成器函数，只是产生了生成器对象
print(g)
# 采用next获得元素,获得生成器中的yiled的产出值 i
print("yield产生i=",next(g)) # 开始执行函数，一直到yield暂停，会产出一个i
print("yield产生i=",next(g)) # 当再次调用next的时候，会从上次程序暂停的位置继续执行
print("yield产生i=",next(g))

# 练习 菲波那切数列
def fib():
    a=0
    b=1
    for i in range(100):
        yield b
        a,b=b,a+b
f=fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))








