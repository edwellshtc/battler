#This module contains the various weapons to choose from
from actions import stab, slash, shoot

class Weapon:
    def __init__(self, name, damage, wep_range, attack_type):
        self.damage = damage
        self.name = name
        self.range = wep_range
        self.attack_type = attack_type

class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe", 8, 1, [slash])

class Dagger(Weapon):
    def __init__(self):
        super().__init__("Dagger", 6, 1, [stab])

class Bow(Weapon):
    def __init__(self, num_arrows = 10):
        super().__init__("Bow", 7, 3, [shoot])
        self.num_arrows = num_arrows

    def shoot_arrow(self):
        pass






