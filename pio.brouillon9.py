import tkinter as tk
import random

class Game2048:
    def init(self):
        self.color = {
            2: "#EEE4DA",
            4: "#EDE0C8",
            8: "#F2B179",
            16: "#F59563",
            32: "#F67C5F",
            64: "#F65E3B",
            128: "#EDCF72",
            256: "#EDCC61",
            512: "#EDC850",
            1024: "#EDC53F",
            2048: "#EDC22E",
        }
        self.size = 4
        self.empty = 0
        self.score = 0
        self.mat = [[self.empty for j in range(self.size)] for i in range(self.size)]
        self.gui = tk.Tk()
        self.gui.title("2048")
        self.gui.geometry("400x400+200+100")
        self.gui.bind("<Key>", self.key_pressed)
        self.init_gui()

def init_gui(self):
        self.cell = []
        for i in range(self.size):
            self.cell.append([])
            for j in range(self.size):
                label = tk.Label(self.gui, text="", width=5, height=2, font=("Helvetica", 20, "bold"), bg="#CDC1B4")
                label.grid(row=i, column=j, padx=5, pady=5)
                self.cell[-1].append(label)
        self.update_gui()

def update_gui(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.mat[i][j] == self.empty:
                    self.cell[i][j]["text"] = ""
                    self.cell[i][j]["bg"] = "#CDC1B4"
                else:
                    self.cell[i][j]["text"] = "{}".format(self.mat[i][j])
                    self.cell[i][j]["bg"] = self.color[self.mat[i][j]]

def add_random_tile(self):
        while True:
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            if self.mat[i][j] == self.empty:
                self.mat[i][j] = 2 if random.random() < 0.9 else 4
                break

def key_pressed(self, event):
        temp = [row[:] for row in self.mat]
        if event.keysym == "Up":
            self.move_up()
        elif event.keysym == "Down":
            self.move_down()
        elif event.keysym == "Left":
            self.move_left()
        elif event.keysym == "Right":
            self.move_right()
        if self.is_game_over():
            message = "Score : {}".format(self.score)
            tk.messagebox.showinfo("Game Over", message)
            self.gui.destroy()
            return
        if temp != self.mat:
            self.add_random_tile()
            self.update_gui()

def move_left(self):
        for i in range(self.size):
            k = 0
            for j in range(1, self.size):
                if self.mat[i][j] != self.empty:
                    temp = self.mat[i][j]
                    self.mat[i][j] = self.empty
                    if self.mat[i][k] == self.empty:
                        self.mat[i][k] = temp
                    elif self.mat[i][k] == temp:
                        self.mat[i][k] *= 2
                        self.score += self.mat[i][k]
                        k += 1
                        self.mat[i][k] = self.empty
                    else:
                        k += 1
                        self.mat[i][k] = temp[15:12]
def move_right(self):
        for i in range(self.size):
            k = self.size - 1
            for j in range(self.size - 2, -1, -1):
                if self.mat[i][j] != self.empty:
                    temp = self.mat[i][j]
                    self.mat[i][j] = self.empty
                    if self.mat[i][k] == self.empty:
                        self.mat[i][k] = temp
                    elif self.mat[i][k] == temp:
                        self.mat[i][k] = 2
                        self.score += self.mat[i][k]
                        k -= 1
                        self.mat[i][k] = self.empty
                    else:
                        k -= 1
                        self.mat[i][k] = temp

def move_up(self):
        for j in range(self.size):
            k = 0
            for i in range(1, self.size):
                if self.mat[i][j] != self.empty:
                    temp = self.mat[i][j]
                    self.mat[i][j] = self.empty
                    if self.mat[k][j] == self.empty:
                        self.mat[k][j] = temp
                    elif self.mat[k][j] == temp:
                        self.mat[k][j]= 2
                        self.score += self.mat[k][j]
                        k += 1
                        self.mat[k][j] = self.empty
                    else:
                        k += 1
                        self.mat[k][j] = temp


def move_down(self):
        for j in range(self.size):
            k = self.size - 1
            for i in range(self.size - 2, -1, -1):
                if self.mat[i][j] != self.empty:
                    temp = self.mat[i][j]
                    self.mat[i][j] = self.empty
                    if self.mat[k][j] == self.empty:
                        self.mat[k][j] = temp
                    elif self.mat[k][j] == temp:
                        self.mat[k][j] *= 2
                        self.score += self.mat[k][j]
                        k -= 1
                        self.mat[k][j] = self.empty
                    else:
                        k -= 1
                        self.mat[k][j] = temp

def is_game_over(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.mat[i][j] == self.empty:
                    return False
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.mat[i][j] == self.mat[i][j + 1]:
                    return False
        for i in range(self.size - 1):
            for j in range(self.size):
                if self.mat[i][j] == self.mat[i + 1][j]:
                    return False
        return True

def run(self):
        self.add_random_tile()
        self.add_random_tile()
        self.update_gui()
        self.gui.mainloop()

game = Game2048()
game.run()
