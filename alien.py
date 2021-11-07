import pygame
from pygame import image
from pygame.draw import rect
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного пришельца"""
    def __init__(self,game) -> None:
        super().__init__()
        self.screen=game.screen
        #Загрузка изображения пришельца и нажначение атрибута rect
        self.image=pygame.image.load("images/alien.png")
        self.rect=self.image.get_rect()
        #Новый пришелец появляется в углу экрана
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #
        self.x=float(self.rect.x)
