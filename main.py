import sys, pygame
from spritevoiture import SpriteVoiture
from boutoncoulissant import BoutonCoulissant
pygame.init()


size = width, hight = 1280, 800
screen = pygame.display.set_mode(size)
input_rect = pygame.Rect(950,0, 330, 800)
pygame.display.set_caption('Simulateur bouchons')


####### Mise en forme du texte dans la section options ###
fontTitre = pygame.font.Font('freesansbold.ttf', 29)
fontSousTitre = pygame.font.Font('freesansbold.ttf', 20)
fontText = pygame.font.Font('freesansbold.ttf', 15)

textOptions = fontSousTitre.render('Options', True, (255,255,255), (96,96,96))
textSimulateur = fontTitre.render('Simulateur bouchons', True, (255,255,255), (96,96,96))
textVitesseGlobal = fontText.render("Vitesse globale demandée", True, (255,255,255), (96,96,96))
textRect1 = textOptions.get_rect()
textRect2 = textSimulateur.get_rect()
textRect3 = textVitesseGlobal.get_rect()
textRect1.center = (1120,60)
textRect2.center = (1120,30)
textRect3.center = (1120, 140)
##############################################################

#### Sprites voiture ####### Section temporaire avant l'ajout d'un bouton
voiture1 = SpriteVoiture(0)
voiture2 = SpriteVoiture(180)
#voiture3 = SpriteVoiture(747,226)
voiture_group = pygame.sprite.Group()
voiture_group.add(voiture1)
voiture_group.add(voiture2)
#voiture_group.add(voiture3)
#############################

boutons_group = pygame.sprite.Group()
boutoncoulissant1 = BoutonCoulissant(1100,160)
boutons_group.add(boutoncoulissant1)

while 1:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.KEYDOWN:
            #print(event)
            if event.key == 27:
                sys.exit()
            if event.key == 1073741906: # fleche haut
                for voiture in voiture_group.sprites():
                    voiture.changevitesse(voiture.checkvitesse()+1)
            if event.key == 1073741905: # fleche bas
                for voiture in voiture_group.sprites():
                    voiture.changevitesse(voiture.checkvitesse()-1)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 128, 0))
    pygame.draw.rect(screen, (96, 96, 96), input_rect)
    screen.blit(textOptions, textRect1)
    screen.blit(textSimulateur, textRect2)
    screen.blit(textVitesseGlobal, textRect3)

    #Design graphique du rond point#
    pygame.draw.circle(screen, (255, 255, 255), (475, 400), 350)
    pygame.draw.circle(screen, (0, 128, 0), (475, 400), 296)
    pygame.draw.arc(screen, (0, 0, 0), (150, 80, 650, 643), 0, 360)
    ################################

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, 150, 310, 30))


    voiture_group.draw(screen)
    voiture_group.update()
    boutons_group.draw(screen)
    boutons_group.update()
    for voiture in voiture_group:
        voiture.changevitesse(round(boutoncoulissant1.valeur()))
    pygame.display.flip()


