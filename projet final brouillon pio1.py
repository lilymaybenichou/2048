import tkinter as tk 
def affiche_bouton1():
    zoneaffi['text']="vous avez cliquer sur le bouton 1"

def affiche_bouton2():
    zoneaffi['text']=" vous avez cliquer sur le bouton 2"

def affiche_label():
    zoneaffi['text']=edit.get()

fenetre= tk.Tk()
fenetre.title("j aime les bananes")
edit=tk.Entry(fenetre)
edit.pack()
zoneaffi=tk.Label(fenetre,text="zone affichage",bg="red")
zoneaffi.pack()
bouton1=tk.Button(fenetre,text="bouton1",command=affiche_bouton1)
bouton1.pack()
bouton2=tk.Button(fenetre,text="boutton 2",command=affiche_bouton2)
bouton2.pack()
bouton3=tk.Button(fenetre,text="bouton 3", command=affiche_label)
bouton3.pack()

fenetre.mainloop()