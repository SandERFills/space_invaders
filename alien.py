import pygame
from pygame import image
from pygame.draw import rect
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного пришельца"""
    def __init__(self,game) -> None:
        super().__init__()
        self.screen=game.screen
        self.setting=game.setting
        #Загрузка изображения пришельца и нажначение атрибута rect
        self.image=pygame.image.load("images/alien.png")
        self.rect=self.image.get_rect()
        #Новый пришелец появляется в углу экрана
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #
        self.x=float(self.rect.x)
    def update(self):
        self.x+=self.setting.alien_speed* self.setting.fleet_direct
        self.rect.x=self.x
    def check_edges(self):
        """Возвращает True,если пришелец находиться у края экрана"""
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right or self.rect.left <=0:
            return True