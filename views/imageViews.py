from tkinter import *
from PIL import ImageTk, Image
import customtkinter as ctk
import os

class fullView(Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Editor")
        self.geometry('1080x720')

        self.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
        self.rowconfigure(0, weight = 1)

        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        APP_ICON = f"{location}\\..\\images\\icon.ico"
        self.iconbitmap(APP_ICON)
        
        self.IMAGES_FOLDER = f"{location}\\..\\images\\"


        self.img_list = [self.IMAGES_FOLDER + img for img in os.listdir(self.IMAGES_FOLDER)]
        self.img_index = 0 # was 'i'
        self.img_lenght = len(self.img_list) - 1 # was 'leng'

        self.viewElements()

    def img_update(self):
        global resized_tk

        image_original = Image.open(self.img_list[self.img_index])
        ImageFrame_ratio = image_original.width / image_original.height

        frame_width = self.ImageFrame.winfo_width()
        frame_height = self.ImageFrame.winfo_height()

        if frame_width / frame_height > ImageFrame_ratio:
            width = int(frame_height * ImageFrame_ratio)
            height = frame_height
        else:
            height = int(frame_width / ImageFrame_ratio)
            width = frame_width

        resized_image = image_original.resize((width, height))
        resized_tk = ImageTk.PhotoImage(resized_image)

        self.ImageFrame.delete("all")
        self.ImageFrame.create_image(frame_width//2, frame_height//2, anchor='center', image=resized_tk)

        self.status.config(text=f"Image {self.img_index + 1} of {self.img_index + 1}")

    def buttons_update(self):
        if self.img_index == 0:
            self.back.configure(state=DISABLED, fg_color='red')
        else:
            self.back.configure(state=NORMAL, fg_color='blue')

        if self.img_index == self.img_lenght:
            self.front.configure(state=DISABLED, fg_color='red')
        else:
            self.front.configure(state=NORMAL, fg_color='blue')

    def frontF(self):
        self.img_index += 1
        self.buttons_update()
        self.img_update()
        
    def backF(self):
        self.img_index -= 1
        self.buttons_update()
        self.img_update()
        
    def viewElements(self):
        ## TODO: CHANGE GRID
        self.ImageFrame = Canvas(self, background= 'black', bd=0, highlightthickness=0, relief='ridge')
        self.ButtonFrame = Frame(self)

        image_original = Image.open(self.img_list[self.img_index])
        image_ratio = image_original.size[0] / image_original.size[1] # not used

        image_tk = ImageTk.PhotoImage(image_original) # not used

        self.ImageFrame.bind('<Configure>', lambda event: self.img_update())

        holder = ctk.CTkLabel(self.ButtonFrame, text=" ")
        holder.pack(pady=40)

        self.back = ctk.CTkButton(self.ButtonFrame, text="<", command=lambda: self.backF())
        self.back.pack(pady=10)

        self.front = ctk.CTkButton(self.ButtonFrame, text=">", command=lambda: self.frontF())
        self.front.pack(pady=10)

        self.buttons_update() 

        self.status = Label(self.ButtonFrame, text=f"image {self.img_index + 1} of {self.img_lenght + 1}")
        self.status.pack(pady=10)

        leave = ctk.CTkButton(self.ButtonFrame, text="Close app", command=exit)
        leave.pack(pady=200)

        self.ImageFrame.grid(row=0, column=2, columnspan=3, sticky= NSEW)
        self.ButtonFrame.grid(row=0, column=0, sticky= NSEW)