import pygame
import snake

pygame.init()

snake = snake.SnakeObject()

width = 500
height = 500

win = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))

    for i in range(height // 30):
        for j in range(width // 30):
            pygame.draw.rect(win, (0, 0, 0), (j * 30, i * 30, 30, 30), 2)

    snake.update()

    pygame.display.update()
