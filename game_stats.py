import json,os
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # 在此处加载最高分
        self.high_score = self.load_high_score()
        # self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        # 加载已经保存的最高分，如果没有则返回0
        try:
            if os.path.exists('high_score.json'):
                with open('high_score.json', 'r') as f:
                    return json.load(f)
        except:
            pass
        return 0

    def save_high_score(self):
        # 保存最高分到json文件中
        try:
            with open('high_score.json', 'w') as f:
                json.dump(self.high_score, f)
        except:
            pass