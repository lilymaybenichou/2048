
from tkinter import *
from PIL import ImageTk, Image
win = Tk()
win.geometry("700x500")
frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("image/OIP.jpg"))
label = Label(frame, image = img)
label.pack()
win.mainloop()