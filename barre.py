import pygame

# Définition des constantes
LARGEUR_BARRE = 100
HAUTEUR_BARRE = 20
VITESSE_BARRE = 15
BLANC = (255, 255, 255)


class Barre:
    def __init__(self, x, y, largeur=LARGEUR_BARRE, hauteur=HAUTEUR_BARRE):
        # Initialise de la barre avec sa position et taille
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur

    def deplacer(self, dx):
        # Déplacement horizontal de la barre et l'empêche de sortir de l'écran
        self.x += dx
        if self.x < 0:
            self.x = 0
        elif self.x > LARGEUR_ECRAN - self.largeur:
            self.x = LARGEUR_ECRAN - self.largeur

    def dessiner(self, ecran):
        # Dessine la barre sur l'écran
        pygame.draw.rect(ecran, BLANC, (self.x, self.y, self.largeur, self.hauteur))


class CasseBrique:
    def __init__(self):
        # Initialise du jeu avec l'écran, la barre, le score, les vies et l'état du jeu
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        self.barre = Barre(LARGEUR_ECRAN // 2, HAUTEUR_ECRAN - 50)
        self.score = 0
        self.vies = 3
        self.en_cours = True
        self.direction_barre = 0

    def demarrer(self):
        # Boucle principale du jeu
        while self.en_cours:
            self.gerer_evenements()
            self.mettre_a_jour()
            self.afficher()
            pygame.time.delay(30)

    def bouger_barre(self, direction):
        # Déplace la barre à gauche ou à droite en fonction de l'entrée de l'utilisateur
        if direction == 'gauche':
            self.barre.deplacer(-VITESSE_BARRE)
        elif direction == 'droite':
            self.barre.deplacer(VITESSE_BARRE)

    def gerer_evenements(self):
        # Gère les événements comme la fermeture de la fenêtre et les touches du clavier
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.en_cours = False
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_LEFT:
                    self.direction_barre = -1
                elif evenement.key == pygame.K_RIGHT:
                    self.direction_barre = 1
            elif evenement.type == pygame.KEYUP:
                if evenement.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.direction_barre = 0

    def mettre_a_jour(self):
        # Met à jour la position de la barre en fonction de la direction
        if self.direction_barre != 0:
            self.barre.deplacer(self.direction_barre * VITESSE_BARRE)

    def afficher(self):
        # Affiche les éléments du jeu sur l'écran
        self.ecran.fill((0, 0, 0))
        self.barre.dessiner(self.ecran)
        # Affiche le score et les vies restantes
        texte_score = pygame.font.SysFont(None, 36).render(f'Score: {self.score}', True, BLANC)
        texte_vies = pygame.font.SysFont(None, 36).render(f'Vies: {self.vies}', True, BLANC)
        self.ecran.blit(texte_score, (10, 10))
        self.ecran.blit(texte_vies, (LARGEUR_ECRAN - 110, 10))
        pygame.display.flip()
