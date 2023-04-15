import tkinter as tk
import random
from tkinter import *
from tkinter import Widget, filedialog

#nouveau brouillon 
# pour info ce brouillon a ete rediger que pour le code pas pour interface grafique
# Pour afficher le jeu
fenetre = tk.Tk()
fenetre.title("2048")
score = 0
fenetre.geometry("1000x1000")
fenetre["bg"]="red"

label1 = tk.Label(fenetre, text="Welcome to the 2048 Game ", font = ("helvetica", "30"),fg="blue") # création d'un widget


label1.grid(column=6, row=6)

#Les Differentes fonctions 

def affichage():
    """ Modifie le texte d'un label. """
    global cpt
    cpt += 1
    label.config(text="tu as cliqué une fois sur le bouton play " + str(cpt)+ " fois")

cpt = 0

label = tk.Label(fenetre, text="texte avant de cliquer sur le bouton",
                  padx=20, pady=20, font = ("helvetica", "7") , fg="red" ,bg="blue"
                )
label.grid(row=0, column=6)






# creation d un grille pour le jeu
grille = []
for i in range(4):
    grille.append([0] * 4) # la grille ici permettra de definir 

# Fonction pour ajouter un nombre aléatoire dans la grille
def ajouter_nombre():
    global grille
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    while grille[x][y] != 0: # x= row , y=column
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    grille[x][y] = random.choice([2,4])


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
    score_label.config(text="Score : " + str(score))# permettant de affihcer le score 
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
                score += grille[i][j-1] # score pour augmenter le score on additionne en 
                # fonction de ce qui se passe sur la grille 
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
    ajouter_nombre()  # ajout different nombre dans la grille 
    # affiche grille permet permet de faire le changement sur la grille
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
                k = i # k=i
                while k < 3 and grille[k+1][j] == 0: # si k est different de i on ajoute
                    # on ajoute +1
                    k += 1
                if k != i:
                    grille[k][j] = grille[i][j]
                    grille[i][j] = 0
    for i in range(2, -1, -1): # on decale la grille 
        for j in range(4): # 
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
bouton_play=tk.Button(fenetre,text="Play",font=("Helvetica",20),fg="grey",bg="black",command=affichage)
bouton_play.grid(row=5,column=4)
gauche_button = tk.Button(fenetre, text="Left", command=deplacer_gauche, font=("Helvetica", 20),fg="red")
gauche_button.grid(row=5, column=0)
droite_button = tk.Button(fenetre, text="Right", command=deplacer_droite, font=("Helvetica", 20),fg="yellow")
droite_button.grid(row=5, column=1)
haut_button = tk.Button(fenetre, text="UP", command=deplacer_haut, font=("Helvetica", 20),fg="blue")
haut_button.grid(row=5, column=2)
bas_button = tk.Button(fenetre, text="Down", command=deplacer_bas, font=("Helvetica", 20),fg="green")
bas_button.grid(row=5, column=3)

# Ajout de deux nombres aléatoires dans la grille
ajouter_nombre()
ajouter_nombre()
afficher_grille()

# Menu 

mon_menu= tk.Menu(fenetre)
exit=tk.Menu(mon_menu,tearoff=0)
exit.add_command(label="quitter")
aide=tk.Menu(mon_menu,tearoff=0)
aide.add_command(label="regle du jeu",command=help)
fichier= tk.Menu(mon_menu,tearoff=0)
fichier.add_command(label="Enregistrer sous")
fichier.add_command(label="Partager score")
option = tk.Menu(mon_menu,tearoff=0)
option.add_command(label="changer qlqc")
option.add_command(label=" difficulte ")
notezlejeu= tk.Menu(mon_menu,tearoff=0)
notezlejeu.add_command(label="note")
rejouer= tk.Menu(mon_menu,tearoff=0)
rejouer.add_command(label="Restart")
mon_menu.add_cascade(label="Fichier",menu=fichier)
mon_menu.add_cascade(label="Option",menu=option)
mon_menu.add_cascade(label="Aide",menu= aide)
mon_menu.add_cascade(label="Exit",menu=exit)
mon_menu.add_cascade(label="Note",menu=notezlejeu)
mon_menu.add_cascade(label="Rejouer",menu=rejouer)

fenetre.config(menu=mon_menu)

# Lancement de la boucle principale
fenetre.mainloop()