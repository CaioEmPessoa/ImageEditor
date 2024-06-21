from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Image Editor")

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
folder = f"{location}\\images\\"
icon = f"{location}\\src\\icon.ico"
root.iconbitmap(icon)

img_list = [folder + img for img in os.listdir(folder)]
leng = len(img_list) - 1
i = 0

status = Label(root, text=f"image {i + 1} of {leng + 1}")

def frontF():
    global image
    global back
    global front
    global i
    global img_list
    global open_img
    global leng
    global status

    i += 1
    image.grid_forget()
    open_img = ImageTk.PhotoImage(Image.open(img_list[i]))
    image = Label(image=open_img)
    back = Button(text="<", command=backF)
    leave = Button(text="Close", command=exit)
    status = Label(root, text=f"image {i + 1} of {leng + 1}")
    if i == leng:
        front = Button(root, text=">", state=DISABLED)
    else:
        front = Button(text=">", command=frontF)

    image.grid(row=0, column=0, columnspan= 3)
    back.grid(row=1, column=0)
    leave.grid(row=1, column=1)
    front.grid(row=1, column=2)
    status.grid(row=2, column=2, sticky=E)


def backF():
    global image
    global back
    global front
    global i
    global img_list
    global open_img
    global status

    i -= 1
    image.grid_forget()
    open_img = ImageTk.PhotoImage(Image.open(img_list[i]))
    image = Label(image=open_img)
    leave = Button(text="Close", command=exit)
    front = Button(text=">", command=frontF)
    status = Label(root, text=f"image {i + 1} of {leng + 1}")
    if i == 0:
        back = Button(root, text="<", state=DISABLED)
    else:
        back = Button(text="<", command=backF)

    image.grid(row=0, column=0, columnspan= 3)
    back.grid(row=1, column=0)
    leave.grid(row=1, column=1)
    front.grid(row=1, column=2)
    status.grid(row=2, column=2, sticky=E)
    
open_img = ImageTk.PhotoImage(Image.open(img_list[i]))

image = Label(image=open_img)
leave = Button(text="Close", command=exit)
if i == leng:
    front = Button(root, text=">", state=DISABLED)
else:
    front = Button(text=">", command=frontF)
if i == 0:
    back = Button(root, text="<", state=DISABLED)
else:
    back = Button(text="<", command=backF)

image.grid(row=0, column=0, columnspan= 3)
back.grid(row=1, column=0)
leave.grid(row=1, column=1)
front.grid(row=1, column=2, pady=3)
status.grid(row=2, column=2, sticky=E)

root.mainloop()