import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game, width=None, height=None):
        """Инициализация пришельца."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения
        self.image = pygame.image.load('images/alien.bmp')

        # Масштабирование изображения, если заданы размеры
        if width and height:
            self.image = pygame.transform.scale(self.image, (100, 65))

        # Получение прямоугольника
        self.rect = self.image.get_rect()

        # Начальная позиция
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции
        self.x = float(self.rect.x)

    def check_edges(self):
        """Проверяет, достиг ли пришелец края экрана."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self):
        """Перемещает пришельца влево или вправо."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
