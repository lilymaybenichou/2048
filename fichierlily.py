#lily

import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import numpy as np
from random import*


#L=[[2,0,0,0]]
def grille_depart():
    nbliste=[2,2,2,2,2,2,2,2,2,4]
    L=[]
    for i in range (4):
        x=[0,0,0,0]
        L.append(x)
    y=randrange(0,4)
    i=randrange(0,4)
    z=choice(nbliste)
    L[y][i]=z 
    return L
#grille_depart()

def finjeu (grille):
    cpt = 16
    for i in range(4):
        for j in range(4) :
            if grille[i][j]!=0:
                cpt-=1
    if cpt==0 :
        return False
    else :
        return True

grille1=grille_depart()
print(grille1)

#finjeu(grille1)

def joueur_tuile():
    x=randint(0,3)
    y=randint(0,3)
    nbliste=[2,2,2,2,2,2,2,2,2,4]
    while grille1[x][y]!=0:
        x=randint(0,3)
        y=randint(0,3)
    grille1[x][y]=choice(nbliste)


#joueur_tuile(grille1)

#fonctions de directions
def mouvemement(direction):
        if direction=="down":
                for i in range(4):
                        for j in range (2,-1,-1):
                                        for y in range(j,3):
                                                if grille1[y+1][i]==0:
                                                        grille1[y+1][i]=grille1[y][i]
                                                        grille1[y][i]=0
                                                elif grille1[y+1][i]==grille1[y][i]:
                                                        grille1[y+1][i]=grille1[y+1][i]*2
                                                        grille1[y][i]=0
                                                        break
        elif direction=="up":
                for i in range(4):
                        for j in range (1,4):
                                        for y in range(j,0,-1):
                                                if grille1[y-1][i]==0:
                                                        grille1[y-1][i]=grille1[y][i]
                                                        grille1[y][i]=0
                                                elif grille1[y-1][i]==grille1[y][i]:
                                                        grille1[y-1][i]=grille1[y-1][i]*2
                                                        grille1[y][i]=0
                                                        break
        elif direction=="gauche":
                for j in range(4):
                        # Déplace les tuiles vers la gauche
                        for i in range(1, 4):
                                        for y in range(i, 0, -1):
                                                if grille1[j][y-1] == 0:
                                                        grille1[j][y-1] = grille1[j][y]
                                                        grille1[j][y] = 0
                                                elif grille1[j][y-1] == grille1[j][y]:
                                                        grille1[j][y-1] =grille1[j][y-1]* 2
                                                        grille1[j][y] = 0
                                                        break           
        elif direction=="right":     
               for j in range(4):
                        # Déplace les tuiles vers la droite
                        for i in range(2, -1, -1):
                                        for y in range(i, 3):
                                                if grille1[j][y+1] == 0:
                                                        grille1[j][y+1] = grille1[j][y]
                                                        grille1[j][y] = 0
                                                elif grille1[j][y+1] == grille1[j][y]:
                                                        grille1[j][y+1] = grille1[j][y+1]*2
                                                        grille1[j][y] = 0
                                                        break


def update_board():
    for row in range(4):
        for col in range(4):
            cell = tuiles[row][col]
            cell.config(text=str(grille1[row][col]) if grille1[row][col] else "",
                        bg=dico_couleur.get(grille1[row][col], "white"))
#affichage tkinter

fenetre=tk.Tk()
fenetre.title("2048")

tuiles=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

dico_couleur={
       2:"#B0E0E6",
       4:"#ADD8E6",
       8:"#87CEFA",
       16:"#87CEEB",
       32:"#00BFFF",
       64:"#1E90FF",
       128:"#B0C4DE",
       256:"#6495ED",
       512:"#4682B4",
       1024:"#4169E1",
       2048:"#104E8B",
}

   
#Tuiles
for j in range(0,4):
       for i in range(0,):
              tuile=tk.Label(fenetre,text="",font=('Helvetica', '30' ,'bold'),width=4, height=2, bd=2, relief="ridge")
              tuile.grid(row=j,column=i,padx=5,pady=5)
              tuiles[j][i]=tuile

#Butons
update_board()
joueur_tuile()
update_board()
#Tuiles


def appui_clavier(event):
        if event.keysym == "Left":
              mouvemement("gauche")
              joueur_tuile()
              update_board()
        elif event.keysym == "Right":
               mouvemement("droite")
               joueur_tuile()
               update_board()
        elif event.keysym == "Up":
               mouvemement("haut")
               joueur_tuile()
               update_board()
        elif event.keysym == "Down":
               mouvemement("bas")
               joueur_tuile()
               update_board()

fenetre.bind("<KeyPress>",appui_clavier)
fenetre.mainloop()
                
