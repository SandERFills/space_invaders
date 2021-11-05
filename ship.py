import pygame
from Settings import Settings

class Ship():
    """Класс для управления кораблём"""
    def __init__(self,ai_game):
        """Инициализирует корабль и задаёт его начальную позицию"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        #Загружает изображение и получает прямоугольник
        self.image=pygame.image.load('images/ship3mini.png')
        self.rect=self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края  экрана
        self.x=float(self.rect.x)
        self.rect.midbottom=self.screen.get_rect().midbottom
        #флаг перемещения
        self.moving_right=False
        self.moving_left=False
        #
        self.settings=ai_game.setting
    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        """Обновляет позицию корабля с учётом флага"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        self.rect.x=self.x
        # print(f"позиция по Х = {self.rect.x}")
        # print(f"Позиция по Y = {self.rect.y}")
        
