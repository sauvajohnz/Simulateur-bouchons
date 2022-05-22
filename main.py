import sys, pygame
from spritevoiture import SpriteVoiture
from boutoncoulissant import BoutonCoulissant
from boutoncliquant import BoutonCliquant
pygame.init()


size = width, hight = 1280, 800
screen = pygame.display.set_mode(size)
input_rect = pygame.Rect(950,0, 330, 800)
pygame.display.set_caption('Simulateur bouchons')
clock = pygame.time.Clock()


####### Mise en forme du texte dans la section options ###
fontTitre = pygame.font.Font('freesansbold.ttf', 29)
fontSousTitre = pygame.font.Font('freesansbold.ttf', 20)
fontText = pygame.font.Font('freesansbold.ttf', 15)

textOptions = fontSousTitre.render('Options', True, (255,255,255), (96,96,96))
textSimulateur = fontTitre.render('Simulateur bouchons', True, (255,255,255), (96,96,96))
textRect1 = textOptions.get_rect()
textRect2 = textSimulateur.get_rect()

textRect1.center = (1120,60)
textRect2.center = (1120,30)
#############################################################


#####################Ajout des sprites#######################
#Les voitures(Fonction car on peut demander a changer le nombre de voitures)
voiture_group = pygame.sprite.Group()
voiture1 = SpriteVoiture(0)
voiture_group.add(voiture1)
voiture_init = 2 # Nbr de voitures au lancement du programme
tableau_voitures = []
def placer_vehicules(nbr):
    voiture_group.empty()
    for i in range(nbr):
        voiture = SpriteVoiture((360/nbr)*(i))
        voiture_group.add(voiture)
        tableau_voitures.append(voiture)
placer_vehicules(voiture_init)

#Les boutons
boutons_group = pygame.sprite.Group()
boutoncoulissant1 = BoutonCoulissant(164.5, 40, 30) #Vitesse globale demandee
boutoncoulissant2 = BoutonCoulissant(219.5, 17, voiture_init) #Densité vehicules
boutoncoulissant3 = BoutonCoulissant(329.5, 40, 30) #Vitesse vehicule genant
boutoncliquant1 = BoutonCliquant(274.5, False) #Activer vehicule genant
boutons_group.add(boutoncoulissant1)
boutons_group.add(boutoncoulissant2)
boutons_group.add(boutoncoulissant3)
boutons_group.add(boutoncliquant1)
#############################################################


while 1:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.KEYDOWN:
            #print(event)
            if event.key == 27:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONUP :
            x, y = pygame.mouse.get_pos()
            if x > 960 and x < 1270 and y < 180 and y > 150:  # Bouton vitesse globale
                boutoncoulissant1.get_pressed(x)
            elif x > 960 and x < 1270 and y < 235 and y > 205: # Bouton nombre vehicules
                boutoncoulissant2.get_pressed(x)
                placer_vehicules(round(boutoncoulissant2.valeur()))
            elif x > 960 and x < 992 and y < 290 and y > 260:  # Bouton vitesse globale
                boutoncliquant1.get_pressed(x)
            elif x > 960 and x < 1270 and y < 345 and y > 315:
                boutoncoulissant3.get_pressed(x)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 128, 0))
    pygame.draw.rect(screen, (96, 96, 96), input_rect)
    screen.blit(textOptions, textRect1)
    screen.blit(textSimulateur, textRect2)

    #######Text FPS#########
    clock.tick()  # On update la clock
    textFPS = fontText.render(f"FPS: {round(clock.get_fps())}", True, (255, 255, 255), (96, 96, 96))
    textRect5 = textFPS.get_rect()
    textRect5.center = (27, 8)
    screen.blit(textFPS, textRect5)
    #######################


    #Design graphique du rond point#
    pygame.draw.circle(screen, (255, 255, 255), (475, 400), 350)
    pygame.draw.circle(screen, (0, 128, 0), (475, 400), 296)
    pygame.draw.arc(screen, (0, 0, 0), (150, 80, 650, 643), 0, 360)
    ################################

    #Bouton vitesse globale#
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, 150, 310, 30))
    textVitesseGlobal = fontText.render(f"Vitesse globale demandée({round(boutoncoulissant1.valeur())} km/h)", True, (255, 255, 255), (96, 96, 96))
    textRect3 = textVitesseGlobal.get_rect()
    textRect3.center = (1120, 140)
    screen.blit(textVitesseGlobal, textRect3)
    #########################

    #Bouton nombre vehicules#
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, 205, 310, 30))
    textVehiculeGlobal = fontText.render(f"Densité de vehicules({round(boutoncoulissant2.valeur())} vehicules)", True, (255, 255, 255), (96, 96, 96))
    textRect4 = textVehiculeGlobal.get_rect()
    textRect4.center = (1120, 195)
    screen.blit(textVehiculeGlobal, textRect4)
    ########################

    #Bouton activer vebicule genant#
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, 260, 32, 30))
    textVehiculeGenant = fontText.render(f"Activer vehicule genant", True,(255, 255, 255), (96, 96, 96))
    textRect5 = textVehiculeGenant.get_rect()
    textRect5.center = (1120, 275)
    screen.blit(textVehiculeGenant, textRect5)
    ########################

    # Bouton vitesse vehicule genant#
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, 315, 310, 30))
    textVitesseVehiculeGenant = fontText.render(f"Vitesse du vehicule genant({round(boutoncoulissant3.valeur())} km/h)", True, (255, 255, 255), (96, 96, 96))
    textRect6 = textVitesseVehiculeGenant.get_rect()
    textRect6.center = (1120, 305)
    screen.blit(textVitesseVehiculeGenant, textRect6)
    ########################


    ###Ajout des sprites###
    voiture_group.draw(screen)
    voiture_group.update()
    boutons_group.draw(screen)
    #####################

    #####Vitesse#####
    for voiture in voiture_group: #On distingue le vehicule genant des autres vehicules
        if voiture == tableau_voitures[0] and boutoncliquant1.valeur() == True:
            tableau_voitures[0].changevitesse(round(boutoncoulissant3.valeur()))
        else:
            voiture.changevitesse(round(boutoncoulissant1.valeur()))
    ######################

    #####Collisions######
    tableau_voitures = []
    for voiture in voiture_group:
        tableau_voitures.append(voiture)
    voitures_devant = pygame.sprite.Group() #On regarde pour chaque vehicule s'il rentre en collision avec celui de devant
    for i in range(len(tableau_voitures)-1):
        voitures_devant.empty()
        voitures_devant.add(tableau_voitures[i])
        tableau_voitures[i+1].collide(voitures_devant)
    voitures_devant.empty() #On regarde si le premier vehicule rentre en collision avec le dernier
    voitures_devant.add(tableau_voitures[len(tableau_voitures)- 1])
    tableau_voitures[0].collide(voitures_devant)
    #####################


    pygame.display.flip()



