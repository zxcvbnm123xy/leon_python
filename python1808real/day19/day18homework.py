# 1.当创建一个线程时，该线程是前台线程还是后台线程？
import time,threading
# def x():
#     print("x方法开始执行")
#     time.sleep(1)
#     print("x方法执行结束")
#
# t=threading.Thread(target=x)
# # 设置守护线程，必须在start之前。
# # t.setDaemon(True)
# # 另外一种设置方式：
# t.daemon=True
# t.start()
# print("主线程执行")

# 线程开启的时候，默认为非守护线程（False前台线程），cpu分配时间片均等，所有线程都会全部执行完毕
# 守护线程（True,后台线程），当非守护线程执行完毕时，守护线程也被迫执行完毕。


# 2.两个线程，使用同一个函数作为target，对同一个全局变量增加若干次（次数多一点），
# 出现什么情况。i=0
#线程共享变量，全局变量
# a=0
# def mission1():
#   global a
#   for i in range(1000000):
#       a+=1
#   t=threading.current_thread()
#   t2.join()
#   print("在{}线程中，mission方法中的a={}".format(t.name,a))
#
# t1=threading.Thread(target=mission1)
# t2=threading.Thread(target=mission1)
# t1.start()
# t2.start()
# # t1.join()
# # t2.join()
# # 这里的join只对于抢占主线程有用，对于t1和t2之间两个子线程没有用。
#
# print("主方法中a={}".format(a))
#
# 两个线程 调用mission
# print(a)
#
#
#
# 3.两个线程，使用同一个函数作为target，然后在函数内定义一个局部变量，两个线程分别对该变量自增若干次，会出现什么情况。
# 多线程中，对于局部变量不是共享的。
# 每个线程都会创建自己的命名空间，在自己下面的局部变量是自己独享的，不跟其他的线程共享
def mission1():
  a=0
  for i in range(1000000):
      a+=1
  t=threading.current_thread()
  print("在{}线程中，mission方法中的a={}".format(t.name,a))

t1=threading.Thread(target=mission1)
t2=threading.Thread(target=mission1)
t1.start()
t2.start()
# print("主方法中a={}".format(a))