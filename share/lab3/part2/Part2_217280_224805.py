import socket
import sys

HOST = "tcpip.epfl.ch"
PORT = 5003

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def abort():
  sock.close()
  sys.exit(1)

def read_PMUs(base_length):
  base_length = 18
  increased_length = 0

  while True:
    data = sock.recv(base_length + increased_length).decode()
    if data:
      if int(data[-(increased_length + 1):]) + 1 == (increased_length + 1) * 10:
        increased_length += 1
      print(data)
    else:
      break

def read_whole(read_size):
  acc = ""
  call_amnt = 0

  while True:
    data = sock.recv(read_size).decode()
    call_amnt += 1
    if data:
      acc += data
    else:
      break;

  print("[INFO] Number of `recv` called: {}\n[INFO] Received from the server:".format(call_amnt))
  print(acc)

def ask_server(message, handling, arg):
  sock.send(message.encode())

  handling(arg)

if len(sys.argv) < 2:
  print("Usage: '", sys.argv[0], " <option>' where <option> is either -flood or -short")
  abort()

option = sys.argv[1]
if option in "-short":
  if len(sys.argv) < 3:
    print("Usage: '", sys.argv[0], " -short d' where d is either 0 or 1")
    abort()
  d = int(sys.argv[2])
  if d > 1:
    print("the d value can only be either 0 or 1")
    abort()
  message = "CMD_short:{}".format(d)
  base_length = 18
  ask_server(message, read_PMUs, base_length)
elif option in "-flood":
  if len(sys.argv) < 3:
    print("Usage: '", sys.argv[0], " -flood read_size' where read_size is a positive integer")
    abort()
  read_size = int(sys.argv[2])
  ask_server("CMD_floodme", read_whole, read_size)
else:
  print("option: " + option + " is not recognized! Use either -flood or -short")
  abort()

