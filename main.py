import pygame
import sys
import Common
import food
import snake


pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    win.fill((255, 255, 255))

    for i in range(height // 30):
        for j in range(width // 30):
            pygame.draw.rect(win, (0, 0, 0), (j * 30, i * 30, 30, 30), 2)

    def draw_block(color, ):
        pygame.draw.rect(win, (0, 0, 0), (j * 30, i * 30, 30, 30))



    pygame.display.update()