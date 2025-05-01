class Weapon():
    def __init__(self, name, damage):
        self.damage = damage
        self.name = name

class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe", 5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__("Dagger", 3)


