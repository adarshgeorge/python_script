import os

f = os.popen('cat /etc/ssh/sshd_config|grep Port')
port = f.read()
num = port.split()
print(num[1])
