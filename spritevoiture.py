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
    def update(self):
        #On fait avancer la voiture
        x = self.rect.center[0]
        y = self.rect.center[1]
        self.rot_img(x,y)
        clock = pygame.time.Clock()
        # print(x,y)

        if x >= 125 and x <= 825 and y >= 50 and y <= 750: #On verifie qu'on est bien dans le cercle
            """On calcule l'angle que fais l'image par rapport au centre du rond point"""
            if x < 475 and y < 440:
                angle = math.atan((400-y)/(x-475)) - 2*math.asin(1)
            else:
                angle = (2 * math.atan(((400 - y) / r) / (1 + ((x - 475) / r))))
            print(x,y)
            print(angle*57.3)

            # On fait avancer la position de l'image 1 degrès plus loin
            x = r*math.cos(angle - 0.0172665) + 475
            y = 400 - (r*math.sin(angle - 0.0172665))
            self.rect.center = [x, y]


