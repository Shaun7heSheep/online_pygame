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

# read a string (position) and return int_tupple
def read_pos(string):
    string = string.split(',')
    return int(string[0]), int(string[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

# starting positions for players
pos =  [(0,0), (100,100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            packet = conn.recv(2048)
            data = read_pos(packet.decode())
            pos[player] = data

            if not data:
                print("Disconneted")
                break
            else:
                if player == 1: # if p2 -> send p1 position
                    reply = pos[0]
                else: # if p1 -> send p2 position
                    reply = pos[1]
                print("Recieved: ", data)
                print("Sending: ", reply)

            rep_packet = str.encode(make_pos(reply))
            conn.sendall(rep_packet)

        except:
            break
    print("Lost connection")
    conn.close()

curr_player = 0
# main server infinite loop
while True:
    conn, addr = s.accept()
    print("Received connection from ", addr)

    start_new_thread(threaded_client, (conn, curr_player))
    curr_player += 1