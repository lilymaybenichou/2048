import tkinter as tk

def afficher_grille(grille):
    # Créer une fenêtre Tkinter
    fenetre = tk.Tk()
    fenetre.title("2048")

    # Parcourir la grille et créer des étiquettes pour chaque valeur
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            etiquette = tk.Label(fenetre, text=grille[i][j], font=("Helvetica", 20), padx=20, pady=20)
            etiquette.grid(row=i, column=j)  # Positionner chaque étiquette sur la grille

    grille = [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    afficher_grille(grille)



    # Afficher la fenêtre Tkinter
    fenetre.mainloop()




