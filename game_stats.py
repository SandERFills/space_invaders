class GameStats():
    """Отслеживание статистики в игре"""
    def __init__(self,game):
        self.setting=game.setting
        self.reset_stats()
        #Игра запускается в активном состоянии
        self.game_active=False
    

    def reset_stats(self):
        """Инициализация статистики и"""
        self.ships_left=self.setting.ship_limit
        self.score=0