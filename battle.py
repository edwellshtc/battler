import random
import sys

def battle(character1, character2):

    print(f"This is a battle between {character1.name} and {character2.name}")
    print(f"--{character1.name} has {character1.health}hp and {character1.armour} armour--")
    print(f"--{character2.name} has {character2.health}hp and {character2.armour} armour--")
    print(f"{character1.name} it is your turn")

    while True:
        attack(character1, character2)
        if character2.health <= 0:
            print(f"{character2.name} is dead! GAME OVER")
            sys.exit(1)
        random.shuffle(character2.weapon)
        attack(character2, character1) 
        if character1.health <= 0:
            print(f"{character1.name} is dead! GAME OVER")
            sys.exit(1)


def attack(attacker, defender):

    # rolling damage between 1 and char strength then taking off defender armour
    attack_damage = random.randint(1, attacker.weapon[0].damage)
    print(f"{attacker.name} tries to hit {defender.name} with their {attacker.weapon[0].name} and rolls a {attack_damage}")

    #check if defenders armour blocks the blow completely
    if attack_damage - defender.armour <= 0:
        print(
            f"{defender.name}'s armour completely blocks the blow!"
        )
        return

    #deal the damage
    defender.take_damage(attack_damage - defender.armour)
    print(f"{attacker.name} hits {defender.name} for {attack_damage - defender.armour} damage!")
    print(f"{defender.name}'s health is now {defender.health}hp")


