# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |
#   | |                1er Partie :                | |
#   | |         Importation des différents         | |
#   | |                   Modules                  | |
# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |

import tkinter as tk 
import webbrowser
import tkinter as tk
import random
from tkinter import *
from tkinter import Widget, filedialog

# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |
#   | |                2eme Partie :               | |
#   | |         Affichage de la Fenetre du         | |
#   | |                 Jeu 2048                   | |
# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |

fenetre = tk.Tk()
fenetre.title("2048")
score = 0 # definir le score = 0 pour le commencement du jeu 
fenetre.geometry("1000x1000")
fenetre["bg"]="dodgerBlue4" # couleur de la fenetre 

# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |
#   | |                3eme Partie :               | |
#   | |         Dictioonnaire du numero des        | |
#   | |          cases et de leurs couleurs        | |
# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |

tile_colors = {
    2: "#fcefe6",
    4: "#f2f8cb",
    8: "#f5b682", 
    16: "#f29446", 
    32: "#ff775c", 
    64: "#e64c2e", 
    128: "#ede291", 
    256: "#fce130", 
    512: "#ffdb4a", 
    1024: "#f0b922", 
    2048: "#fad74d"
}

# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |
#   | |               4eme Partie :                | |
#   | |     Les différents Label d'affichage       | |
#   | |              (Zone de texte)               | |
# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |

label1 = tk.Label(fenetre, text="Welcome to the 2048 Game ", font = ("helvetica", "30"),fg='black',bg='DodgerBlue4') # création d'un widget
label1.grid(column=0,row=10,columnspan=6)
score_label = Label(fenetre, text="Score : ", font=("Helvetica", 20))
score_label.grid(row=4, column=0)
labelfin = Label(fenetre)
labelfin.grid(row=6, column=2)

# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |
#   | |               5eme Partie :                | |
#   | |        Les différentes fonctions du        | |
#   | |       jeu pour son bon fontionnement       | |
# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |

def save():
    ouvrir_fichier= filedialog.asksaveasfile(title="Partie a sauvegarder")

def load():
    ouvrir_fichier=filedialog.askopenfile(title=" Partie a reprendre")



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
def ajoutenombre(): 
    global grille 
    x = random.randint(0, 3)  
    y = random.randint(0, 3) 
    while grille[x][y] != 0: 
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    grille[x][y] = random.choice([2,4]) 
    
# la fonction ajouter_nombre permet de ajouter 1 nombres dans une ligne ou colonnes aleatoires tirees
# au sort 
#Pour Conclure la fonction ajouter_nombre():
#Plus Précisement cette fonction permet ajouter soit un 2 ou un 4 dans une grille de jeu 
# global grille (deja definit en commentaire )
# la fonction ici donne grace a la fontion random randint donne 2 nombre soit un 2 ou 4 dans la grille 
# ici on cherche a ce que a ce que certain endroit de la grille ne sont pas vides pour ajouter des nombres
# ensuite on ajoute soit un deux ou quatre 


# Fonction pour afficher la grille

def affichagegrille(grille, score, fenetre):
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 0:
                label = Label(fenetre, text=0, font=("Helvetica", 20), width=4, height=2, bg="white")
                label.grid(row=i, column=j)
            else:
                label = Label(fenetre, text=grille[i][j], font=("Helvetica", 20), width=4, height=2, bg=tile_colors.get(grille[i][j]))
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


   
# Fonction pour savoir si on as gagner ou non  
def gagner(): #verifie le 2048
    for row in grille:
        if 2048 in row: 
            return True
        
# Fonction pour savoir si on as perdu 
def perdu(): # verifie tout est remplie dans la grille 
    for row in grille:
        if 0 in row:
           return False 
    for i in range(4): # verifie que on peut pas additonner de nombre 
        for j in range(4):
            if (i < 3 and grille[i][j] == grille[i+1][j]) or (j < 3 and grille[i][j] == grille[i][j+1]):
                return False       
    return True 
    
