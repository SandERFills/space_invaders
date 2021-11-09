class GameStats():
    """Отслеживание статистики в игре"""
    def __init__(self,game):
        self.setting=game.setting
        self.reset_stats()
    

    def reset_stats(self):
        """Инициализация статистики и"""
        self.ships_left=self.setting.ship_limit