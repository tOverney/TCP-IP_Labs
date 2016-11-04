import socket
import struct

MCAST_GRP = '224.1.1.1' 
MCAST_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)

sock.bind((MCAST_GRP, MCAST_PORT))

group = socket.inet_aton(MCAST_GRP)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while 1:
    try:
        data, addr = sock.recvfrom(65507)
    except socket.error:
        continue
    
    print(data[6:].decode())