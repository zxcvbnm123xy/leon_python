"""
第十九章  网络编程
"""
# 一、网络基础
# 1. 计算机网络：将地理位置不同的，具有独立功能的多台计算机（计算机本身和外部设备），通过通信
#               通信线路连接起来，从而实现信息或者资源的共享。
# 早期  软盘  1.44mb

"""
计算机网络的七层结构：
应用层
表示层
会话层
传输层
网络层
数据链路层：硬件相关
物理层：硬件相关
"""

# 2. 计算机通讯协议
# 发送的请求http://www.baidu.com   01011011
# 在计算机网络中定义的规范，计算机的通信协议（网络协议）
# 三个要素：
# 语义：要做什么
# 语法：怎么做
# 时序：传输时的顺序

# 跟网络相关的协议
"""
HTTP协议：超文本传输协议
IP协议：  互联网协议
TCP：     传输控制协议
UDP:      用户数据报协议
FTP:      文本传输协议
"""

"""
应用层: HTTP,FTP
传输层：TCP,UDP
网络层：IP协议
"""

"""
传输层中的两个重要协议：
TCP：基于连接的协议，点对点的通道， 
     TCP能够保证一方传输的数据一定可以被另外一方准确的接到，而且接到的顺序跟传送的时候一致
     类似于打电话，对方必须得接听。
     三次握手：
     客户端说：我能够跟你连接吗
     服务端：可以
     客户端：我知道，发送数据
     
UDP：无连接协议，不是安全可靠的协议。发送信息的时候，不需要建立任何连接
     不保证对方一定接到，接到了，也不保证发送的顺序
"""

"""
IP: 确定的独一无二的网络地址
分成四个段位  每段8个数据位，每段0-255

端口号：一台计算机可能启用多个应用程序，给每个应用程序一个端口号 
16位 
oracle  1521
tomcat  8080
"""

# 二、url--统一资源定位
# 超级链接
# 以字符串序列，引用到网络上的资源地址（文件，目录，数据。。。。）
# 1.基本组成
# 分为两个部分（使用//进行分隔）
# https://www.baidu.com
# 协议标识符：使用哪一种协议获取相关资源

# 资源名称：资源的详细地址。
# 主机名称
# 文件名称（路径）
# 端口号
# 相关引用
# http://192.168.2.1:8080/baidu/index.html?
#2. 解析url
# 在python中通过urlparse函数来对指定的url进行解析
# 解析的结果分为六个部分（ParseResult元组，是元组的子类型）
# 协议、网络地址、路径、路径参数、查询参数，引用片段
#127.0.0.1 本地回环地址  localhost
url="http://127.0.0.1:9900/abc/index.html?a=admin&b=123"
from urllib.parse import urlparse
result=urlparse(url)
print(result)

# 3. 发送请求
# 通过python发送请求，得到返回值是源代码
# 两种方式
# 第一种方式urllib.request.urlopen方法
from urllib.request import  urlopen
#参数是指定的url请求，返回 一个响应对象
response=urlopen("https://www.baidu.com/img/bd_logo1.png?where=super")
# 响应对象跟文件对象类似，可以通过read来返回内容，返回的内容是以字节的格式
# html=response.read()
# # print(html)
# with open("c:/download.png","wb") as f:
#     f.write(html)


r1=urlopen("https://baike.baidu.com/item/%E5%90%B4%E7%A7%80%E6%B3%A2/1967656?fr=aladdin")
print(r1.read().decode())

# 第二种方式 urlretrieve 单纯的下载
from urllib.request import urlretrieve
urlretrieve("https://www.baidu.com/img/bd_logo1.png?where=super","c:/download1.png")

# 练习：https://www.csdn.net/ 使用urlopen解析地址
# 提取源码中的 所有http://url连接
import re
url="https://www.csdn.net/"
response=urlopen(url)
content=response.read().decode()
print(content)
res_url=r"<a.*?href=\"(http.*?)\".*?</a>"
urls=re.findall(res_url,content,re.IGNORECASE|re.MULTILINE|re.DOTALL)
for url in urls:
    print(url)


# 三、socket编程
# tcp或者udp
# 1. tcp的socket编程
# 点对点，准确无误，可靠安全协议
# socket 套接字编程
# tcp_server
# tcp_client


