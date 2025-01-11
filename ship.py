import pygame

class Ship:
    def __init__(self, ai_game, width=None, height=None):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загрузка изображения корабля
        self.image = pygame.image.load('images/ship.bmp')

        # Масштабирование изображения, если заданы размеры
        if width and height:
            self.image = pygame.transform.scale(self.image, (100, 80))

        # Получение прямоугольника
        self.rect = self.image.get_rect()

        # Начальная позиция корабля
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение точной позиции
        self.x = float(self.rect.x)

        # Флаги движения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля в зависимости от флагов движения."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление позиции прямоугольника
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней части экрана."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
