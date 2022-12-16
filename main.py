import pygame
import sys

pygame.init()
widht = 500
height = 500
win = pygame.display.set_mode((widht, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
