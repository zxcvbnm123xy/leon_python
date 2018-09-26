# 1.当创建一个线程时，该线程是前台线程还是后台线程？
import time,threading
def x():
    print("x方法开始执行")
    time.sleep(0.1)
    print("x方法执行结束")
t=threading.Thread(target=x)
# 设置守护线程，必须在start之前
# t.setDaemon(True)
# 另一种设置方式：
t.daemon=True
t.start()
print("主线程执行")

# 2.两个线程，使用同一个函数作为target，对同一个全局变量增加若干次（次数多一点），会出现什么情况。i=0
#
# a=0
# def mission1():
#   global a
#   for i in range(1000000):
#       a+=1
#   print("在{}线程中，misson方法中的a={}".format(t.name,a))
# def mission2():
#   global a
#   for i in range(1000000):
#       a+=1
#     t=threading.current_thread()
#   t1.join()
#   print("在{}线程中，misson方法中的a={}".format(t.name,a))

# t1=threading.Thread(target=mission1)
# t2=threading.Thread(target=mission2)
# t1.start()
# t2.start()
# # t1.join()
# # t2.join()
# # join只对于抢占主线程有用，对于t1，和t2没有用
# print("在主线程中a={}".format(a))
# 两个线程 调用mission
# print(a)
def mission1():
  a=0
  for i in range(1000000):
      a+=1
  t=threading.current_thread()
  print("在{}线程中，misson方法中的a={}".format(t.name,a))
t1=threading.Thread(target=mission1)
t2=threading.Thread(target=mission1)
t1.start()
t2.start()
#
#
# 3.两个线程，使用同一个函数作为target，然后在函数内定义一个局部变量，两个线程分别对该变量自增若干次，会出现什么情况。
# 多线程中，对于局部变量不共享
# 每个线程都会穿件自己的命名空间，在自己下面的局部空间，不与人共享
def mission1():
  a=0
  for i in range(1000000):
      a+=1
  t=threading.current_thread()
  print("在{}线程中，misson方法中的a={}".format(t.name,a))
t1=threading.Thread(target=mission1)
t2=threading.Thread(target=mission1)
t1.start()
t2.start()