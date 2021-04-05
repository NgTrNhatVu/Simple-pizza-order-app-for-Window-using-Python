from tkinter import *

from PIL import Image, ImageTk

import Algorithms
from helper import Helper
from Order import Order

#https://www.pizzaexpress.vn/
#List toàn cục chứa các variable cho radio buttons
radio_var = []

class App:
    def __init__(self, window, radio_var, pizza_list):
        self.window = window
        self.window.title("Dumb Pizza")
        self.window.geometry("800x500")
        
        #Khai báo các Frame
        self.info_frame = ''
        
        #Tạo Canvas
        self.main_canvas = Canvas(self.window)
        self.main_canvas.pack(side =LEFT, fill = BOTH, expand=1)
        
        #scrollbar
        self.my_scrollbar = Scrollbar(self.window, orient=VERTICAL, command=self.main_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)
        
        #Configure main_canvas cho scrollbar
        self.main_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(
            scrollregion = self.main_canvas.bbox("all"))
            )
        
        #Tạo frame khác bên trong canvas
        self.main_frame = Frame(self.main_canvas)
        self.main_frame.pack(side = BOTTOM)
        
        self.main_canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        
        self.info_frame = Frame(self.main_frame)
                
        #Banner
        banner_image = Image.open("img/banner.jpg").resize((700, 150), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(banner_image)

        banner = Label(self.main_frame, image=test)
        banner.pack(side=TOP, fill=X)
        banner.image = test
        
        #MENU FRAME
        self.menu_frame = Frame(self.main_frame)
        self.menu_frame.pack(side=BOTTOM)
        
        #Tạo và thêm variables cho radio buttons vào list toàn cục đã tạo
        for i in range (len(pizza_list)):
            var = StringVar()
            #Phải có hàm set() để không bị lỗi
            #Không chọn gì thì sẽ hiển thị text này ở thông tin đơn hàng
            var.set("Vui lòng chọn kích cỡ") 
            radio_var.append(var)

        #=====  Hien thi ten san pham
        #Tieu de
        Label(self.menu_frame, text="Tên sản phẩm", font="bold", fg='#ca3435').grid(
            row = 2, column = 0, padx=10, pady=10)
        Label(self.menu_frame, text="Size nhỏ", font="bold", fg='#ca3435').grid(
            row = 2, column = 1, padx=10, pady=10)
        Label(self.menu_frame, text="Size vừa", font="bold", fg='#ca3435').grid(
            row = 2, column = 2, padx=10, pady=10)
        Label(self.menu_frame, text="Size lớn", font="bold", fg='#ca3435').grid(
            row = 2, column = 3, padx=10, pady=10)
        
        #Tạo từng hàng chứa thông tin từng sản phẩm
        r = 3
        index = 0
        for pizza in pizza_list:
            self.create_pro_row(
                pizza,
                radio_var[index],
                pizza.get_name(),
                pizza.get_s(),
                pizza.get_m(),
                pizza.get_l(),
                r
            )
            r += 1
            index += 1
            
    # function tao mot hang thong tin san pham
    def create_pro_row(self, a_pizza,radio_var, name, price_s, price_m, price_l, r):
        
        Label(self.menu_frame, text = name).grid(row = r, column = 0, pady=5)
        
        a = Radiobutton(self.menu_frame, text = f'{price_s}₫', variable = radio_var, value = "s")
        a.grid(row = r, column = 1)
        
        
        b = Radiobutton(self.menu_frame, text = f'{price_m}₫', variable =  radio_var, value = "m")
        b.grid(row = r, column = 2)
        
        c = Radiobutton(self.menu_frame, text = f'{price_l}₫', variable =  radio_var, value = "l")
        c.grid(row = r, column = 3)
        
        buy_btn = Button(
            self.menu_frame, text="Mua ngay",
            command=lambda: self.show_details(a_pizza, radio_var.get())
            )
        buy_btn.grid(row=r, column=4)
        #Hiệu ứng đổi màu khi hover
        buy_btn.bind("<Enter>", self.on_enter)
        buy_btn.bind("<Leave>", self.on_leave)
        return a, b, c
    
    def on_enter(self, e):
        e.widget['background'] = '#ca3435'
        e.widget['foreground'] = 'white'
    
    def on_leave(self, e):
        e.widget['background'] = 'SystemButtonFace'
        e.widget['foreground'] = 'black'
    
    def show_details(self, product, size):
        # Hủy frame chứa menu
        self.menu_frame.forget()
        order = Order(
            self.window,
            product.get_pro_id(),
            product.get_name(),
            product.get_pro_type(),
            size,
            product.get_status()
        )
        #Lấy và hiển thị frame mới được tạo trong hàm Order.pro_detail()
        
        pro_frame = order.cart(self.window, self.info_frame)
        pro_frame.pack()
        self.info_frame.pack(side=TOP)
        back_to_menu_btn = Button(
            self.main_frame, text="Mua thêm sản phẩm",
            command=lambda: self.back_to_menu(back_to_menu_btn)
            )
        back_to_menu_btn.pack(side=BOTTOM, padx=5, pady=5)
        back_to_menu_btn.bind("<Enter>", self.on_enter)
        back_to_menu_btn.bind("<Leave>", self.on_leave)
        
    def back_to_menu(self, back_btn):
        self.info_frame.forget()
        back_btn.forget()
        self.menu_frame.pack()

    
# def main():
#     #DRIVER CODE HERE!!!!
#     # Algorithms.quick_sort_by_id(products)
#     # Algorithms.quick_sort_by_name(products)
#     # Algorithms.quick_sort_by_price(products)
#     Algorithms.searching(pizzas, "Pizza")

if __name__ == "__main__":
    window = Tk()
    # khởi tạo list cac san pham
    pizzas = Helper("dataPizza.xlsx").get_list_of_product()
    app = App(window, radio_var, pizzas)

    window.mainloop()
