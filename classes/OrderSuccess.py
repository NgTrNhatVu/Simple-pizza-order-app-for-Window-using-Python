from tkinter import *
from PIL import Image, ImageTk

class OrderSuccess:
    def create_frame(self, contain_frame):
        banner_image = Image.open(
            "./img/shipping.jpg").resize((720, 400), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(banner_image)

        banner = Label(contain_frame, image=test)
        banner.pack(side=TOP, fill=BOTH, expand=True, anchor=CENTER)
        banner.image = test
        
        