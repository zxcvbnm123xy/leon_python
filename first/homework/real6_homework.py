# 1.	编写程序，将字典中的键与值互换。
#\
def q1():
    d={"tom":99,"linda":88,"xiaowang":77}
    d_new={}
    for k,v in d.items():
            d_new[v]=k
    print(d_new)

# q1_1()

# 2.元组是否可以总是可以作为字典的键值？
#

"""
如果元组中有可变类型，则不能作为字典的键值
"""

# 3.	去除列表中的重复元素
#
def q3():
    li = ["a", "s", "a", "f", "s", "b", "e"]
    li_new=[]
    for i in li:
        if i not in li_new:
            li_new.append(i)
    print(li_new)

def q3_1():
    li=["a","s","a","f","s","b","e"]
    li=list(set(li))
    print(li)

def q3_2():
    li = ["a", "s", "a", "f", "s", "b", "e"]
    new_li = list(set(li))
    new_li.sort(key=li.index)
    print(new_li)
# q3_1()

# 4.现存任意两个字符串s1与s2，判断s1中的字符在s2中存在的个数（重复的算1个，一条语句实现）
#
def q4():
    s1="dasdasdasdasd"
    s2="asdasdeefafafaff"
    count=0
    for i in s1:
        for j in s2:
            if j in i:
                count+=1
    print(count)
# 5.	实现一个人力资源管理员工管理（员工编号+姓名）的程序。功能：入职，离职，修改，
# 查看所有员工信息，搜索指定员工，重置。
def q5():
    """
    1:入职，2:离职，3:修改，4:查看所有员工信息，5:搜索指定员工，6:重置，7:退出
    :return:
    """
    employee = {}
    while True:
        id_num=input("请输入编号选择（1-6）：")
        if id_num=="1":
            id=input("请输入员工编号：")
            if id in employee:
                print("该编号已经存在，请重新舒服！")
                continue
            name=input("请输入名字：")
            employee[id]=name
            print("添加成功！")
        elif id_num=="2":
            id = input("请输入员工编号：")
            if id not in employee:
                print("该编号不存在，请重新输入!")
                continue
            employee.pop(id)
            print("删除成功！")
        elif id_num=="3":
            id = input("请输入员工编号：")
            if id not in employee:
                print("该编号不存在，请重新输入!")
                continue
            name=input("请重新输入名字：")
            employee[id]=name
            print("修改成功！")
        elif id_num=="4":
           for k,v in employee.items():
               print(k,v)
        elif id_num=="5":
            id = input("请输入员工编号：")
            if id not in employee:
                print("该编号不存在，请重新输入!")
                continue
            print("该员工信息：",id,employee[id])
        elif id_num=="6":
            if "y"!=input("您确定要删除所有员工信息吗？（y/n）"):
                continue
            employee.clear()
            print("所有员工信息已清空！")
        elif id_num=="7":
            print("感谢使用，再见！")
            break
        else:
            print("输入错误，请重新输入！")
q5()


# 6.	验证集合与字典的copy方法。
# 字典是浅拷贝
# 集合无论深拷贝浅拷贝，拷贝之后的对象不再是之前的对象。
#
def q6():
    import copy
    d={1:"a",2:"b",3:"c",4:[1,2]}
    d1=copy.copy(d)
    d2=copy.deepcopy(d)
    d[1]="a_new"
    d[4][0]="1_new"
    print(id(d),id(d1),id(d2))
    print(d,d1,d2)

    s={1,2,3}
    s1=copy.copy(s)
    s2=copy.deepcopy(s)
    s.remove(1)
    print(id(s),id(s1),id(s2))
    print(s,s1,s2)
#
# 7.	详细说说tuple、list、dict的用法，它们的特点
"""
元组：有序，不变类型，可重复。保证数据的安全性
列表: 有序，可变类型，可重复，列表的方法和功能最丰富的。list(序列)
字典：无序，key是不可变类型，key不可重复。存储双数据，利用key对字典元素进行排序
"""

# 8.	请去除a字符串多次出现的字母，仅留最先出现的一个。例 ‘abcabbd’，经过去除后，输出 ‘abcd’
def q8():
    """
    现将字符串变成列表，再将列表变成set去重，
    去重之后在变回列表，为了调用sort方法
    指定key，key按照字符串中每个元素的索引
    :return:
    """
    a="asdasdasdasfraasfaffg4tt4"
    b=list(set(a))
    print(b)
    b.sort(key=a.index)
    # print("".join(b))
    print(b)

# 9.	不使用for循环判断search字符串中的字母是否存在在a字符串中。
#
#
search="sadas"
a="asdasdfadfadafsa"
search_set=set(search)
a_set=set(a)
a_set.update(search_set)
print(a_set)
print(len(a_set)==len(set(a)))

"""
第八章 函数
"""
def f1(a,b,c=0,* args,**kwargs):
    print("a={} b={} c={} args={} kwargs={}".format(a,b,c,args,kwargs))







