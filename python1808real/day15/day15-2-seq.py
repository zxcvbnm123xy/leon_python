"""
四、序列化
# 操作数据时，显示、分析、传送。。。。
# 每一种情况都适合使用不同的数据形式

序列化：对不同类型的文件进行操作。
      目前，一般提到的序列化，都是将对象类型的数据转换成字符串类型。
"""
# 1.csv  comma separeted values, 文本格式的文件
# 扩展名是.csv
# 各个元素之间习惯上用,分隔。
"""
学生名字,年龄,所在小组
张三,20,A
李四,30,B
王五,25,C
"""
# 使用python文件操作，向csv类型文件中写数据
# （1）创建csv模式的文件，w
# （2）调用csv包下的写方法。（以前是调用文本对象下的write）
# 一次写一行writer.writerow
# import csv
# with open("c:/test.csv","wt") as f:
#     writer=csv.writer(f) #将f传给csvwrite方法，形成一个写入器
#     writer.writerow(["学生名字","年龄","所在小组"])
#     writer.writerow(["张三","20","A"])
#     writer.writerow(["李四","30","B"])
#     writer.writerow(["王五","25","C"])

# 一次写多行writer.writerows
#newline写入的是新的一行，默认\n,修改成""
# with open("c:/test2.csv","wt",newline="") as f:
#     writer=csv.writer(f) #将f传给csvwrite方法，形成一个写入器
#     writer.writerows([["学生名字","年龄","所在小组"],["张三","20","A"],["李四","30","B"],["王五","25","C"]])


# 2.json
# javascpipt object notation
# 数据交换格式，数据存在的一种形式
#  使用键值对存储数据。多个元素使用,分隔
"""
对象类型：{}
数组：[]
字符串类型:""
布尔：true false
数值：5    1.2
"""
"""
{
    "bg": "green",
    "title": {
        "data": ["data1", "data2", "data3", "data4"],
        "align": "左对齐"
    }
}
json的数据类型跟python中字典特别像，可以在python和json的数据之间进行转换
"""
# （1）python和json之间的转换
# ① 从python的字典，转成json的数据：dump
# 向json格式的文件中写入数据，写入python字典中的数据
import json
d={
    "bg": "green",
    "title": {
        "data": ["data1", "data2", "data3", "data4"],
        "align": "左对齐"
    }
}

with open("c:/test.json","wt") as f:
    # 第一个参数：要写入的字典数据
    # 第二个参数：保存文件对象
    # ensure_ascii=True 在写入json数据时，默认只显示ascii字符集的字符，对于非ascii的字符
    # 只能使用unicode表示，如果需要写入支持非ascii字符，修改ensure_ascii=False
    json.dump(d,f,ensure_ascii=False)

# ② 将json的数据（从json格式文件中读取出来）转换成python的字典:load
with open("c:/test.json","rt") as f:
    # 参数：从哪个文件对象中读取
    # 返回值：读取的内容会自动封装到python的字典中
    d1=json.load(f)
    print(d1,type(d1))



# (2) 序列化和反序列化
#  序列化： 将对象类型的数据，转换成字符串
#  反序列化：将字符串再包装回对象类型数据

# 序列化： 将对象类型的数据转成字符串  dumps
d={
    "bg": "green",
    "title": {
        "data": ["data1", "data2", "data3", "data4"],
        "align": "左对齐"
    }
}
#dumps ：参数是对象，返回值是字符串
s=json.dumps(d,ensure_ascii=False)
print(s)
print(type(s))

# 反序列化：将字符串类型的数据转换成对象 loads
# loads:参数是字符串，返回值是字典类型对象
s1='{"bg": "green", "title": {"data": ["data1", "data2", "data3", "data4"], "align": "左对齐"}}'
d2=json.loads(s1)
print(d2)
print(type(d2))

# 对于字符串、数值、列表、字典、布尔类型 在序列化的时候，都可以跟json中数据类型一一对应

# 如果自定义一个类，能不能直接把这个类创建的对象，序列化成json数据？不可以
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


p=Person("张三",20)
# json.dumps(p) # 暂时还不可以，因为当前python中只实现了对于基础数据类型的序列化。
# json.JSONEncoder :实现对基础类型进行序列化的类

# 自定义序列化类：需要继承json.JSONEncoder，重写内部的default方法
class PersonEncoder(json.JSONEncoder):
    def default(self, o):
        # 判断，是Person产生的对象才能够序列化
        if isinstance(o,Person):
            return "name:{},age:{}".format(o.name,o.age)
        else:
            return super().default(o)

# 使用自定义的序列化进行对对象的序列化：
# dumps(cls=自定义序列化类)
str=json.dumps(p,cls=PersonEncoder,ensure_ascii=False)
print(str)