"""
第六章 数据类型 --列表、元组
"""
# 复习序列：可以存储多个元素，并且是有顺序的【数据集合】。
# 一、列表 list
name1="tom"
name2="jerry"
name3="kate"
# 问题：（1）浪费空间，因为变量名也是需要占用空间  （2）获取任何一个元素的时候，不容易获取到索引
# 列表：能够存储多个元素的数据类型
"""
列表的特点：
1. 列表中的元素可以是多种数据类型
2. 列表中的元素是有序的，元素可以重复
3. 列表是可变数据类型，列表的元素可以被改变
"""
# 1.
# 列表的定义
# 语法：列表名=[元素,元素....]
names=["tom","jerry","kate"]
print(names,type(names))

# 定义空列表
a_null=[]
print(a_null,type(a_null))

# 空列表和非空列表的区别
print(len(names),len(a_null))
print(bool(names),bool(a_null))

# 应用：
# 在条件判断中，判断一个列表非空
# if len(names)>0
# if names

# 列表的内存结构
a=1
b="hello"
c=1
# 对于基础数据类型（数值、字符串、字节、布尔）都在内存中存储一份数据。
names=["tom","jerry","kate",0,[2,3]]
print(names,type(names))

names2=["tom","jerry","kate",0,[2,3],"tom"]
names3=names
print(names==names2)
print(names3==names2)
print(id(names),id(names2),id(names3))

a="tom"
print(id(names[0]),id(a))

print(names2)

# 2. 列表的操作
#（1） 运算符
# 因为列表也是序列，所以列表支持的运算符跟字符串是一样。
# + * in  not in  is  is not == < >
# + 合并 新创建列表将元素进行合并，合并之后仍然得到列表
a=[1,2,[3,4]]
b=[3,4]
print(a+b) # [[1,2],[3,4]]  # 不是这样的。
print(a,b)

# * 重复 将原列表中的元素进行重复，形成新的列表
print(a*3)# 不是[[1,2],[1,2]]

# in  not in  判断元素是否在当前的列表中
a=[1,2,[3,4]]
print(1 in a)  # [1] in a   列表的元素不是列表（不是说列表的元素就不能包含列表）
print([3,4] in a)
print(3 in a)  # 使用in判断的是，某一个元素是否在当前的列表中（当前层）

print(4 in a[2],"4 in a[2]")

s="abc"  #字符串的元素本身还是字符串
print("a" in s)


# is  is not: 比较的对象（内存地址）是否是同一个
#   ==： 比较的是内容是否是同一个
a=[1,2,3,[4,5]]
b=[1,2,3,[4,5]]
c=b
print(a==b,b==c,c==a)
print(a is b,b is c ,c is a)
print(id(a),id(b),id(c))
print(id(a[3]),id(b[3]),id(c[3]),"id(a[3]),id(b[3]),id(c[3])")



#（2）索引
# 通过索引访问列表中的单个元素
# 语法：列表名[index]
# index  正数，从左到右的顺序
#         负数，从右到左的顺序
#         0，第一个元素（从左到右，第一个元素0）
                  #   （从右到左，第一个（最后一个元素）元素是-1）
a=["tom","jerry","kate",["hanmeimei","leili"]]
print(a[0])
print(a[1])
print(a[-1])
b=a[-1]  #['hanmeimei', 'leili']
print(b[0])
print(a[-1][0])
# print(a[50])  #索引越界会报异常
# 索引的范围：-len(a)  len(a)-1
print(len(a))

# 列表的元素能不能修改。
print(id(a))
a[0]="tom_new"
print(id(a))
print(a)

# 字符串不能变类型，元素不能修改
# s="abc"
# s[0]="a_new"


# 练习：
# 使用索引实现列表中两个元素的对调
names=["tom","jerry","kate",["hanmeimei","leili"]]
names[1],names[2]=names[2],names[1]
print(names)

# 使用索引替换所有元素为"new"
for i in range(len(names)):
    # names[i]="new"
    names[i]=["new"]
print(names)



