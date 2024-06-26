from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
import os

root = Tk()
root.title("Image Editor")

root.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
root.rowconfigure(0, weight = 1)

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
folder = f"{location}\\images\\"
icon = f"{location}\\src\\icon.ico"
root.iconbitmap(icon)

img_list = [folder + img for img in os.listdir(folder)]
leng = len(img_list) - 1
i = 0

ImageFrame = Canvas(root, background= 'black', bd = 0)
ButtonFrame = Frame(root)

status = Label(ButtonFrame, text=f"image {i + 1} of {leng + 1}")
status.pack()

def screen():
    global image
    global back
    global front
    global i
    global img_list
    global open_img
    global leng
    global status

    image.grid_forget()
    image_original = Image.open(img_list[i])
    open_img = ImageTk.PhotoImage(image_original)
    image = Label(image=open_img)
    leave = Button(text="Close", command=exit)
    status = Label(root, text=f"image {i + 1} of {leng + 1}")
    if i == 0:
        back = Button(root, text="<", state=DISABLED)
    else:
        back = Button(text="<", command=backF)
    if i == leng:
        front = Button(root, text=">", state=DISABLED)
    else:
        front = Button(text=">", command=frontF)

    ImageFrame.grid(row=1, column=1)
    image.grid(row=0, column=0, columnspan= 3)
    back.grid(row=1, column=0)
    leave.grid(row=1, column=1)
    front.grid(row=1, column=2, pady=3)
    status.grid(row=2, column=2, sticky=E)


def frontF():
    global i
    i += 1
    screen()

def backF():
    global i
    i -= 1
    screen()
    
image_original = Image.open(img_list[i])
open_img = ImageTk.PhotoImage(image_original)


image = Label(ImageFrame, image=open_img)
image.pack()
leave = Button(text="Close", command=exit)
leave.pack()
if i == leng:
    front = Button(ButtonFrame, text=">", state=DISABLED)
else:
    front = Button(text=">", command=frontF)
front.pack()
if i == 0:
    back = Button(ButtonFrame, text="<", state=DISABLED)
else:
    back = Button(text="<", command=backF)
back.pack()

ImageFrame.grid(row=0, column=1, columnspan=3, sticky= NSEW)
ButtonFrame.grid(row=0, column=0, sticky= NSEW)

root.mainloop()