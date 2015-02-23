import socket #for sockets
import sys #for exit

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failet to create socket'
    sys.exit()
            
host = 'localhost';
port = 8889;

while(1):
    msg = raw_input('Enter message to send:').decode("utf-8")
   
    try:
    #Set the whole string
        s.sendto(msg.encode("utf-8"), (host,port))
        
        #receive data from cluent (data, addr)
        d = s.recvfrom(1024)
        reply =d[0]
        addr = d[1]
        
        print 'Server reply:'+reply.decode("utf-8")
        
    except socket.error, msg:
        print 'Error Code:'+str(msg[0])+'Message'+msg[1]
        sys.exit()
