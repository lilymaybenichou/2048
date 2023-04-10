import tkinter as tk
import random
#nouveau brouillon 
# pour info ce brouillon a ete rediger que pour le code pas pour interface grafique
# Pour afficher le jeu
fenetre = tk.Tk()
fenetre.title("2048")
score = 0

# creation d un grille pour le jeu
grille = []
for i in range(4):
    grille.append([0] * 4)

# Fonction pour ajouter un nombre aléatoire dans la grille
def ajouter_nombre():
    global grille
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    while grille[x][y] != 0:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    grille[x][y] = random.choice([2, 4])

# Fonction pour afficher la grille
def afficher_grille():
    global grille, score
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 0:
                label = tk.Label(fenetre, text="", font=("Helvetica", 20), width=4, height=2, bg="gray")
                label.grid(row=i, column=j)
            else:
                label = tk.Label(fenetre, text=str(grille[i][j]), font=("Helvetica", 20), width=4, height=2, bg="white")
                label.grid(row=i, column=j)
    score_label.config(text="Score : " + str(score))
# Fonction pour déplacer les nombres vers la gauche
def deplacer_gauche():
    global grille, score
    for i in range(4):
        for j in range(1, 4):
            if grille[i][j] != 0:
                k = j
                while k > 0 and grille[i][k-1] == 0:
                    k -= 1
                if k != j:
                    grille[i][k] = grille[i][j]
                    grille[i][j] = 0
    for i in range(4):
        for j in range(1, 4):
            if grille[i][j] != 0 and grille[i][j] == grille[i][j-1]:
                grille[i][j-1] *= 2
                grille[i][j] = 0
                score += grille[i][j-1]
    ajouter_nombre()
    afficher_grille()
# Fonction pour déplacer les nombres vers la droite
def deplacer_droite():
    global grille, score
    for i in range(4):
        for j in range(2, -1, -1):
            if grille[i][j] != 0:
                k = j
                while k < 3 and grille[i][k+1] == 0:
                    k += 1
                if k != j:
                    grille[i][k] = grille[i][j]
                    grille[i][j] = 0
    for i in range(4):
        for j in range(2, -1, -1):
            if grille[i][j] != 0 and grille[i][j] == grille[i][j+1]:
                grille[i][j+1] = 2
                grille[i][j] = 0
                score += grille[i][j+1]
    ajouter_nombre()
    afficher_grille()

# Fonction pour déplacer les nombres vers le haut
def deplacer_haut():
    global grille, score
    for i in range(1, 4):
        for j in range(4):
            if grille[i][j] != 0:
                k = i
                while k > 0 and grille[k-1][j] == 0:
                    k -= 1
                if k != i:
                    grille[k][j] = grille[i][j]
                    grille[i][j] = 0
    for i in range(1, 4):
        for j in range(4):
            if grille[i][j] != 0 and grille[i][j] == grille[i-1][j]:
                grille[i-1][j]= 2
                grille[i][j] = 0
                score += grille[i-1][j]
    ajouter_nombre()
    afficher_grille()
    
# Fonction pour déplacer les nombres vers le bas
def deplacer_bas():
    global grille, score
    for i in range(2, -1, -1):
        for j in range(4):
            if grille[i][j] != 0:
                k = i
                while k < 3 and grille[k+1][j] == 0:
                    k += 1
                if k != i:
                    grille[k][j] = grille[i][j]
                    grille[i][j] = 0
    for i in range(2, -1, -1):
        for j in range(4):
            if grille[i][j] != 0 and grille[i][j] == grille[i+1][j]:
                grille[i+1][j] *= 2
                grille[i][j] = 0
                score += grille[i+1][j]
    ajouter_nombre()
    afficher_grille()

# Affiche le score
score_label = tk.Label(fenetre, text="Score : " + str(score), font=("Helvetica", 20))
score_label.grid(row=4, column=0, columnspan=4)
# LEs different bouton de controle
gauche_button = tk.Button(fenetre, text="Left", command=deplacer_gauche, font=("Helvetica", 20))
gauche_button.grid(row=5, column=0)
droite_button = tk.Button(fenetre, text="Right", command=deplacer_droite, font=("Helvetica", 20))
droite_button.grid(row=5, column=1)
haut_button = tk.Button(fenetre, text="UP", command=deplacer_haut, font=("Helvetica", 20))
haut_button.grid(row=5, column=2)
bas_button = tk.Button(fenetre, text="Down", command=deplacer_bas, font=("Helvetica", 20))
bas_button.grid(row=5, column=3)

# Ajout de deux nombres aléatoires dans la grille
ajouter_nombre()
ajouter_nombre()
afficher_grille()

# Lancement de la boucle principale
fenetre.mainloop()