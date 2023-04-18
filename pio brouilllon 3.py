import tkinter as tk 
import webbrowser
import tkinter as tk
import random
from tkinter import *
from tkinter import Widget, filedialog
from PIL import ImageTk , Image

#nouveau brouillon 
# pour info ce brouillon a ete rediger que pour le code pas pour interface grafique
# Pour afficher le jeu
fenetre = tk.Tk()
fenetre.title("2048")
score = 0 # definir le score = 0 pour le commencement du jeu 
fenetre.geometry("1000x1000")
fenetre["bg"]="dodgerBlue4" # couleur de la fenetre 

# Pour afficher un label de bienvenue 
label1 = tk.Label(fenetre, text="Welcome to the 2048 Game ", font = ("helvetica", "30"),fg='black',bg='DodgerBlue4') # création d'un widget
label1.grid(column=0, row=10,columnspan=6)

#Les Differentes fonctions 

# Fonction en lien avec le bouton play 
def affichage():
    # modifie le texte en label 
    global cpt
    cpt += 1
    label.config(text="tu as cliqué une fois sur le bouton play " + str(cpt)+ " fois")

cpt = 0

label = tk.Label(fenetre, text="texte avant de cliquer sur le bouton",
                  padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="White" ,bg="DodgerBlue4"
                )
label.grid(row=0, column=6)






# creation d un grille pour le jeu
grille = [] # une matrice vide 
for i in range(4): # 4 ligne
    grille.append([0] * 4) # la grille ici permettra de definir on affiche au debut une grille vide
    # avec les colonnes vides 

# Fonction pour ajouter un nombre aléatoire dans la grille
def ajouter_nombre(): # ajout d'un nombre aleatoire au fil de la partie
    global grille # la fonction global permet de indiquer que la variable utilise a l interieur de la fonction et la meme que celle utiliser a exterieur 
    x = random.randint(0, 3) # ajoute dans une ligne aleatoire  
    y = random.randint(0, 3) # ajoute dans une colonne aleatoire
    while grille[x][y] != 0: # x= row , y=column ;pas egal a 0 = il y a de la place 
        x = random.randint(0, 3) # ajoute dans une ligne aleatoire
        y = random.randint(0, 3) # ajoute dans une colonne aleatoire
    grille[x][y] = random.choice([2,4]) # choisi dans la grille peut importe les lignes et les colonnes
    # soit 2,2 ou un 2,4
# la fonction ajouter_nombre permet de ajouter 2 nombres dans une ligne ou colonnes aleatoires tirees
# au sort 


               


# Fonction pour afficher la grille
def afficher_grille():
    global grille, score # definir le score pour que le score evolue
    for i in range(4): # (4)
        for j in range(4): #(4)
            if grille[i][j] == 0: # # Comme la grille =0  creation de label 
                label = tk.Label(fenetre, text="", font=("Helvetica", 20), width=4, height=2, bg="gray")# definir le label avec 4 barre grise
                label.grid(row=i, column=j) # definir que i = row et column = j 
            else:# sinon si grille[i][j] !=0 alors le else s execute
                label = tk.Label(fenetre, text=str(grille[i][j]), font=("Helvetica", 20), width=4, height=2, bg="white")
                label.grid(row=i, column=j)
    score_label.config(text="Score : " + str(score))# permettant de affihcer le score et son evolution grace au str
# Fonction pour déplacer les nombres vers la gauche
def deplacer_gauche(): # marche 100%
    global grille, score # definir le score 
    for i in range(4): #  on prent les ligne ici i sont les ligne
        for j in range(1, 4): # dans les colonnes de 1 a 4
            if grille[i][j] != 0: # si la grille n est pas egale a zero
                k = j # k=column
                while k > 0 and grille[i][k-1] == 0: # sinon si k pas egal a zeo et grille de ligne de k-1 est egal a zero
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
                grille[i][j+1] *= 2
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
                grille[i-1][j] *= 2
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
score_label = tk.Label(fenetre, text="Score : " + str(score), font=("Helvetica", 20),bg='DodgerBlue4')
score_label.grid( column=0,row=4,columnspan=3 )



