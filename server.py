import pickle
import socket
import sys
from _thread import *
from player import Player

# create server socket
server_ip = sys.argv[1]
server_port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket
s.bind((server_ip, server_port))

print("Server started! Waiting for connection...")
s.listen(2)

# store Player objects
players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            packet = conn.recv(2048)
            data = pickle.loads(packet)
            players[player] = data

            if not data:
                print("Disconneted")
                break
            else:
                if player == 1: # if p2 -> send p1 position
                    reply = players[0]
                else: # if p1 -> send p2 position
                    reply = players[1]
                print("Recieved: ", data)
                print("Sending: ", reply)

            rep_packet = pickle.dumps(reply)
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