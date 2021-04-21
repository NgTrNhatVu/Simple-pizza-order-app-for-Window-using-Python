from tkinter import *

from PIL import Image, ImageTk

import Algorithms
from ACanvas import ACanvas
from ClientInfo import ClientInfo
from Bill import *
from Helper import Helper
from Order import Order

# https://www.pizzaexpress.vn/


# Global list holds variables for radio buttons
# Bug fixed: radio buttons turn on when hover
radio_var = []


class App:
    def __init__(self, window, radio_var, pizza_list):
        self.window = window
        self.window.title("Dumb Pizza")
        self.window.geometry("1000x500")

        self.pizza_list = pizza_list

        # Initializing and temporary hidding all canvas
        self.__main_canvas = ACanvas(self.window)
        self.__main_canvas.repack()

        # Initializing frames inside their canvases
        self.menu_frame = Frame(self.__main_canvas.main_frame)
        self.cart_frame = Frame(self.__main_canvas.main_frame)
        self.bill_frame = Frame(self.__main_canvas.main_frame)
        self.create_menu_frame()

        self.buying_list = {
            "pro_id": [],
            "pro_name": [],
            "size": []
        }
        # Creating order object which holds all products in cart
        self.__order = Order()

################################ MENU START HERE   #############################
    def create_menu_frame(self):
        # Displaying canvas 1, which has the menu in it
        # Displaying menu frame
        self.menu_frame.pack(side=BOTTOM, fill=BOTH,
                             expand=True)

        # Tạo và thêm variables cho radio buttons vào list toàn cục đã tạo
        for i in range(len(self.pizza_list)):
            var = StringVar()
            # Phải có hàm set() để không bị lỗi
            # Không chọn gì thì sẽ hiển thị text này ở thông tin đơn hàng
            var.set("Chọn kích cỡ")
            radio_var.append(var)

        # ============== Displaying the MENU =================
        # The menu table's headers
        Label(self.menu_frame, text="Tên sản phẩm", font="bold", fg='#ca3435').grid(
            row=2, column=0, padx=10, pady=10)
        Label(self.menu_frame, text="Size nhỏ", font="bold", fg='#ca3435').grid(
            row=2, column=1, padx=10, pady=10)
        Label(self.menu_frame, text="Size vừa", font="bold", fg='#ca3435').grid(
            row=2, column=2, padx=10, pady=10)
        Label(self.menu_frame, text="Size lớn", font="bold", fg='#ca3435').grid(
            row=2, column=3, padx=10, pady=10)

        # Creating rows that hold product's information row by row
        r = 3
        index = 0
        for pizza in self.pizza_list:
            self.__create_pro_row(
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
            
    # This function create a row hold ONE product's information in the menu
    def __create_pro_row(self, a_pizza, radio_var, name, price_s, price_m, price_l, r):

        Label(self.menu_frame, text=name).grid(row=r, column=0, pady=5)

        a = Radiobutton(self.menu_frame, width=8, text=f'{price_s}₫', variable=radio_var,
                        value="s", indicator=0)
        a.grid(row=r, column=1)

        b = Radiobutton(self.menu_frame, width=8, text=f'{price_m}₫', variable=radio_var,
                        value="m", indicator=0)
        b.grid(row=r, column=2)

        c = Radiobutton(self.menu_frame, width=8, text=f'{price_l}₫', variable=radio_var,
                        value="l", indicator=0)
        c.grid(row=r, column=3)

        buy_btn = Button(
            self.menu_frame, text="Mua ngay",
            command=lambda: self.create_cart_frame(a_pizza, radio_var.get())
        )
        buy_btn.grid(row=r, column=4)
        # Changing color on hover affect
        buy_btn.bind("<Enter>", self.__on_enter)
        buy_btn.bind("<Leave>", self.__on_leave)
        return a, b, c

################################ MENU END HERE   #############################


################################ CART START HERE   #############################
    def create_cart_frame(self, product, size):
        # Hidding canvas 1, which displays menu
        self.menu_frame.forget()
        # Displaying canvas 2
        self.cart_frame.pack(side=BOTTOM, fill=BOTH,
                             expand=True)
        # Changing title
        self.window.title("Dumb Pizza - Đặt hàng")
        # Displaying cart frame
        self.cart_frame.pack(side=BOTTOM, fill=BOTH,
                             expand=True, anchor=CENTER)

        self.__order.add_product(product.get_pro_id(), size)

        # Creating a frame hold ONE product's information
        self.__products_in_cart_frame = self.__order.pro_info(self.cart_frame)
        self.__products_in_cart_frame.pack(side=TOP)

        # Initializing and displaying the frame that gets customer's information
        self.__info_form = ClientInfo()
        self.__info_form_frame = self.__info_form.create_form(self.cart_frame)
        self.__info_form_frame.pack()

        #Frame for three buttons
        self.__button_frame = Frame(self.cart_frame)
        self.__button_frame.pack(side=BOTTOM, padx=5, pady=5)
        
        # "Buy more product" button
        back_to_menu_btn = Button(
            self.__button_frame, text="Chọn thêm sản phẩm", width=20,
            command=lambda: self.__back_to_menu()
        )
        back_to_menu_btn.grid(row=0, column=0, padx=3)
        back_to_menu_btn.bind("<Enter>", self.__on_enter)
        back_to_menu_btn.bind("<Leave>", self.__on_leave)
        # Update cart button
        update_btn = Button(
            self.__button_frame, text="Không cần tải lại", width=20
        )
        update_btn.grid(row=0, column=1, padx=3)
        update_btn.bind("<Enter>", self.__on_enter)
        update_btn.bind("<Leave>", self.__on_leave)
        # Buy button
        buy_btn = Button(
            self.__button_frame, text="Mua ngay", width=20,
            command=lambda: self.__create_bill_frame()
        )
        buy_btn.grid(row=0, column=2, padx=3)
        buy_btn.bind("<Enter>", self.__on_enter)
        buy_btn.bind("<Leave>", self.__on_leave)
        
################################ CART END HERE   #############################


################################ BILL START HERE   #############################
    def __create_bill_frame(self):
        #self.__info_form.buying()
        
        #Get customer's info from ClientInfo.py
        self.__info_form.set_info()
        
        #Hide everything in cart frame
        self.__info_form_frame.destroy()
        self.__products_in_cart_frame.destroy()
        self.__button_frame.destroy()
        self.cart_frame.forget()
        
        #Create bill frame
        self.bill_frame.pack(side=BOTTOM, fill=BOTH,
                             expand=True)
        
        inner_bill = Bill(self.__order.get_pro_list(), self.__info_form.get_info(), self.__order.get_price_list())
        
        inner_bill.create_bill(self.bill_frame).pack()

################################ BILL END HERE   #############################


    def __on_enter(self, e):
        e.widget['background'] = '#ca3435'
        e.widget['foreground'] = 'white'

    def __on_leave(self, e):
        e.widget['background'] = 'SystemButtonFace'
        e.widget['foreground'] = 'black'

    def __back_to_menu(self):
        self.__info_form_frame.destroy()
        self.__products_in_cart_frame.destroy()
        self.__button_frame.destroy()
        self.cart_frame.forget()
        #Re-create menu frame
        self.create_menu_frame()

# def main():
#     #DRIVER CODE HERE!!!!
#     # Algorithms.quick_sort_by_id(products)
#     # Algorithms.quick_sort_by_name(products)
#     # Algorithms.quick_sort_by_price(products)
#     Algorithms.searching(pizzas, "Pizza")


if __name__ == "__main__":
    window = Tk()
    # Creating a list of objects that hold all product objects
    pizzas = Helper("./dataPizza.xlsx").get_list_of_product()
    app = App(window, radio_var, pizzas)

    window.mainloop()
