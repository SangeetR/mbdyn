import socket
import threading
import os 


HEADER = 64
SERVER = "./a-simple-unix-socket-server"
DISCONNECT_MESSAGE = "!DISCONNECT"
ENCODING = "utf-8"


try:
    os.unlink(SERVER)
except OSError:
    if os.path.exists(SERVER):
        raise


server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(SERVER)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(ENCODING)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(ENCODING)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen(10)
    print(f"[LISTINING] Server is running on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] : {threading.active_count() - 1}")


print("[STARTING] server is starting ...")
start()
        