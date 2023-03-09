import tkinter as tk 

fenetre=tk.Tk()
fenetre.title("jeu 2048")
fenetre.geometry("700x500")
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
fenetre.mainloop()