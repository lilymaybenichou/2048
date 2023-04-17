import tkinter as tk 
from tkinter import*
fenetre1= tk.Tk()
fenetre1.title("bonjour")
fenetre1.geometry("800x500")
# Definir l image 
bg= PhotoImage(file="image/OIP.jpg")
#Label 
my_label= Label(fenetre1, image=bg)
my_label.pack()
fenetre1.mainloop()