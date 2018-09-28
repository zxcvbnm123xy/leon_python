"""
并发编程

一、进程
concurrent.futures.ProcessPoolExecutor 创建进程
submit 一次只能提交一个任务到进程池，返回值是待执行任务列表
as_completed: 保证每个任务执行完毕，再执行每个任务下面的内容
wait：（return_when）:ALL_COMPLETED\FIRST_COMPLETED\FIRST_EXCEPTION
"""



# ⑥ map 取代for循环submit的操作
#       返回值：进程任务调用后的返回值集合。（自带as_completed）
#       相当于submit+as_completed
"""
语法：
map(func，iterables)
func: 需要执行的任务（函数）
iterables：多次任务传入的参数
iterables参数使用：
   如果进程任务只有单个参数：多个任务直接打包传入  比如：range(1,6)
   如果进程任务有多个参数，传入多个元组
   ((任务一的参数1，任务二的参数1)，（任务一的参数2，任务二的参数2))
"""
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import time
def doTask1(x):
    time.sleep(0.5)
    return "{}发试卷".format(x)
#
# def doTask2(x,y):
#     return "{}-{}发试卷".format(x,y)
# if __name__=="__main__":
#     with ProcessPoolExecutor(max_workers=3) as executor:
#         # results=executor.map(doTask1,range(10))  # 单参数
#         # results=executor.map(doTask2,(1,2),("a","b")) #多参数
#         args=[(1,"a"),(2,"b"),(3,"c")] # 多参数使用zip传递，建议
#         results=executor.map(doTask2,* list(zip(* args)))
#         for i in results:
#             print(i)

"""
submit和map比较
1. map代码简洁，执行顺是按照调用的顺序执行，多个进程只能执行一个任务。
2. submit一次只能提交一个任务，代码复杂，执行顺序不是按照调用的顺序执行，多个进程可以同时执行多个任务。
"""
from concurrent.futures import as_completed
if __name__=="__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        tasks=[executor.submit(doTask1,i) for i in range(100)]
        # tasks是即将要执行的任务列表
        for index,i in enumerate(as_completed(tasks)):
            # 保证第i个任务一定是执行完毕了，才执行for循环里面的内容
            # print(i.result())
            # time.sleep(0.3)
            print("第{}个任务,{}---执行状态{}----完成状态{}".format(i.result(),index,i.running(),i.done()))

# 将案例按照map方式修改一下。