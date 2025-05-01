from player import Player
from enemies import Enemy
from battle import *


def main():
    print("****************************************")
    print("****  Welcome to the FINAL BATTLE!  ****")
    print("****************************************")
    player1 = Player()
    enemy = Enemy()
    battle(player1, enemy)



if __name__ == "__main__":
    main()