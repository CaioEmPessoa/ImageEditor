from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users/User/Documents/programa acao/ImageViewer/src/icon.ico')

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
folder = f"{location}\\images\\"
img_list = [folder + img for img in os.listdir(folder)]

def frontF():
    global i
    i += 1
    global image
    image.grid_forget()
    image = Label(image=open_img)
    image.grid(row=0, column=0, columnspan= 3)

def backF():
    global i
    i -= 1
    global image
    image.grid_forget()
    image = Label(image=open_img)
    image.grid(row=0, column=0, columnspan= 3)

i = 0
open_img = ImageTk.PhotoImage(Image.open(img_list[i]))

image = Label(image=open_img)
back = Button(text="<", command=backF)
leave = Button(text="Close", command=exit)
front = Button(text=">", command=frontF)

image.grid(row=0, column=0, columnspan= 3)
back.grid(row=1, column=0)
leave.grid(row=1, column=1)
front.grid(row=1, column=2)

root.mainloop()