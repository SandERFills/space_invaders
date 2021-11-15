import sys
import pygame
from pygame import image
from time import sleep
from game_stats import GameStats
from bullet import Bullet
from pygame.constants import KEYDOWN, KEYUP
from Settings import Settings
from ship import Ship
from alien import Alien
from star import Star
from random import randint, shuffle
from eyedrop import Eyedrop
from button import Button
<<<<<<< HEAD
from scoreboard import Scoreboard
# class LogInConsole():
#     def log():
#         print
=======
>>>>>>> 0fddc30fa357ab5317a6d8863f366a38b8400d2b
class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""
        pygame.init()
        self.setting=Settings()
        self.bullets=pygame.sprite.Group()
        self.screen=pygame.display.set_mode((1280,800))
        self.setting.screen_height=self.screen.get_rect().height
        self.setting.screen_width=self.screen.get_rect().width
        self.stars=pygame.sprite.Group()
        self.ship=Ship(self)
        
        self.ship.center_ship()
        self.stats=GameStats(self)
        pygame.display.set_caption("Alien Invasion")
        self.aliens=pygame.sprite.Group()
        self.eyedrops=pygame.sprite.Group()
        self._create_fleet()
        self._creat_star_sky()
        self._create_eyedrops()
        self.play_button=Button(self,"Play")
        self.sb=Scoreboard(self)
    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_event()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._check_fleet_adges()
                self._update_eyes_drop()
                # print(f"num of eyedrop {len(self.eyedrops)}")
                self._check_eyedrop_edge()
            #Отображение последнего отрисованного экрана
            self._update_screen()
    def _check_event(self):
        """Обрабатывает нажатие клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT :
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
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
                
    def _check_play_button(self,mouse_pos):
        """Запускает новую игру при нажатии кнопки"""
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.stats.game_active=True

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()    
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
        # self._check_bullet_collision()
    # def _check_bullet_collision(self):
    #     collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
    #     if not self.aliens:
    #         self.bullets.empty()
    #         self._create_fleet()
    def _update_aliens(self):
        self.aliens.update()
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            sleep(0.5)
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            print("Корабль уничтожен!")
        self._check_aliens_bottom()
    def _update_eyes_drop(self):
        self.eyedrops.update()
    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем"""
        if self.stats.ships_left>0:    
            self.stats.ships_left-=1
            #очистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()
            #Создание вого флота и размещение корабля в центр
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)
        #Пауза 
        sleep(0.5)
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
    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего экрана"""
        screen_rect=self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #проиисходит тоже ,что при столкновении с кораблём
                self._ship_hit()
                break
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
        self.stars.draw(self.screen)
        self.ship.blitme()
        self.sb.show_score()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        self.eyedrops.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
        # print(len(self.bullets))
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()