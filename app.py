import tkinter
from tkinter import *
root = tkinter.Tk()
root.title("calculator")
e=Entry(root,width=35)
def button_add():
    return
button_1 = Button(root, text="1", padx=40,pady=20,command=button_add)

button_1.grid(row=1,column=1)
root.mainloop()