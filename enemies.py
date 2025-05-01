class Enemy():
    name = "A Bandit"
    health = 30
    armour = 3
    strength = 3

    def take_damage(self, damage):
        self.health -= damage