
from multiprocessing import Pool
import time
# 1. 获得multiprocessing.Pool下的进程池同步申请和异步申请后，进程的返回值

def sum(a,b):
    s=0
    for i in range (a,b):
        s+=i
    return s

# 同步申请 apply的返回值就是执行进程任务的返回值
def sum_apply(b1,b2):
    pool=Pool(4)
    result=[]
    for i in [b1,b2]:
        result.append(pool.apply(sum,args=(0,i)))
    return result


def sum_applyasync(b1,b2):
    pool = Pool(4)
    result=[]
    for i in [b1,b2]:
        result.append(pool.apply_async(sum,args=(0,i)).get())
    pool.close()
    pool.join()
    return result

from multiprocessing.pool import ApplyResult
# if  __name__=="__main__":
#     start=time.time()
#     result=sum_applyasync(10000000,20000000)
#     end=time.time()
#     print("执行的结果是={}".format(result))
#     print("执行的时间={}".format(end-start))





# 2. 尝试使用concurrent.futures模块的进程池完成累加的案例（计算密集型和IO密集型）
from concurrent.futures import ProcessPoolExecutor,as_completed
#ProcessPoolExecutor 上下文管理器，使用with语句体
def sum_processExecutor(b1,b2):
    with ProcessPoolExecutor(max_workers=4) as executor:
        # executor.submit(sum,0,b1)
        # executor.submit(sum,0,b2)
        tasks=[executor.submit(sum,x,y) for x,y in [(0,b1),(0,b2)]]
        # as_completed(待执行任务)，保证每个任务都执行完毕之后，再执行每个任务的下面代码
        for i in as_completed(tasks):
            print(i.result())

if  __name__=="__main__":
    start=time.time()
    sum_processExecutor(10000000,20000000)
    end=time.time()
    print("执行的时间={}".format(end-start))

