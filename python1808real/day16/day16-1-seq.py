"""
第十四章 序列化

3. pickle
"""
# 专门对于python进行序列化
# 跟json相比，pickle的优缺点
# json：文本格式.json，可以查看
# pickle: 二进制格式.pickle，不能查看

# json： 只支持基本的内建类型转换，字符串、数值、字典、列表、字典。
#          但是自定义类产生的对象，不能直接被json序列化，只能自己实现类。
# pickle: 可以所有的类，不需要自己定新的类来处理

# json：适用广泛，java  php python 都可以使用
# pickle，只能应用于python

# 使用pickle进行序列化，只需要调用pickle包下的dump和load方法即可

import pickle
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person("张三",20)
# 序列化：
with open("c:/person.pickle","wb") as f:
    # 参数
    # 第一个参数：指定序列化对象
    # 第二个参数：指定序列话之后存储到哪个文件
    pickle.dump(p,f)

# 反序列化：将pickle类型的数据转换成python中的对象
#c:/person.pickle
with open("c:/person.pickle","rb") as f:
    # 参数：需要进行反序列化的文件
    p2=pickle.load(f)
print(p2)
print(p2.name)
print(p2.age)



# 五、上下文管理器
# with语句体
# 关于文件使用with 打开文件，离开with语句体的时候，可以自动关闭文件：是因为open方法内部实现了上下文管理器的功能
#
# with 语句体会返回一个上下文管理器，上下文管理器中定义一些列魔法方法
# 上下文管理器给with提供了上下文环境
# 在上下文管理器中魔法方法：
# __enter__: 当进入with语句体的时候会执行的语句，适合一些初始化的方法
# __exit__：当离开with语句体的时候会执行的语句，适合一些清理方法

# 1. 自定义类实现上下文管理器
# 自己定义一个上下文管理器
# 只需要定义一个类，实现__enter__   __exit__
# class MyManager :
#     def __enter__(self):
#         print("进入了with语句")
#         return "success"
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#         print("离开了with语句")
#
# with MyManager() as f:
#     print(f)
#     print("执行了with语句体")

# __enter__方法： 可以有返回值，返回值会直接绑定with语句体中 as后面的变量
# __exit__方法：有以下的参数
"""
exc_type, exc_val, exc_tb 
参数都是用来处理with语句体中的异常的，如果with语句体执行的时候没有异常，他们的值都是None
exc_type：with语句体中产生的异常类型
exc_val：with语句体中产生异常的对象
exc_tb：with语句体中产生异常堆栈轨迹的回溯对象
"""
class MyManager :
    def __enter__(self):
        print("进入了with语句")
        return "success"
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print("离开了with语句")
        # return True # 希望镇压异常

with MyManager() as f:
    print(f)
    # 1/0
    # raise ValueError("with语句体中产生了异常")
    # print("执行了with语句体")

# 当with语句体出现异常的时候，
# __exit__的返回值如果是False，那么with语句体就会抛出异常。
# 如果返回值是True，则会镇压异常，with语句体就不会抛出异常信息。


#2. 使用装饰器完成上下文管理器
# 用来修饰一个生成器，把生成器函数装饰成上下文处理器
# contextlib.contextmanager装饰器
from contextlib import contextmanager
@contextmanager
def gen():
    print("生成器开始执行")
    try :
        yield "产出值"
    except Exception:
        print("捕获异常")
    finally:
        print("yield之后")

with gen() as f:
    print("with语句体中as后面的变量f=",f)
    raise Exception("在with语句体中抛出的异常")

# __enter__: yield之前的内容
# yield产出的值，with语句体中as后面绑定的变量
# __exit__： yield之后的内容
