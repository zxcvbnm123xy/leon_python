import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("127.0.0.1",8888))

with open("c:/a.txt","rb") as f:
    s.sendfile(f)

