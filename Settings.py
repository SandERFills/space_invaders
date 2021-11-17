class Settings():
    def __init__(self):
        self.screen_width=1366
        self.screen_height=768
        self.bg_color=(230,230, 128)
        self.ship_limit=3
        #Параметры снаряда
        self.bullet_width=300
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=3
        #Настройки для пришельцев
        self.fleet_drop_speed=10
        self.fleet_direct=1
        #Настройки для капельки
        self.eyedrop_speed=1
        self.eyedrop_drop_speed=1
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_setting()
    def initialize_dynamic_setting(self):
        """Инициализирует настройки изменяющиеся в ходе игры"""
        self.ship_speed=1.5
        self.bullet_speed=3.0
        self.alien_speed=1.0
        #fleet_direction=1 обозначает движение вправо; a -1 - влево
        self.fleet_direct=1
        #подсчёт очков
        self.alien_points=50
    def icrease_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)


        