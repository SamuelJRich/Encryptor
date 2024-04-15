from tkinter import *
from tkinter import ttk

root = Tk()

rtFrm = ttk.Frame(root, padding=150)
rtFrm.grid()
ttk.Button(rtFrm, text="Click me", command=root.destroy).grid(column=1, row=0)

root.mainloop()