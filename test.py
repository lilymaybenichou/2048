import tkinter as tk

racine = tk.Tk()
racine.title("Exemple")
label = tk.Label(racine, text="Texte dans la fenetre", font=("helvetica", "20"))
label.grid()
racine.mainloop()