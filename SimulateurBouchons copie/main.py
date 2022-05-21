import sys, pygame
from spritevoiture import SpriteVoiture
pygame.init()


size = width, hight = 1280, 800
screen = pygame.display.set_mode(size)
input_rect = pygame.Rect(950,0, 330, 800)
pygame.display.set_caption('Simulateur bouchons')

####### Mise en forme du texte dans la section options ###
fontTitre = pygame.font.Font('freesansbold.ttf', 29)
fontSousTitre = pygame.font.Font('freesansbold.ttf', 20)

textOptions = fontSousTitre.render('Options', True, (255,255,255), (96,96,96))
textSimulateur = fontTitre.render('Simulateur bouchons', True, (255,255,255), (96,96,96))
textRect1 = textOptions.get_rect()
textRect2 = textSimulateur.get_rect()
textRect1.center = (1120,60)
textRect2.center = (1120,30)
##############################################################

#### Sprites voiture #######
voiture = SpriteVoiture(475, 77)
#voiture2 = SpriteVoiture(212,212)
#voiture3 = SpriteVoiture(747,226)
voiture_group = pygame.sprite.Group()
voiture_group.add(voiture)
#voiture_group.add(voiture2)
#voiture_group.add(voiture3)
#############################

while 1:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.KEYDOWN:
            #print(event)
            if event.key == 27:
                sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 128, 0))
    pygame.draw.rect(screen, (96, 96, 96), input_rect)
    screen.blit(textOptions, textRect1)
    screen.blit(textSimulateur, textRect2)

    pygame.draw.circle(screen, (255, 255, 255), (475, 400), 350)
    pygame.draw.circle(screen, (0, 128, 0), (475, 400), 296)
    pygame.draw.arc(screen, (0, 0, 0), (150, 80, 650, 643), 0, 360)

    voiture_group.draw(screen)
    voiture_group.update()
    pygame.display.flip()


