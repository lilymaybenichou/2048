import tkinter as tk
import random
fenetre = tk.Tk()
fenetre.title("2048")



HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 4
hauteur_case = HEIGHT // 4


grille = []
for i in range(4):
    grille.append([0] * 4)




canvas = tk.Canvas(fenetre, bg="red", height=HEIGHT, width=WIDTH)
canvas.grid()
for i in range(4):
    for j in range(4):
        if (i+j) % 2 == 0:
            color = "yellow"
        else:
            color = "black"
        canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)
        

# Fonction pour ajouter un nombre aléatoire dans la grille
def ajouter_nombre():
    global grille
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    while grille[x][y] != 0: # x= row , y=column
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    grille[x][y] = random.choice([2,2])















fenetre.mainloop() 


 








