import tkinter as tk
import random
from tkinter import *  
  
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.geometry("400x400")
fenetre.title("Jeu 2048")


# on initialise une grille vide
grid = [[0 for i in range(4)] for j in range(4)]

# on ajoute aléatoirement un nombre 2 ou 4 au début
def init_grid():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    x, y = random.choice(empty_cells)
    grid[x][y] = random.choice([2, 4])

# on affiche la grille dans la fenêtre
def draw_grid():
    for i in range(4):
        for j in range(4):
            cell = tk.Frame(fenetre, bg="white", width=100, height=100)
            cell.grid(row=i, column=j, padx=5, pady=5)
            label = tk.Label(cell, text=str(grid[i][j]) if grid[i][j] != 0 else "",
                             font=("Helvetica", 32), justify="center")
            label.pack(expand=True)

# on bouge les tuiles vers la droite
def move_right():
    global grid

    # on parcourt chaque ligne de droite à gauche
    for i in range(4):
        for j in range(2, -1, -1):
            # si la case suivante est vide
            if grid[i][j+1] == 0:
                # on décale la tuile sur la droite
                grid[i][j+1] = grid[i][j]
                grid[i][j] = 0
            # si deux tuiles adjacentes ont la même valeur
            elif grid[i][j+1] == grid[i][j]:
                # on les fusionne
                grid[i][j+1] *= 2
                grid[i][j] = 0

    draw_grid()
    check_gameover()

# on bouge les tuiles vers la gauche
def move_left():
    global grid

# on parcourt chaque ligne de gauche à droite
    for i in range(4):
        for j in range(1, 4):
            # si la case précédente est vide
            if grid[i][j-1] == 0:
                # on décale la tuile sur la gauche
                grid[i][j-1] = grid[i][j]
                grid[i][j] = 0
            # si deux tuiles adjacentes ont la même valeur
            elif grid[i][j-1] == grid[i][j]:
                # on les fusionne
                grid[i][j-1] = 2
                grid[i][j] = 0

    draw_grid()
    check_gameover()

# on bouge les tuiles vers le bas
def move_down():
    global grid

    # on parcourt chaque colonne de bas en haut
    for i in range(2, -1, -1):
        for j in range(4):
            # si la case suivante est vide
            if grid[i+1][j] == 0:
                # on décale la tuile vers le bas
                grid[i+1][j] = grid[i][j]
                grid[i][j] = 0
            # si deux tuiles adjacentes ont la même valeur
            elif grid[i+1][j] == grid[i][j]:
                # on les fusionne
                grid[i+1][j]= 2
                grid[i][j] = 0

    draw_grid()
    check_gameover()
# on bouge les tuiles vers le haut
def move_up():
    global grid

    # on parcourt chaque colonne de haut en bas
    for i in range(1, 4):
        for j in range(4):
            # si la case précédente est vide
            if grid[i-1][j] == 0:
                # on décale la tuile vers le haut
                grid[i-1][j] = grid[i][j]
                grid[i][j] = 0
            # si deux tuiles adjacentes ont la même valeur
            elif grid[i-1][j] == grid[i][j]:
                # on les fusionne
                grid[i-1][j] *= 2
                grid[i][j] = 0

    draw_grid()
    check_gameover()

# on vérifie si le joueur a gagné
def check_win():
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return True
    return False

# on vérifie si le joueur a perdu
def check_gameover():
    # on vérifie s'il y a une case vide pour pouvoir encore bouger les tuiles
    if 0 in grid[0] or 0 in grid[1] or 0 in grid[2] or 0 in grid[3]:
        return False

    # on vérifie si deux tuiles adjacentes ont la même valeur pour pouvoir encore les fusionner
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] or grid[j][i] == grid[j+1][i]:
                return False
# si aucune des conditions de mouvement n'est satisfaite alors le joueur a perdu


# on ajoute les boutons pour chaque direction
bouton_left = tk.Button(fenetre, text="Left", command=move_left)
bouton_left.grid(row=5, column=0)

bouton_right = tk.Button(fenetre, text="Right", command=move_right)
bouton_right.grid(row=5, column=1)

bouton_up = tk.Button(fenetre, text="Up", command=move_up)
bouton_up.grid(row=5, column=2)

bouton_down = tk.Button(fenetre, text="Down", command=move_down)
bouton_down.grid(row=5, column=3)

# on initialise la grille et on affiche le jeu dans la fenêtre
init_grid()
draw_grid()

# on lance la boucle principale
fenetre.mainloop()