import pickle
import socket
import sys
from _thread import *
from player import Player
from game import Game

# create server socket
server_ip = sys.argv[1]
server_port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket
s.bind((server_ip, server_port))

print("Server started! Waiting for connection...")
s.listen(2)

connected = set() # store clients' addresses
games = {} # key: gameId / value: game obj
idCount = 0

def threaded_client(conn, p, gID):
    global idCount

    conn.send(str.encode(str(p)))
    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.reset()
                    elif data != "get":
                        game.play(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
    
    print('Lost connection!')
    try:
        print('Closing Game ', gameId)
        del games[gameId]
    except:
        pass
    idCount -= 1
    conn.close()


# main server infinite loop
while True:
    conn, addr = s.accept()
    print("Received connection from ", addr)

    idCount += 1
    p = 0
    # 2 players will join in a same game.
    gameId = (idCount - 1)//2

    # New comming player will have to wait for 
    # a new room (gameId) if there's no room available
    if idCount % 2 == 1:
        print('Creating new game...')
        games[gameId] = Game(gameId)
    else:
        # 2 players are connected --> Game is ready
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))