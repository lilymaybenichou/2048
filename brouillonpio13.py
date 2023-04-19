from tkinter import *

root = Tk()

# Chargement de l'image
bg_image = PhotoImage(file="image/file/P.png")

# Création d'un Label avec l'image en arrière-plan
background_label = Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Ajout de vos widgets (exemple)
label = Label(root, text="Mon texte")
label.pack()

root.mainloop()