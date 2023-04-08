

# propre projet 


import tkinter as tk
from tkinter import Widget, filedialog
from random import * 
from time import* 
import random

fenetre=tk.Tk()
fenetre['bg']="red"

def fermer_fenetre():
    fenetre.destroy()


tailledutableau=4


# Pris de Amin     
val_num = {
  "number": [2,4,8,16,32,64,128,256,512,1024,2048],
  "number_color":["#000000","#1A1A1A","#333333","#4D4D4D","#666666","#808080","#9A9A9A","#B3B3B3","#CDCDCD","#E6E6E6","#FFFFFF"],
  "colors_case": ["#FFE6E6","#FFB3B3","#FF8080","#FF4D4D","#FF1A1A","#FF0000","#E60000","#B30000","#800000","#4D0000","#1A0000"]
}
    
    
def play(): #Marche (100%) pris de Amin
    V=["2","2","2","2","2","2","2","4","2"]
    N=["2","2","4","2","2","2","2","2","2"]
    color1=""
    color2=""
    texte1=""
    texte2=""
    V1=choice(V)
    V2=choice(N)
    B1=choice(V)
    B2=choice(N)
    if B1=='4':
        texte1=val_num["number_color"][1]
    else:
        texte1=val_num["number_color"][0]
    if B2=='4':
        texte2=val_num["number_color"][1]
    else:
        texte2=val_num["number_color"][0]
    if V1=='4':
        color1=val_num["colors_case"][1]
    else:
        color1=val_num["colors_case"][0]
    if V2=='4':
        color2=val_num["colors_case"][1]
    else:
        color2=val_num["colors_case"][0]

    hasardrow1=randint(1,4,)
    hasardcolumn1=randint(1,4)
    hasardrow2=randint(1,4)
    hasardcolumn2=randint(1,4)

    debut1=tk.Label(fenetre, text=V1,bg=color1,fg=texte1,height=3,width=6,font=("Helvetica", 20),bd=2)
    debut1.grid(row=int(hasardrow1),column=int(hasardcolumn1))
    debut2=tk.Label(fenetre, text=V2,bg=color2,fg=texte2,height=3,width=6,font=("Helvetica", 20),bd=2)
    debut2.grid(row=int(hasardrow2),column=int(hasardcolumn2))
  




#b (pour info i=ligne , j= colonne)
# creation d une fonction pour faire bouger une ligne a gauche par exemple 
def transposeuneseulligne(row):
    # permetrre a tout les elements de bouger si possible vers la gauche but rechercher 
    for j in range (tailledutableau - 1):
      for i in range (tailledutableau -1,0,-1):
        # ici permettre au case vide d etre remplie du faite que elle se feront bouger vers les case libres
        if row[i-1] ==0 : # 
           row[i - 1] = row[i]
           row[i] = 0

    # permettre a toute les valeur de fusionner vers la gauche 
    for i in range(tailledutableau - 1):
        # test pour savoir si les deux valeurs sont identtique et pour le prochain 
        if row[i] == row[i+1]:
          row[i]*=2
          row[i + 1] = 0 

    # tous faire mettre vers la gauche encore une fois 
    for i in range(tailledutableau -1,0,-1):
        if row[i - 1]==0 :
           row[i - 1] = row[i]
           row[i]=0
    return row 

# cette fonction fusionne tous le tableau a gauche 
def transposegauche(actuelletableau):
    # fusionne tout les lignes a gauche du tableau 
    for i in range(tailledutableau):
        actuelletableau[i] = transposeuneseulligne(actuelletableau[i])

    return actuelletableau
    
# fonction pour les differentes direction 
def reverse(row):
    # tous les element dans la ligne son dans une liste et leur role sera inverser 
    new=[] # defini une nouvelle liste new
    for i in range(tailledutableau -1,-1,-1): # taille du tableau = 4 
        new.append(row[i]) # premettant d apparaitre le row 
    return new # retourner indefiniment la liste 

# fonction pour fusionner tout les element a droite 
def transposedroite(actuelletableau):
    #pour toute les ligne du tableau 
   for i in range(tailledutableau):
       # Renverse lles lignes transpose a gauche  et les reverse en arriere
       actuelletableau[i]= reverse(actuelletableau[i])
       actuelletableau[i]= transposeuneseulligne(actuelletableau[i])
       actuelletableau[i]= reverse(actuelletableau[i])
   return actuelletableau


