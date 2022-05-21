import pygame
#x€[960,1270]
#y€[150,180]

class BoutonCoulissant(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([7, 25])
        self.image.fill((96,96,96))
        self.rect = self.image.get_rect()
        self.rect.center = [1220, 164.5]
        self.pressed = False

    def update(self):
        x, y = pygame.mouse.get_pos()
        if x > 960 and x < 1270 and y < 180 and y > 150: #Si la souris est dans le carré
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.rect.center = [x, 164.5]

    def valeur(self):
        valeur = (self.rect[0] - 960)*40/310
        if valeur > 0:
            return valeur
