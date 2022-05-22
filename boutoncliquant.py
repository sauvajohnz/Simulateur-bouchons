import pygame
#x€[960,992] cad 32
#y€[150,180] cad 30

class BoutonCliquant(pygame.sprite.Sprite):
    def __init__(self, pos_y, valeur_init):
        super().__init__()
        self.y = pos_y
        self.pressed = valeur_init
        self.image = pygame.Surface([25, 25])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = [975, pos_y]

    def get_pressed(self, x):
        if self.pressed == False:
            self.pressed = True
            self.image.fill((96, 96, 96))
        else:
            self.pressed = False
            self.image.fill((255, 255, 255))
    def valeur(self):
        return self.pressed