# si on peut pas mutiplier de nombre et que il y pas de case vide olr un game over s'affiche
#CCL (la fonction perdu):
# ici la fonction permet de savoir si le jeu et terminé et que nous avons perdu la perdu 
# le code au debut regarde si la grille est remplie la boucle for parcourt toute les lignes de la 
# grille et regarde si il y a un 0 . Si il y a bien un zéro dans la ligne alors il y a une cases vides 
# et donc le jeu n' est pas encore fini donc on renvoie donc un false 
# mais si la grille et pleine le code regarde si on ne peut pas bouger dans la grille 
#on utilise une autre boucle for qui voie toute les cases de la grille (les ligne et les colonnes)
# ici le 3 ici correspond a la taille de la grille , la boucle for parcourt donc les indices de 0 à 3 
# ce qui donne bien 4 indices pour 4 lignes et 4 colonnes 
# ici la boucle for regardes les positions(i,j) de la grille en commencant par (0,0) en haut et a gauche 
# et ensuite de (3,3) pour en bas et a droite 
# le return True permet de de donner la permission que si on peut pas additioner aucun nombre et 
# que aucune case et vide alors on c est la fin du jeu 


# Fonction pour déplacer les nombres vers le bas
def transposebas():
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
    ajoutenombre()
    affichagegrille(grille,score,fenetre) 
    if gagner():
        label = tk.Label(fenetre, text="WIN!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Green" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)
    if perdu():
        label = tk.Label(fenetre, text="DEFEAT!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Red" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)

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
def transposehaut():
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
    ajoutenombre() 
    affichagegrille(grille,score,fenetre)
    if gagner():
        label = tk.Label(fenetre, text="WIN!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Green" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)
    if perdu():
        label = tk.Label(fenetre, text="DEFEAT!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Red" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)

# Conclusion : ici cette focntion permet de deplacer tout les nombres vers le haut 
#la 1ere boucle for ici parcourt les lignes de la deuxieme a la quatrieme ligne tandis que la 2eme boucle for ici parcourt chaque colonne 
# de la matrice  si la case contient une nombre pas egal a zero alors la fonction cherche la permiere 
# case vide en dessous de cette case et deplace le nombre 
# la deuxieme boucle double boucle (=boucle imbriquées) for permet la verification de si deux nombres 
# sont a coté dans une colonne (car elle le deplace vers le haut et si c est le cas alors )=
# il y a une addition et on deplace le resultat de l addition dans la case vide en dessous de l additon
# ensuite il y a la mise a jour 


# Fonction pour déplacer les nombres vers la gauche
def transposegauche(): 
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
                
    ajoutenombre() 
    affichagegrille(grille,score,fenetre) 
    if gagner():
        label = tk.Label(fenetre, text="WIN!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Green" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)
    if perdu(): 
        label = tk.Label(fenetre, text="DEFEAT!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Red" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)


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
def transposedroite(): 
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
    ajoutenombre() 
    affichagegrille(grille,score,fenetre) 
    if gagner():
        label = tk.Label(fenetre, text="WIN!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Green" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)
    if perdu():
        label = tk.Label(fenetre, text="DEFEAT!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Red" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)

#Conclusion :Cette Fonction permet de déplacer les nombres vers la droite ,
# la premiere boucle permet a la fonction de voyager a chaque ligne tandis que la  deuxieme boucle permet
# de parcourir de la troisieme a la premiere colonne , si la case a un nombre qui n est pas egal a zéro 
# alors la fonction cherche la premiere case vide a droite de cette case et deplace le nombre 
# la deuxieme boucle permet la verification pour savoir si deux nombres sont identiques et cote 
# a cote si c est le cas elle sont toutes les deux additionners et le resultat et deplacer dans une 
# case vide a droite 
# a la fin la fonction ajoute ensuite un nombre aleatoire et met a jour le score et affiche la nouvelle
# grille qui es mis a jour


# Affichage du score
score_label = Label(fenetre, text="Score : ", font=("Helvetica", 20))
score_label.grid(row=4, column=0)


# ici le code permet de afficher 2 chiffres lorsque l'on appuye sur le bouton play 
affichagegrille(grille,score,fenetre)
# ici le bouton play est détruit une fois après sont utilisation grace a la method after()
# pour que le bouton play ne sois pas utiliser 2 fois 
def fonctionlieeaplay():
  ajoutenombre()
  ajoutenombre()
  affichagegrille(grille,score,fenetre)
  bouton_play.after(1,bouton_play.destroy)



# LEs different bouton de controle
bouton_play=tk.Button(fenetre,text="Play",font=("Helvetica",20),command=fonctionlieeaplay,bg="DodgerBlue3")
bouton_play.grid(row=5,column=4)
gauche_button = tk.Button(fenetre, text="Left", command=transposegauche, font=("Helvetica", 20),bg="DodgerBlue3")
gauche_button.grid(row=5, column=0)
droite_button = tk.Button(fenetre, text="Right", command=transposedroite, font=("Helvetica", 20),bg="DodgerBlue3")
droite_button.grid(row=5, column=1)
haut_button = tk.Button(fenetre, text="UP", command=transposehaut, font=("Helvetica", 20),bg="DodgerBlue3")
haut_button.grid(row=5, column=2)
bas_button = tk.Button(fenetre, text="Down", command=transposebas, font=("Helvetica", 20),bg="DodgerBlue3")
bas_button.grid(row=5, column=3)




