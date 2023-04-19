import tkinter as tk

# Créer une grille de taille 100x100 remplie de 0 (cases blanches)
grid_size = 100
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Position de départ de la fourmi au centre de la grille
ant_pos = (grid_size // 2, grid_size // 2)
# Direction de départ de la fourmi vers le nord
ant_dir = 'N'

# Créer une fenêtre Tkinter pour afficher la grille
root = tk.Tk()
root.title("Jeu de la fourmi de Langton")

# Créer un canvas Tkinter pour afficher la grille
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Afficher la grille sur le canvas en utilisant des carrés noirs pour les cases noires
def draw_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 0:
                canvas.create_rectangle(i*5, j*5, i*5+5, j*5+5, fill="white")
            else:
                canvas.create_rectangle(i*5, j*5, i*5+5, j*5+5, fill="black")

# Dessiner la grille initiale
draw_grid()

# Créer des boutons pour sauvegarder et charger le jeu
def save_game():
    # Sauvegarder l'état actuel de la grille et la position de la fourmi dans un fichier
    with open("game_state.txt", "w") as file:
        file.write(str(grid) + "\n")
        file.write(str(ant_pos[0]) + "," + str(ant_pos[1]) + "\n")
        file.write(ant_dir)

def load_game():
    # Charger l'état précédemment sauvegardé du fichier
    with open("game_state.txt", "r") as file:
        # Lire la grille et la position de la fourmi depuis le fichier
        grid_str = file.readline().rstrip()
        ant_pos_str = file.readline().rstrip()
        ant_dir_str = file.readline().rstrip()

    # Convertir les chaînes de caractères en liste et tuple respectivement
    global grid, ant_pos, ant_dir
    grid = eval(grid_str)
    ant_pos = tuple(map(int, ant_pos_str.split(',')))
    ant_dir = ant_dir_str

    # Redessiner la grille avec l'état chargé
    canvas.delete("all")
    draw_grid()

# Créer les boutons pour sauvegarder et charger le jeu
save_button = tk.Button(root, text="Sauvegarder", command=save_game)
save_button.pack(side="left")

load_button = tk.Button(root, text="Charger", command=load_game)
load_button.pack(side="right")

# Lancer la boucle principale Tkinter
root.mainloop()