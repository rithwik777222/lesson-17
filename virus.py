from tkinter import *
from tkinter import messagebox

r = Tk()
r.geometry("200x200")

def msg():
    messagebox.showwarning("alert","stop!virus found.")

button = Button(r,text="scan for virus",command=msg)
button.place(x=40,y=80)

r.mainloop()