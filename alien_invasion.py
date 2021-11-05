import sys
import pygame
from bullet import Bullet
from pygame.constants import KEYDOWN, KEYUP
from Settings import Settings
from ship import Ship
# class LogInConsole():
#     def log():
#         print
class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""
        pygame.init()
        self.setting=Settings()
        self.bullets=pygame.sprite.Group()
        self.screen=pygame.display.set_mode((0,0))
        self.setting.screen_height=self.screen.get_rect().height
        self.setting.screen_width=self.screen.get_rect().width
        
        self.ship=Ship(self)
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            #Отображение последнего отрисованного экрана
            self._update_screen()
        
    def _check_event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                sys.exit()
            
            self._check_keydown_events(event)
            self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        """Реагирует на нажатие клавиши"""
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                self.ship.moving_right=True 
            elif event.key==pygame.K_LEFT:
                self.ship.moving_left=True
            if event.key==pygame.K_q:
                sys.exit()
            elif event.key==pygame.K_SPACE:
                self._fire_bullet()
    def _check_keyup_events(self,event):
        """Реагирует на отпускание клавиши"""
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                self.ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                self.ship.moving_left=False
    def _fire_bullet(self):
        """Создание нового снаряда в включение его в группу bullets"""
        if len(self.bullets)<self.setting.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
    def _update_screen(self):
        pygame.display.flip()
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # print(len(self.bullets))
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()