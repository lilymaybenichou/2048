#lily

import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import numpy as np
from random import*

def systeme2048(nombre):
    L=[2,4,8,16,32,64,128,256,512,1024,2048]
    if nombre in L:
        x=nombre*2
        return x
    else :
       print("nombre hors jeu")
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

#joueur_tuile(grille1)

#fonctions de directions
def mouvemement(direction,grille):
        if direction=="down":
                for i in range(len(grille)):
                        if grille[0][i]==grille[1][i]:
                                x=grille[0][i]+grille[1][i]
                                grille[0][i]=0
                        else:
                                x=0
                        if grille[1][i]==grille[2][i]:
                                y=grille[2][i]+grille[1][i]
                                grille[1][i]=0
                        else:
                                y=0
                        if grille[2][i]==grille[3][i]:
                                z=grille[2][i]+grille[3][i]
                                grille[2][i]=0
                        else:
                                z=0
                        grille[1][i]=x
                        grille[2][i]=y
                        grille[3][i]=z
                        for j in range (1,3):
                                if grille[j+1][i]==0:
                                        grille[j+1][i],grille[j][i]=grille[j][i],grille[j+1][i]
        if direction=="up":
                for i in range(len(grille)):
                        if grille[0][i]==grille[1][i]:
                                x=grille[0][i]+grille[1][i]
                                grille[1][i]=0
                        else:
                                x=0
                        if grille[1][i]==grille[2][i]:
                                y=grille[2][i]+grille[1][i]
                                grille[2][i]=0
                        else:
                                y=0
                        if grille[2][i]==grille[3][i]:
                                z=grille[2][i]+grille[3][i]
                                grille[3][i]=0
                        else:
                                z=0
                        grille[0][i]=x
                        grille[1][i]=y
                        grille[2][i]=z
                        for j in range (1,3):
                                if grille[j-1][i]==0:
                                        grille[j-1][i],grille[j][i]=grille[j][i],grille[j-1][i]
        if direction=="left":
               for i in range(len(grille)):
                        for j in range(1,len(grille[i])):
                                if grille[i][j]!=0:
                                        for k in range(j,0,-1):
                                                if grille[i][k-1]==0:
                                                        grille[i][k-1]=grille[i][k]
                                                        grille[i][k]=0
                             
                                                elif grille[i][k-1]==grille[i][k]:
                                                       grille[i][k-1]*=2
                                                       grille[i][k]=0
                                                       break
                                                        
                             





                #for i in range (1,len(grille)):
                        #for j in range(len(grille[i])):
                                #if grille[i][j]!=0:
                                        #for k in range(j,0,-1):
                                                #if grille[i][k-1]==0:
                                                        #grille[i][k-1]=grille[i][k]
                                                        #grille[i][k]=0
        
                                                
        
        
                        
        if direction=="right":     
                for i in range (len(grille)):
                        if grille[i][0]==grille[i][1]:
                                x=grille[i][0]+grille[i][1]
                                grille[i][0]=0
                        else:
                                x=0
                        if grille[i][1]==grille[i][2]:
                                y=grille[i][1]+grille[i][2]
                                grille[i][1]=0
                        else:
                                y=0
                        if grille[i][2]==grille[i][3]:
                                z=grille[i][2]+grille[i][3]
                                grille[i][2]=0
                        else:
                                z=0
                        grille[i][1]=x
                        grille[i][2]=y
                        grille[i][3]=z
                        for j in range(0,3):
                                if grille[i][j+1]==0 :
                                        grille[i][j+1],grille[i][j]=grille[i][j],grille[i][j+1]
        return grille



#affichage tkinter
def testjeu(grille):
        x=16
        while x!=0:
                x=16
                for i in range(len(grille)):
                     for j in range(len(grille[i])):
                          if grille[i][j]!=0:
                               x-=1
                fenetre=tk.Tk()
                fenetre.title("2048")

                #Butons
                exit=tk.Button(fenetre,text='Exit',command=lambda:mouvemement("left",grille))
                exit.grid(column=0,row=3)

                save=tk.Button(fenetre,text='Save')
                save.grid(column=0,row=2)

                load=tk.Button(fenetre,text='Load')
                load.grid(column=0,row=1)

                start=tk.Button(fenetre,text='Start')
                start.grid(column=0,row=0)

                #Tuiles
                tuile1=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile1.create_text(60, 60, text= str(grille[0][0]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile1.grid(column=1,row=0)

                tuile2=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile2.create_text(60, 60, text= str(grille[0][1]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile2.grid(column=2,row=0)

                tuile3=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile3.create_text(60, 60, text= str(grille[0][2]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile3.grid(column=3,row=0)

                tuile4=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile4.create_text(60, 60, text= str(grille[0][3]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile4.grid(column=4,row=0)

                tuile5=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile5.create_text(60, 60, text= str(grille[1][0]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile5.grid(column=1,row=1)

                tuile6=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile6.create_text(60, 60, text= str(grille[1][1]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile6.grid(column=2,row=1)

                tuile7=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile7.create_text(60, 60, text= str(grille[1][2]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile7.grid(column=3,row=1)

                tuile8=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile8.create_text(60, 60, text= str(grille[1][3]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile8.grid(column=4,row=1)

                tuile9=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile9.create_text(60, 60, text= str(grille[2][0]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile9.grid(column=1,row=2)

                tuile10=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile10.create_text(60, 60, text= str(grille[2][1]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile10.grid(column=2,row=2)

                tuile11=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile11.create_text(60, 60, text= str(grille[2][2]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile11.grid(column=3,row=2)

                tuile12=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile12.create_text(60, 60, text= str(grille[2][3]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile12.grid(column=4,row=2)

                tuile13=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile13.create_text(60, 60, text= str(grille[3][0]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile13.grid(column=1,row=3)

                tuile14=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile14.create_text(60, 60, text= str(grille[3][1]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile14.grid(column=2,row=3)

                tuile15=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile15.create_text(60, 60, text= str(grille[3][2]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile15.grid(column=3,row=3)

                tuile16=tk.Canvas(fenetre,width=100,height=100,bg="white",bd=5,relief='ridge')
                tuile16.create_text(60, 60, text= str(grille[3][3]),fill="black",font=('Helvetica', '30' ,'bold'))
                tuile16.grid(column=4,row=3)
                fenetre.mainloop()
                

testjeu(grille1)