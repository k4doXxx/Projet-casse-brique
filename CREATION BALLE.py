# ==== CREATION BALLE ====

def balles_creation(x, y, balles_liste):
    """création d'une balle avec la barre d'espace"""
    
    global nombre_balles

    # btnr pour eviter les balles multiples
    if pyxel.btnr(pyxel.KEY_SPACE):
        if (nombre_balles < MAX_BALLES):
            balles_liste.append([x+4, y-4])
            nombre_balles += 1
    return balles_liste
