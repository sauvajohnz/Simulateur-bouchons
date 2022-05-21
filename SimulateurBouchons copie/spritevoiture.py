import pygame, math
r = 323

class SpriteVoiture(pygame.sprite.Sprite):
    def load_img(self):
        "Permet de load l'image en enlevant les bords blancs genants"
        img = pygame.image.load("spritevoiture 2.png")
        img.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        img = img.convert_alpha()
        return img
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = self.load_img()
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.bas = False
        self.gauche = False
    def update(self):
        #On fait avancer la voiture
        x = self.rect.center[0]
        y = self.rect.center[1]
        print(x,y)
        clock = pygame.time.Clock()
        if x >= 125 and x <= 825 and y >= 50 and y <= 750:
            #angle = (2*math.atan( ((400 - y) / r) / (1 + ((475 - x)/ r)) ))
            if x != 475:
                angle = -math.atan((400 - y) / (475 - x))
                print(angle * 57.3)
            else:
                print("Ah!")
                if y < 100:
                    print("En haut")
                    angle = 1.57
                else:
                    print("En bas")
                    angle = -1.57
            #print(angle*57.3)
            #clock.tick(135)
            if y > 400:
                self.bas = True
            elif y < 400:
                self.bas = False
            if x > 475:
                self.gauche = False
            elif x < 475:
                self.gauche = True


            if angle > 0 and self.bas == True:
                print("a")
                angle = -(1.57 - angle) - 1.57
            elif angle < 0 and self.gauche == True:
                print("changé!")
                angle = -(1.57 - angle)  - 1.57
                print(f"angle changé={angle}")

            print(angle*57.3)
            # On fait avancer la position de l'image
            x = r*math.cos(angle - 0.0172665) + 475
            y = 400 - (r*math.sin(angle - 0.0172665))
            self.rect.center = [x, y]

            #Rotation de l'image
            img = self.load_img()
            if x != 475:
                angle = math.atan( (400-y) / (475 - x)) * 57.3
            else:
                angle = 0

            if x < 475:
                angle += 180
            self.image = rotated_image = pygame.transform.rotate(img, 270 - angle)
