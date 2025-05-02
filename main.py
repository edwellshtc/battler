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
    background = pygame.transform.scale(background, (1200, 720))

    player_surface = pygame.image.load('graphics/Knight_idle.png')
    player_surface = pygame.transform.scale(player_surface, (500, 500)) #Resizing player image
    player_x_pos = -200

    #enemy icon, change this to take various enemies at later date?
    enemy_surface = pygame.image.load('graphics/skel_at_1.png')
    enemy_surface = pygame.transform.scale(enemy_surface, (500, 500))
    enemy_surface = pygame.transform.flip(enemy_surface, True, False) #Flip the enemies icon
    enemy_x_pos = 900


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(background,(0,0))#Display base surface - the dungeon background

        #Create player and move them from left at start
        screen.blit(player_surface,(player_x_pos, 0))
        if player_x_pos < 200:
            player_x_pos += 2

        #Create enemy and move them from right at start
        screen.blit(enemy_surface,(enemy_x_pos, 0))
        if enemy_x_pos > 500:
            enemy_x_pos -=2

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