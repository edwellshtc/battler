from player import Player
from battle import *
from weapons import Axe, Dagger, Bow
from enemies import Bandit, BanditArcher

def main():
    print("****************************************")
    print("****  Welcome to the FINAL BATTLE!  ****")
    print("****************************************")
    player1 = Player("Gleddy", 20, 1, [Axe()])
    player2 = BanditArcher()

    battle(player1, player2)


if __name__ == "__main__":
    main()