#（3）切片
# 切片获得一定区域的元素，按照固定规则（步长）
# 列表的切片是新创建列表对象。
# 格式：列表名[start:end:step]
# start: 正数、负数、0  （可以越界，不会报错） 默认值0  切片中包含start
# end: 正数、负数、0  （可以越界，不会报错）   默认值len  切片中不包含end
# step：正数、负数  代表切片获取时候的方向  step默认1
# start end的方向要跟step保持一致：
# step是正数，start位置应该在end的左侧
#       负数，start位置应该在end的右侧
a=["aaa","bbb","ccc","ddd","eee"]
print(a[0:3])
print(a[0:-2])
print(a[0:5:2])
print(a[0:5:-2])

s="abc"
print(id(s),id(s[:]))
# 列表作为整切片，跟原列表对象不是同一个对象
print(id(a),id(a[:]))

# 切片的赋值: 给列表的切片赋值，一定建议要赋予列表
a=["aaa","bbb","ccc","ddd","eee"]
# a[1:3]=["new"]
a[1:3]=["new","happy","year"]
print(a)

#如果切片赋值时，给予的是数值类型，会报错
a=["aaa","bbb","ccc","ddd","eee"]
# a[1:3]=1
#如果切片赋值时，给予的是序列类型，会将序列类型中的所有元素当成列表的元素进行赋值。
a[1:3]="new"
a[1:3]=["n","e","w"]
print(a)

# 练习：希望删除或者插入元素使用切片赋值完成。
a=["aaa","bbb","ccc","ddd","eee"]
# a[1:1]=[8,9,10]
# print(a)
a[1:2]=[]
print(a)


# 3.列表的相关方法
# (1) 添加
# append: 向列表的尾部追加一个元素，原地操作
a=["aaa","bbb","ccc","ddd","eee"]
# a.append("fff")
print(id(a))
a.append(["fff","ggg"])
print(a)
print(id(a))

s="abc" # 字符串的操作都是不原地操作（字符串是不可变数据类型）
print(s)
s_new=s.replace("a","f")
print(s)
print(s_new)
print(id(s),id(s_new))

#  extend 合并,将参数列表中的元素合并到原列表中。 原地操作
a=["aaa","bbb","ccc","ddd","eee"]
b=["fff","ggg"]
a.extend(b)
print(a)
print(b)

# + 合并，是新创建列表合并
a=["aaa","bbb","ccc","ddd","eee"]
b=["fff","ggg"]
print(a+b)
print(a)
print(b)

# insert：可以向列表中的指定位置加入一个元素
# index:要插入的位置   object：要插入的元素
a=["aaa","bbb","ccc","ddd","eee"]
a.insert(1,"fff")
print(a)
# insert元素到列表尾部
# a.insert(-1,"iii")
a.insert(len(a),"iii")
print(a)


#(2)删除
# pop : 删除指定位置的一个元素
# index：要删除元素的位置，当index不写参数，默认删除最后一个元素
# 返回值：刚刚删除的元素的内容
a=["aaa","bbb","ccc","ddd","eee"]
# print(a.pop(2))
# print(a)
print(a.pop())
print(a)
# print(a.pop(6)) #  pop中的index属于索引，索引越界会报错

# remove: 删除指定内容的一个元素
# object是要删除元素的内容
a=["aaa","bbb","ccc","ddd","eee"]
a.remove("ddd")
print(a)
# a.remove("ddafafd")  #x not in list 如果元素不存在也会 报错

# del:删除列表中的某个元素，按照索引删除
a=["aaa","bbb","ccc","ddd","eee"]
del a[1]
# del a[10] # 索引越界会报错
print(a)

# clear ：清空列表中的所有元素
a.clear()
print(a,len(a))

#（3） 检索
# index：根据参数查找到参数在列表中的位置。返回的是位置
a=["aaa","bbb","ccc","ddd","eee"]
# object：是要查找的元素
# start：默认0
# end : 默认len(li)
# 指定查找范围，包含start，不包含end
print(a.index("ccc"))
print(a.index("ccc",0,5))
# print(a.index("ccc",3,5))
# print(a.index("cccd")) # 索引不存在会报错


# (4) 统计
# a.count()
# object：要统计的元素 （没有start和end）
a=["aaa","bbb","ccc","ddd","eee","ccc","ddd","eee","ddd","eee"]
print(a)
print(a.count("eee"))
print(a.count("eee3"))

