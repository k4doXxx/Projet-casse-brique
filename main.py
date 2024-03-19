import pygame

pygame.init()

# Définition des constantes
LARGEUR_ECRAN, HAUTEUR_ECRAN = 800, 600
LARGEUR_BRIQUE, HAUTEUR_BRIQUE = 60, 20
LARGEUR_BARRE, HAUTEUR_BARRE, VITESSE_BARRE = 100, 20, 10
RAYON_BALLE, VITESSE_BALLE = 7, 7
NB_LIGNES_BRIQUES, NB_COLONNES_BRIQUES = 5, 10
BLANC, ROUGE, VERT, BLEU, NOIR = (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)
COULEURS_BRIQUES = [ROUGE, VERT, BLEU, (255, 255, 0), (255, 165, 0)]

# Configurer l'affichage
ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
pygame.display.set_caption("CASSE-BRIQUE DE LA MORT QUI TUE")


# Classes
class Barre:
    def __init__(self, x, y, largeur=LARGEUR_BARRE, hauteur=HAUTEUR_BARRE, couleur=BLANC):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur

    def deplacer(self, dx, largeur_ecran):
        self.x += dx
        if self.x < 0:
            self.x = 0
        elif self.x + self.largeur > largeur_ecran:
            self.x = largeur_ecran - self.largeur

    def dessiner(self, ecran):
        pygame.draw.rect(ecran, self.couleur, (self.x, self.y, self.largeur, self.hauteur))


class Balle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = VITESSE_BALLE
        self.vy = -VITESSE_BALLE

    def deplacer(self, largeur_ecran, hauteur_ecran):
        self.x += self.vx
        self.y += self.vy
        if self.x - RAYON_BALLE < 0 or self.x + RAYON_BALLE > largeur_ecran:
            self.vx *= -1
        if self.y - RAYON_BALLE < 0 or self.y + RAYON_BALLE > hauteur_ecran:
            self.vy *= -1

    def dessiner(self, ecran):
        pygame.draw.circle(ecran, BLANC, (int(self.x), int(self.y)), RAYON_BALLE)

    def collision_avec_barre(self, barre):
        if (barre.x < self.x < barre.x + barre.largeur) and \
                (self.y + RAYON_BALLE > barre.y and self.y - RAYON_BALLE < barre.y + barre.hauteur):
            self.vy *= -1

    def augmenter_vitesse(self):
        self.vx *= 1.01
        self.vy *= 1.01


class Brique:
    def __init__(self, x, y, largeur=LARGEUR_BRIQUE, hauteur=HAUTEUR_BRIQUE, couleur=BLANC):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.est_detruite = False

    def dessiner(self, ecran):
        if not self.est_detruite:
            pygame.draw.rect(ecran, self.couleur, (self.x, self.y, self.largeur, self.hauteur))

    def collision_avec_balle(self, balle):
        if (self.x < balle.x < self.x + self.largeur) and \
                (self.y < balle.y < self.y + self.hauteur) and not self.est_detruite:
            self.est_detruite = True
            # Déterminer si la collision est plus horizontale ou verticale
            if abs(balle.x - (self.x + self.largeur / 2)) > abs(balle.y - (self.y + self.hauteur / 2)):
                # Collision horizontale, inverser la vitesse x
                balle.vx *= -1
            else:
                # Collision verticale, inverser la vitesse y
                balle.vy *= -1
            return True
        return False


class CasseBrique:
    def __init__(self):
        self.ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
        self.barre = Barre(LARGEUR_ECRAN // 2, HAUTEUR_ECRAN - 50)
        self.balle = Balle(LARGEUR_ECRAN // 2, HAUTEUR_ECRAN // 2)
        self.briques = []
        self.initialiser_briques()
        self.score = 0
        self.vies = 3
        self.en_cours = True
        self.direction_barre = 0

    def initialiser_briques(self):
        marge_horizontale = 5
        espace_entre_briques = 5
        total_briques_largeur = NB_COLONNES_BRIQUES * LARGEUR_BRIQUE + (NB_COLONNES_BRIQUES - 1) * espace_entre_briques
        debut_x = (LARGEUR_ECRAN - total_briques_largeur) // 2

        for i in range(NB_LIGNES_BRIQUES):
            couleur_brique = COULEURS_BRIQUES[i % len(COULEURS_BRIQUES)]  # Choisir la couleur de la rangée de briques
            for j in range(NB_COLONNES_BRIQUES):
                x = debut_x + j * (LARGEUR_BRIQUE + espace_entre_briques)
                y = marge_horizontale + i * (HAUTEUR_BRIQUE + espace_entre_briques)
                brique = Brique(x, y, couleur=couleur_brique)
                self.briques.append(brique)

    def gerer_evenements(self):
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
        self.barre.deplacer(self.direction_barre * VITESSE_BARRE, LARGEUR_ECRAN)
        self.balle.deplacer(LARGEUR_ECRAN, HAUTEUR_ECRAN)
        self.balle.collision_avec_barre(self.barre)
        for brique in self.briques:
            if brique.collision_avec_balle(self.balle):
                self.score += 1
                self.balle.augmenter_vitesse()

    def afficher(self):
        self.ecran.fill(NOIR)
        self.barre.dessiner(self.ecran)
        self.balle.dessiner(self.ecran)
        for brique in self.briques:
            brique.dessiner(self.ecran)
        texte_score = pygame.font.SysFont(None, 36).render(f'Score: {self.score}', True, BLANC)
        texte_vies = pygame.font.SysFont(None, 36).render(f'Vies: {self.vies}', True, BLANC)
        self.ecran.blit(texte_score, (10, 10))
        self.ecran.blit(texte_vies, (LARGEUR_ECRAN - 110, 10))
        pygame.display.flip()

    def demarrer(self):
        while self.en_cours:
            self.gerer_evenements()
            self.mettre_a_jour()
            self.afficher()
            pygame.time.delay(30)
            if not self.en_cours:
                # Afficher un message de fin de jeu et quitter
                print("Fin du jeu. Merci d'avoir joué !")
                pygame.quit()
                break


# Démarrage du jeu
if __name__ == '__main__':
    jeu = CasseBrique()
    jeu.demarrer()
    pygame.quit()
