from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap('C:/Users/User/Documents/programa acao/ImageViewer/images/icon.ico')

img_list = []

image = Label(image=img_list)
back = Button(text="<")
leave = Button(text="Close", command=exit)
front = Button(text=">")


image.grid(row=0, column=0, columnspan= 3)
back.grid(row=1, column=0)
leave.grid(row=1, column=1)
front.grid(row=1, column=2)

root.mainloop()