#(5) 反向:原地反向
a=["aaa","bbb","ccc","ddd","eee","ccc","ddd","eee","ddd","eee"]
# a.reverse()
print(a)
# reversed方法不是原地反向，是新创建列表进行反向。
print(list(reversed(a)))
print(a)

#（6）排序 :list对象下的sort方法是原地排序
a=["aaa","bbb","ccc","ddd","eee","caa","ddd","eee","ddd","eee"]
# a.sort()
# reverse: 升序（默认）False  降序 True
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 新创建列表进行排序
a=["aaa","bbb","ccc","ddd","eee","caa","ddd","eee","ddd","eee"]
print(a)
print(sorted(a,reverse=True) )
print(a)


# (7)列表的复制
# 赋值
# 深拷贝  copy包下的deepCopy
# 浅拷贝  list对象下copy方法，copy包copy方法，切片，*
# ① 赋值
a=[1,2,[3,4]]
b=a
print(a)
print(b)
print(id(a),id(b))
a[0]="new"
a[2][0]="new"
print(a,b)

# ② list对象下的copy方法
# 浅拷贝只拷贝第一层对象
a=[1,2,[3,4]]
b=a.copy()
print(id(a),id(b))
a[0]="new"
a[2][0]="new"
print(a,b)

# 对于不可变类型来说，原列表的元素发生改变，不会影响新复制的列表
# 对于可变类型来说，原列表的元素发生改变，会影响新复制的列表

# ③ 切片: 浅拷贝
a=[1,2,[3,4]]
b=a[:]
print(id(a),id(b))
a[0]="new"
a[2][0]="new"
print(a,b)


# ④ copy包下的copy方法  :浅拷贝
import copy
a=[1,2,[3,4]]
b=copy.copy(a)
print(id(a),id(b))
a[0]="new"
a[2][0]="new"
print(a,b)


# ⑤ 深拷贝 copy包下的deepcopy
# 一直拷贝到不可变类型为止
# 无论可变类型的元素还是不可变类型的元素，原列表中的元素发生改变都不影响复制之后的列表。
a=[1,2,[3,4]]
c=copy.deepcopy(a)
print(id(a),id(c))
print(id(a[0]),id(c[0]))
print(id(a[2]),id(c[2]))
print(id(a[2][0]),id(c[2][0]))
a[0]="new"
a[2][0]="new"
print(a,c)
print(id(a),id(c))
print(id(a[0]),id(c[0]))
print(id(a[2]),id(c[2]))
print(id(a[2][0]),id(c[2][0]))


# 练习：
a=["aaa","bbb","ccc","ddd","eee","caa","ddd","eee","ddd","eee"]
b=a
c=a[:]
d=copy.deepcopy(a)
a.sort()
#
print(a,b,c,d,sep="\n")


# ⑥通过* 拷贝
# 所有的对象都不进行复制，无论是可变类型还是不可变类型
b=[["_"]*3]*3
print(b)
print(id(b[0][0]),id(b[0][1]))
print(id(b[0]),id(b[1]))
b[0][0]="new"
print(b)


# 4. 列表的遍历
li=[1,2,3,4,5]
for i in li:
    print(i)

# 使用下标遍历
for index in range(len(li)):
    print(li[index])

# 使用enumerate遍历，可以得到index和元素
for index,i in enumerate(li):
    print(index,i)

# 对多维列表进行遍历
li=[[1,2,3,4],[5,6]]
for i in li:
    # print(i)
    for j in i:
        print(j)

# 多维列表的索引遍历
li=[[1,2,3,4],
    [5,6]]
for i in range(len(li)):
    # print(li[index1])
    for j in range(len(li[i])):
        print(li[i][j])

# 5.列表推导式
# 快速形成新列表的一种方式
# 处理原列表li 中的每一个元素，形成新的列表
# 语法： [输出内容  for 每个元素的名字i  in 列表li if 条件]
li=[1,2,3,4,5]
li_new=[]
for i in li :
    if i >=3:
        li_new.append(i*2)
print(li_new)

print([i*2 for i in li])
print([i*2 for i in li if i>=3])

# 练习
names=["tom","jerry","kate","bob","alice","smith","jack","a","bb"]
# 需求：只获取长度超过3个字符的人名，将他们变成大写。
print([i.upper() for i in names if len(i)>3])
import time
print(time.time())
#隔一秒


