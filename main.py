import sys, pygame
from spritevoiture import SpriteVoiture
from boutoncoulissant import BoutonCoulissant
from boutoncliquant import BoutonCliquant
from math import pow
from random import randrange
pygame.init()



###Mise en forme globale de l'application###
size = width, hight = 1280, 800
screen = pygame.display.set_mode(size)
input_rect = pygame.Rect(950,0, 330, 800)
pygame.display.set_caption('Simulateur bouchons')
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
acceleration = 1


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

placer_vehicules(voiture_init+10, diametre_init)


#Les boutons
boutons_group = pygame.sprite.Group()
boutoncoulissant1 = BoutonCoulissant(164.5, 40, 30, fond = "images/fond_vitesse_globale.png") #Vitesse globale demandee
boutoncoulissant2 = BoutonCoulissant(219.5, 100, voiture_init) #Densité vehicules
boutoncoulissant3 = BoutonCoulissant(329.5, 40, 30, fond = "images/fond_vitesse_globale.png") #Vitesse vehicule genant
boutoncliquant1 = BoutonCliquant(274.5, False) #Activer vehicule genant
boutoncoulissant4 = BoutonCoulissant(385.5, 180, diametre_init, valeur_min=10) #Diametre rond point
boutoncoulissant5 = BoutonCoulissant(445.5, 2000, 120.516) #Acceleration
boutoncoulissant6 = BoutonCoulissant(505.5, 20, 0) # Variation vitesse
boutons_group.add(boutoncoulissant1)
boutons_group.add(boutoncoulissant2)
boutons_group.add(boutoncoulissant3)
boutons_group.add(boutoncliquant1)
boutons_group.add(boutoncoulissant4)
boutons_group.add(boutoncoulissant5)
boutons_group.add(boutoncoulissant6)
#############################################################

def adapter_vitesse_voiture_genante():
    "Fonction qui adapte la vitesse de la voiture genante, si le bouton l'activant est coché ou non"
    vitesse_totale = 0
    if boutoncliquant1.valeur() == True:
        vitesse_totale += tableau_voitures[0].changevitesse(round(boutoncoulissant3.valeur()), horloge_interne)
    else:
        vitesse_totale += tableau_voitures[0].changevitesse(round(boutoncoulissant1.valeur()), horloge_interne)
    return vitesse_totale

def attribuer_variation_vitesse(vitesse_demandee, erreur, nbrvoit):
    "Ajout une marge d'erreur sur la vitesse demandée pour chaque voiture"
    vitesse_propre = []
    for i in range(nbrvoit):
        if int((erreur/100)*vitesse_demandee) != 0:
            if randrange(0,2) == 1:
                vitesse_propre.append(vitesse_demandee - int(randrange(0, int((erreur/100)*vitesse_demandee))))
            else:
                vitesse_propre.append(vitesse_demandee + int(randrange(0,int((erreur/100)*vitesse_demandee))))
        else:
            vitesse_propre.append(vitesse_demandee)
    #print(vitesse_propre)
    return vitesse_propre
vitesse_propre = [30 for i in range(12)]


#Horloge interne programme initialisation
horloge_interne = 0
horloge_pygame = 0


