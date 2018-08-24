#1.编写程序，将字典中的键与值互换。
# d={1:"one",2:"two"}

def que1():
    #方法一：
    d={1:"one",2:"two"}
    d_new={}
    for kay,val in d.items():
        d_new[val]=kay
    print(d_new)

    #方法二:
    d={1:"one",2:"two"}
    d_new=dict([val,kay] for kay,val in d.items())
    print(d_new)

#2.元组是否可以总是可以作为字典的键值？

d={"tom":99,"kitty":59,("lily",1,"linda"):12}
"""
键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
"""

#3.现在有一个列表list =[1,2,5,4,1,5,6,8,0,2]，希望去除重复元素，
# 使用set和不使用set两种方式

def que3():
    #使用set方式
    l_new =[1,2,5,4,1,5,6,8,0,2]
    l_new=list(set(l_new ))
    print(l_new )

    #不使用set方式
    list =[1,2,5,4,1,5,6,8,0,2]
    l_new=[]
    for i in list:
        if i not in l_new:
            l_new.append(i)
    print(l_new)

#4. 字典中存储了学生成绩{"tom":100,"kate":90,"jerry":95}，
# 分别实现按照学生名字和按照成绩排序
# def que4():
d={"tom":100,"zoo":90,"kate":90,"jerry":95,"apple":77}
# print(sorted(d.keys()))
# print(sorted(d.values()))
#按key排序
print(sorted(d.items()))

# 按value排序
# v_list=list(d.values())
# v_list.sort()
# print(v_list)

