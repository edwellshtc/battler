#This module contains the actions for all the weapons
import random

def stab(user, target, weapon, damage):
    attack_damage = random.randint(1, damage)
    print(
        f"""
        {user} tries to stab {target} with their {weapon}  
        {user} rolls a {attack_damage} 
        """)
    return attack_damage

def slash(user, target, weapon, damage):
    attack_damage = random.randint(1, damage)
    attack_damage += 2
    print(
        f"""
        {user} tries to slash {target} with their {weapon}  
        {user} rolls a {attack_damage} 
        """)
    return attack_damage

def shoot(user, target, weapon, damage):
    attack_damage = random.randint(1, damage)
    print(
        f"""
        {user} tries to shoot {target} with their {weapon}  
        {user} rolls a {attack_damage} 
        """)
    return attack_damage

