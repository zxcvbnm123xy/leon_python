import socket,threading

def receive(socket):
    while True:
        content = socket.recv(1024)
        print(content.decode())
def sendMessage(socket):
    while True:
        content = input()
        if content == "exit":
            break
        socket.sendall(content.encode())


# # socket.socket()
# #第一个参数地址族
# #第二个参数通信类型（tcp:socket.SOCK_STREAM    udp）
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# #绑定s的ip和端口
# s.bind(("127.0.0.1",8888))
#
# #进行监听
# s.listen()
#
# #接受客户端发送的请求
# # tcp在接受请求之后，会创建一个新的socket来客户端进行通信
# # 原因：如果使用原来的socket对象，那么就没有监听的socket
# # accept返回两个内容，一个是新创建socket，远程的ip地址（客户端的地址）
# so,addr=s.accept()
# print("新创建的socket",so)
# print("客户端的地址",addr)
#
# # 接受客户端发送的信息
# # 按字节接受 接受的大小字节的模式接受，单位是字节
# # recv阻塞函数
# # content=so.recv(1024)
# # print(content.decode())
# # while True:
# #     content = so.recv(1024)
# #     print(content.decode())
# #
# #     # 服务端发送消息
# #     so.sendall(input("服务端说：").encode())
#
# # 服务端，有两个线程，一个是负责发送，一个负责接收
# t1=threading.Thread(target=receive,args=(so,))
# t2=threading.Thread(target=sendMessage,args=(so,))
# t1.start()
# t2.start()

# 多线程解决问题的时候，使用main
if __name__=="__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8888))
    s.listen()
    so, addr = s.accept()
    t1=threading.Thread(target=receive,args=(so,))
    t2=threading.Thread(target=sendMessage,args=(so,))
    t1.start()
    t2.start()