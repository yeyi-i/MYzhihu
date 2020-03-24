#!/usr/bin/python3

import socket

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 8888

# 连接服务，指定主机和端口
s.connect((host, port))

s.send("https://www.zhihu.com/question/380089207/answer/1084080389".encode('utf-8'))
msg = s.recv(1024)
print(msg.decode('utf-8'))
s.close()
