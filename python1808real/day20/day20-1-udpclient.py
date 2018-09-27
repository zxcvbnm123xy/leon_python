import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# upd不需要connect
# s.connect()

# sendto发送消息
# 第一个参数：指定要发送的数据(字节模式传输)
# 第二个参数：指定要发送到的ip和端口号
s.sendto("udp协议下的客户端发送的信息".encode(),("127.0.0.1",8888))