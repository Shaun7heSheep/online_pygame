import pygame

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
