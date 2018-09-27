import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("127.0.0.1",8888))

s.listen()

so,addr=s.accept()

b=bytes()
while True:
    data=so.recv(1)
    if not data:  # 发送完毕
        break
    b+=data
# print(b)
with open("d:/a.txt","wb") as f:
    f.write(b)


