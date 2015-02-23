import socket
import sys

HOST =''
PORT = 8889

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print 'Socket Created'
except socket.error, msg:
    print 'Failet to create socket. Error code:' + str(msg[0]) + 'Message' + msg
    sys.exit()
    
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error Code:'+str(msg[0])+'Message'+msg[1]
    sys.exit()
    
print 'Socket Bind Complete'

while 1:
    d=s.recvfrom(1024)
    data=d[0]
    addr=d[1]
    
    if not data:
        break
    reply ="OK..." + data.upper()
    
    s.sendto(reply,addr)
    print 'Message['+addr[0]+':'+str(addr[1])+']-'+data.strip()
    
s.close()   