# configuration des options dans le menu 

def save():
    fichier=[('Tous Documents','*.')
             ,('Fichier Python','*.py'),
             ('Fichier Texte','*.txt'),
             ('Fichier Mp3','*.mp3')
             ]
    sauvegarderfichier= filedialog.asksaveasfile(title="Partie a sauvegarder",filetypes=fichier,defaultextension=fichier)
    
def load():
    fichier = filedialog.askopenfile(mode ='r', filetypes =[('Tous Documents','*.')
                                                           ,('Fichier Python','*.py'),
                                                            ('Fichier Texte','*.txt'),
                                                            ('Fichier Mp3','*.mp3')
                                                            ])
    if fichier is not None: #Si le fichier n'est pas nulle
        contenu = fichier.read() # le contenu du fichier est lu
        print(contenu) # Puis on print le contenu du fichier 

def fermer_fenetre():
    fenetre.destroy()

def help():
    fenetre2=tk.Tk()
    fenetre2.title("Help 2048")
    fenetre2.geometry("800x200")
    fenetre2['bg']="LemonChiffon2"
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

def partage5():
    webbrowser.open("https://www.pinterest.fr/")

def partage6():
    webbrowser.open("https://www.tiktok.com/fr/")

def avis():
    fenetre6=tk.Tk()
    fenetre6['bg']="firebrick1"
    fenetre6.title("Note du jeu 2048")
    fenetre6.geometry("1000x1000")
    label9=tk.Label(fenetre6,text="Notez le jeu 2048 les etoiles dependent de votre appreciation.",bg="firebrick1")
    label9.pack()
    app1=tk.Checkbutton(fenetre6,text="1 étoile",bg="ivory2")
    app2=tk.Checkbutton(fenetre6,text="2 étoile",bg="ivory2")
    app3=tk.Checkbutton(fenetre6,text="3 étoile",bg="ivory2")
    app4=tk.Checkbutton(fenetre6,text="4 étoile",bg="ivory2")
    app5=tk.Checkbutton(fenetre6,text="5 étoile",bg="ivory2")
    
    app1.pack()
    app2.pack()
    app3.pack()
    app4.pack()
    app5.pack()

def difficile():
    fenetre7=tk.Tk()
    fenetre7['bg']="alice blue"
    fenetre7.title("Fenetre difficulté ")
    fenetre7.geometry("400x400")
    label2=tk.Label(fenetre7,text="Vous ne pouvez pas modifier la difficulté du jeu 2048",bg="khaki",fg="blue")
    label2.pack()

def avisecrit():
    fenetre0=tk.Tk()
    fenetre0.title("Appréciation écrite")
    fenetre0.geometry("200x200")
    fenetre0['bg']="RoyalBlue2"
    edit=tk.Entry(fenetre0)
    edit.pack()
    button9=tk.Button(fenetre0,text="Envoyer") 
    button9.pack()

def play2():
  ajoutenombre()
  ajoutenombre()
  affichagegrille(grille,score,fenetre)
  
def restart():
    global grille,score
    score=0
    grille = [] 
    for i in range(4):  
        grille.append([0] * 4)
    bouton_play6=tk.Button(fenetre,text="Play",font=("Helvetica",20),command=play2,bg="DodgerBlue3")
    bouton_play6.grid(row=5,column=4)
    bouton_play6.after(5000,bouton_play6.destroy)

#Toute les fonctions que vous appercevez au dessus nous seront utile pour la conception des menus unpeu plus tard




grille = [] 
for i in range(4):
    grille.append([0] * 4) 

# Création d'une grille pour le jeu 16 cases (4x4) au début toutes les valeurs sont égales à 0
# Une liste égal à 0 est une liste nulle
# La boucle ici permet d'ajouter ici 4 petites listes
# La fonction append permet d'ajouter des 0 au petite liste donc elle sont egal à 0
#                                                                                          grille = matrice [0,0,0,0
#                                                                                                            0,0,0,0
#                                                                                                            0,0,0,0
#                                                                                                            0,0,0,0]




