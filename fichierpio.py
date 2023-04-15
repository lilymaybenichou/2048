

# propre projet 


import tkinter as tk
from tkinter import Widget, filedialog
from random import * 
from time import* 
import random

fenetre=tk.Tk()
fenetre['bg']="red"

grille=['4x4']

def play():
    global grille 
    



    

bouton1=tk.Button(fenetre,text='Play',bg='red')
bouton1.grid(row=1,column=0)
bouton2=tk.Button(fenetre,text='Left',bg='red')
bouton2.grid(row=2,column=0)
bouton3=tk.Button(fenetre,text='Right',bg='yellow')
bouton3.grid(row=3,column=0)
bouton4=tk.Button(fenetre,text='Down',bg='black')
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


# fonction pour savoire la victoire ou non
def check_win():
    global tableau
    
    for i in range(tailledutableau):
        for j in range(tailledutableau):
            if tableau[i][j] == 2048:
                return True
    return False









fenetre.mainloop() 







       