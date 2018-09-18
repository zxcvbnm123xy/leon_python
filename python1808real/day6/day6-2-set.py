"""
集合： 顶层是字典实现  set
"""
# 集合：字典中所有的value为None，相当于使用key组成集合
# 集合的规则跟字典的key的规则一致
"""
特点：
1. 不能重复
2. 集合的元素是不可变类型
3. 集合是无序
"""
# 集合无论如何也不能使用索引去获得元素。
# java中集合 是list（列表）是同一类，跟python不同。注意区分
# 一、创建集合
# 语法：名字={元素,}
# 语法：名字=set(序列)
a={1,2,3,5,6}
b=set([2,3,4,5,4])
print(a,b)
print(type(a),type(b))
# 创建的时候会直接去掉重复的元素。

print(len(a))
# 创建空集合
# set_null={}  #创建的是空字典
set_null=set()
print(type(set_null))
print(len(set_null))

# 二、集合运算
# 不支持 + *
# 支持< > 代表子集和父集的比较
# 支持 in  not in  is  is not   ==
a={1,2,3,5,6}
b={1,2,3,5,6}
print(a ==b)
print(a is b)
print(1 in a)

a={1,2,3,5,6}
b={1,2,5,6,7,9}
# 差集 -
print(a-b)
print(b-a)


# 并集 |
print(a|b) # 去掉重复元素

# 交集 &
print(a&b)

# 对称差集 ^: 两个集合中不同时出现的元素
print(a^b)


# 支持< > 代表子集和父集的比较  父集>子集
s={1,2,3}
t={2,3}
print(s>t)

#三、集合的方法
# 1 添加类型
# add 可以加入指定的元素，如果重复，不添加
s={1,2,3}
s.add(4)
s.add(4)
print(s)

# 2. 删除
# remove 删除集合中的指定元素，如果不存在会报异常
s.remove(4)
# s.remove(6)
print(s)
s={1,2,3}


s.discard(3) # 删除集合中指定元素，不存在不会报错
s.discard(4)
print(s)

# s.pop()   # 随机删除一个元素
s.pop()
print(s)

# clear()清空集合中的所有元素
s.clear()
print(s)

# copy() 复制集合中所有的元素
s={1,2,3}
s1=s.copy()
print(id(s),id(s1))

# 交集、差集、并集、对称差集
a={1,2,3,5,6}
b={1,2,5,6,7,9}
print(a-b)
print(a.difference(b)) # difference相当于新创建集合
print(a,b)
a.difference_update(b) # update 原地改变
print(a)

# 交集
a={1,2,3,5,6}
b={1,2,5,6,7,9}
print(a.intersection(b))
print(a&b)
a.intersection_update(b)
print(a)

# 并集
a={1,2,3,5,6}
b={1,2,5,6,7,9}
print(a.union(b))
a.update(b)
print(a)

# 对称差集
a={1,2,3,5,6}
b={1,2,5,6,7,9}
print(a.symmetric_difference(b))
print(a^b)
a.symmetric_difference_update(b)
print(a)

# 判断交集是否为空
#为空为True  否则是False
a={1,2,3,5,6}
b={1,2,5,6,7,9}
print(a.isdisjoint(b))

# a是否是b的子集
a.issubset(b)

# a是否是b的父集合
a.issuperset(b)


# 四、集合遍历
s={1,2,3,"hello"}
for i in s:
    print(i)

# 五、集合推导式: 返回的是集合
# 格式={返回集合类型的元素  for i in  迭代对象}
s={1,2,3}
print({i+2 for i in s})

# 六、数据转换
# set
# dict
s="abcc"
t=(1,2,3)
se={1,2,3}

print(list(s))
print(list(t))
print(list(se))
print(set(s))
print(set(t))

print(dict(a=1,b=2,c=3))
