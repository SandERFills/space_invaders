from sys import path
import pygame
from pygame.sprite import Sprite
import pygame
class Eyedrop(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen=game.screen
        self.setting=game.setting
        self.image=pygame.image.load('images/eyedropmini.png')
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.x+=self.setting.eyedrop_speed
        self.rect.y+=self.setting.eyedrop_drop_speed
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right or self.rect.bottom >=screen_rect.bottom:
            return True
