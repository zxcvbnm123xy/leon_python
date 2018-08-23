"""
第六章 数据类型（列表和元组）
"""
# 列表 list
# 一、列表的定义
# 需求：想存储一个人的名字
name1="tom"
name2="jerry"
name3="kate"
# 使用多个字符串存储多个名字问题：
# （1）变量名也是需要占用内容
# （2）需要查找第50个人的名字谁

# 列表：可以存储多个数据元素（计算机中对于可以存储多个数据元素的数据类型---集合类型）
# 列表的定义：列表名字=[元素,]
names=["tom","jerry","kate",1,3,[4,5]]
print(type(names),names)
names_null=[]
print(type(names_null),names_null)

print(len(names))
print(len(names_null))

print(bool(names),"当names中有元素时，转换成布尔型")
print(bool(names_null),"当names中有没有元素时，转换成布尔型")

# 应用
# if len(names_null)==0:
# if not names_null:
#
# if len(names_null) != 0:
# if  names_null:



# 列表的内存结构
# 列表的名字，列表对象，列表元素（字符串、数值、列表。。。)
"""
列表的相关特性：
（1）列表中的元素可以是多种类型
（2）列表的元素是有序
（3）列表是可变的数据类型，列表中的元素是可以修改的。
"""


#二、列表的相关操作
# 1. 运算符 +  *  in  not in   is  is not  ==  >  <=
# + 合并 列表的+新创建列表
# [1, 3, 4, 5]
a=[1,3]
b=[4,5]
print(a+b,a,b)  #千万注意不是：[[1,3],[4,5]]


#* 重复 新创建列表，将原列表中的元素进行重复
print(a*3,a)      #千万注意不是：[[1,3],[1,3],[1,3]]


# in  not in：元素是否存在在当前的列表中
# 列表的元素：数值、字符串、字节、列表。。。。
print(1 in a)
x="abc"  # 对于字符串来说， 字符串的元素仍然是字符串
print("a" in x)

names=["tom","jerry","kate",1,3,[4,5]]
print(4 in names)


# ==  is
# 列表作为可变的数据类型a和b不是同一个对象 is返回False  ==返回True
a=[1,3,4]
b=[1,3,4]
c=a
print(id(a),id(b),id(c))


# > < 按照元素逐个比较
print([1,2,3]<[2,3])
print([1,2,3]<[1,3])


# 2. 索引：获取单个元素
# 语法：列表名[index]
# index: 第一个元素从索引为0开始，正数：从左到右  负数：从右到左
# 索引不能越界  范围[-len(li),len(li)-1]
print(a[1])
print(a[-1])
# print(a[-100])
print(id(a[0]),id(b[0]))
x=1
print(id(x))

# 列表的元素是否可变
# s="abc"
# s[0]="6"

l=[1,2,3]
l[0]="6"
print(l)


#练习
# (1). 将下面列表在中tom和jerry元素位置对调
names=["tom","jerry","kate",1,3,[4,5]]
print(id(names))
names[0],names[1]=names[1],names[0]
print(names)
print(id(names))

# (2).新定义一个names_new，画出内存图。
names_new=["tom","jerry","kate",1,3,[4,5]]
print(id(names[5]),id(names_new[5]))
names_new2=names_new


# 3. 切片：获取列表中的多个元素：依然是列表
# 列表名[start:end]
# 包含start，不包含end
# start:正数、负数、0,start省略是0
# end：正数、负数、0，end省略是len(li)
# 默认情况下获取的时候，start在end的左侧
names=["tom","jerry","kate",1,3,[4,5]]
print(names[1:3])

# 字符串的索引获取的依然是单个字符串
s="hello"
# 列表的索引获取的是单个元素
l=[1,2,3]
print(s[0],l[0])

# 字符串的切片获取出来依然是字符串
# 列表的切片 获取出来依然是列表
print(s[1:3])
print(l[1:3])
print(l[-100:100])

# 使用列表切片进行对列表元素的修改。
# 注意：切片直接跟列表进行绑定，尽量不要跟单个元素进行绑定
# 如果单个元素属于序列类型，这时候，列表的切片能够自动将序列转换成列表的元素
# 如果单个元素不是序列类型（可迭代对象），这时候会出错。
l=[1,2,3]
# l[1:3]=["a","b","c"]
# l[1:3]="a"  # 不建议这样写
l[1:3]=["a"]  # 建议这样写
# l[1:3]=100 # 报错
print(l)

# l[1]=["a","b","c"]
# print(l)


# 三、列表中的相关方法
li=["a","b","c","d","e"]
# 1.  添加
# +合并：新创建列表进行合并
print(li+["z"],li)

#append对列表中的元素进行追加，追加到列表的尾部，原地修改
#print(li.append("z")) # 注意使用的时候，append的方法返回值是None
li.append("z")
print(li)

# 字符的相关方法都不是原地修改，都是新创建字符串
# s="abc"
# print(s.replace("a","d"))
# print(s)

# insert插入元素，可以向列表中的index位置，插入object元素
# li.insert(index，object)
li=["a","b","c","d","e"]
li.insert(2,"z")
print(li)

# 练习：使用insert能不能达到append效果
# li.append("happy")
print(li)
# li.insert(0,"happy")
# print(li)
li.insert(len(li),"happy")
print(li)


# 2. 删除
# （1）pop
# li.pop(index)  可以删除index指定位置的元素，一次只能删除一个元素
# pop的返回值是删除元素的内容
# index如果省略，会默认删除列表中的最后一个元素
print(li.pop(1))
print(li)
li.pop()
print(li)
# li.pop(100) # 索引越界报错

# (2)remove:根据传入参数的内容删除指定元素，一次只能删一个,只删除第一次出现的元素
#  remove如果指定元素不存在，会报错
li.remove("c")
print(li)
# li.remove("new")
li=["a","b","c","d","e","a"]
li.remove("a")
print(li)

#3. 检索
# li.index(要检索的内容,起始位置，终止)
# 包含起始位置， 不包含终止
print(li.index("d"))
# print(li.index("dd")) #如果要检索的内容不存在，会报错

#4.统计
li=["a","b","c","d","e","a"]
print(li.count("a"))

#5.反向:原地反向
li.reverse()
print(li)

#6.排序sort: 原地排序
# 列表中的元素类型不一致，不能进行sort排序。
# reverse参数：默认升序False
# 降序reverse=True
li=["a","f","c","u","e","t"]
# li.sort()
# print(li)
li.sort(reverse=True)
print(li)

#降序可以通过先调用sort升序排序，再调用reverse反向

# print(3>"a")
# li=[3,"a"]
# li.sort()

# 7.列表的复制
#（1）赋值
#（2）copy方法
#（3）切片
#（4）copy包下的copy和deepcopy
#（5）*

# 使用赋值进行复制
li=[1,2,3,[4,5]]
li1=li
print(id(li),id(li1))
li[0]="new"
# n=li[3]
# n[0]="new"
li[3][0]="new"
print(li,li1)

# 使用列表的copy方法进行复制
# 只负责复制当前的列表对象（只复制第一层）
li=[1,2,3,[4,5]]
li2=li.copy()
print(id(li),id(li2))
li[0]="new"
li[3][0]="new"
print(li,li2)
