"""
第七章： 数据类型 字典和集合
字典：dict
"""
# 需求：存储学生的名字和成绩
names=["mike","tom","jerry"]
score=[90,80,70]
# 字典：页----字

# 一、字典的定义
# 键--值
# 格式：  字典名={key1:value1,key2:value2,......}
s={"mike":90,"tom":80,"jerry":70,"kate":66,"lily":100}
# print(type(s),s)

# 字典中键值存储：
# 字典的键会通过hash(哈希)函数映射成唯一个一个值，当前的值会关联到自己value内存
# 字典key  ：必须是可哈希的对象，在python中不可变类型就是可哈希的对象
# 字典value: 没有要求
# d={[1,2,3]:100}

"""
字典的特点：
（1）字典的键值对是无序存储
（2）字典的key是不能重复的。一旦重复了，后面的元素会覆盖前面的元素。
（3）字典的key必须是不可变类型
"""
# a=[1,2,3]----20002
# d={a:80}
# a[0]="new"-----200005
# d={"tom":100,"tom":10}
# print(d)


# 二、字典的操作
# 1.操作符
# 因 为字典是无序
# 没有 +  *  <  >
# is ==
s={"mike":90,"tom":80,"jerry":70,"kate":66,"lily":100}
s1={"mike":90,"tom":80,"jerry":70,"kate":66,"lily":100}
print(id(s),id(s1))
s2=s
print(id(s2),id(s))
print(s==s1)

#
# in 判断key是否存在在字典中
print("mike" in  s)
print(90 in s)

# 2. 索引：在字典中没有索引 （因为字典无序）
# 在python的字典中直接通过key去访问值
# 格式  字典名[Key]可以得到key对应的value
s={"mike":90,"tom":80,"jerry":70,"kate":66,"lily":100}
# 访问字典的value
print(s["tom"])

# 对字典的value进行赋值
# 如果key不存在，会追加键值对
# 如果key存在，会覆盖键值对的值
s["tom"]=88
print(s)
s["tom1"]=88
print(s)
# print(s["jerry1"])#  #访问的时候，如果key不存在，会报错。



# 三、字典的相关方法
# 1. 跟创建相关
#fromkeys(seq)  #新创建字典
# seq：序列：创建同值不同键的字典，键就是传入的seq中每个元素
d={}
# d.fromkeys((1,2,3))
print(d.fromkeys((1,2,3)))
print(d.fromkeys((1,2,3),("one","two","three")))

# 2.删除
# pop(key):根据key值删除键值对,能够返回删除键值对的值
s={"mike":90,"tom":80,"jerry":70,"kate":66,"lily":100}
print(s.pop("tom"))
print(s)
# s.pop("tom1") pop的参数指定key不存在时，会报错

# 3. 获取
# 对于这样访问字典：字典[key]  功能的升级
# 当key不存在时，不会报错 ，默认返回None,也可以指定default
#get(key,default)
s={"mike":90,"tom":80,"jerry":70,"kate":66,"lily":100}
print(s["tom"])
print(s.get("tom"))

print(s.get("tom1"),"当前的key不存在")
# print(s["tom1"])报错

#4. 遍历
s={"mike":90,"tom":80,"jerry":70,"kate":66,"lily":100}

# 直接遍历字典，只能获得key
for i in s:
    print(i)

#（1）返回字典中所有的键
# s.keys()
for i in s.keys():
    print(i)
#(2) 返回字典中所有的value
s.values()
for i in s.values():
    print(i)

#(3)返回字典中所有的键值对,以元组形式返回
s.items()
for i in s.items():
    print(i)
    print(i[0],i[1])

for k,v in s.items():
    print(k,v)
