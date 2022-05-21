import pygame, math

r = 323

class SpriteVoiture(pygame.sprite.Sprite):
    def load_img(self):
        "Permet de load l'image en enlevant les bords blancs genants"
        img = pygame.image.load("spritevoiture 2.png")
        img.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        img = img.convert_alpha()
        return img
    def rot_img(self, x, y):
        "permet de faire une rotation de l'image suivant sa position dans le cercle pour donner l'effet qu'elle tourne"
        img = self.load_img()
        if x != 475:
            angle = (math.atan((400 - y) / (475 - x))) * 57.3
        else:
            angle = 90
        if x < 475:
            angle += 180
        #self.image = rotated_image = pygame.transform.rotate(img, 270 - angle)
        loc = img.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(img, 270 - angle)
        rot_sprite.get_rect().center = loc
        self.image = rot_sprite
        self.rect = self.image.get_rect(center=self.rect.center)
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = self.load_img()
        self.rect = self.image.get_rect(center=(pos_x,pos_y))
        self.rect.center = [pos_x, pos_y]
        self.vitesse = 30 #en km/h
    def update(self):
        #On fait avancer la voiture
        x = self.rect.center[0]
        y = self.rect.center[1]
        self.rot_img(x,y)
        clock = pygame.time.Clock()
        # print(x,y)
        t = pygame.time.get_ticks() / 1000
        w = self.vitesse*2*math.pi/230

        #Calcul de la position en fonction du temps et de la vitesse
        x = r*math.cos(-w*t) + 475
        y = 400 - (r*math.sin(-w*t))
        self.rect.center = [x, y]


