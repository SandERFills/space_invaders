
import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scoreboard():
    """Класс для вывода игровой информации"""
    def __init__(self,ai_game):
        """Инициализирует атрибут подсчёта очков"""
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.setting=ai_game.setting
        self.stats=ai_game.stats
        self.prep_ships()
        #Настройки шрифта для вывода счёта
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        #Подготовка исходного изображения
        self.prep_score()
        self.prep_high_score()
        self.prep_lvl()
    def prep_score(self):
        """Преобразует текущий счёт в графическое изображение"""
        rounted_score=round(self.stats.score,-1)
        score_str='{:,}'.format(rounted_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.setting.bg_color)
        #Ввод счёт в правой верхней части экрана.
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
    def prep_high_score(self):
        high_score=round(self.stats.high_score,-1)
        high_score_str="{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,
        self.text_color,self.setting.bg_color)
        #Выравнивание по центру верхней стороны
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top
    def check_high_score(self):
        """Проверяет ,появился ли новый рекорд"""
        if self.stats.score>self.stats.high_score:
            self.stats.high_score=self.stats.score
            self.prep_high_score()
    def prep_lvl(self):
        lvl_str="Level: "
        lvl_str+=str(self.stats.level)
        self.lvl_image=self.font.render(lvl_str,True,self.text_color,self.setting.bg_color)

        self.lvl_rect=self.lvl_image.get_rect()
        self.lvl_rect.right=self.score_rect.right
        self.lvl_rect.top=self.score_rect.bottom+10
    def prep_ships(self):
        """Сообщает количество оставшихся кораблей"""
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_game)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)
    def show_score(self):
        """Выводит счёт на экран"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.lvl_image,self.lvl_rect)
        self.ships.draw(self.screen)