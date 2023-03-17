# brouillon projet

import tkinter as tk 
import numpy as np
from tkinter import filedialog

def fermer_fenetre():
    fenetre.destroy()

def ouvrir():
    ouvrir_fichier = filedialog.askopenfilename(title=" ouvrir un fichier")

def sauvegarder():
    ouvrir_fichier = filedialog.asksaveasfile(title =" sauvagarder la partie")

fenetre= tk.Tk()
fenetre.title(" 2048")



fenetre.geometry('700x500')


fenetre['bg']='purple'
bouton1=tk.Button(fenetre,text='Play',height=2,width=5,bg='blue')
bouton1.grid(column=7)
bouton2=tk.Button(fenetre,text='Left',height=2,width=5,bg='red')
bouton2.grid(column=7)
bouton3=tk.Button(fenetre,text='Right',height=2,width=5,bg='yellow')
bouton3.grid(column=7)
bouton4=tk.Button(fenetre,text='Down',height=2,width=5,bg='black',fg='red')
bouton4.grid(column=7)
bouton5=tk.Button(fenetre,text='Up',height=2,width=5,bg='green')
bouton5.grid(column=7)
bouton6=tk.Button(fenetre,text='Exit',height=2,width=5,bg='grey',command=fermer_fenetre)
bouton6.grid(column=7)
bouton7=tk.Button(fenetre,text='Save',height=2,width=5,bg='orange',command=sauvegarder)
bouton7.grid(column=7)
bouton8=tk.Button(fenetre,text='Load',height=2,width=5,bg='white',command=ouvrir)
bouton8.grid(column=7)



tableau=np.array([[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]])
tableau

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

import tkinter as tk 

fenetre=tk.Tk()
listepourboutton=[]
fenetre.title("2048 jeu video")
fenetre.geometry("420x420")
for a in range(0,420,105):
    for b in range(0,420,105):
        bouton=tk.Button(fenetre)
        bouton.place(x=a,y=b,width=140,height=140)
        listepourboutton.append(bouton)
fenetre.mainloop()

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




