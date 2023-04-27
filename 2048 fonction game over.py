def gameover():
    # Vérifier si la grille est pleine
    for row in grille:
        if 0 in row:
            return False
    # Si elle est pleine, vérifier si aucun mouvement possible ne permet de combiner des nombres
    for i in range(4):
        for j in range(4):
            if (i < 3 and grille[i][j] == grille[i+1][j]) or (j < 3 and grille[i][j] == grille[i][j+1]):
                return False
    # Si aucune combinaison ou case vide n'est possible, c'est un game over
    return True