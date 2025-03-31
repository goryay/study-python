import json
from pathlib import Path


class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        path = Path('high_score.json')
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.ship_count = self.ships_left
        self.score = 0
        self.level = 1
