import pygame
#x€[960,1270] cad  310
#y€[150,180] cad 30

class BoutonCoulissant(pygame.sprite.Sprite):
    def __init__(self, pos_y, valeur_max, valeur_init):
        super().__init__()
        self.y = pos_y
        self.valeur_max = valeur_max
        self.pos_init = ((valeur_init*310)/valeur_max) + 960
        self.image = pygame.Surface([7, 25])
        self.image.fill((96,96,96))
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_init, pos_y]
        self.pressed = False

    def get_pressed(self, x):
        self.rect.center = [x, self.y]

    def valeur(self):
        valeur = (self.rect[0] - 960)*self.valeur_max/310
        if valeur > 0 and str(valeur) != 'None':
            return valeur
        return 0