while 1:
    #Pour l'acceleration du programme, nous souhaitons modifier artificiellement l'horloge interne du programme
    #(ex: 10 secondes de programmes s'écoulent en 1s dans la vraie vie), on base donc l'horloge artificelle par rapport à la
    #vraie horloge, a laquel nous ajoutons un facteur multiplicatif
    diff_horloges = (pygame.time.get_ticks()/1000) - horloge_pygame #On regarde combiens de temps s'est écoulé depuis le retour a la boucle
    horloge_pygame = pygame.time.get_ticks()/1000 #On actualise la vraie horloge
    horloge_interne += diff_horloges*(boutoncoulissant5.valeur()/100) #L'horloge interne est le temps passé, multiplié par le facteur d'acceleration


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
                vitesse_propre = attribuer_variation_vitesse(round(boutoncoulissant1.valeur()), boutoncoulissant6.valeur(), round((boutoncoulissant4.valeur() * 3.141 / 4.2) * round(boutoncoulissant2.valeur()) / 100))
            elif x > 960 and x < 1270 and y < 235 and y > 205: # Bouton nombre vehicules
                boutoncoulissant2.get_pressed(x)
                placer_vehicules(round(boutoncoulissant2.valeur()), boutoncoulissant4.valeur())
                vitesse_propre = attribuer_variation_vitesse(round(boutoncoulissant1.valeur()), boutoncoulissant6.valeur(), round((boutoncoulissant4.valeur() * 3.141 / 4.2) * round(boutoncoulissant2.valeur()) / 100))
            elif x > 960 and x < 992 and y < 290 and y > 260:  # Bouton activer vehicule genant
                boutoncliquant1.get_pressed(x)
            elif x > 960 and x < 1270 and y < 345 and y > 315: # Bouton vitesse vehicule genant
                boutoncoulissant3.get_pressed(x)
            elif x > 960 and x < 1270 and y < 400 and y > 370: #Bouton diametre rond point:
                boutoncoulissant4.get_pressed(x)
                placer_vehicules(round(boutoncoulissant2.valeur()), boutoncoulissant4.valeur())
                vitesse_propre = attribuer_variation_vitesse(round(boutoncoulissant1.valeur()),boutoncoulissant6.valeur(),round((boutoncoulissant4.valeur()*3.141/4.2)*round(boutoncoulissant2.valeur())/100))
            elif x > 960 and x < 1270 and y < 460 and y > 430:  # Bouton accélerer
                boutoncoulissant5.get_pressed(x)
            elif x > 960 and x < 1270 and y < 520 and y > 490:  # Bouton accélerer
                boutoncoulissant6.get_pressed(x)
                vitesse_propre = attribuer_variation_vitesse(round(boutoncoulissant1.valeur()), boutoncoulissant6.valeur(), round((boutoncoulissant4.valeur() * 3.141 / 4.2) * round(boutoncoulissant2.valeur()) / 100))
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



    #Bouton densité vehicules#
    textVehiculeGenant = fontText.render(f"Activer vehicule genant", True,(255, 255, 255), (96, 96, 96))
    textRect5 = textVehiculeGenant.get_rect()
    textRect5.center = (1120, 275)
    screen.blit(textVehiculeGenant, textRect5)
    ########################

    #Actualisation des valeurs des boutons#
    boutoncoulissant1.update(screen, f"Vitesse globale demandée({round(boutoncoulissant1.valeur())} km/h)")
    boutoncoulissant2.update(screen, f"Densité de vehicules({nombre_voitures_actuel} vehicules)")
    boutoncoulissant3.update(screen, f"Vitesse du vehicule genant({round(boutoncoulissant3.valeur())} km/h)")
    boutoncoulissant4.update(screen, f"Diametre rond point({round(boutoncoulissant4.valeur())} m)")
    boutoncoulissant5.update(screen, f"Accélerer ({round(boutoncoulissant5.valeur())}%)")
    boutoncoulissant6.update(screen, f"Variation de vitesse ({round(boutoncoulissant6.valeur())}%)")
    #####################################

    ###Ajout des sprites###
    voiture_group.draw(screen)
    voiture_group.update(horloge_interne)
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
        if tableau_voitures[i+1].collide(voitures_devant, horloge_interne) == False:
            vitesse_totale += tableau_voitures[i+1].changevitesse(vitesse_propre[i], horloge_interne)
    voitures_devant.empty() #On regarde si le premier vehicule rentre en collision avec le dernier
    if len(tableau_voitures) > 2:
        voitures_devant.add(tableau_voitures[len(tableau_voitures)- 1])
        if tableau_voitures[0].collide(voitures_devant, horloge_interne) == False: #Si il n'y a pas collision, on peut augmenter la vitesse
            vitesse_totale += adapter_vitesse_voiture_genante()
    else:
        if len(tableau_voitures) >= 1:
            vitesse_totale += adapter_vitesse_voiture_genante()
        else:
            nombre_voitures_actuel = 1
    #####################

    #####TEXT INFO EN HAUT A GAUCHE###
    #Vitesse moyenne
    textVitesseMoyenne = fontText.render(f"Vitesse moyenne: {round(vitesse_totale/nombre_voitures_actuel)}km/h", True, (255, 255, 255), (96, 96, 96))
    screen.blit(textVitesseMoyenne, (0,0))

    #Remplissage
    textRemplMoyen = fontText.render(f"Remplissage: {round(boutoncoulissant2.valeur())}%", True, (255, 255, 255), (96, 96, 96))
    screen.blit(textRemplMoyen, (0, 14))
    ##############################


    pygame.display.flip()



