from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
import os

root = Tk()
root.title("Image Editor")
root.geometry('1080x720')

root.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
root.rowconfigure(0, weight = 1)

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
folder = f"{location}\\images\\"
icon = f"{location}\\src\\icon.ico"
root.iconbitmap(icon)

img_list = [folder + img for img in os.listdir(folder)]
leng = len(img_list) - 1
i = 0

ImageFrame = Canvas(root, background= 'black', bd=0, highlightthickness=0, relief='ridge')
ButtonFrame = Frame(root)

def stretch_image(img):
    global resized_tk
    
    width = img.width
    height = img.height
    
    resized_img = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_img)

    ImageFrame.create_image(0,0, image=resized_tk, anchor='nw')

def screen():
    global image
    global back
    global front
    global i
    global img_list
    global open_img
    global leng
    global status

    image_original = Image.open(img_list[i])
    open_img = ImageTk.PhotoImage(image_original)
    ImageFrame.create_image(0,0, image=open_img)
    if i == 0:
        back = ctk.CTkButton(ButtonFrame, text="<", state=DISABLED)
    else:
        back = ctk.CTkButton(ButtonFrame, text="<", command=backF)
    back.pack(pady=10)
    if i == leng:
        front = ctk.CTkButton(ButtonFrame, text=">", state=DISABLED)
    else:
        front = ctk.CTkButton(ButtonFrame, text=">", command=frontF)
    front.pack(pady=10)
    status = Label(ButtonFrame, text=f"image {i + 1} of {leng + 1}")
    status.pack(pady=10)
    leave = ctk.CTkButton(ButtonFrame, text="Close app", command=exit)
    leave.pack(pady=250)
    ImageFrame.grid(row=0, column=2, columnspan=3, sticky= NSEW)
    ButtonFrame.grid(row=0, column=0, sticky= NSEW)


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


#image = Label(ImageFrame, image=open_img)
#image.pack()
#ImageFrame.create_image(0,0, image=open_img, anchor = 'nw')
ImageFrame.bind('<Configure>', stretch_image)

if i == 0:
    back = ctk.CTkButton(ButtonFrame, text="<", state=DISABLED)
else:
    back = ctk.CTkButton(ButtonFrame, text="<", command=backF)
back.pack(pady=10)

if i == leng:
    front = ctk.CTkButton(ButtonFrame, text=">", state=DISABLED)
else:
    front = ctk.CTkButton(ButtonFrame, text=">", command=frontF)
front.pack(pady=10)

status = Label(ButtonFrame, text=f"image {i + 1} of {leng + 1}")
status.pack(pady=10)

leave = ctk.CTkButton(ButtonFrame, text="Close app", command=exit)
leave.pack(pady=200)

ImageFrame.grid(row=0, column=2, columnspan=3, sticky= NSEW)
ButtonFrame.grid(row=0, column=0, sticky= NSEW)

root.mainloop()