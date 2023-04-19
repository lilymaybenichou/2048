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
    y=randrange(0,2)
    i=randrange(0,2)
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
                               if grille1[i][j]!=0:
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
                               if grille1[i][j]!=0:
                                        for y in range(j,0,-1):
                                                if grille1[y-1][i]==0:
                                                        grille1[y-1][i]=grille1[y][i]
                                                        grille1[y][i]=0
                                                elif grille1[y-1][i]==grille1[y][i]:
                                                        grille1[y-1][i]=grille1[y-1][i]*2
                                                        grille1[y][i]=0
                                                        break
        elif direction=="gauche"
                for j in range(4):
                        # Déplace les tuiles vers la gauche
                        for i in range(1, 4):
                                if grille1[j][i] != 0:
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
                                if grille1[j][i] != 0:
                                        for y in range(i, 3):
                                                if grille1[j][y+1] == 0:
                                                        grille1[j][y+1] = grille1[j][y]
                                                        grille1[j][y] = 0
                                                elif grille1[j][y+1] == grille1[j][y]:
                                                        grille1[j][y+1] = grille1[j][y+1]*2
                                                        grille1[j][y] = 0
                                                        break



#affichage tkinter

fenetre=tk.Tk()
fenetre.title("2048")

#Butons
exit=tk.Button(fenetre,text='Exit',command=lambda:mouvemement("left",grille1))
exit.grid(column=0,row=3)

save=tk.Button(fenetre,text='Save')
save.grid(column=0,row=2)

load=tk.Button(fenetre,text='Load')
load.grid(column=0,row=1)

start=tk.Button(fenetre,text='Start')
start.grid(column=0,row=0)

#Tuiles
tuile1=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile1.create_text(60, 60, text= str(grille1[0][0]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile1.grid(column=1,row=0)

tuile2=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile2.create_text(60, 60, text= str(grille1[0][1]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile2.grid(column=2,row=0)

tuile3=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile3.create_text(60, 60, text= str(grille1[0][2]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile3.grid(column=3,row=0)

tuile4=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile4.create_text(60, 60, text= str(grille1[0][3]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile4.grid(column=4,row=0)

tuile5=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile5.create_text(60, 60, text= str(grille1[1][0]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile5.grid(column=1,row=1)

tuile6=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile6.create_text(60, 60, text= str(grille1[1][1]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile6.grid(column=2,row=1)

tuile7=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile7.create_text(60, 60, text= str(grille1[1][2]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile7.grid(column=3,row=1)

tuile8=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile8.create_text(60, 60, text= str(grille1[1][3]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile8.grid(column=4,row=1)

tuile9=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile9.create_text(60, 60, text= str(grille1[2][0]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile9.grid(column=1,row=2)

tuile10=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile10.create_text(60, 60, text= str(grille1[2][1]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile10.grid(column=2,row=2)

tuile11=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile11.create_text(60, 60, text= str(grille1[2][2]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile11.grid(column=3,row=2)

tuile12=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile12.create_text(60, 60, text= str(grille1[2][3]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile12.grid(column=4,row=2)

tuile13=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile13.create_text(60, 60, text= str(grille1[3][0]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile13.grid(column=1,row=3)

tuile14=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile14.create_text(60, 60, text= str(grille1[3][1]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile14.grid(column=2,row=3)

tuile15=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile15.create_text(60, 60, text= str(grille1[3][2]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile15.grid(column=3,row=3)

tuile16=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
tuile16.create_text(60, 60, text= str(grille1[3][3]),fill="black",font=('Helvetica', '30' ,'bold'))
tuile16.grid(column=4,row=3)


def appui_clavier(event):
        if event.keysym == "Left":
              mouvemement("gauche")
        elif event.keysym == "Right":
               mouvemement("droite")
        elif event.keysym == "Up":
               mouvemement("haut")
        elif event.keysym == "Down":
               mouvemement("bas")

fenetre.bind("<KeyPress>",appui_clavier)
fenetre.mainloop()
                
