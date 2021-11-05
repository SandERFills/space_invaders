
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """Cоздаёт объект снарядов в текущей позиции корабля."""
    def __init__(self,ai_screen): 
        super().__init__()
        self.screen=ai_screen.screen
        self.setting=ai_screen.setting
        self.color=self.setting.bullet_color
        
         #создание новой поверхности,без изображения,в точке 0:0 
         #с хитбоксом из настроек пули
        self.rect=pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)
        self.rect.midtop=ai_screen.ship.rect.midtop
        self.y=float(self.rect.y)
    def update(self):
        """Перемещение снаряда вверх по экрану"""
        #обновление позиции снаряда в вещественном формате
        self.y-=self.setting.bullet_speed
        #Обновление позиции прямоугольника
        self.rect.y=self.y
    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen,self.color,self.rect)