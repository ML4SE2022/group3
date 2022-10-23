import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
text.insert(tk.END, "Hello, world!")
text.config(state="disabled")
text.pack()

root.mainloop()