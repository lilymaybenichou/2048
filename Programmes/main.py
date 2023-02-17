import tkinter as tk

main = tk.Tk()
main.title("Exemple")
label = tk.Label(main, text="Texte dans la fenetre", font=("helvetica", "20"))
label.grid()
main.mainloop()