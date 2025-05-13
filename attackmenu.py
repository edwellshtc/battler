import pygame

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, screen):

        action = False
        #mouse position
        pos = pygame.mouse.get_pos()

        #Check mouse over and clicking button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

def create_attack_button():
    attack_img = pygame.image.load('graphics/Attack_Button.png').convert_alpha()
    return Button(100, 500, attack_img)