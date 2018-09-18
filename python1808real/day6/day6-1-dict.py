"""
第七章 字典和集合
"""
# 字典
# 映射类型数据：根据“键” 映射到“值”
# 学成的成绩
names=["tom","jerry","kate"]
scores=[100,80,77]
# 使用字典 形成 名字-成绩的对照表
# 名字--key  键
# 成绩--value值

# 字典的原理：
# 哈希表（散列表）：这种表能够根据键值对直接进行访问的数据结构

# 通过把key和value映射到表的一个位置记录上，相当于使用哈希函数将key值映射成一个唯一的哈希code
# 将哈希code跟value关联。

# 如果key在映射成hashcode的时候，结果是重复的，python选择开放寻址法，一直找到没有冲突的唯一值。4

# 一、字典的定义 dict
# 格式：{key1:value1,key2:value2....}
# 格式：dict(key1=value1,key2=value2......)
#如果定义字典的时候key重复，使用后面value覆盖前面的value值
"""
# 字典的特点
1. 字典中的键值对是无序存储
2. 字典中key是不可变数据类型，value不限制
3. 字典中key不能重复
"""

s={"tom":100,"jerry":80,"kate":89,"tom":99}
print(s,type(s))
s1=dict(tom=100,jerry=80,kate=89)
print(s1,type(s1))

# b=[1,2,3]
# s={"a":1,b:2}
# b[0]="new"

#定义空字典
d={}
print(d,type(d))

print(len(s))
print(len(d))

# 二、字典key和value的访问和修改
# 字典不能通过索引访问键值对，因为无序的数据类型
# 只能通过key访问值
# 格式： 字典[key]  (key必须存在)
s={"tom":100,"jerry":80,"kate":89}
print(s["tom"])
# print(s["tom1"]) # 报错

# 通过key修改值
# 格式： 字典[key]  (key可以不存在)
# 如果key存在：会修改key对应的value
# 如果key并不存在：会新创建key，value键值对
s["tom"]=99
print(s)
s["tom1"]=55
print(s)
s["aa"]=[1,2]
print(s)


# 三、字典的操作
# 运算符
# 不支持 +  *   >  <
# *  +  本质上 __mul__   __add__去实现
# 支持 in   not  in  判断键是否存在
# ==  != 比较键值对内容是否一致
# is  is not 比较字典是否同一个对象
s={"tom":100,"jerry":80,"kate":89}
print("tom" in s)
print(100 in s)

s1={"tom":100,"jerry":80,"kate":89}
print(s==s1)
print(s is s1)


# 四、字典的方法
# 1 创建追加相关
# fromkeys ：创建同值不同键的字典
d={}
print(d.fromkeys([1,2,3]))
print(d.fromkeys([1,2,3],"hello"))
print(d.fromkeys([1,2,3],("a","b","c")))

# setdefault(key,value)
# 如果key不存在，会创建一个指定value 为 值的键值对，如果value不写，则为None
d.setdefault(4)
d.setdefault(4,100)
print(d)
# 如果key存在，则不改变原来键值对的内容
# 这一点跟 字典[key]=value(如果key存在会覆盖原来value) 进行区分

# update方法：追加字典的key和value，可以追加一个字典(一次性可以加多个键值对)
d={1:"a",2:"b",3:"c"}
a={4:"e",5:"f"}
d.update(a)
print(d)
# 相当于起到了+的作用，合并键值对


# 2. 删除
# pop: 删除指定的键值对。同时返回该键绑定的值。
# print(d.pop(6)) 如果key不存在会报错
print(d.pop(4))
print(d)

# popitem(): 随机删除一个键值对，可以返回被删除的键值
print(d.popitem())
print(d)

# clear()清空字典的元素
d.clear()
print(d)

#3. 获取
# get(key) :根据key获得value值, 如果key不存在，不会报错，甚至可以指定相关信息。
# 字典[key] 如果key不存在会报错
d={1:"a",2:"b",3:"c"}
a={4:"e",5:"f"}
d.update(a)
print(d)
print(d.get(5))
print(d.get(6)) # 默认不存在会返回None
print(d.get(6,"没有这个key值")) # 可以通过参数的形式指定返回值


#4. 复制类型
# 赋值、 copy
d={1:"a",2:"b",3:"c",4:["e","f"]}
d1=d.copy()
d2=d
print(id(d),id(d2),id(d1))
d[1]="new"
d[4][0]="new"
print(d1)
#copy实现的是浅拷贝，只拷贝字典对象（第一层对象）
# 值的元素是可变类型，则影响复制之后的值
# 值的元素是不可变数据类型，则不影响复制之后的值

import copy
d={1:"a",2:"b",3:"c",4:["e","f"]}
d3=copy.deepcopy(d)
print(id(d),id(d3))
d[1]="new"
d[4][0]="new"
print(d3)
# 深拷贝会拷贝到不可变数据类型为止。

# 5. 字典遍历相关
# keys():返回字典中的所有键
# values():返回字典中的所有值
# items（）：返回字典中所有的键值对(键值对是以元组的形式返回)
d={1:"a",2:"b",3:"c",4:["e","f"]}
# for k in d:#遍历时默认返回的是所有键
for k in d.keys():
    print(k)
print(d.keys())
for v in d.values():
    print(v)
print(d.values())
print(d.items())
for k,v in d.items():
    print(k,v)
for i in d.items():
    print(i)
    print(i[0],i[1])

# 6.字典推导式：得到的是字典
# 格式：{字典类型的表达式 for k,v in 字典}
d={1:"a",2:"b",3:"c",4:["e","f"]}
print({k*2:v for k,v in d.items()})
print({k:v*2 for k,v in d.items()})
