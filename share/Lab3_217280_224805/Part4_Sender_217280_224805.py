import socket
import struct

MCAST_GRP = '224.1.1.1' 
MCAST_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.settimeout(1)

identifier = ""
while len(identifier.encode()) != 6:
    identifier = input('Enter you sciper:')
    
try:
    while True:
        text = input('Enter a text (exit with q):')
        
        if text == "q":
            break
        
        message = identifier+text
        sent = sock.sendto(message.encode(), (MCAST_GRP, MCAST_PORT))
        

finally:
    print('closing socket')
    sock.close()