# LEs different bouton de controle
bouton_play=tk.Button(fenetre,text="Play",font=("Helvetica",20),command=affichage,bg="DodgerBlue3")
bouton_play.grid(row=5,column=4)
gauche_button = tk.Button(fenetre, text="Left", command=deplacer_gauche, font=("Helvetica", 20),bg="DodgerBlue3")
gauche_button.grid(row=5, column=0)
droite_button = tk.Button(fenetre, text="Right", command=deplacer_droite, font=("Helvetica", 20),bg="DodgerBlue3")
droite_button.grid(row=5, column=1)
haut_button = tk.Button(fenetre, text="UP", command=deplacer_haut, font=("Helvetica", 20),bg="DodgerBlue3")
haut_button.grid(row=5, column=2)
bas_button = tk.Button(fenetre, text="Down", command=deplacer_bas, font=("Helvetica", 20),bg="DodgerBlue3")
bas_button.grid(row=5, column=3)

# Ajout de deux nombres aléatoires dans la grille
ajouter_nombre()
ajouter_nombre()
afficher_grille()


# configuration des options dans le menu 

def save():
    ouvrir_fichier= filedialog.asksaveasfile(title="partie a sauvegarder")
def fermer_fenetre():
    fenetre.destroy()
def help():
    fenetre2=tk.Tk()
    fenetre2.title("help 2048")
    fenetre2.geometry("800x800")
    label=tk.Label(fenetre2,fg="black",text="Sur une grille de 16 cases on fait bouger les tuiles pour obtenir le score maximum jusqu'a ce que toute les tuiles sont gelée")
    label.pack()
    fenetre2.mainloop()
def partage():
    webbrowser.open("https://www.instagram.com/?hl=fr")






def avis():
    fenetre6=tk.Tk()
    fenetre6['bg']="orange"
    fenetre6.title("Note du jeu 2048")
    fenetre6.geometry("1000x1000")
    label9=tk.Label(fenetre6,text="Notez le jeu 2048 les etoiles dependent de votre appreciation.")
    label9.pack()
    app1=tk.Button(fenetre6,text="1 etoile",fg="yellow",bg="green")
    app2=tk.Button(fenetre6,text="2 etoile",fg="yellow",bg="green")
    app3=tk.Button(fenetre6,text="3 etoile",fg="yellow",bg="green")
    app4=tk.Button(fenetre6,text="4etoile",fg="yellow",bg="green")
    app5=tk.Button(fenetre6,text="5etoile",fg="yellow",bg="green")
    
    app1.pack()
    app2.pack()
    app3.pack()
    app4.pack()
    app5.pack()




# Menu 

mon_menu= tk.Menu(fenetre)
exit=tk.Menu(mon_menu,tearoff=0)
exit.add_command(label="Etes vous sur de vouloir quitter le jeu ",command=fermer_fenetre)
aide=tk.Menu(mon_menu,tearoff=0)
aide.add_command(label="regle du jeu",command=help)
fichier= tk.Menu(mon_menu,tearoff=0)
fichier.add_command(label="Enregistrer sous",command=save)
fichier.add_command(label="Partager score",command=partage)
option = tk.Menu(mon_menu,tearoff=0)
option.add_command(label="changer qlqc")
option.add_command(label=" difficulte ")
notezlejeu= tk.Menu(mon_menu,tearoff=0)
notezlejeu.add_command(label="note",command=avis)
rejouer= tk.Menu(mon_menu,tearoff=0)
rejouer.add_command(label="Restart")
Sauvegarder=tk.Menu(mon_menu,tearoff=0) 
Sauvegarder.add_command(label="Sauvegarder")
mon_menu.add_cascade(label="Fichier",menu=fichier)
mon_menu.add_cascade(label="Option",menu=option)
mon_menu.add_cascade(label="Aide",menu= aide)
mon_menu.add_cascade(label="Exit",menu=exit)
mon_menu.add_cascade(label="Note",menu=notezlejeu)
mon_menu.add_cascade(label="Rejouer",menu=rejouer)
mon_menu.add_cascade(label="Sauvegarder",menu=Sauvegarder)

fenetre.config(menu=mon_menu)

# Lancement de la boucle principale
fenetre.mainloop()