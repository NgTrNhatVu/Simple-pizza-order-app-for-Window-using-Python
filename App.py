from tkinter import *

from PIL import Image, ImageTk

import Algorithms
from A_Canvas import A_Canvas
from ClientInfo import ClientInfo
from Helper import Helper
from Order import Order

# https://www.pizzaexpress.vn/
# List toàn cục chứa các variable cho radio buttons
radio_var = []


class App:
    def __init__(self, window, radio_var, pizza_list):
        self.window = window
        self.window.title("Dumb Pizza")
        self.window.geometry("800x500")

        self.pizza_list = pizza_list

        # Khai báo các Canvas
        self.canvas1 = A_Canvas(self.window)
        self.canvas2 = A_Canvas(self.window)

        # Tạm thòi ẩn các canvas
        self.canvas1.forget_all()
        self.canvas2.forget_all()

        # Khai báo các Frame
        self.menu_frame = Frame(self.canvas1.main_frame)
        self.cart_frame = Frame(self.canvas2.main_frame)

        self.create_menu_frame()

        self.buying_list = {
            "pro_id": [],
            "pro_name": [],
            "size": []
        }

    def create_menu_frame(self):
        # Hiện thị canvas 1
        self.canvas1.repack()
        # MENU FRAME
        self.menu_frame.pack(side=BOTTOM)

        # Tạo và thêm variables cho radio buttons vào list toàn cục đã tạo
        for i in range(len(self.pizza_list)):
            var = StringVar()
            # Phải có hàm set() để không bị lỗi
            # Không chọn gì thì sẽ hiển thị text này ở thông tin đơn hàng
            var.set("Vui lòng chọn kích cỡ")
            radio_var.append(var)

        # =====  Hien thi ten san pham
        # Tieu de
        Label(self.menu_frame, text="Tên sản phẩm", font="bold", fg='#ca3435').grid(
            row=2, column=0, padx=10, pady=10)
        Label(self.menu_frame, text="Size nhỏ", font="bold", fg='#ca3435').grid(
            row=2, column=1, padx=10, pady=10)
        Label(self.menu_frame, text="Size vừa", font="bold", fg='#ca3435').grid(
            row=2, column=2, padx=10, pady=10)
        Label(self.menu_frame, text="Size lớn", font="bold", fg='#ca3435').grid(
            row=2, column=3, padx=10, pady=10)

        # Tạo từng hàng chứa thông tin từng sản phẩm
        r = 3
        index = 0
        for pizza in self.pizza_list:
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
    def create_pro_row(self, a_pizza, radio_var, name, price_s, price_m, price_l, r):

        Label(self.menu_frame, text=name).grid(row=r, column=0, pady=5)

        a = Radiobutton(self.menu_frame,
                        text=f'{price_s}₫', variable=radio_var, value="s")
        a.grid(row=r, column=1)

        b = Radiobutton(self.menu_frame,
                        text=f'{price_m}₫', variable=radio_var, value="m")
        b.grid(row=r, column=2)

        c = Radiobutton(self.menu_frame,
                        text=f'{price_l}₫', variable=radio_var, value="l")
        c.grid(row=r, column=3)

        buy_btn = Button(
            self.menu_frame, text="Mua ngay",
            command=lambda: self.create_cart_frame(a_pizza, radio_var.get())
        )
        buy_btn.grid(row=r, column=4)
        # Hiệu ứng đổi màu khi hover
        buy_btn.bind("<Enter>", self.on_enter)
        buy_btn.bind("<Leave>", self.on_leave)
        return a, b, c

    def on_enter(self, e):
        e.widget['background'] = '#ca3435'
        e.widget['foreground'] = 'white'

    def on_leave(self, e):
        e.widget['background'] = 'SystemButtonFace'
        e.widget['foreground'] = 'black'

    def create_cart_frame(self, product, size):
        # Hủy canvas 1 chứa menu
        self.canvas1.forget_all()
        # Hiển thị canvas 2
        self.canvas2.repack()
        # Hiển thị frame Giỏ hàng
        self.cart_frame.pack(side=BOTTOM)
        order = Order(
            self.window,
            product.get_pro_id(),
            product.get_name(),
            product.get_pro_type(),
            size,
            product.get_status()
        )

        # Tạo frame chứa thông tin sản phẩm
        pro_frame = order.cart(self.window, self.cart_frame)
        pro_frame.pack()

        # Frame lấy thông tin khách hàng
        self.info_form_frame = ClientInfo.create_form(self.cart_frame)
        self.info_form_frame.pack(side=TOP)

        # Nút tiếp tục mua sắm
        back_to_menu_btn = Button(
            self.cart_frame, text="Chọn thêm sản phẩm",
            command=lambda: self.back_to_menu(back_to_menu_btn)
        )
        back_to_menu_btn.pack(side=BOTTOM, padx=5, pady=5)
        back_to_menu_btn.bind("<Enter>", self.on_enter)
        back_to_menu_btn.bind("<Leave>", self.on_leave)
        # Nút mua hàng
        buy_btn = Button(
            self.cart_frame, text="Mua ngay",
            command=lambda: self.buy()
        )

    def buy(self):
        print("Mua hang")

    def back_to_menu(self, back_btn):
        self.canvas2.forget_all()
        self.info_form_frame.destroy()
        back_btn.destroy()
        self.create_menu_frame()

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
