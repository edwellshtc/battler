def battle(character1, character2):
    print(f"This is a battle between {character1.name} and {character2.name}")
    print(f"--{character1.name} has {character1.health}hp--")
    print(f"--{character2.name} has {character2.health}hp--")
    print(f"{character1.name} goes first!")
    attack(character1, character2)

def attack(attacker, defender):
    print(f"{attacker.name} hits {defender.name} for {attacker.strength}hp!")
    defender.take_damage(attacker.strength)
    print(f"{defender.name}'s health is now {defender.health}hp")
