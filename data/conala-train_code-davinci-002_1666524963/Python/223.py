from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

canvas.create_text(100, 50, text="Hello World", font=("Times", 20))

root.mainloop()