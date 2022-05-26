import sys, pygame
from spritevoiture import SpriteVoiture
from boutoncoulissant import BoutonCoulissant
from boutoncliquant import BoutonCliquant
from math import pow
pygame.init()
#To do:
# - Optimiser l'espace de rajout des options en mettant le code dans les class


###Mise en forme globale de l'application###
size = width, hight = 1280, 800
screen = pygame.display.set_mode(size)
input_rect = pygame.Rect(950,0, 330, 800)
pygame.display.set_caption('Simulateur bouchons')
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
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
#Les voitures
voiture_group = pygame.sprite.Group()
voiture_init = 50 # Nbr de voitures au lancement du programme
diametre_init = 26.1
tableau_voitures = []
def placer_vehicules(nbr_vehicules_pourcent, diametre):
    "Fonction qui ajoute les voitures en fonction de la densitée demandée"
    voiture_group.empty()
    nbr = round((diametre*3.141/4.2)*nbr_vehicules_pourcent/100)
    for i in range(nbr):
        voiture = SpriteVoiture((360/nbr)*(i), diametre)
        voiture_group.add(voiture)
        tableau_voitures.append(voiture)
placer_vehicules(voiture_init, diametre_init)

#Les boutons
boutons_group = pygame.sprite.Group()
boutoncoulissant1 = BoutonCoulissant(164.5, 40, 30) #Vitesse globale demandee
boutoncoulissant2 = BoutonCoulissant(219.5, 100, voiture_init) #Densité vehicules
boutoncoulissant3 = BoutonCoulissant(329.5, 40, 30) #Vitesse vehicule genant
boutoncliquant1 = BoutonCliquant(274.5, False) #Activer vehicule genant
boutoncoulissant4 = BoutonCoulissant(385.5, 180, diametre_init, valeur_min=10) #Diametre rond point
boutons_group.add(boutoncoulissant1)
boutons_group.add(boutoncoulissant2)
boutons_group.add(boutoncoulissant3)
boutons_group.add(boutoncliquant1)
boutons_group.add(boutoncoulissant4)
#############################################################

