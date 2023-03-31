import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import numpy as np
from random import*

tableau = np.array([[0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]])

#fonction
def fermer_fenetre(): #Marche (100%)
    fenetre.destroy()

def ouvrir(): #Marche (100%) Pris de Pio
    ouvrir_fichier = filedialog.askopenfilename(title=" ouvrir un fichier")

def sauvegarder(): #Marche (100%) Pris de Pio
    ouvrir_fichier = filedialog.asksaveasfile(title =" sauvagarder la partie")

def help(): #Pris de Pio
    import tkinter as tk 
    fenetre2=tk.Tk()
    fenetre2.title("help 2048")
    fenetre2.geometry("800x800")
    label=tk.Label(fenetre2,fg="black",text="Sur une grille de 16 cases on fait bouger les tuiles pour obtenir un 2048")
    label.pack()
    fenetre2.mainloop()
import webbrowser

def partage(): #Pris de Pio
    webbrowser.open("https://www.instagram.com/?hl=fr")

def avis(): #Pris de Pio
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
     

from random import*

def play(): #Marche (75%)
    V=["2","2","2","2","2","2","2","4","2"]
    hasardrow1=randint(4,7)
    hasardcolumn1=randint(3,6)
    hasardrow2=randint(4,7)
    hasardcolumn2=randint(3,6)
    casedebut1=tk.Canvas(width=100,height=100,bg="#FCE6CC")
    casedebut1.grid(row=int(hasardrow1),column=int(hasardcolumn1))
    casedebut2=tk.Canvas(width=100,height=100,bg="#FCE6CC")
    casedebut2.grid(row=int(hasardrow2),column=int(hasardcolumn2))
    debut1=tk.Label(fenetre, text=choice(V),bg="#FFC0C0",height=3,width=6,font=("Helvetica", 20))
    debut1.grid(row=int(hasardrow1),column=int(hasardcolumn1))
    debut2=tk.Label(fenetre, text=choice(V),bg="#FFC0C0",height=3,width=6,font=("Helvetica", 20))
    debut2.grid(row=int(hasardrow2),column=int(hasardcolumn2))
    bouton1=tk.Button(fenetre,text='Try Again',height=2,width=12,bg='Blue',command=tryagain)
    bouton1.grid(row=1, column=1)

def tryagain(): #Marche pas (25%)
    casedebut1.delete(ALL)
    casedebut1.delete(ALL)
    debut1.delete(ALL)
    debut2.delete(ALL)
    bouton1=tk.Button(fenetre,text='Play',height=2,width=12,bg='green',command=play)
    bouton1.grid(row=1, column=1)

def left(): #Marche pas (0%)
    pass

def right(): #Marche pas (0%)
    pass

def up(): #Marche pas (0%)
    pass

def down(): #Marche pas (0%)
    pass

#fenetre
fenetre=tk.Tk()
fenetre.title("Jeu du 2048")
fenetre.geometry('700x600')
fenetre.minsize(665, 570)
fenetre['bg']='#FFC584'

#zonetexte
affi1=tk.Label(fenetre, text="°",fg="#FFC584",bg="#FFC584",height=3,width=3)
affi1.grid(column=2, row=0)
affi1=tk.Label(fenetre, text="°",fg="#FFC584",bg="#FFC584",height=3,width=3)
affi1.grid(column=8, row=0)
affi1=tk.Label(fenetre, text="°",fg="#FFC584",bg="#FFC584",height=3,width=3)
affi1.grid(column=0, row=0)

#bouton
bouton1=tk.Button(fenetre,text='Play',height=2,width=12,bg='green',command=play)
bouton1.grid(row=1, column=1)
bouton6=tk.Button(fenetre,text='Exit',height=2,width=12,bg='red',command=fermer_fenetre)
bouton6.grid(row=1, column=9, columnspan=2)
bouton7=tk.Button(fenetre,text='Save',height=2,width=12,bg='grey',command=sauvegarder)
bouton7.grid(row=2, column=9, columnspan=2)
bouton8=tk.Button(fenetre,text='Load',height=2,width=12,bg='grey',command=ouvrir)
bouton8.grid(row=3, column=9, columnspan=2)

#tableau
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

#Menu (APPARTENANT A PIOOOOOOOO !)
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

#touche (source d'utilisation : https://infoforall.fr/python/python-act150.html)
fenetre.bind('Left', left)
fenetre.bind('Right', right)
fenetre.bind('Up', up)
fenetre.bind('Down', down)
fenetre.bind('Enter', play)
fenetre.bind('e', exit)