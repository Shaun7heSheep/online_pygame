import pygame
import sys
from pygame.key import start_text_input
from network import Network

# server address
server_ip = sys.argv[1]
server_port = int(sys.argv[2])

# create window frame
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0

class Player():
    def __init__(self, x, y, width, height, color) -> None:
        # player position
        self.x = x
        self.y = y

        # player size
        self.width = width
        self.height = height

        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3 # velocity (speed); how fast a player can move

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    # check keyboard interupts
    def move(self):
        k = pygame.key.get_pressed()

        if k[pygame.K_LEFT]:
            self.x -= self.vel

        if k[pygame.K_RIGHT]:
            self.x += self.vel

        if k[pygame.K_UP]:
            self.y -= self.vel

        if k[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    # update player in frame
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

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