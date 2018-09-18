# 1.	编写程序，将字典中的键与值互换。
d={1:"a",2:"b"}
d_new={}
for k,v in d.items():
    # 方式一
    # d_new[v]=k   #对于key相同时，会覆盖原来的value

    # 方式二
    # d_new.setdefault(v,k)  # 对于key相同时，不会覆盖原来的value

    # 方式三 update
    t={v:k}
    d_new.update(t)   #对于key相同时，会覆盖原来的value

#字典推导式-----得到新的字典
print({v:k for k,v in d.items()})


print(d_new)


# 2.	元组是否可以总是可以作为字典的键值？
# 只有当元组的元素全部都是不可变类型的对象时，才能够作为字典的key
# t=(1,2,[1])
# x={t,"aa"}
#
# 3.	去除列表中的重复元素
li=[1,1,2,3,4,7,8,2,1,2]
print(li)

#方式一：
#将temp设置为空列表，遍历原来的li，将不在temp中的元素加入的temp中。
temp=[]
for x in li:
    if x not in temp:
        temp.append(x)
print(temp)

# 方式二：
# 设置temp空列表，遍历原来的li，从第一个元素开始（i），判断第二个元素(i+1)到最后一个元素，
# 判断i个元素是否存在在  从i+1到最后一个元素
# 如果存在，说明有重复，不是唯一的，所以不要
# 如果不存在，说明是唯一，加入到temp
temp=[]
for index,i in enumerate(li):
    if i not in li[index+1:]:
        temp.append(i)
print(temp)

# 方式三：
print(list(set(li)))

#

#
# 4.	现存任意两个字符串s1与s2，判断s1中的字符在s2中存在的个数
# （重复的算1个，一条语句实现）
s1="aabbccddkk"
s2="adluglkdjkb"
print(len(set(s1)&set(s2)))


#
# 5.	实现一个人力资源管理员工管理（员工编号+姓名）的程序。
def que5():
    info="""功能：1入职，2离职，3修改，4查看所有员工信息，5搜索指定员工，6重置,7 退出。"""
    person={}
    #如果person已存在员工，那么num就取员工编号的最大值max(person)
    # 否则取1000000
    # 1000001  张三
    # 1000002  李四
    num=max(person) if person else 1000000
    while True:
        print(info)
        c=input("请输入您的选择：")
        if c=="1":
            # id=input("请输入员工编号：")
            num += 1
            if num in person:
                print("员工编号已存在")
                continue
            name=input("请输入员工姓名：")
            person[num]=name
            print("添加成功！")
        elif c=="2":
            id=int(input("输入要离职的员工编号："))
            if id  not in person:
                print("员工不存在")
                continue
            person.pop(id)
            print("删除成功！")
        elif c=="3":
            id = int(input("输入要修改的员工编号："))
            if id  not in person:
                print("员工不存在")
                continue
            name=input("员工的新名字：")
            person[id]=name
            print("修改成功")
        elif c=="4":
            if person:
                for  k,v in person.items():
                    print(k,v)
            else:
                print("暂时无员工信息")
        elif c=="5":
            id = int(input("输入要修改的员工编号："))
            if id not in person:
                print("员工不存在")
                continue
            print(id,person[id])
        elif c=="6":
            person.clear()
        elif c=="7":
            break
        else:
            print("输入有误！")



#
#
#
# 6.	验证集合与字典的copy方法。
# 字典是浅拷贝
# 集合无论深拷贝浅拷贝，拷贝之后的对象不再是之前的对象。
d={1:"a",2:"b",3:["d","f"]}
d1=d.copy()
import copy
d2=copy.copy(d)
d3=copy.deepcopy(d)
print(id(d),id(d1),id(2))
d[1]="a_new"
d[3][0]="d_new"
print(d)
print(d1)
print(d2)
print(d3)

s={1,2,3}
s1=s.copy()
s2=copy.copy(s)
s3=copy.deepcopy(s)
print(id(s),id(s1),id(s2),id(s3))
#
#
# 7.	详细说说tuple、list、dict的用法，它们的特点
"""
tuple：元组，固定长度不可变的顺序容器，访问效率很高，适合存储常量，
     在函数定义和返回的时候，经常最为参数和返回值
list: 列表，可变类型存储类型，方法丰富。
dict: 键值对，值和长度是可变的，适合存储的键值对。
# id:[name,age,gender]
# log={id:[operation,id,name,time]} 添加修改删除。

"""

# 8.	请去除a字符串多次出现的字母，仅留最先出现的一个。
# 例 ‘abcabbd’，经过去除后，输出 ‘abcd’
# 先将字符串变成列表，再将列表转换成set（去重复）
a="adkfjadkljfdlskfj"
li=list(a)
print(li)
set_list=list(set(li))
print(set_list)

# 去重复之后再变回列表（为了调用sort），列表是无序
#指定key，key按照字符串中每个元素的索引。
#key指定排序的规则，将每个元素分别使用key指定函数，获取返回值，会使用返回值排序
set_list.sort(key=a.index)
print(set_list)


# 9.	不使用for循环判断search字符串中的字母是否存在在a字符串中。
a="DJLKDFJSKboyLFDJKdjkdfjsdk"
search="boy1"
print(set(a))
print(set(search))
a_set=set(a)
search_set=set(search)
a_set.update(search_set)
print(len(a_set)==len(set(a)))

print(a_set.issuperset(search_set))
#
