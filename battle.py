import random

def battle(character1, character2):

    print(f"This is a battle between {character1.name} and {character2.name}")
    print(f"--{character1.name} has {character1.health}hp--")
    print(f"--{character2.name} has {character2.health}hp--")
    print(f"{character1.name} goes first!")
    attack(character1, character2)
    attack(character2, character1)

def attack(attacker, defender):

    # rolling damage between 1 and char strength then taking off defender armour
    attack_damage = random.randint(1, attacker.weapon.damage)
    print(f"{attacker.name} tries to hit {defender.name} with their {attacker.weapon.name} and rolls a {attack_damage}")
    #check if defenders armour blocks the blow completely
    if attack_damage - defender.armour <= 0:
        print(
            f"{defender.name}'s armour completely blocks the blow!"
        )
        return
    #deal the damage
    print(f"{attacker.name} hits {defender.name} for {attack_damage - defender.armour} damage!")
    defender.take_damage(attack_damage - defender.armour)
    print(f"{defender.name}'s health is now {defender.health}hp")

