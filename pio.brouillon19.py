import tkinter as tk 
import webbrowser
import tkinter as tk
import random
from tkinter import *
from tkinter import Widget, filedialog
import copy

#nouveau brouillon 
# pour info ce brouillon a ete rediger que pour le code pas pour interface grafique
# Pour afficher le jeu
fenetre = tk.Tk()
fenetre.title("2048")
score = 0 # definir le score = 0 pour le commencement du jeu 
fenetre.geometry("1000x1000")
fenetre["bg"]="dodgerBlue4" # couleur de la fenetre 


# Pas obligatoire de mettre une image en arrière plan 
# Chargement de l'image
#bg_image = PhotoImage(file="P.png")

# Création d'un Label avec l'image en arrière-plan
#background_label = Label(fenetre, image=bg_image)
#background_label.place(relwidth=1, relheight=1)











# Pour afficher un label de bienvenue 
label1 = tk.Label(fenetre, text="Welcome to the 2048 Game ", font = ("helvetica", "30"),fg='black',bg='DodgerBlue4') # création d'un widget
label1.grid(column=0,row=10,columnspan=6)

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






# creation d un grille pour le jeu 4x4 soit 16 cases au debut toute les valeurs sont egales a 0
grille = [] # une liste egal a 0 soit une liste nulle 
for i in range(4): # la boucle ici permet ajouter ici 4 petite liste 
    grille.append([0] * 4) # la fonction append permet d ajouter des 0 au petite liste donc elle sont
    # egal a zero
    #grille = matrice [0,0,0,0
     #                 0,0,0,0
    #                  0,0,0,0
    #                  0,0,0,0]



# Fonction pour ajouter un nombre aléatoire dans la grille
def ajouter_nombre(): # ajout d'un nombre aleatoire au fil de la partie
    global grille # la fonction global permet de indiquer que la variable utilise a l interieur de la fonction et la meme que celle utiliser a exterieur 
    x = random.randint(0, 3) # ajoute dans une ligne aleatoire  
    y = random.randint(0, 3) # ajoute dans une colonne aleatoire
    while grille[x][y] != 0: # x= row , y=column ;pas egal a 0 = il y a de la place 
        x = random.randint(0, 3) # ajoute dans une ligne aleatoire
        y = random.randint(0, 3) # ajoute dans une colonne aleatoire
    grille[x][y] = random.choice([2,4]) # choisi dans la grille peut importe les lignes et les colonnes
    
# la fonction ajouter_nombre permet de ajouter 1 nombres dans une ligne ou colonnes aleatoires tirees
# au sort 

#Pour Conclure la fonction ajouter_nombre():
#Plus Précisement cette fonction permet ajouter soit un 2 ou un 4 dans une grille de jeu 
# global grille (deja definit en commentaire )
# la fonction ici donne grace a la fontion random randint donne 2 nombre soit un 2 ou 4 dans la grille 
# ici on cherche a ce que a ce que certain endroit de la grille ne sont pas vides pour ajouter des nombres
# ensuite on ajoute soit un deux ou quatre 


               


# Fonction pour afficher la grille

def afficher_grille(grille, score, fenetre):
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 0:
                label = Label(fenetre, text=0, font=("Helvetica", 20), width=4, height=2, bg="gray")
                label.grid(row=i, column=j)
            else:
                label = Label(fenetre, text=grille[i][j], font=("Helvetica", 20), width=4, height=2, bg="white")
                label.grid(row=i, column=j)
    score_label = Label(fenetre, text=score, font=("Helvetica", 20))
    score_label.grid(row=4, column=0, columnspan=4)
   


# Conclusion: la fonction affiche grille permet d afficher la grille dans la fenetre , la grille est 
# stocker dans une variable globale et le score aussi *
# la boucle for ici permet de se promener dans la grille et verifie si la valeur et egale a zéro 
# si la ligne precedente est vrai alors il y a la creation d un label  totalement vide avec de la couleur qui est
# du gris si ce n est pas le cas alors elle cree un label avec comme fond du une couleur blanche 
# et la valeur 
# score_label affiche le score actuel a cote du text "Score"



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
    afficher_grille(grille,score,fenetre) 

