import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import numpy as np
from random import*

tableau = np.array([[0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]])

#fonction
def fermer_fenetre():
    fenetre.destroy()

def ouvrir():
    ouvrir_fichier = filedialog.askopenfilename(title=" ouvrir un fichier")

def sauvegarder():
    ouvrir_fichier = filedialog.asksaveasfile(title =" sauvagarder la partie")

def play():
    c=random.randint(0,6)
    alea=tk.Label(fenetre,text=c,bg="#FFC584")
    alea.grid(row=0,column=4)

def left():
    pass

def right():
    pass

def up():
    pass

def down():
    pass

#fenetre
fenetre=tk.Tk()
fenetre.title("Jeu du 2048")
fenetre.geometry('700x600')
fenetre['bg']='#FFC584'

#bouton
bouton1=tk.Button(fenetre,text='Play',height=2,width=5,bg='green',command=play)
bouton1.grid(row=1, column=0, columnspan=2, rowspan=2)
bouton6=tk.Button(fenetre,text='Exit',height=2,width=5,bg='red',command=fermer_fenetre)
bouton6.grid(row=1, column=9, columnspan=2)
bouton7=tk.Button(fenetre,text='Save',height=2,width=5,bg='grey',command=sauvegarder)
bouton7.grid(row=2, column=9, columnspan=2)
bouton8=tk.Button(fenetre,text='Load',height=2,width=5,bg='grey',command=ouvrir)
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

#touche (source d'utilisation : https://infoforall.fr/python/python-act150.html)
fenetre.bind('Left', left)
fenetre.bind('Right', right)
fenetre.bind('Up', up)
fenetre.bind('Down', down)
fenetre.bind('Enter', play)
fenetre.bind('E', exit)