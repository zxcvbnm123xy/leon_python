"""
元组
戴了枷锁的列表
"""
# 元组的元素不能修改：不可变的数据类型
# 条件：元组的元素是不可变类型的时候，不能修改，如果元组的元素是可变类型，当前元素的子元素是可以修改。
# 元组的意义：保证数据在程序运行中的安全性，能够保证不会意外由自己活着他人修改（参数的传递）

# 一、元组的定义  tuple
# 1. 普通元组
# 语法： 变量名=(元素,)或者不写()
a=(1,2,3)
b=1,2,3
print(a,b)
print(type(a),type(b))

# 2. 创建只有1个元素的元组，必须在元素后面加,  如果不加,python解释器会认为是括号内部的元素类型
#    创建0个元素的元组
# c=(1)
# c=("st")
c=(1,)
c=1,
print(c,type(c),len(c))

d=()
print(d,type(d),len(d))

# 创建元组的时候，必须要使用小括号的情况
# 1. 如果定义空元组，必须使用小括号
# 2. 嵌套元组
e=(1,2,(3,4))
# 3. 当元组作为表达式的一部分，参数运算的时候，必须使用小括号
x=(1,2)+(3,4)
print(x)
y=1,2+3,4
print(y)


# 二、元组的相关操作
# 1.运算符
# + * in not in  is  is not  > <
print((1,2)+(3,4))
print((1,2)*2)

a=[1,2]
print(a+[[3,4]])

b=(1,2)
print(b+((3,4),)) # 一个元素的元组使用的时候，必须加,



# 2.索引
# 名字[index]：
# 元组的元素不能修改
a=(1,2,3)
print(a[1])
# a[1]="new"
a=(1,2,3,[4,5])
print(id(a))
print(id(a[3]),"id(a[3])")
a[3][0]="new"
print(a)
print(id(a))
print(id(a[3]),"id(a[3])")


# 切片
print(a[0:2])
# 整切片: 指向同一个对象。
print(id(a),id(a[:]))

# 结论：字符串、元组的整切片都指向自己，列表的整切片是浅拷贝（新创建对象）

# 元组被修改？
a=(1,2,3)
print(id(a))
a=a[:1]+("new",)+a[2:]
print(a)
print(id(a))

# 三、元组的方法
# 元组因为不可修改，元组只剩下 索引和统计
a=(1,2,3,1)
print(a.count(1))
print(a.index(1))
# print(a.index(2,2,5))
# 元组的复制只能通过 赋值、切片、copy包下copy、deepcopy
# 赋值、切片、copy包下copy 都指向自己

# 四、元组的遍历
t=("a","b","c","d")
for i in t:
    print(i)
for i in range(len(t)):
    print(t[i])
for index ,i in enumerate(t):
    print(index,i)

# 五、元组推导式
# 其实就生成器表达式
# (输出表达式 for i in 元组)----生成器对象--需要通过list或者遍历可以获得到所有元素
a=(1,2,3)
print(list(i*2 for i in a))
b=(i*2 for i in a)
for  i in b:
    print(i)

# 六、命名元组
# 元组是有名字，元组的元素都是有名字
# 定义命名元组
# 可以使用三种方式
from collections import namedtuple
# namedtuple(元组的名字，"元组的各个元素的名字（空格，"," ，[]")
# 学生元组
namedtuple("student","name age sex")
namedtuple("student","name,age,sex")  # 推荐
namedtuple("student",["name","age","sex"])


stu=namedtuple("student","name,age,sex")  # 推荐
print(stu)
print(stu("张三",20,"男"))
s1=stu("张三",20,"男")
print("当前s1的名字是{}".format(s1.name)) # 可以直接通过  元组的名.元素名
print("当前s1的信息是姓名%s,年龄%s,性别%s" % (s1.name,s1.age,s1.sex))
print("当前s1的信息是姓名%s,年龄%s,性别%s" % s1)

import time
print(time.localtime())

# 总结 序列
# 字符串、字节、列表、元组
# 序列的特点：
"""
共同的操作
1. 都可以通过索引获得一个元素
2. 都可以通过切片获得多个元素
3. 都有共同的运算符
4. 都是可迭代对象，都可以遍历
5. len()获得长度

相关方法：
1. list
2. tuple
3. str
4. bytes
5. max
6. min
7. sum
8. sorted
9. reversed
"""
s="abc"
t=(1,2,3)
li=[1,2,3]
b=b"abc"

print(list(s))
print(list(t))
print(list(b))

print(tuple(s))
print(tuple(t))
print(tuple(b))

print(str(t))
print(str(li))
print(str(b))

print(bytes(s,encoding="utf-8"))
print(bytes(t)) # 列表和元组的元素必须是数值类型。
print(bytes(li))


# max、min、sum里面的元素必须是可操作的
# max 和min：内部元素必须是互相可以比较，元素之间都支持>  <
# sum 元素必须是可相加的

print(max(li))
print(max(t))
print(max(s))
print(max(b))

print(min(li))
print(min(t))
print(min(s))
print(min(b))

print(sum(li))
print(sum(t))
# print(sum(s))
print(sum(b))

#sorted 使用的时候，元素必须全部支持<  >
# sorted的返回值是列表
# li=[1,2,3,"a"]
print(sorted(li))
print(sorted(t))
print(sorted(s))
print(sorted(b))

# reversed返回值是列表类型
li=[1,2,3,"a"]
print(list(reversed(li)))
print(list(reversed(t)) ) 
print(list(reversed(s)) ) 
print(list(reversed(b)) ) 