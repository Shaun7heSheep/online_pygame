import pygame
import sys
from pygame.key import start_text_input
from network import Network
from player import Player

# server address
server_ip = sys.argv[1]
server_port = int(sys.argv[2])

# create window frame
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0

# read a string (position) and return int_tupple
def read_pos(string):
    string = string.split(',')
    return int(string[0]), int(string[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redraw_Window(win, player, player2):
    # window background color
    win.fill((255,255,255))
    # draw window frame and player
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network(server_ip, server_port)

    # get starting position of this player from server
    startPos = read_pos(n.getPos())

    # Generate player (This = green; p2 = red)
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0)) # pos(0, 0) because haven't received from server yet

    while run:
        clock.tick(60) # 60 fps

        # send p1 (this) position to server and get back p2 position
        p2_Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2_Pos[0]
        p2.y = p2_Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_Window(window, p, p2)

main()