import pygame, math

r = 323  # rayon du cercle en pixel sur l'application

class SpriteVoiture(pygame.sprite.Sprite):
    def __init__(self, phase, diametre):
        super().__init__()
        self.diametre = diametre #Diametre du rond point
        self.circ = 468.54* math.pow(round(diametre*math.pi/4.2), -0.9711) # Longueur de la largeur de la bordure du rond point(pour redimensionner la voiture)
        self.couleur = "bleu"
        self.vitesse = 30  # en km/h
        self.retard = 0  # Retard/avance accumulé lors de variation de vitesse
        self.phase = phase/57.3 # Phase par rapport aux autres voitures(Seulement pour le départ)
        self.image = self.load_img()
        self.rect = self.image.get_rect()
        self.lastcall = 0 #Pour savoir quand est ce qu'est la derniere fois qu'on a demander à changer la vitesse

    def load_img(self):
        """Permet de load l'image en enlevant les bords blancs genants"""
        self.updatecolor()
        img = pygame.image.load(f"images/spritevoiture_{self.couleur}.png")
        img = pygame.transform.scale(img, (self.circ*4, self.circ*2))
        img.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        img = img.convert_alpha()
        return img

    def rot_img(self, x, y):
        "permet de faire une rotation de l'image suivant sa position dans le cercle pour donner l'effet qu'elle tourne"
        img = self.load_img()
        if x != 475:
            angle = (math.atan((400 - y) / (475 - x))) * 57.3
        else:#Dans ce cas on est aux pôles du cercle, on ne peut pas diviser par 0 alors on le fait manuellement
            if y < 200:
                angle = -90
            else:
                angle = 90
        if x < 475:
            angle += 180
        #On fait une rotation d'image par rapport au centre
        self.image = pygame.transform.rotate(img, 270 - angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, t):
        # On fait avancer la voiture
        x = self.rect.center[0]
        y = self.rect.center[1]
        self.rot_img(x, y)
        clock = pygame.time.Clock()
        # print(x,y)
        w = ((self.vitesse*2)/3.6) / (self.diametre)
        # Calcul de la position en fonction du temps et de la vitesse
        x = r * math.cos(-w * t + self.retard + self.phase) + 475
        y = 400 - (r * math.sin(-w * t + self.retard + self.phase))
        self.rect.center = [x, y]

    def changevitesse(self, vitesse, temps):
        "modifier la vitesse de la voiture"
        lastcall = self.lastcall
        self.lastcall = temps
        delta_tmps = (temps - lastcall)
        if vitesse >= 0 and vitesse != self.vitesse:
            if self.vitesse >= vitesse:
                self.retard -= (2 * temps / (self.diametre))*((self.vitesse - vitesse)/3.6)
            else:
                if (vitesse - self.vitesse) > 3:
                    vitesse = self.vitesse + 10.8*delta_tmps #10.8 étant la norme d'acceleration
                else:
                    vitesse = self.vitesse + (vitesse - self.vitesse)*delta_tmps
                self.retard += (2 * temps / (self.diametre))*((vitesse - self.vitesse)/3.6)
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
    def collide(self, spriteGroup, temps):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.changevitesse(0, temps)
            return True
        return False