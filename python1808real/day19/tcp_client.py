# 客户端
# 创建socket
import socket,threading
from  day19.tcp_server import receive,sendMessage
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接服务端
s.connect(("127.0.0.1",8888))

# 向服务端发送消息
# 参数，发送的信息，字节类型
# s.sendall(input("客户端说：").encode())
# while True:
#     content=input("客户端说：")
#     if content=="exit":
#         break
#     s.sendall(content.encode())
#
#     #客户端接受服务端传过来的信息
#     print(s.recv(1024).decode())

# 客户端，有两个线程，一个负责发送，一个负责接收
t1=threading.Thread(target=receive,args=(s,))
t2=threading.Thread(target=sendMessage,args=(s,))
t1.start()
t2.start()