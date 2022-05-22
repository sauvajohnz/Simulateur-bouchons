import pygame, math

r = 323  # rayon du cercle en pixel sur l'application


class SpriteVoiture(pygame.sprite.Sprite):
    def __init__(self, phase):
        super().__init__()
        self.couleur = "bleu"
        self.vitesse = 8  # en km/h
        self.retard = 0  # Retard/avance accumulé lors de variation de vitesse
        self.phase = phase/57.3 # Phase par rapport aux autres voitures(Seulement pour le départ)
        self.image = self.load_img()
        self.rect = self.image.get_rect()

    def load_img(self):
        """Permet de load l'image en enlevant les bords blancs genants"""
        self.updatecolor()
        img = pygame.image.load(f"spritevoiture_{self.couleur}.png")
        img.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        img = img.convert_alpha()
        return img

    def rot_img(self, x, y):
        "permet de faire une rotation de l'image suivant sa position dans le cercle pour donner l'effet qu'elle tourne"
        img = self.load_img()
        if x != 475:
            angle = (math.atan((400 - y) / (475 - x))) * 57.3
        else:
            if y < 200:
                angle = 90
            else:
                angle = -90
        if x < 475:
            angle += 180
        loc = img.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(img, 270 - angle)
        rot_sprite.get_rect().center = loc
        self.image = rot_sprite
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        # On fait avancer la voiture
        x = self.rect.center[0]
        y = self.rect.center[1]
        self.rot_img(x, y)
        clock = pygame.time.Clock()
        # print(x,y)
        self.collision = False
        t = pygame.time.get_ticks() / 1000
        w = self.vitesse * 2 * math.pi / 230
        # Calcul de la position en fonction du temps et de la vitesse
        x = r * math.cos(-w * t + self.retard + self.phase) + 475
        y = 400 - (r * math.sin(-w * t + self.retard + self.phase))
        self.rect.center = [x, y]

    def changevitesse(self, vitesse):
        "modifier la vitesse de la voiture"
        if vitesse >= 0 and vitesse != self.vitesse:
            if self.vitesse >= vitesse:
                self.retard -= (2 * math.pi * pygame.time.get_ticks() / (1000 * 230))*(self.vitesse - vitesse)
            else:
                if self.vitesse <= 5:
                    vitesse = self.vitesse +0.1
                elif self.vitesse <= 10:
                    vitesse = self.vitesse +0.3
                elif self.vitesse <= 25:
                    vitesse = self.vitesse + 0.6

                self.retard += (2 * math.pi * pygame.time.get_ticks() / (1000 * 230))*(vitesse - self.vitesse)
            self.vitesse = vitesse
            return int(self.vitesse)
        return vitesse
    def checkvitesse(self):
        "retourne la valeur de la vitesse de la voiture"
        return self.vitesse

    def updatecolor(self):
        "change la couleur de la voiture en fonction de sa vitesse"
        if self.vitesse <= 3:
            self.couleur = "rouge"
        elif self.vitesse <= 8:
            self.couleur = "orange"
        elif self.vitesse <= 15:
            self.couleur = "jaune"
        elif self.vitesse <= 20:
            self.couleur = "bleu"
        elif self.vitesse <= 25:
            self.couleur = "vertclair"
        else:
            self.couleur = "vertfonce"
        # 0-3km/h : rouge
        # 3-8km/h : orange
        # 8-15km/h : jaune
        # 15-20 km/h: bleu
        # 20-25 km/h: vert clair
        # 25-40 km/h: vert foncé
    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.collision = True
            self.changevitesse(0)