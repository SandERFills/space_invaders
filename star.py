import pygame
from pygame import image
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self,game_screen):
        super().__init__()
        self.screen=game_screen.screen
        self.image=pygame.image.load('images/starmini.png')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
