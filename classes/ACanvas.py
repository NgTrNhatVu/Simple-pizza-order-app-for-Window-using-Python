from tkinter import *
from PIL import Image, ImageTk


class ACanvas:
    def __init__(self, window):
        # Creating a canvas
        self.main_canvas = ''
        self.main_canvas = Canvas(window, bg='#ca3435')
        self.main_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # scrollbar
        self.my_scrollbar = Scrollbar(
            window, orient=VERTICAL, command=self.main_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure main_canvas for scrollbar
        self.main_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(
            scrollregion=self.main_canvas.bbox("all"))
        )

        # Making a frame inside the new canvas 
        self.main_frame = Frame(self.main_canvas,)

        self.main_canvas.create_window(
            0, 0, window=self.main_frame, anchor="nw")
        # self.main_canvas.bind("<Configure>", self.__onCanvasConfigure)
        # Banner
        banner_image = Image.open(
            "./img/banner.jpg").resize((700, 150), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(banner_image)

        self.banner = Label(self.main_frame, image=test)
        self.banner.pack(side=TOP, fill=BOTH, expand=True, anchor=CENTER)
        self.banner.image = test

    # def __onCanvasConfigure(self, e):
    #     self.main_canvas.itemconfig('main_frame', height=self.main_canvas.winfo_height(), width=self.main_canvas.winfo_width())
    
    def forget_all(self):
        self.main_canvas.forget()
        self.my_scrollbar.forget()

    def repack(self):
        self.main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)
