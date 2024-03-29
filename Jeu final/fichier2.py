
import tkinter as tk 
import webbrowser
import tkinter as tk
import random
from tkinter import *
from tkinter import Widget, filedialog



fenetre = tk.Tk()
fenetre.title("2048")
score = 0 # definir le score = 0 pour le commencement du jeu 
fenetre.geometry("1000x1000")
fenetre["bg"]="dodgerBlue4" # couleur de la fenetre 

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


label1 = tk.Label(fenetre, text="Welcome to the 2048 Game ", font = ("helvetica", "30"),fg='black',bg='DodgerBlue4') # création d'un widget
label1.grid(column=0,row=10,columnspan=6)
score_label = Label(fenetre, text="Score : ", font=("Helvetica", 20))
score_label.grid(row=4, column=0)
labelfin = Label(fenetre)
labelfin.grid(row=6, column=2)



def save():
    ouvrir_fichier= filedialog.asksaveasfile(title="Partie a sauvegarder")

def load():
    ouvrir_fichier=filedialog.askopenfile(title=" Partie a reprendre")

grille = [] # une liste egal a 0 soit une liste nulle 
for i in range(4): # la boucle ici permet ajouter ici 4 petite liste 
    grille.append([0] * 4) # la fonction append permet d ajouter des 0 au petite liste donc elle sont
    # egal a zero
    #grille = matrice [0,0,0,0
     #                 0,0,0,0
    #                  0,0,0,0
    #                  0,0,0,0]

def ajoutenombre(): 
    global grille 
    x = random.randint(0, 3)  
    y = random.randint(0, 3) 
    while grille[x][y] != 0: 
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    grille[x][y] = random.choice([2,4]) 
    

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
    
def gagner(): 
    for row in grille:
        if 2048 in row: 
            return True
         
def perdu():
    for row in grille:
        if 0 in row:
           return False 
    for i in range(4): # verifie que on peut pas additonner de nombre 
        for j in range(4):
            if (i < 3 and grille[i][j] == grille[i+1][j]) or (j < 3 and grille[i][j] == grille[i][j+1]):
                return False       
    return True 
    
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






def ajoutenombre(): 
    global grille 
    x = random.randint(0, 3)  
    y = random.randint(0, 3) 
    while grille[x][y] != 0: 
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    grille[x][y] = random.choice([2,4]) 






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
        
def perdu(): 
    for row in grille:
        if 0 in row:
           return False 
    for i in range(4): # verifie que on peut pas additonner de nombre 
        for j in range(4):
            if (i < 3 and grille[i][j] == grille[i+1][j]) or (j < 3 and grille[i][j] == grille[i][j+1]):
                return False       
    return True 
            

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

affichagegrille(grille,score,fenetre)

def fonctionlieeaplay():
  ajoutenombre()
  ajoutenombre()
  affichagegrille(grille,score,fenetre)
  bouton_play.after(1,bouton_play.destroy)


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
