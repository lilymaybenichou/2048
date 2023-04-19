from tkinter import *

root = Tk()

# Chargement de l'image
bg_image = PhotoImage(file="chemin/vers/l/image.png")

# Récupération des dimensions de l'image et création du Canvas de la même taille
w = bg_image.width()
h = bg_image.height()
canvas = Canvas(root, width=w, height=h)

# Ajout de l'image au canvas
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Ajout de vos widgets dans le canvas (exemple)
label = Label(root, text="Mon texte")
canvas.create_window( window=label)

# Affichage du canvas
canvas.pack()

root.mainloop()