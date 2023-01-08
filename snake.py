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

    def event_loop(self, change_to):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'

