import pygame
import snake
import apple
import random

pygame.init()

snake = snake.SnakeObject()

all_sprites = pygame.sprite.Group()
all_sprites.add(snake)
apple_sprites = pygame.sprite.Group()

count_apples = random.randint(2, 5)
for i in range(count_apples):
    appleObject = apple.AppleObject()
    apple_sprites.add(appleObject)


width = 500
height = 500

win = pygame.display.set_mode((width, height))

FPS = 60
clock = pygame.time.Clock()

count = 0

game_over = False
is_win = False

while (not game_over) or (not is_win):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))

    hits = pygame.sprite.spritecollide(snake, apple_sprites, True)
    if len(hits) != 0:
        appleObject = apple.AppleObject()
        apple_sprites.add(appleObject)
        count += 1
    if snake.rect.left <= 0 or snake.rect.right >= width or snake.rect.top <= 0 or snake.rect.bottom >= height:
        game_over = True
    if count == 10:
        is_win = True
        break
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(str(count), True,
                      (180, 0, 0))
    win.blit(text1, (width - 25, 20))
    all_sprites.draw(win)
    all_sprites.update()
    apple_sprites.draw(win)
    apple_sprites.update()
    pygame.display.update()
    clock.tick(FPS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    f1 = pygame.font.Font(None, 36)
    text = ""
    if is_win:
        text = "Вы выиграли"
    else:
        text = "Вы проиграли"
    text1 = f1.render(text, True,
                      (180, 0, 0))
    win.blit(text1, (width / 2 - 100, height / 2))
    pygame.display.update()