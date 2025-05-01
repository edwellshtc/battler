class Player():
    name = "Gleddy"
    health = 50
    armor = 5
    strength = 5

    def take_damage(self, damage):
        self.health -= damage

