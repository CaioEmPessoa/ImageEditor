from PIL import ImageTk, Image
import customtkinter as ctk
import os

class fullView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Image Editor")
        self.geometry('1080x720')

        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure(1, weight = 1)

        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        APP_ICON = f"{location}\\..\\images\\icon.ico"
        self.iconbitmap(APP_ICON)

        self.config(background='black')

        self.IMAGES_FOLDER = f"{location}\\..\\images\\"

        ## TODO:
        ## in future remove this code and pass img_list in main.py 
        ## or a src file (probably)
        self.img_list = [self.IMAGES_FOLDER + img for img in os.listdir(self.IMAGES_FOLDER)]
        self.img_index = 0 # was 'i'
        self.img_lenght = len(self.img_list) - 1 # was 'leng'

        self.viewElements()

    def img_update(self, img_index):
        if img_index < 0 or img_index > self.img_lenght:
            return
        
        self.img_index = img_index

        image_original = Image.open(self.img_list[img_index])
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
        self.resized_tk = ImageTk.PhotoImage(resized_image)

        self.ImageFrame.delete("all")
        self.ImageFrame.create_image(frame_width//2, frame_height//2, anchor='center', image=self.resized_tk)

        self.status.configure(text=f"Image {img_index + 1} of {self.img_lenght + 1}")
        
        image_name = self.img_list[img_index].split("\\")[-1]
        self.imageNameLabel.configure(text=image_name)

        self.buttons_update()

    # JUST VISUAL, CAN REMOVE
    def buttons_update(self):
        if self.img_index == 0:
            self.back.configure(state="disabled")
        else:
            self.back.configure(state="normal")

        if self.img_index == self.img_lenght:
            self.front.configure(state="disabled")
        else:
            self.front.configure(state="normal")

    ## TODO: would be better to pass img_index as a parameter 
    def frontF(self):
        self.img_update(self.img_index+1)
        
    def backF(self):
        self.img_update(self.img_index-1)
        
    def viewElements(self):
        self.imageNameLabel = ctk.CTkLabel(self, text="Image Name Preview", fg_color='black', 
                                           font=("Consolas", 30))
        self.imageNameLabel.grid(row=0, column=0)

        self.ImageFrame = ctk.CTkCanvas(self,  bd=0, background="black", highlightthickness=0, relief='ridge')
        self.ImageFrame.bind('<Configure>', lambda event: self.img_update(self.img_index))
        self.ImageFrame.grid(row=1, column=0, sticky= "NSEW", padx=15, pady=15)
        
        self.ButtonFrame = ctk.CTkFrame(self, fg_color='black')
        self.ButtonFrame.grid(row=2, column=0, pady=15, sticky= "NSEW")

        self.ButtonFrame.columnconfigure((0, 1), weight = 1, uniform = 'a')
        self.ButtonFrame.rowconfigure((0, 1), weight = 1)

        holder = ctk.CTkLabel(self.ButtonFrame, text=" ")
        holder.grid(row=0, column=0)

        self.back = ctk.CTkButton(self.ButtonFrame, text="<", command=self.backF)
        self.back.grid(row=0, column=0)

        self.front = ctk.CTkButton(self.ButtonFrame, text=">", command=self.frontF)
        self.front.grid(row=0, column=1)

        self.status = ctk.CTkLabel(self.ButtonFrame, text=f"image {self.img_index + 1} of {self.img_lenght + 1}")
        self.status.grid(row=1, columnspan=2)

        #leave = ctk.CTkButton(self.ButtonFrame, text="Close app", command=exit)
        #leave.pack(pady=200)

        self.bind("<Right>", lambda s: self.frontF())
        self.bind("<Left>", lambda s: self.backF())
        self.focus_set()

        self.buttons_update() 

class runView():
    fullView().mainloop()

if __name__ == "__main__":
    runView()