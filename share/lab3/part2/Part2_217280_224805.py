import socket
import sys

HOST = "tcpip.epfl.ch"
PORT = 5003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

if len(sys.argv) < 2:
    print("Usage: '", sys.argv[0], " d' where d is either 0 or 1")
    sys.exit(1)

d = int(sys.argv[1])

message = "CMD_short:{}".format(d)
sock.send(message.encode())

base_length = 18
increased_length = 0

while True:
  data = sock.recv(base_length + increased_length).decode()
  if data:
    if int(data[-(increased_length + 1):]) + 1 == (increased_length + 1) * 10:
      increased_length += 1
    print(data)
  else:
    pass

sock.close()