#Conclusion: ici la fonction permet de deplacer les nombres vers le bas 
#* 
#ici il y a l utilisation d une double boucle soit for i in range et ensuite la boucle for j in range
#Cela permet de voyager a travers les differentes cases du tableau 
# la premiere boucle for parcout les lignes de de la troisime a la premiere tandis que la deuxieme parcourt chaque colonne
#si une case n est pas egal a zero et donc elle n est pas vide , la fonction cherche et trouve la premiere
# case vide et en dessous de elle et elle regarde toutes les cases en dessous de elles dans la meme colonnes
#Si il y a une case vide trouver par la fonction alors alors la fonction deplace une case non vide vers
# la case vide sinon elle ne fait rien 
#lors de la seconde boucle imbriquée , la fonction voyage a travers chaque case et signale les cases(ici 2 cases) avec
# le meme nombres qui sont a coté  .  Si c est le cas alors la case qui est dessous est multiplier par deux 
#et la case du haut est remplacer par un zero  le score augmente a la valeur de la case du bas qui est multiplier par deux 
# A la fin , la fonction appel 2 autres fonctions soit la fonctions ici ajouter_nombre() et la 
# la fonction afficher_grille() pour mettre a jour la grille 



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
    afficher_grille(grille,score,fenetre)

# Conclusion : ici cette focntion permet de deplacer tout les nombres vers le haut 
#la 1ere boucle for ici parcourt les lignes de la deuxieme a la quatrieme ligne tandis que la 2eme boucle for ici parcourt chaque colonne 
# de la matrice  si la case contient une nombre pas egal a zero alors la fonction cherche la permiere 
# case vide en dessous de cette case et deplace le nombre 
# la deuxieme boucle double boucle (=boucle imbriquées) for permet la verification de si deux nombres 
# sont a coté dans une colonne (car elle le deplace vers le haut et si c est le cas alors )=
# il y a une addition et on deplace le resultat de l addition dans la case vide en dessous de l additon
# ensuite il y a la mise a jour 


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
    afficher_grille(grille,score,fenetre) 

# Conclusion: la fonction ici permet de deplacer les nombres vers la gauche 
# la premiere boucle for voyage a travers chaque ligne tandis que la seconde avance a travers chaque colonne de la deuxieme a la quatrieme
# si une case contient un nombre pas egal a zero alors la fonction cherhcera la permiere case vide 
# a gauche de cette case et elle y de placera le nombre 
# la deuxime boucle for permet la verification pour savoir si deux nombres identique sont cote a cote 
# si elle est verifier et vrai alors elle les additonen et deplace le resulat dans la case vide 
# a gauche des deux nombres identiques cote a cote additionner 
# ensuite la fonction ajoute un nombre aleatoire a la grille , affiche la grille et met 
# a jour le score 







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
    ajouter_nombre() 
    afficher_grille(grille,score,fenetre) 

#Conclusion :cette fonction permet de deplacer les nombres vers la droite ,
# la premiere boucle permet a la fonction de voyager a chaque ligne tandis que la  deuxieme boucle permet
# de parcourir de la troisieme a la premiere colonne , si la case a un nombre qui n est pas egal a zéro 
# alors la fonction cherche la premiere case vide a droite de cette case et deplace le nombre 
# la deuxieme boucle permet la verification pour savoir si deux nombres sont identiques et cote 
# a cote si c est le cas elle sont toutes les deux additionners et le resultat et deplacer dans une 
# case vide a droite 
# a la fin la fonction ajoute ensuite un nombre aleatoire et met a jour le score et affiche la nouvelle
# grille qui es mis a jour



    


# Affiche le score
# Affichage du score
score_label = Label(fenetre, text="Score : ", font=("Helvetica", 20))
score_label.grid(row=4, column=0)
score_value = Label(fenetre, text=score, font=("Helvetica", 20))
score_value.grid(row=4, column=1, columnspan=3)



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
afficher_grille(grille,score,fenetre)


# configuration des options dans le menu 

def save():
    ouvrir_fichier= filedialog.asksaveasfile(title="Partie a sauvegarder")
def load():
    ouvrir_fichier=filedialog.askopenfile(title=" Partie a reprendre")
def fermer_fenetre():
    fenetre.destroy()
