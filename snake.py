import pygame
import Common


class SnakeObject(pygame.sprite.Sprite):
    # Создаем инициализатор(конструктор)
    def __init__(self):
        # Вызываем конструктор самого класса Sprite
        super().__init__()
        # Загружаем изображение
        self.image = pygame.image.load('snake-right.png')
        # Настраиваем его. Не нужно здесь ничего менять, просто копируйте
        self.image = self.image.convert_alpha()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        # Задаем размер. Первая 100 - ширина, вторая 100 - высота
        self.image = pygame.transform.scale(self.image, (20, 100))
        self.angle = 270
        self.image = pygame.transform.rotate(self.image, self.angle)
        # Задаем границы
        self.rect = self.image.get_rect()
        self.rect.top = 1
        self.rect.left = 1


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.top -= 5
        if keys[pygame.K_DOWN]:
            self.rect.top += 5
        if keys[pygame.K_LEFT]:
            self.rect.left -= 5
            #self.image = pygame.image.load('snake-left.png')
        if keys[pygame.K_RIGHT]:
            self.rect.left += 5

    '''def update(self):
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
                    change_to = 'DOWN'''''