def ajoutenombre(): 
    global grille 
    x = random.randint(0, 3)  
    y = random.randint(0, 3) 
    while grille[x][y] != 0: 
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    grille[x][y] = random.choice([2,4]) 

# Fonction pour ajouter un nombre aléatoire dans la grille
# la fonction ajouter_nombre permet d'ajouter 1 nombre dans une ligne ou colonne aleatoire tirée au sort 
# Pour conclure la fonction ajouter_nombre():
# Plus Précisement cette fonction permet d'ajouter soit un 2 soit un 4 dans une grille de jeu global grille (deja definit en commentaire)
# la fonction ici donne grace a la fonction random randint 2 nombres soit un 2 ou 4 dans la grille
# ici on s'assure que certain endroit de la grille ne sont pas vide pour ajouter des nombres
# ensuite on ajoute soit un 2 soit un 4




def affichagegrille(grille, score, fenetre):
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 0:
                label = Label(fenetre, text=0, font=("Helvetica", 20), width=4, height=2, bg="white")
                label.grid(row=i, column=j)
            else:
                label = Label(fenetre, text=grille[i][j], font=("Helvetica", 20), width=4, height=2, bg=tile_colors.get(grille[i][j]))
                label.grid(row=i, column=j)
    score_label = Label(fenetre, text=score, font=("Helvetica", 20))
    score_label.grid(row=4, column=0, columnspan=4)
    if gagner():
        label = tk.Label(fenetre, text="WIN!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="White" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)
    
  
def gagner():
    for row in grille:
        if 2048 in row: 
            return True
        
def perdu(): # verifie tout est remplie dans la grille 
    for row in grille:
        if 0 in row:
           return False 
    for i in range(4): # verifie que on peut pas additonner de nombre 
        for j in range(4):
            if (i < 3 and grille[i][j] == grille[i+1][j]) or (j < 3 and grille[i][j] == grille[i][j+1]):
                return False       
    return True 
    
        
# Fonction pour afficher la grille
# La fonction affiche grille permet d afficher la grille dans la fenetre , la grille est stocker dans une variable globale et le score aussi
# La boucle for ici permet de parcourir la grille et vérifier si la valeur et égale a zéro 
# Si la ligne précedente est vrai alors il y a la creation d'un label totalement vide de couleur grise
# Si ce n'est pas le cas alors elle créé un label de couleur de fond blanc et la valeur score_label affiche le score actuel a cote du text "Score"
# La fonction gagner() permet de savoir on a gagné ou pas




def transposebas():
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
    ajoutenombre()
    affichagegrille(grille,score,fenetre) 
    if gagner():
        label = tk.Label(fenetre, text="WIN!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="White" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)
    if perdu():
        label = tk.Label(fenetre, text="DEFEAT!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Red" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)

# Fonction pour déplacer les nombres vers le bas
# Ici la fonction permet de déplacer les nombres vers le bas
# Puis il y a l'utilisation d'une double boucle soit for i in range et ensuite la boucle for j in range
# Cela permet de parcourir a travers les differentes cases du tableau 
# La premiere boucle for parcourt les lignes de de la troisième à la premiere tandis que la deuxieme parcourt chaque colonne
# Si une case n est pas egal a zéro, elle n'est donc pas vide, la fonction cherche et trouve la premiere
# case vide et en dessous de elle et elle regarde toutes les cases en dessous de elle dans la meme colonne
# Si il y a une case vide trouver par la fonction alors alors la fonction déplace une case non vide vers la case vide sinon elle ne fait rien 
# Lors de la seconde boucle imbriquée, la fonction parcourt à travers chaque case et signale les cases(ici 2 cases) avec
# le meme nombre de case à côté. Si c'est le cas alors la case qui est dessous est multiplier par deux 
# et la case du haut est remplacer par un zero  le score augmente a la valeur de la case du bas qui est multiplier par deux 
# A la fin, la fonction appel 2 autres fonctions soit la fonction ajouter_nombre() et la la fonction afficher_grille() pour mettre a jour la grille 




def transposehaut():
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
    ajoutenombre() 
    affichagegrille(grille,score,fenetre)
    if gagner():
        label = tk.Label(fenetre, text="WIN!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="White" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)
    if perdu():
        label = tk.Label(fenetre, text="DEFEAT!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Red" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)

# Fonction pour déplacer les nombres vers le haut
# Ici cette focntion permet de deplacer tout les nombres vers le haut 
# la 1ere boucle for ici parcourt les lignes de la deuxieme a la quatrieme ligne tandis que la 2eme boucle for ici parcourt chaque colonne 
# de la matrice si la case contient une nombre pas egal a zero alors la fonction cherche la première case vide en dessous de cette case 
# et deplace le nombre.
# la deuxieme double boucle (=boucle imbriquées) for permet de verifier si deux nombres 
# sont a coté dans une colonne (car elle le deplace vers le haut et si c est le cas alors)
# il y a une addition et on déplace le resultat de l'addition dans la case vide en dessous de l'additon ensuite il y a la mise a jour.




def transposegauche(): 
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
                
    ajoutenombre() 
    affichagegrille(grille,score,fenetre) 
    if gagner():
        label = tk.Label(fenetre, text="WIN!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="White" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)
    if perdu():
        label = tk.Label(fenetre, text="DEFEAT!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Red" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)

# Fonction pour déplacer les nombres vers la gauche
# La fonction ici permet de deplacer les nombres vers la gauche 
# la premiere boucle for voyage a travers chaque ligne tandis que la seconde avance a travers chaque colonne de la deuxieme a la quatrieme
# si une case contient un nombre pas égal a zero alors la fonction cherchera la permiere case vide 
# a gauche de cette case et elle y de placera le nombre 
# la deuxime boucle for permet la verification pour savoir si deux nombres identique sont cote a cote 
# si elle est verifier et vrai alors elle les additonen et deplace le resulat dans la case vide 
# a gauche des deux nombres identiques cote a cote additionner 
# ensuite la fonction ajoute un nombre aleatoire a la grille , affiche la grille et met a jour le score 




def transposedroite(): 
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
    ajoutenombre() 
    affichagegrille(grille,score,fenetre)
    if gagner():
        label = tk.Label(fenetre, text="WIN!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="White" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)
    if perdu():
        label = tk.Label(fenetre, text="DEFEAT!",
                        padx=20, pady=20, font = ("TimesNewRoman", "15") , fg="Red" ,bg="DodgerBlue4"
                        )
        label.grid(row=0, column=6)

# Fonction pour déplacer les nombres vers la droite
# Cette fonction permet de deplacer les nombres vers la droite ,
# la premiere boucle permet a la fonction de parcourir à chaque ligne tandis que la deuxieme boucle permet
# de parcourir de la troisieme a la premiere colonne , si la case a un nombre qui n est pas egal a zéro 
# alors la fonction cherche la premiere case vide a droite de cette case et deplace le nombre 
# la deuxieme boucle permet de verifier si deux nombres sont identiques et à côté 
# a cote si c est le cas elle sont toutes les deux additionners et le resultat et deplacer dans une case vide a droite 
# a la fin la fonction ajoute ensuite un nombre aleatoire et met a jour le score et affiche la nouvelle grille qui est mis a jour




affichagegrille(grille,score,fenetre)

# ici le code permet de afficher 2 chiffres lorsque l'on appuye sur le bouton play 




def fonctionlieeaplay():
  ajoutenombre()
  ajoutenombre()
  affichagegrille(grille,score,fenetre)
  bouton_play.after(1,bouton_play.destroy)

# ici le bouton play est détruit une fois après sont utilisation grace a la method after()
# pour que le bouton play ne sois pas utiliser 2 fois 




# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |
#   | |               6eme Partie :                | |
#   | |        Les boutons de côntrole que         | |
#   | |        nous avons relié aux fonctions      | |
# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |

bouton_play=tk.Button(fenetre,text="Play",font=("Helvetica",20),command=fonctionlieeaplay,bg="DodgerBlue3")
bouton_play.grid(row=5,column=4)

gauche_button = tk.Button(fenetre, text="Left", command=transposegauche, font=("Helvetica", 20),bg="DodgerBlue3")
gauche_button.grid(row=5, column=0)

droite_button = tk.Button(fenetre, text="Right", command=transposedroite, font=("Helvetica", 20),bg="DodgerBlue3")
droite_button.grid(row=5, column=1)

haut_button = tk.Button(fenetre, text="UP", command=transposehaut, font=("Helvetica", 20),bg="DodgerBlue3")
haut_button.grid(row=5, column=2)

bas_button = tk.Button(fenetre, text="Down", command=transposebas, font=("Helvetica", 20),bg="DodgerBlue3")
bas_button.grid(row=5, column=3)

# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |
#   | |               7eme Partie :                | |
#   | |        La configruation du menu que        | |
#   | |        nous avons relié aux fonctions      | |
# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |


mon_menu= tk.Menu(fenetre)
exit=tk.Menu(mon_menu,tearoff=0)
exit.add_command(label="Etes vous sur de vouloir quitter le jeu ",command=fermer_fenetre)
aide=tk.Menu(mon_menu,tearoff=0)
aide.add_command(label="Règle du jeu",command=help)
fichier= tk.Menu(mon_menu,tearoff=0)
fichier.add_command(label="Enregistrer sous",command=save)
fichier.add_command(label="Partager le score (Instagram)",command=partage)
fichier.add_command(label="Partager le score (Facebook)",command=partage2)
fichier.add_command(label="Partager le score(Twitter)",command=partage3)
fichier.add_command(label="Partager le score(Snapchat)",command=partage4)
fichier.add_command(label="Partager le score(Pinterest)",command=partage5)
fichier.add_command(label="Partager le score(TikTok)",command=partage6)
option = tk.Menu(mon_menu,tearoff=0)
option.add_command(label=" Difficulté ",command=difficile)
notezlejeu= tk.Menu(mon_menu,tearoff=0)
notezlejeu.add_command(label="Note",command=avis)
notezlejeu.add_command(label="Appréciation",command=avisecrit)
rejouer= tk.Menu(mon_menu,tearoff=0)
rejouer.add_command(label="Restart",command=restart)
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


# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |
#   | |              8eme Partie :                 | |
#   | |        Zone de Test echoué pour la         | |
#   | |            fonction Game Over              | |
# __| |____________________________________________| |__
#(__   ____________________________________________   __)
#   | |                                            | |

#TEST GAME OVER DE LILY-MAY

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


#TEST GAME OVER DE AMIN

#tentative echoué de la fonction game over, dans un premier temps on regarde si tout les cases sont remplis en parcourant la grille, lorsque une case
#est rempli on fais +1 a cs et si cs = 16 ça veut dire que tout les cases sont remplis donc on passe au test d'assemblage entre une case et les cases qui les entourent
#ensuite on regarde si pour tout les cases la valeur a droite a gauche en haut et en bas correspond a celle de la case pour les combiner, si ce n'est pas
#le cas pour tout les cases on peut directement renvoyez game over
#def gameover():
    #cs=0
    #for i in range(3):
        #for j in range(3):
            #if grille[i][j] != 0:
                #cs=cs+1
                #if cs==16:
                    #return(testaddition())

#def testaddition():
    #add=0
    #for i in range(3):
        #for j in range(3):
            #if i==3 and j==3:
                #if grille[i][j]!=grille[i-1][j] or grille[i][j]!=grille[i][j-1]:
                    #add=add+1
            #if i==0 and j==0:
                #if grille[i][j]!=grille[i+1][j] or grille[i][j]!=grille[i][j+1]:
                    #add=add+1
            #if i==0 and j==3:
                #if grille[i][j]!=grille[i+1][j] or grille[i][j]!=grille[i][j-1]:
                    #add=add+1
            #if i==3 and j==0:
                #if grille[i][j]!=grille[i][j+1] or grille[i][j]!=grille[i-1][j]:
                    #add=add+1
            #if (i==3 and j==2) or (i==3 and j==1):
                #if grille[i][j]!=grille[i-1][j] or grille[i][j]!=grille[i][j-1] or grille[i][j]!=grille[i][j+1]:
                    #add=add+1
            #if (i==0 and j==2) or (i==0 and j==1):
                #if grille[i][j]!=grille[i+1][j] or grille[i][j]!=grille[i][j-1] or grille[i][j]!=grille[i][j+1]:
                    #add=add+1
            #if (i==2 and j==3) or (i==1 and j==3):
                #if grille[i][j]!=grille[1][j-1] or grille[i][j]!=grille[i-1][j] or grille[i][j]!=grille[i+1][j]:
                    #add=add+1
            #if (i==2 and j==0) or (i==1 and j==0):
                #if grille[i][j]!=grille[1][j+1] or grille[i][j]!=grille[i-1][j] or grille[i][j]!=grille[i+1][j]:
                    #add=add+1
            #else:
                #if grille[i][j]!=grille[1][j+1] or grille[i][j]!=grille[i][j-1] or grille[i][j]!=grille[i+1][j] or grille[i][j]!=grille[i-1][j]:
                    #add=add+1
            #if add==16:
                #labelfin=tk.Label(fenetre,fg="black",text="Game OVER")
                #labelfin.pack()