import pygame
#x€[960,1270] cad  310
#y€[150,180] cad 30

class BoutonCoulissant(pygame.sprite.Sprite):
    def __init__(self, pos_y, valeur_max, valeur_init, valeur_min = 1,fond = "null"):
        super().__init__()
        if fond != "null":
            self.fond = fond
        else:
            self.fond = fond
        self.y = pos_y
        self.valeur_min = valeur_min
        self.valeur_max = valeur_max
        self.pos_init = ((valeur_init*310)/valeur_max) + 960
        self.image = pygame.Surface([7, 25])
        self.image.fill((96, 96, 96))
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_init, pos_y]

    def get_pressed(self, x):
        self.rect.center = [x, self.y]

    def valeur(self):
        if self.valeur_min != 1:
            valeur = ((self.rect[0] - 960)*self.valeur_max/310) + self.valeur_min #Règle de trois, permettant de renvoyer la valeur du bouton
        else:
            valeur = ((self.rect[0] - 960) * self.valeur_max / 310)
        if valeur > 0 and str(valeur) != 'None':
            return valeur
        return 0

    def update(self, screen, text):
        fontText = pygame.font.Font('freesansbold.ttf', 15)
        text = str(text)
        # Carré blanc, avec ou sans fond
        if self.fond != "null":
            screen.blit(pygame.image.load(self.fond), (960, self.y - 14.5))
        else:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, self.y - 14.5, 310, 30))
        # Text affiché au dessus du carré
        text = fontText.render(text, True, (255, 255, 255), (96, 96, 96))
        textRect = text.get_rect()
        textRect.center = (1120, self.y - 25.5)
        screen.blit(text, textRect)

