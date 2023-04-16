import tkinter as tk 

fenet=tk.Tk()
fenet.geometry('500x500')
fenet.title('Welcome to the 2048 game ')

# definir la grille 
# matrice 4x4 soit 16
# ici les zéros représentent les cases vides
# aux debut elle sont vides puis au fur et a mesures elles se remplissent 

def afficher_grille(grille):
    for i in range(len(grille)):
      for j in range(len(grille[i])):
          print(grille[i][j],end='\t')
          # afficher chaque element de la grille 
          print('\n')# sauter une ligne apres 
          # chaque ligne de la grille 


grille=[
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]
]
afficher_grille(grille)




def move_left(grid):
    # déplace toutes les tuiles à gauche
    for i in range(4):
        for j in range(1, 4):
            if grid[i][j] != 0:
                k = j
                while k > 0 and grid[i][k-1] == 0:
                    k -= 1
                if k != j:
                    grid[i][k] = grid[i][j]
                    grid[i][j] = 0
    # combine les tuiles identiques
    for i in range(4):
        for j in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0
    # déplace encore une fois toutes les tuiles à gauche
    for i in range(4):
        for j in range(1, 4):
            if grid[i][j] != 0:
                k = j
                while k > 0 and grid[i][k-1] == 0:
                    k -= 1
                if k != j:
                    grid[i][k] = grid[i][j]
                    grid[i][j] = 0
    return grid

def move_right(grid):
    # déplace toutes les tuiles à droite
    for i in range(4):
        for j in range(2, -1, -1):
            if grid[i][j] != 0:
                k = j
                while k < 3 and grid[i][k+1] == 0:
                    k += 1
                if k != j:
                    grid[i][k] = grid[i][j]
                    grid[i][j] = 0
    # combine les tuiles identiques
    for i in range(4):
        for j in range(2, -1, -1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j-1]:
                grid[i][j] *= 2
                grid[i][j-1] = 0
    # déplace encore une fois toutes les tuiles à droite
    for i in range(4):
        for j in range(2, -1, -1):
            if grid[i][j] != 0:
                k = j
                while k < 3 and grid[i][k+1] == 0:
                    k += 1
                if k != j:
                    grid[i][k] = grid[i][j]
                    grid[i][j] = 0
    return grid

def move_up(grid):
    # déplace toutes les tuiles vers le haut
    for j in range(4):
        for i in range(1, 4):
            if grid[i][j] != 0:
                k = i
                while k > 0 and grid[k-1][j] == 0:
                    k -= 1
                if k != i:
                    grid[k][j] = grid[i][j]
                    grid[i][j] = 0
    # combine les tuiles identiques
    for j in range(4):
        for i in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i+1][j]:
                grid[i][j] = 2
                grid[i+1][j] = 0
    # déplace encore une fois toutes les tuiles vers le haut
    for j in range(4):
        for i in range(1, 4):
            if grid[i][j] != 0:
                k = i
                while k > 0 and grid[k-1][j] == 0:
                    k -= 1
                if k != i:
                    grid[k][j] = grid[i][j]
                    grid[i][j] = 0
    return grid

def move_down(grid):
    # déplace toutes les tuiles vers le bas
    for j in range(4):
        for i in range(2, -1, -1):
            if grid[i][j] != 0:
                k = i
                while k < 3 and grid[k+1][j] == 0:
                    k += 1
                if k != i:
                    grid[k][j] = grid[i][j]
                    grid[i][j] = 0
    # combine les tuiles identiques
    for j in range(4):
        for i in range(2, -1, -1):
            if grid[i][j] != 0 and grid[i][j] == grid[i-1][j]:
                grid[i][j]= 2
                grid[i-1][j] = 0
    # déplace encore une fois toutes les tuiles vers le bas
    for j in range(4):
        for i in range(2, -1, -1):
            if grid[i][j] != 0:
                k = i
                while k < 3 and grid[k+1][j] == 0:
                    k += 1
                if k != i:
                    grid[k][j] = grid[i][j]
                    grid[i][j] = 0
    return grid


def has_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return True
    return False

def has_lost(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                return False
    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i+1][j]:
                return False
    return True


button1=tk.Button(fenet,bg="red",text=" Gauche ",command=move_left)
button2=tk.Button(fenet,bg="blue",text="Droite",command=move_right)
button3=tk.Button(fenet,bg="grey",text="Haut",command=move_up)
button4=tk.Button(fenet,bg="white",text="Bas",command=move_down)

button1.pack()
button2.pack()
button3.pack()
button4.pack()




fenet.mainloop()