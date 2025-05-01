class Weapon:
    def __init__(self, name, damage, wep_range):
        self.damage = damage
        self.name = name
        self.range = wep_range

class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe", 8, 1)

class Dagger(Weapon):
    def __init__(self):
        super().__init__("Dagger", 6, 1)

class Bow(Weapon):
    def __init__(self, num_arrows = 10):
        super().__init__("Bow", 7, 3)
        self.num_arrows = num_arrows

    def fire_arrow(self):
        pass






