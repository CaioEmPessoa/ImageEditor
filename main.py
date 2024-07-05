from src import *
from views import imageViews

class MainApp():
    def __init__(self):
        super().__init__()

        image_views = imageViews.fullView()        
        image_views.mainloop()

if __name__ == "__main__":
    main_app = MainApp()