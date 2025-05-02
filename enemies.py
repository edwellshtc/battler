#This module contains all the enemies the player can fight against
from player import Player
from weapons import Axe, Dagger, Bow
import random

class Enemy(Player):
    def __init__(self, name, health, armour, weapon_list):
        super().__init__(name, health, armour, None)
        self.weapon_inventory = weapon_list

    def choose_weapon(self):
        self.weapon = random.choice(self.weapon_inventory)

class Bandit(Enemy):
    def __init__(self):
        super().__init__("Bandit", 20, 1, None)
        self.weapon_inventory = [Dagger()]

class BanditArcher(Enemy):
    def __init__(self):
        super().__init__("Bandit Archer", 20, 1, None)
        self.weapon_inventory = [Dagger(), Bow()]
