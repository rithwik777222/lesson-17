from tkinter import *
import PIL
from PIL import Image, ImageTk

r = Tk()
r.title('image')
r.geometry('400x400')

upload = Image.open("hogwarts.jpg")

image= ImageTk.PhotoImage(upload)

label = Label(r,image=image,height=350,width=300)
label.place(x=50,y=0)
label2= Label(r,text='yay we have an image!!')
label2.place(x=40,y=360)

r.mainloop()