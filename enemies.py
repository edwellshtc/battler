from player import Player
from weapons import Axe, Dagger, Bow

class Bandit(Player):
    def __init__(self):
        super().__init__("Bandit", 20, 1, Dagger())

class BanditArcher(Player):
    def __init__(self):
        super().__init__("Bandit Archer", 10, 1, [Bow(), Dagger()])