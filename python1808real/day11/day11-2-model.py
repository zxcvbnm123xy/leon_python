"""
第十一章 模块和包
"""
# 一、模块
# 1.模块的基本定义
# 模块的定义：一个py文件就是一个模块。————物理的角度
# 模块中包含：定义的语句（类、函数、变量）
# 模块在内存中存储的名字就是py文件的文件名。
# 为什么划分模块？
# 代码太多，不能都存在在一个文件中；会出现名称冲突
# 划分模块之后的好处：
# 1. 定义模块有利于将项目按照功能进行划分，方便协作开发
# 2. 模块提供了独立的命名空间（全局命名空间），解决了命名冲突问题
# 3. 模块可以供多个人使用，提高了程序的复用性。

# 2.模块的使用
# 模块和模块之间的访问：通过导入
# （1）使用import导入
# 导入模块的格式：import 模块名（如果有多个模块，可以是用,分隔）
# import random,math
# 当我们在代码上import 模块，计算机执行了什么内容？
# 当导入了一个模块之后，被导入模块中的语句就会被执行。只执行一次。
# 按照惯例，模块的导入模块的最上方

# 调用导入模块的格式：模块名.名称
# 使用import导入的模式，名字不会跟被导入模块中的名字冲突
#
# print(math.pow(2,4))
#
# # 导入自定一定another模块
# import another1808
# print(another1808.x)
# another1808.fun()
#
# x=1
# print(x)

# （2） from ...import...
# 通过指定要导入的内容来导入
# 被导入的模块都会在导入之后，执行一次，而且只执行一次，跟import是一样的。
# 导入语法格式： from  模块名 import 名称1，名称2.....
# 调用导入模块的语法：  直接使用名称1，名称2

# 注意：from import的方式因为使用的是名字，所以容易跟当前模块中的名字冲突
# 后者覆盖前者
# from another1808 import x,fun,helloworldpython
# print(x)
# fun()
# print(x)
# print(helloworldpython)

# 使用from  import可以导入当前模块前部名称  *
# 格式  from 模块 import  * （慎用）

# 3. 模块的别名
# 当导入模块时，可以使用as来为模块中的名称指定别名
# 语法
"""
import  模块名 as 模块别名,  模块名 as 模块别名
from 模块名 import 名称1 as 名称1别名，名称2 as 名称2别名,
"""
# 当名称有别名了之后，原名字失效。

# from another1808 import x,fun,helloworldpython as y
# print(y)
# print(helloworldpython) 失效

# import another1808 as an
# print(an.x)
# print(another1808.x)  失效
"""
别名的好处：
（1）可以解决当前模块和导入模块的名称冲突问题
（2）当名字特别长时候，可以简化调用
"""

# 4.隐藏模块的数据
# 注意：只对from 模块 import *这种情况有效，对于import无效
#      下面两种方式中，如果一个带有_的变量放在__all__，程序会认为可以导入。
# from another1808 import *
# 可以在使用from  import的时候，选择性导入名称。
# 方式有两种：
#（1）指定不能被导入的名字： 名字前面使用_，这样的名字不会被from import * 导入。
# print(_w)
#（2）指定能被导入的名字： 在模块内定义 __all__，关联列表，列表中的元素是能够被导入的名字
# print(helloworldpython)
# print(_w)
# print(another1808._w)

# 5.__name__
# 当前模块的名称
# 对于一个py文件来说，执行方式有两种：
# （1）直接run :__main__
# （2）被导入  :another1808
import another1808
print(another1808.__name__)
# 当导入模块中有不希望被导入时执行的代码，
# 可以加入if __name__=="__main__"判断。

# 6.模块的搜索路径
#当import  名称，按照如下的路径搜索名称
"""
 (1) 内置解释器中搜索
（2）作为脚本执行的模块所在路径
（3）python的path环境变量指定路径下
（4）python的安装路径（lib）
"""
import sys
print(sys.maxsize)
import random
random.randint(1,3)
# 注意：类名、方法名、变量名、模块名 都不要跟内建命名空间的名字和lib包下的名字一样。

# 7. 模块缓存
# 导入模块的时候，只会执行一次被导入的模块
#是因为python在导入模块时，会缓存加载模块，产生pyc文件，是字节码文件，也叫预编译
# 什么时候创建？创建在哪？
# （1）自定义模块被导入的时候，会产生
# （2）会创建到，同路径下的__pycache__的包下
# 作用：加快模块的加载速度，因为第二次加载直接读取缓存文件。不会加快模块的执行速度。