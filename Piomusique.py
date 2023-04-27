#Fonction pour la création d'une musique 
from tkinter import * 
import pygame 
#Création d'une fenétre
fenetre=Tk()
fenetre.title("pio")
fenetre.geometry("500x400")

pygame.mixer.init()
#Fonction play, permettant de jouer une musique donnée
def play():
    pygame.mixer.music.load("Music/Elektronomia_-_Limitless_Loadedsongs.com.mp3")
    pygame.mixer.music.play(loops=0)
#Lorsque l'on clique sur le bouton "Play song", la musique en question est jouée
my_button = Button(fenetre,text="Play song",font=("Helvetica",32),command=play)
my_button.pack(pady=20)
#Pour afficher une fenetre
fenetre.mainloop()
