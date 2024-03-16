import pygame

largeur_ecran = 800
hauteur_ecran = 600

pygame.init()
pygame.display.set_caption("CASSE-BRIQUE DE LA MORT QUI TUE ")

screen = pygame.display.set_mode([largeur_ecran, hauteur_ecran])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

pygame.display.flip()

pygame.quit()

class CasseBrique:
    def __init__(self, initFentetre, initBarre, initBalle, initBrique, initScore):
        self.fenetre = initFentetre
        self.barre = initBarre
        self.balle = initBalle
        self.brique = initBrique
        self.score = initScore

    def __init__(self):
        pass
