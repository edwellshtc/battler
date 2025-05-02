from player import Player
from battle import *
from weapons import Axe, Dagger, Bow
from enemies import Bandit, BanditArcher
import pygame
from sys import exit

def main():

    def enemy_animation():
        nonlocal enemy_surface, enemy_walk_index
        enemy_walk_index += 0.1
        if enemy_walk_index >= len(enemy_walk): enemy_walk_index = 0
        enemy_surface = enemy_walk[int(enemy_walk_index)]

    def player_animation():
        nonlocal player_surface, player_walk_index
        player_walk_index += 0.2
        if player_walk_index >= len(player_walk): player_walk_index = 0
        player_surface = player_walk[int(player_walk_index)]

    pygame.init()  # starting pygame
    screen = pygame.display.set_mode((1200, 720)) #Screen window size
    pygame.display.set_caption("Battler") #Naming the window
    clock = pygame.time.Clock()

    background = pygame.image.load('graphics/Battleground2.png').convert()
    background = pygame.transform.scale(background, (1200, 720))

    player_x_pos = -200

    knight_walk_1 = pygame.image.load('graphics/knight_walk_1.png').convert_alpha()
    knight_walk_2 = pygame.image.load('graphics/knight_walk_2.png').convert_alpha()
    knight_walk_3 = pygame.image.load('graphics/knight_walk_3.png').convert_alpha()
    knight_walk_4 = pygame.image.load('graphics/knight_walk_4.png').convert_alpha()
    knight_walk_5 = pygame.image.load('graphics/knight_walk_5.png').convert_alpha()
    knight_walk_6 = pygame.image.load('graphics/knight_walk_6.png').convert_alpha()
    knight_walk_7 = pygame.image.load('graphics/knight_walk_7.png').convert_alpha()

    player_walk = [knight_walk_1, knight_walk_2, knight_walk_3, knight_walk_4, knight_walk_5, knight_walk_6, knight_walk_7]
    player_walk_index = 0
    for image in range(len(player_walk)):
        player_walk[image] = pygame.transform.scale(player_walk[image], (500, 500))

    player_surface = player_walk[player_walk_index]

    #enemy icon, change this to take various enemies at later date?

    enemy_x_pos = 900

    enemy_walk_1 = pygame.image.load('graphics/skel_walk_1.png').convert_alpha()
    enemy_walk_2 = pygame.image.load('graphics/skel_walk_2.png').convert_alpha()
    enemy_walk_3 = pygame.image.load('graphics/skel_walk_3.png').convert_alpha()
    enemy_walk_4 = pygame.image.load('graphics/skel_walk_4.png').convert_alpha()
    enemy_walk_5 = pygame.image.load('graphics/skel_walk_5.png').convert_alpha()
    enemy_walk_6 = pygame.image.load('graphics/skel_walk_6.png').convert_alpha()
    enemy_walk_7 = pygame.image.load('graphics/skel_walk_7.png').convert_alpha()

    enemy_walk = [enemy_walk_1, enemy_walk_2, enemy_walk_3, enemy_walk_4, enemy_walk_5, enemy_walk_6, enemy_walk_7]
    enemy_walk_index = 0
    for image in range(len(enemy_walk)):
        enemy_walk[image] = pygame.transform.scale(enemy_walk[image],(500, 500))
    for image in range(len(enemy_walk)):
        enemy_walk[image] = pygame.transform.flip(enemy_walk[image], True, False)

    enemy_surface = enemy_walk[enemy_walk_index]

    #MAIN GAME LOOP
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(background,(0,0))#Display base surface - the dungeon background

        #Create player and move them from left at start
        screen.blit(player_surface,(player_x_pos, 0))
        if player_x_pos < 200:
            player_x_pos += 4
            player_animation()
        if player_x_pos >= 200:
            player_surface = pygame.image.load('graphics/Knight_idle.png').convert_alpha()
            player_surface = pygame.transform.scale(player_surface, (500, 500))

        #Create enemy and move them from right at start
        screen.blit(enemy_surface,(enemy_x_pos, 0))
        if enemy_x_pos > 500:
            enemy_x_pos -=2.5
            enemy_animation()
        if enemy_x_pos <= 500:
            enemy_surface = pygame.image.load('graphics/skel_idle.png').convert_alpha()
            enemy_surface = pygame.transform.scale(enemy_surface, (500, 500))
            enemy_surface = pygame.transform.flip(enemy_surface, True, False)



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