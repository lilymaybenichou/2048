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