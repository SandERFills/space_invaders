import sys
import pygame
from pygame import image
from bullet import Bullet
from pygame.constants import KEYDOWN, KEYUP
from Settings import Settings
from ship import Ship
from alien import Alien
from star import Star
from random import randint
from eyedrop import Eyedrop
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
        self.stars=pygame.sprite.Group()
        self.ship=Ship(self)
        pygame.display.set_caption("Alien Invasion")
        
        self.aliens=pygame.sprite.Group()
        self.eyedrops=pygame.sprite.Group()
        self._create_fleet()
        self._creat_star_sky()
        self._create_eyedrops()
    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._check_fleet_adges()
            self._update_eyes_drop()
            print(f"num of eyedrop {len(self.eyedrops)}")
            self._check_eyedrop_edge()
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
    def _update_aliens(self):
        self.aliens.update()
    def _update_eyes_drop(self):
        self.eyedrops.update()
    def _create_fleet(self):
        """Создание флота вторжения"""
        #Создание пришельца и вычисляет количество пришельцов в ряду
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        avaible_space_x=self.setting.screen_width-(2*alien_width)
        numbers_of_aliens=avaible_space_x//(2*alien_width)
        """Определяет количество рядов,помещающихся на экране"""
        ship_height=self.ship.rect.height
        avaible_space_y=(self.setting.screen_height-(3*alien_height)-ship_height)
        numbers_of_rows=avaible_space_y//(2*alien_height)
        #Создание флота     
        for row_numbers in range(numbers_of_rows):
            for alien_number in range(numbers_of_aliens):
               self._create_alien(alien_number,row_numbers)
    def _check_fleet_adges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._chanhe_fleet_direction()
                break
    def _chanhe_fleet_direction(self):
        """Опускает флот и меняет направление флота"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.setting.fleet_drop_speed
        self.setting.fleet_direct*=-1
    def _creat_star_sky(self):
        # star=Star(self)
        # star_width,star_height=star.rect.size
        # avaible_space_x=self.setting.screen_width-(2*star_width)
        # number_of_star=avaible_space_x//(2*star_width)
        rand_number=randint(0,20)
        for star_rows in range(rand_number):
            for star_number in range(rand_number):
                self._create_star(star_number,star_rows)
    def _create_star(self,star_num,row_num):
        star=Star(self)
        star_width,star_height=star.rect.size
        star.x=star_width +2*star_width*star_num
        star.rect.x=star.x
        star.y=star_height+2*star_height*row_num
        star.rect.y=star.y
        self.stars.add(star)
    def _create_alien(self,alien_num,row_num):
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        alien.x=alien_width+2*alien_width*alien_num
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_num
        self.aliens.add(alien)
    def _create_eyedrops(self):
       rand_num= randint(5,10)
       for eyedrops_rows in range(rand_num):
           for eyedrops_number in range(rand_num):
               self._create_eyedrop(eyedrops_number,eyedrops_rows)
    def _create_eyedrop(self,eyedrops_num,eye_rows):
        eyedrop=Eyedrop(self)
        eye_width,eye_height=eyedrop.rect.size
        eyedrop.rect.x=eye_width+eyedrops_num*eye_width*eyedrops_num
        eyedrop.rect.y=eye_height+eye_rows*eye_height*eye_rows
        self.eyedrops.add(eyedrop)
    def _check_eyedrop_edge(self):
        for eye in self.eyedrops.sprites():
            if eye.check_edges():
                self.eyedrops.remove(eye)
                break
    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.stars.draw(self.screen)
        self.aliens.draw(self.screen)
        self.eyedrops.draw(self.screen)
        pygame.display.flip()
        # print(len(self.bullets))
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()