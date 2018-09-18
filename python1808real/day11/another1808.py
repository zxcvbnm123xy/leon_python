print("another模块执行")
x="x在anther中的全局变量"
def fun():
    print("fun方法：在another模块下的fun方法执行")
helloworldpython="hello world python"
_w="不会被from import * 导入的参数_w"
# __all__=["x","fun","_w"]  # 注意是变量的"名字"，不是写变量

#打印__name__
print(__name__)
print("dddddddddd")

if __name__=="__main__":
    print("其他的代码块")
    print("其他的代码块")
    print("其他的代码块")
    print("其他的代码块")
    print("其他的代码块")