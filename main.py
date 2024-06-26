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
    open_img = ImageTk.PhotoImage(Image.open(img_list[i]))
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

    image.grid(row=0, column=0, columnspan= 3)
    back.grid(row=1, column=0)
    leave.grid(row=1, column=1)
    front.grid(row=1, column=2)
    status.grid(row=2, column=2, sticky=E)


def frontF():
    global i
    i += 1
    screen()

def backF():
    global i
    i -= 1
    screen()
    
open_img = ImageTk.PhotoImage(Image.open(img_list[i]))

image = Label(image=open_img)
holder1 = Label(root, padx=1920, pady=2)
holder2 = Label(root, pady=1080, padx=2)
leave = Button(text="Close", command=exit)
if i == leng:
    front = Button(root, text=">", state=DISABLED)
else:
    front = Button(text=">", command=frontF)
if i == 0:
    back = Button(root, text="<", state=DISABLED)
else:
    back = Button(text="<", command=backF)

holder1.grid(row=0, column=0)
holder2.grid(row=0, column=3)
image.grid(row=1, column=1, columnspan= 3)
back.grid(row=2, column=0)
leave.grid(row=2, column=1)
front.grid(row=2, column=2, pady=3)
status.grid(row=3, column=2, sticky=E)

root.mainloop()