# pour aller en haut
# la fonction transpose permet de retourner le tableau a travers une diagonale
# creation de la fonction transpose permettant la transpose dans tout le tableau 
# par exemple un element de la premiere ligne et de la deuxieme colonne,
#ira dans la deuxieme ligne de la premiere colonne
# creation de la fonction transpose 
# pas actuellement fini
def transpose(actuelletableau):
    for j in range(tailledutableau): # permmenant a des element de voir si il sont dans differente diagonale 
        for i in range(j,tailledutableau):
            if not i == j : # pour les partagers echanger les element de la diagonale
                bones = actuelletableau[j][i] # echanger les element 
                actuelletableau[j][i] = actuelletableau[i][j]
                actuelletableau[i][j] = bones # j ai choisi le bones par hasard pour definir
    return actuelletableau                    # actuelletableau[i][j]

# fonction permettant de transposer tout le tableau (on utilisera la fonction transpose gauche)
def transposetoutenhaut(actuelletableau):
    # transpose tout le tableau si il est gauche transpose en arriere 
    actuelletableau = transpose(actuelletableau)
    actuelletableau = transposegauche(actuelletableau)
    actuelletableau = transpose(actuelletableau)

    return actuelletableau

# fonction pour tout mettre en bas (on utilisera la fonction transpose droite)
def toutenbas(actuelletableau):
    actuelletableau= transpose(actuelletableau)
    actuelletableau= transposedroite(actuelletableau)
    actuelletableau= transpose(actuelletableau)

    return actuelletableau # permet de mettre a jour son tableau a chaque fois



    


    
    



    

bouton1=tk.Button(fenetre,text='Play',bg='red',command=play)
bouton1.grid(row=1,column=0)
bouton2=tk.Button(fenetre,text='Left',bg='red',command=transposegauche("actuelletableau"))
bouton2.grid(row=2,column=0)
bouton3=tk.Button(fenetre,text='Right',bg='yellow',command=transposedroite("actuelletableau"))
bouton3.grid(row=3,column=0)
bouton4=tk.Button(fenetre,text='Down',bg='black',fg='red',command=toutenbas("actuelletableau"))
bouton4.grid(row=4,column=0)
bouton5=tk.Button(fenetre,text='Up',bg='green',command=transposetoutenhaut("actuelletableau"))
bouton5.grid(row=5,column=0)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=1,column=1)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=1,column=2)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=1,column=3)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=1,column=4)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=2,column=1)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=2,column=2)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=2,column=3)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=2,column=4)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=3,column=1)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=3,column=2)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=3,column=3)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=3,column=4)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=4,column=1)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=4,column=2)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=4,column=3)
canevas=tk.Canvas(width=100,height=100,bg="white")
canevas.grid(row=4,column=4)

def save():
    ouvrir_fichier= filedialog.asksaveasfile(title="partie a sauvegarder")
def fermer_fenetre():
    fenetre.destroy()
def help():
    import tkinter as tk 
    fenetre2=tk.Tk()
    fenetre2.title("help 2048")
    fenetre2.geometry("800x800")
    label=tk.Label(fenetre2,fg="black",text="Sur une grille de 16 cases on fait bouger les tuiles pour obtenir un 2048")
    label.pack()
    fenetre2.mainloop()
import webbrowser
def partage():
    webbrowser.open("https://www.instagram.com/?hl=fr")

def avis():
    fenetre6=tk.Tk()
    fenetre6['bg']="orange"
    fenetre6.title("Note du jeu 2048")
    fenetre6.geometry("300x300")
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
     
 

    
def restart(): # marche pas demander amin 
    pass

    
    



mon_menu= tk.Menu(fenetre)
exit=tk.Menu(mon_menu,tearoff=0)
exit.add_command(label="quitter",command=fermer_fenetre)
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
mon_menu.add_cascade(label="Fichier",menu=fichier)
mon_menu.add_cascade(label="Option",menu=option)
mon_menu.add_cascade(label="Aide",menu= aide)
mon_menu.add_cascade(label="Exit",menu=exit)
mon_menu.add_cascade(label="Note",menu=notezlejeu)
mon_menu.add_cascade(label="Rejouer",menu=rejouer,command=restart)

fenetre.config(menu=mon_menu)

fenetre.mainloop() 







       