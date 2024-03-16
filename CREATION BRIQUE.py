# === CREATION BRIQUES =====
# =========================================================
def briques_creation(briques_liste):
    global init_jeu, valeurs_brique_par_rangee
    # Liste de brique crée au départ
    if not init_jeu :
#       x_brique = y_brique = 0
       x_brique = 0
       y_brique = TAILLE_BANDE_SCORE

       couleur_brique = NOMBRE_RANGEES_BRIQUES
 #      print (NOMBRE_BRIQUES)
       rangee_brique = 0
       for i in range(NOMBRE_BRIQUES):
          valeur_brique = valeurs_brique_par_rangee[rangee_brique]
          briques_liste.append([x_brique, y_brique, couleur_brique, valeur_brique])
          x_brique = x_brique + TAILLE_BRIQUE_HOR
          if(((i+1)%(NOMBRE_BRIQUES/NOMBRE_RANGEES_BRIQUES)) == 0):
               #nouvelle rangée
               x_brique = 0
               y_brique = y_brique + TAILLE_BRIQUE_VER
               couleur_brique = couleur_brique -1
               rangee_brique  = rangee_brique +1
       init_jeu = True # La partie peut commencer   
    return briques_liste
