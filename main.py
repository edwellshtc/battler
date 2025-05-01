from player import Player
from battle import *
from weapons import Weapon, Axe, Dagger


def main():
    print("****************************************")
    print("****  Welcome to the FINAL BATTLE!  ****")
    print("****************************************")
    player1 = Player("Gleddy", 50, 2, Axe())
    player2 = Player("Bandit", 30, 1, Dagger())
    battle(player1, player2)




if __name__ == "__main__":
    main()