def help():
    fenetre2=tk.Tk()
    fenetre2.title("Help 2048")
    fenetre2.geometry("800x200")
    label=tk.Label(fenetre2,fg="black",text="Sur une grille de 16 cases on fait bouger les tuiles pour obtenir le score maximum jusqu'a ce que toute les tuiles sont gelée")
    label.pack()
    fenetre2.mainloop()
def partage():
    webbrowser.open("https://www.instagram.com/?hl=fr")
def partage2():
    webbrowser.open("https://fr-fr.facebook.com/")
def partage3():
    webbrowser.open("https://twitter.com/?lang=fr")
def partage4():
    webbrowser.open("https://www.snapchat.com/fr-FR")


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

def difficile():
    fenetre2=tk.Tk()
    fenetre2['bg']="navy"
    fenetre2.title("Fenetre difficulté ")
    fenetre2.geometry("400x400")
    label2=tk.Label(fenetre2,text="Vous ne pouvez pas modifier la difficulté",bg="black",fg="white")
    label2.pack()

# savoir si la personne a perdu  fonction game over d ou elle ne peut pas bouger
#def bougepas():
    # creation de 2 copy du tableau 
   # tableaucopya= copy.deepcopy(grille) # fonction deep copy est permet de copier son tableau 
  #  tableaucopyb= copy.deepcopy(grille)
    # test de reconnaisance pour savoir si on peut bouger 
  #  tableaucopya = deplacer_bas(tableaucopya)
  #  if tableaucopya == tableaucopyb:
   #     tableaucopya = deplacer_haut(tableaucopya)
   #     if tableaucopya == tableaucopyb:
    #        tableaucopya = deplacer_gauche(tableaucopya)
    #        if tableaucopya == tableaucopyb:
    #            tableaucopya = deplacer_droite(tableaucopya)
    #            if tableaucopya == tableaucopyb:
    #                return True
   # return False
# arrete de faire (sois arrete le jeu l utilisateur ne peut plus jouer )
#arrete2048=False



# Fonction pour savoir si on as gagner ou non  
#def gagner():
   # for row in grille:
      #  if 2048 in row: 
     #       return True
 #   return False 

#while not arrete2048:
        # savoir si on as gagner 
  #  if gagner():
         #   print()
         #   print("Félicitation pour votre victoire")
          #  arrete2048=True # car le jeu ce termine apres la victoire
        # determine pas de deplacement
#else:
       #     print("Desole vous avez perdu la partie veuilez recommencer le jeu")



# Menu 

mon_menu= tk.Menu(fenetre)
exit=tk.Menu(mon_menu,tearoff=0)
exit.add_command(label="Etes vous sur de vouloir quitter le jeu ",command=fermer_fenetre)
aide=tk.Menu(mon_menu,tearoff=0)
aide.add_command(label="Règle du jeu",command=help)
fichier= tk.Menu(mon_menu,tearoff=0)
fichier.add_command(label="Enregistrer sous",command=save)
fichier.add_command(label="Partager score (Instagram)",command=partage)
fichier.add_command(label="Partager le score (Facebook)",command=partage2)
fichier.add_command(label="Partager le score(Twitter)",command=partage3)
fichier.add_command(label="Partager le score(Snapchat)",command=partage4)
option = tk.Menu(mon_menu,tearoff=0)
option.add_command(label=" Difficulté ",command=difficile)
notezlejeu= tk.Menu(mon_menu,tearoff=0)
notezlejeu.add_command(label="note",command=avis)
rejouer= tk.Menu(mon_menu,tearoff=0)
rejouer.add_command(label="Restart")
Sauvegarder=tk.Menu(mon_menu,tearoff=0) 
Sauvegarder.add_command(label="Charger une Partie",command=load)
mon_menu.add_cascade(label="Fichier",menu=fichier)
mon_menu.add_cascade(label="Option",menu=option)
mon_menu.add_cascade(label="Aide",menu= aide)
mon_menu.add_cascade(label="Exit",menu=exit)
mon_menu.add_cascade(label="Note",menu=notezlejeu)
mon_menu.add_cascade(label="Rejouer",menu=rejouer)
mon_menu.add_cascade(label="Charger une Partie",menu=Sauvegarder)

fenetre.config(menu=mon_menu)

# Lancement de la boucle principale
fenetre.mainloop()