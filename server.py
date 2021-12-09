import socket
from _thread import *
import sys

# create server socket
server_ip = sys.argv[1]
server_port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket
s.bind((server_ip, server_port))

print("Server started! Waiting for connection...")
s.listen(2)

def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconneted")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break

# main server infinite loop
while True:
    conn, addr = s.accept()
    print("Received connection from ", addr)

    start_new_thread(threaded_client, (conn,))