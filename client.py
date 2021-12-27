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
    p = n.getP()

    while run:
        clock.tick(60) # 60 fps
        p2 = n.send(p) # get p2 from server respone

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_Window(window, p, p2)

main()