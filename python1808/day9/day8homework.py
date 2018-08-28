# 1.
# 编写程序，将字典中的键与值互换。
d = {1: "one", 2: "two"}
# 字典创建的方式{键:值,}
# 对字典进行追加元素
# 字典[key]=value
d_new={}
print(len(d_new))
for k,v in d.items():
    d_new[v]=k
print(d_new)




#
# 2.
# 元组是否可以总是可以作为字典的键值？
# 元组的元素只有不可变类型时，可以作为字典的key
# 如果包含可变类型，则不能作为字典的key
t=(1,2,3)
# t=(1,2,3,[4])
x={t:"dddd"}
print(x,type(x))

#
#
# 3.
# 现在有一个列表list = [1, 2, 5, 4, 1, 5, 6, 8, 0, 2]，
# 希望去除重复元素，
# 使用set和不使用set两种方式
list1 = [1, 2, 5, 4, 1, 5, 6, 8, 0, 2]
print(list1)
print(list(set(list1)))
# list1.sort(key=)
temp=[]
for x in list1:
    if x not in temp:
        temp.append(x)
print(temp)
#
# 4.
# 字典中存储了学生成绩
# 如果要把字典中元素变成有序，习惯上将字典中元素转换成元组(key,value)，
# 将整个字典变成列表，最终的结果建议仍然使用元组存储。

# {"tom": 100, "kate": 90, "jerry": 95}，分别实现按照学生名字和按照成绩排序
d={"tom": 100, "kate": 90, "jerry": 95, "lily": 95}
print(sorted(d))
t1=[]
t2=[]
for k,v in d.items():
    # t1+=((k,v))
    t1.append((k,v))
    t2.append((v,k))
print(t1)
print(('jerry', 95)<('tom', 100))
t1.sort()
print(tuple(t1))
t2.sort()
print(t2)

