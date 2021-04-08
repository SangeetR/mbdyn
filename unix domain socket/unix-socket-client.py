import socket

HEADER = 64
SERVER = "./a-simple-unix-socket-server"
DISCONNECT_MESSAGE = "!DISCONNECT"
ENCODING = "utf-8"

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect(SERVER)

def send(message):
    msg = message.encode(ENCODING)
    msg_length = len(msg)
    send_length = str(msg_length).encode(ENCODING)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)


while True:
   print("Type message then press enter to send Or type exit to exit") 
   inpt = input()
   if inpt.strip() == "exit":
    send(DISCONNECT_MESSAGE)
    break
   else:
    send(inpt)