def adapter_vitesse_voiture_genante():
    "Fonction qui adapte la vitesse de la voiture genante, si le bouton l'activant est coché ou non"
    vitesse_totale = 0
    if boutoncliquant1.valeur() == True:
        vitesse_totale += tableau_voitures[0].changevitesse(round(boutoncoulissant3.valeur()))
    else:
        vitesse_totale += tableau_voitures[0].changevitesse(round(boutoncoulissant1.valeur()))
    return vitesse_totale


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
                placer_vehicules(round(boutoncoulissant2.valeur()), boutoncoulissant4.valeur())
            elif x > 960 and x < 992 and y < 290 and y > 260:  # Bouton activer vehicule genant
                boutoncliquant1.get_pressed(x)
            elif x > 960 and x < 1270 and y < 345 and y > 315: # Bouton vitesse vehicule genant
                boutoncoulissant3.get_pressed(x)
            elif x > 960 and x < 1270 and y < 400 and y > 370: #Bouton diametre rond point:
                boutoncoulissant4.get_pressed(x)
                placer_vehicules(round(boutoncoulissant2.valeur()), boutoncoulissant4.valeur())
        if event.type == pygame.QUIT:
            sys.exit()
    nombre_voitures_actuel = round((boutoncoulissant4.valeur() * 3.1419)/ 4.2*boutoncoulissant2.valeur()/100)

    screen.fill((0, 128, 0))
    pygame.draw.rect(screen, (96, 96, 96), input_rect)
    screen.blit(textOptions, textRect1)
    screen.blit(textSimulateur, textRect2)

    #######Text FPS#########
    clock.tick()  # On update la clock
    textFPS = fontText.render(f"FPS: {round(clock.get_fps())}", True, (255, 255, 255), (96, 96, 96))
    screen.blit(textFPS, (0,30))
    #######################


    #Design graphique du rond point#
    circ_ajt = 468.54 * pow(boutoncoulissant4.valeur()*3.141/4.2, -0.9711)
    pygame.draw.circle(screen, (255, 255, 255), (475, 400), 327 + circ_ajt)
    pygame.draw.circle(screen, (0, 128, 0), (475, 400), 323 - circ_ajt)
    pygame.draw.arc(screen, (0, 0, 0), (150, 80, 650, 643), 0, 360)
    ################################

    #Bouton vitesse globale#
    screen.blit(pygame.image.load("images/fond_vitesse_globale.png"), (960,150))
    textVitesseGlobal = fontText.render(f"Vitesse globale demandée({round(boutoncoulissant1.valeur())} km/h)", True, (255, 255, 255), (96, 96, 96))
    textRect3 = textVitesseGlobal.get_rect()
    textRect3.center = (1120, 140)
    screen.blit(textVitesseGlobal, textRect3)
    #########################

    #Bouton densité vehicules#
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, 205, 310, 30, width=300))
    textVehiculeGlobal = fontText.render(f"Densité de vehicules({nombre_voitures_actuel} vehicules)", True, (255, 255, 255), (96, 96, 96))
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

    #Bouton vitesse vehicule genant#
    screen.blit(pygame.image.load("images/fond_vitesse_globale.png"), (960,315))
    textVitesseVehiculeGenant = fontText.render(f"Vitesse du vehicule genant({round(boutoncoulissant3.valeur())} km/h)", True, (255, 255, 255), (96, 96, 96))
    textRect6 = textVitesseVehiculeGenant.get_rect()
    textRect6.center = (1120, 305)
    screen.blit(textVitesseVehiculeGenant, textRect6)
    ########################

    #Bouton diametre rond point#
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(960, 370, 310, 30, width=300))
    textDiametreRd = fontText.render(f"Diametre rond point({round(boutoncoulissant4.valeur())} m)", True,(255, 255, 255), (96, 96, 96))
    textRect7 = textDiametreRd.get_rect()
    textRect7.center = (1120, 360)
    screen.blit(textDiametreRd, textRect7)
    ########################


    ###Ajout des sprites###
    voiture_group.draw(screen)
    voiture_group.update()
    boutons_group.draw(screen)
    #####################

    #####Collisions######
    tableau_voitures = []
    vitesse_totale = 0 #Permet de faire une moyenne de la vitesse
    for voiture in voiture_group: #On créer un tableau de tous les véhicules
        tableau_voitures.append(voiture)
    voitures_devant = pygame.sprite.Group() #On regarde pour chaque vehicule s'il rentre en collision avec celui de devant
    for i in range(len(tableau_voitures)-1):
        voitures_devant.empty()
        voitures_devant.add(tableau_voitures[i])
        if tableau_voitures[i+1].collide(voitures_devant) == False:
            vitesse_totale += tableau_voitures[i+1].changevitesse(round(boutoncoulissant1.valeur()))
    voitures_devant.empty() #On regarde si le premier vehicule rentre en collision avec le dernier
    if len(tableau_voitures) > 2:
        voitures_devant.add(tableau_voitures[len(tableau_voitures)- 1])
        if tableau_voitures[0].collide(voitures_devant) == False: #Si il n'y a pas collision, on peut augmenter la vitesse
            vitesse_totale += adapter_vitesse_voiture_genante()
    else:
        vitesse_totale += adapter_vitesse_voiture_genante()
    #####################


    ##Text Vitesse moyenne##
    textVitesseMoyenne = fontText.render(f"Vitesse moyenne: {round(vitesse_totale/nombre_voitures_actuel)}km/h", True, (255, 255, 255), (96, 96, 96))
    screen.blit(textVitesseMoyenne, (0,0))
    #######################
    print(nombre_voitures_actuel)

    #####Text Remplissage#####
    textRemplMoyen = fontText.render(f"Remplissage: {round(boutoncoulissant2.valeur())}%", True, (255, 255, 255), (96, 96, 96))
    screen.blit(textRemplMoyen, (0, 14))
    ##########################

    pygame.display.flip()



