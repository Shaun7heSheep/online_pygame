import pygame

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

        # update player in frame
        self.rect = (self.x, self.y, self.width, self.height)


def redraw_Window(win, player):
    # window background color
    win.fill((255,255,255))
    # draw window frame and player
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    # Generate player
    p = Player(50, 50, 100, 100, (0, 255, 0))

    while run:
        clock.tick(60) # 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_Window(window, p)

main()