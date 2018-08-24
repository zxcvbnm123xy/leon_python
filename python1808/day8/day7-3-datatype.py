"""
一、数值类型：整数、浮点、复数
二、布尔类型：是数值类型的子类型
转换
int()
float()
complex()
bool()


# 字符串、字节、列表、元组都属于序列（有序，可重复）
三、字符串
四、字节
五、列表
六、元组

序列的特点：
1. len方法获得长度
2. 都可以是用索引
3. 都可以是用切片
4. 都是可迭代对象
5. 有公共的操作符

序列相关方法
list(序列)：能够将序列转换列表
"""
li=[1,2,3]
t=(1,2,3)
st="abc"
by=b"abc"
print(list(t)  )
print(list(st) )
print(list(by) )

#  tuple(序列)：将序列转换成元组
print(tuple(li))
print(tuple(st))
print(tuple(by))


# str(数值)：只能将数值类型的数据转换成字符串。
# 将列表/元组拼成字符串用join，使用的元素必须都是字符串。
# li=["a","b","c"]
# print("".join(t))
# print("".join(li))


# bytes(序列)：将序列转换成字节
print(bytes(li))
print(bytes(t))
print(bytes("abc",encoding="utf-8"))


# min()
# max()
# sum()
# sorted()
# reversed()
li=[1,2,3,-1]
t=(1,2,3)
st="abczf"
by=b"abc"
print(min(li))
# print(min(["a","b",1]))
print(min(t))
print(min(st))
print(min(by))

print(sum(li))
print(sum(t))
# print(sum(("a","b")))
print(sum(by))
# print(sum(st))

#sorted():新创建对象进行排序
print(sorted(li),li)
print(sorted(st))
print(sorted(by))


# reversed():新创建对象进行逆序
print(list(reversed(li)),li)
print(list(reversed(st)),st)
print(list(reversed(by)),by)

"""



# 无序、不重复
七、字典
八、集合
dict()： 将适合对象转换成字典
set(序列)：可以两序列转换成集合

"""
s="abcccb"
print(set(s))
print(dict(tom=90,jerry=100,lily=55))

# 字典和集合同样可以使用len、sum、min、max 、sorted 都是针对key做的操作
d=dict(tom=90,jerry=100,lily=55)
d1={1:"a",3:"c",2:"b"}
se={1,2,3,-1}
print(len(d))
print(len(se))

print(sum(d1))
print(max(d1))

print(sorted(d1))
print(sorted(se))