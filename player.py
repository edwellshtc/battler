#This module contains the basic player info and data

class Player:
    def __init__(self, name, health, armour, weapon):
        self.name = name
        self.health = health
        self.armour = armour
        self.weapon = weapon

    def take_damage(self, damage):
        self.health -= damage






