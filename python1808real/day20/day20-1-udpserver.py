"""
UDP应用
即时消息发送
丢包率

使用udp协议做socket
两个socket对象之间通信
"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",8888))

# udp中不需要下面两个方法
# s.listen()
# s.accept()

# 接受信息
print(s.recv(1024).decode())
