import socket
import os
import sys
import time

PORT = 9918

sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sd.bind(('0.0.0.0', PORT))
sd.listen(5)

for i in range(10):
    if os.fork() == 0:
        sd.close()
        cd = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM)
        cd.connect(('127.0.0.1', PORT))
        sys.exit()

print "Server process pid=%i" % (os.getpid(),)
sockets = []
for i in range(10):
    (cd, address) = sd.accept()
    sockets.append(cd)
    cd.shutdown(socket.SHUT_WR)

os.system("lsof -p %i" % (os.getpid(),))
os.system("netstat -nt|grep :%i" % (PORT,))
time.sleep(10000)
#os.system("netstat -nt|grep :%i" % (PORT,))
