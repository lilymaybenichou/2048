
#lily

import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import numpy as np
from random import*

#def systeme2048(nombre):
    #L=[2,4,8,16,32,64,128,256,512,1024,2048]
    #if nombre in L:
    #    x=nombre*2
    #    return x
    #else :
    #    print("nombre hors jeu")

#systeme2048(64)


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
    L_numpy = np.array(L) 
    return L_numpy
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

grille1=[[2, 0, 0, 0], [2, 0, 0, 0],[4, 0, 0, 0],[4, 0, 0, 0]]

#finjeu(grille1)

def joueur_tuile(grille):
    x=randint(0,3)
    y=randint(0,3)
    nbliste=[2,2,2,2,2,2,2,2,2,4]
    while grille[x][y]!=0:
        x=randint(0,3)
        y=randint(0,3)
    grille[x][y]=choice(nbliste)
    return grille


grille1=[[2, 0, 0, 0], [2, 0, 0, 0],[4, 0, 0, 0],[4, 0, 0, 0]]
def mouvement(grille):
    x=1
    while x!=0:
        n=input("gauche -> 1 ou droite->2 ou haut->3  ou bas->4")
        grille2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        if int(n)==1:
            for i in range (len(grille)):
                if grille[i][0]==grille[i][1]:
                        grille2[i][1]=grille[i][0]+grille[i][1]
                if grille[i][1]==grille[i][2]:
                        grille2[i][2]=grille[i][1]+grille[i][2]
                if grille[i][2]==grille[i][3]:
                        grille2[i][3]=grille[i][2]+grille[i][3]
                for j in range(0,3):
                    if grille2[i][j+1]==0 :
                            grille2[i][j+1],grille2[i][j]=grille2[i][j],grille2[i][j+1]
        if int(n)==2:
            for i in range (len(grille)):
                if grille[i][0]==grille[i][1]:
                        grille2[i][0]=grille[i][0]+grille[i][1]
                if grille[i][2]==grille[i][1]:
                        grille2[i][1]=grille[i][2]+grille[i][1]
                if grille[i][3]==grille[i][2]:
                        grille2[i][2]=grille[i][2]+grille[i][3]
                for j in range (1,3):
                      if grille2[i][j-1]==0:
                        grille2[i][j-1],grille2[i][j]=grille2[i][j],grille2[i][j-1]
        if int(n)==3:
              for i in range(len(grille)):
                if grille[0][i]==grille[1][i]:
                        grille2[0][i]=grille[0][i]+grille[1][i]
                if grille[1][i]==grille[2][i]:
                        grille2[1][i]=grille[2][i]+grille[1][i]
                if grille[2][i]==grille[3][i]:
                        grille2[2][i]=grille[2][i]+grille[3][i]
                for j in range (1,3):
                      if grille2[j-1][i]==0:
                        grille2[j-1][i],grille2[j][i]=grille2[j][i],grille2[j-1][i]
        if int(n)==4:
              for i in range(len(grille)):
                if grille[0][i]==grille[1][i]:
                        grille2[1][i]=grille[0][i]+grille[1][i]
                if grille[1][i]==grille[2][i]:
                        grille2[2][i]=grille[2][i]+grille[1][i]
                if grille[2][i]==grille[3][i]:
                        grille2[3][i]=grille[2][i]+grille[3][i]
                for j in range (1,3):
                      if grille2[j+1][i]==0:
                        grille2[j+1][i],grille2[j][i]=grille2[j][i],grille2[j+1][i]
                                        
        x=0
        print( grille2)
    
#mouvement(grille1)
joueur_tuile(grille1)

fenetre=tk.Tk()
fenetre.title("2048")
