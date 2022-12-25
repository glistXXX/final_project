import pygame
import Common

class SnakeObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        pygame.draw.rect(Common.win, Common.red, (0, 0, 30, 30), 2)
        pygame.draw.rect(Common.win, Common.red, (30, 0, 30, 30), 2)
        pygame.draw.rect(Common.win, Common.red, (60, 0, 30, 30), 2)
        pygame.draw.rect(Common.win, Common.red, (90, 0, 30, 30), 2)

    






