import websocket
import sys

HOST = "ws://tcpip.epfl.ch"
PORT = 5006

websock = websocket.create_connection("{}:{}".format(HOST, PORT))

def abort():
  websock.close()
  sys.exit(1)

def read_PMUs():

  while True:
    data = websock.recv()
    if data:
      print(data.decode("utf-8"))
    else:
      break

def read_whole():
  acc = ""
  call_amnt = 0

  while True:
    data = websock.recv()
    call_amnt += 1
    if data:
      acc += data.decode("utf-8")
    else:
      break;

  print("[INFO] Number of `recv` called: {}\n[INFO] Received from the server:".format(call_amnt))
  print(acc)

def ask_server(message, handling):
  websock.send(message.encode())

  handling()

if len(sys.argv) < 2:
  print("Usage: '", sys.argv[0], " <option>' where <option> is either -flood or -short")
  abort()

option = sys.argv[1]
if option in "-short":
  message = "CMD_short:0"
  ask_server(message, read_PMUs)
elif option in "-flood":
  ask_server("CMD_floodme", read_whole)
else:
  print("option: " + option + " is not recognized! Use either -flood or -short")
  abort()

