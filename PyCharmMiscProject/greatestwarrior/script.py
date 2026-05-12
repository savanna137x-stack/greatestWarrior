class Warrior:
    RANKS = [
        "Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
        "Elite", "Conqueror", "Champion", "Master", "Greatest"
    ]
    MAX_LEVEL = 100
    MAX_EXPERIENCE = 10000

    def __init__(self):
        self._experience = 100
        self._level = 1
        self._rank = self._get_rank_from_level(self._level)
        self._achievements = []

    @property
    def level(self):
        return self._level

    @property
    def experience(self):
        return self._experience

    @property
    def rank(self):
        return self._rank

    @property
    def achievements(self):
        return self._achievements

    def _get_rank_from_level(self, level):
        rank_index = (level - 1) // 10
        return self.RANKS[min(rank_index, len(self.RANKS) - 1)]

    def _get_rank_index(self, rank_name):
        return self.RANKS.index(rank_name)

    def _update_level_and_rank(self):
        self._experience = min(self._experience, self.MAX_EXPERIENCE)
        self._level = min(self.MAX_LEVEL, max(1, self._experience // 100))
        self._rank = self._get_rank_from_level(self._level)

    def battle(self, enemy_level):
        if not (1 <= enemy_level <= self.MAX_LEVEL):
            return "Invalid level"

        enemy_rank = self._get_rank_from_level(enemy_level)
        if (self._get_rank_index(self.rank) < self._get_rank_index(enemy_rank) and
                enemy_level - self.level >= 5):
            return "You've been defeated"

        exp_gain = 0
        message = ""
        diff = self.level - enemy_level

        if diff == 0:
            exp_gain = 10
            message = "A good fight"
        elif diff == 1:
            exp_gain = 5
            message = "A good fight"
        elif diff >= 2:
            exp_gain = 0
            message = "Easy fight"
        elif diff < 0:
            abs_diff = abs(diff)
            exp_gain = 20 * abs_diff * abs_diff
            message = "An intense fight"

        self._experience += exp_gain
        self._update_level_and_rank()

        return message

    def training(self, training_name, experience_gain, min_level):
        if self.level < min_level:
            return "Not strong enough"

        self._experience += experience_gain
        self._update_level_and_rank()

        if training_name not in self._achievements:
            self._achievements.append(training_name)

        return training_name