from tkinter import *
from PIL import Image, ImageTk

class A_Canvas:
    def __init__(self, window):
        #Tạo Canvas
        self.main_canvas = ''
        self.main_canvas = Canvas(window, bg='#ca3435')
        self.main_canvas.pack(side=LEFT, fill = BOTH, expand=1)
        
        #scrollbar
        self.my_scrollbar = Scrollbar(window, orient=VERTICAL, command=self.main_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)
        
        #Configure main_canvas cho scrollbar
        self.main_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(
            scrollregion = self.main_canvas.bbox("all"))
            )
        
        #Tạo frame khác bên trong canvas
        self.main_frame = Frame(self.main_canvas)
        self.main_frame.pack(side = BOTTOM)
        
        self.main_canvas.create_window(1, 0, window=self.main_frame, anchor="n")
                
        #Banner
        banner_image = Image.open("img/banner.jpg").resize((700, 150), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(banner_image)

        banner = Label(self.main_frame, image=test, justify='right')
        banner.pack(side=TOP, fill=X)
        banner.image = test
        
    def forget_all(self):
        self.main_canvas.forget()
        self.my_scrollbar.forget()
        
    def repack(self):
        self.main_canvas.pack(side=LEFT, fill = BOTH, expand=1)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)