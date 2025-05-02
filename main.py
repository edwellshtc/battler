from player import Player
from battle import *
from weapons import Axe, Dagger, Bow
from enemies import Bandit, BanditArcher
import pygame
from sys import exit


def main():
    pygame.init()  # starting pygame
    screen = pygame.display.set_mode((1200, 720)) #Screen window size
    pygame.display.set_caption("Battler") #Naming the window
    clock = pygame.time.Clock()
    background = pygame.image.load('graphics/Battleground2.png')

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(background,(0,0)) #Display base surface - the dungeon background

        pygame.display.update()
        clock.tick(60) #making the loop run 60 times per second (or frames)


    # print("****************************************")
    # print("****  Welcome to the FINAL BATTLE!  ****")
    # print("****************************************")
    # player1 = Player("Gleddy", 20, 1, Axe())
    # player2 = BanditArcher()
    #
    # battle(player1, player2)


if __name__ == "__main__":
    main()