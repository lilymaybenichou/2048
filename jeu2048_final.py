#fichier final du jeu

#amîn
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import numpy as np
from random import*

tableau = np.array([[0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]])

def fermer_fenetre():
    fenetre.destroy()

def play():
    c=random.randint(0,6)
    r=random.randint(0,7)
    c1=tk.Label(fenetre,text="2",bg="black")
    c1.grid(row=c,column=r)

fenetre=tk.Tk()
fenetre.title("Jeu du 2048")
fenetre.geometry('700x600')
fenetre['bg']='#FFC584'

zonaffi=tk.Label(fenetre,text="°",bg="#FFC584")
zonaffi.grid(row=0,column=0)
zonaffi=tk.Label(fenetre,text="°",bg="#FFC584")
zonaffi.grid(row=0,column=0)
zonaffi3=tk.Label(fenetre,text="°",bg="#FFC584")
zonaffi3.grid(row=0,column=7)

canevas1=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas1.grid(row=4,column=3)
canevas2=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas2.grid(row=4,column=4)
canevas2=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas2.grid(row=4,column=5)
canevas4=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas4.grid(row=4,column=6)
canevas5=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas5.grid(row=5,column=3)
canevas6=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas6.grid(row=5,column=4)
canevas7=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas7.grid(row=5,column=5)
canevas8=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas8.grid(row=5,column=6)
canevas9=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas9.grid(row=6,column=3)
canevas10=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas10.grid(row=6,column=4)
canevas11=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas11.grid(row=6,column=5)
canevas12=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas12.grid(row=6,column=6)
canevas13=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas13.grid(row=7,column=3)
canevas14=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas14.grid(row=7,column=4)
canevas15=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas15.grid(row=7,column=5)
canevas16=tk.Canvas(width=100,height=100,bg="#FCE6CC")
canevas16.grid(row=7,column=6)









#pio

# propre projet 


import tkinter as tk
from tkinter import filedialog



def fermer_fenetre():
    fenetre.destroy()

fenetre= tk.Tk()
fenetre.title("Jeu du 2048")
fenetre.geometry('500x450')
fenetre['bg']='black'




bouton1=tk.Button(fenetre,text='Play',bg='red')
bouton1.grid(row=1,column=0)
bouton2=tk.Button(fenetre,text='Left',bg='red')
bouton2.grid(row=2,column=0)
bouton3=tk.Button(fenetre,text='Right',bg='yellow')
bouton3.grid(row=3,column=0)
bouton4=tk.Button(fenetre,text='Down',bg='black',fg='red')
bouton4.grid(row=4,column=0)
bouton5=tk.Button(fenetre,text='Up',bg='green')
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
rejouer.add_command(label="rejouer")
mon_menu.add_cascade(label="Fichier",menu=fichier)
mon_menu.add_cascade(label="Option",menu=option)
mon_menu.add_cascade(label="Aide",menu= aide)
mon_menu.add_cascade(label="Exit",menu=exit)
mon_menu.add_cascade(label="Note",menu=notezlejeu)
mon_menu.add_cascade(label="Rejouer",menu=rejouer)

fenetre.config(menu=mon_menu)

fenetre.mainloop()

print("\033[0;97m 2")
print("\033[0;96m 4")
print("\033[0;95m 8")
print("\033[0;94m 16")
print("\033[0;93m 32")
print("\033[0;92m 64")
print("\033[0;91m 128")
print("\033[0;90m 256")
print("\033[0;37m 512")
print("\033[0;36m 1024")
print("\033[0;35m 2048")
print("\033[0;34m 4096")
print("\033[0;33m 8192")
print("\033[0;32m 16384")
print("\033[0;31m 32768")
print("\033[0;30m 65536")












#lily


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
