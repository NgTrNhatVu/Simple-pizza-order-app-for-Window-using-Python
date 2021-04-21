from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

from Algorithms import Algorithm
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
        self.window.iconphoto(True, ImageTk.PhotoImage(file = "./img/icon.jpg"))
        self.window.geometry("1000x500")

        self.pizza_list = pizza_list

        # Initializing and temporary hidding all canvas
        self.__main_canvas = ACanvas(self.window)
        self.__main_canvas.repack()

        
        # Initializing frames inside their canvases
        self.menu_frame = Frame(self.__main_canvas.main_frame)
        self.cart_frame = Frame(self.__main_canvas.main_frame)
        #self.bill_frame will be initialized later when buy button pressed
        
        #Program starts here by create the menu frame 
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

        #======= Sorting Algorithm
        Label(self.menu_frame, text="Sắp xếp theo: ", font=('default', 10, "bold")).grid(row=1, column=0, padx=10, pady=10)
        sort_choice = StringVar()
        OptionMenu(self.menu_frame, sort_choice, "Tìm theo giá tiền", "Tìm theo bảng chữ cái", 
                   command = self.__sorting).grid(
            row=1, column=1, padx=5, pady=10)
        
        
        #======= Searching Algorithm
        Label(self.menu_frame, text="Tìm kiếm", font=('default', 10, "bold")).grid(row=1, column=2, pady=10)
        self.find_by_name = Entry(self.menu_frame)
        self.find_by_name.grid(row=1, column=3, padx=5, pady=10)
        self.find_by_name.bind("<Return>", self.__searching)
        
        #Reset pizza_list after it got changed due to __searching function
        Button(self.menu_frame, text="Quay lại", command=self.reset_list).grid(
            row=1, column=4, padx=10, pady=10)
        
        #======== To the cart
        Button(self.menu_frame, text="Giỏ hàng", command=self.to_cart).grid(
            row=1, column=5, padx=10, pady=10)

        
        # ============================ Displaying the MENU ============================
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
        r = 3 #first row start at row 3
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
            command=lambda: self.create_cart_frame(product = a_pizza, size = radio_var.get())
        )
        buy_btn.grid(row=r, column=4)
        # Changing color on hover affect
        buy_btn.bind("<Enter>", self.__on_enter)
        buy_btn.bind("<Leave>", self.__on_leave)
    
    def __sorting(self, selection):
        if selection == "Tìm theo giá tiền":
            self.pizza_list = Algorithm().quick_sort_by_price(self.pizza_list)
        if selection == "Tìm theo bảng chữ cái":
            self.pizza_list = Algorithm().quick_sort_by_name(self.pizza_list)
        
        #Delete old menu order
        self.menu_frame.destroy()
        #Re-create menu with new list
        self.menu_frame = Frame(self.__main_canvas.main_frame)
        self.create_menu_frame()
        
    def __searching(self, e):

        self.pizza_list = Algorithm().searching(self.pizza_list, self.find_by_name.get())
        
        #Delete old menu order
        self.menu_frame.destroy()
        #Re-create menu with new list
        self.menu_frame = Frame(self.__main_canvas.main_frame)
        self.create_menu_frame()
        
    def reset_list(self):
        print("reset")
        self.pizza_list = Helper("./dataPizza.xlsx").get_list_of_product()
        
        #Delete old menu order
        self.menu_frame.destroy()
        #Re-create menu with new list
        self.menu_frame = Frame(self.__main_canvas.main_frame)
        self.create_menu_frame()
        
    def to_cart(self):
        self.create_cart_frame()
################################ MENU END HERE   #############################


################################ CART START HERE   #############################
    def create_cart_frame(self, **kwargs):
        # Changing title
        self.window.title("Dumb Pizza - Đặt hàng")
        # Hidding canvas 1, which displays menu
        self.menu_frame.forget()
        # Displaying cart frame
        self.cart_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
        
        #If cart != empty => self.cart_frame.pack()
        
        #If there is any product parse in
        try:
            self.__order.add_product(kwargs['product'].get_pro_id(), kwargs['size'])

            # Creating a frame hold ONE product's information
            self.__products_in_cart_frame = self.__order.pro_info(self.cart_frame)
            self.__products_in_cart_frame.pack(side=TOP)
        except:

            self.__products_in_cart_frame = Label(self.cart_frame, 
                                                  text="Giỏ hàng trống",
                                                  font=("default", 10, "bold"),
                                                  fg = '#ca3435')
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
        # Buy button
        buy_btn = Button(
            self.__button_frame, text="Mua ngay", width=20,
            command=lambda: self.__create_bill_frame()
        )
        buy_btn.grid(row=0, column=2, padx=3)
        buy_btn.bind("<Enter>", self.__on_enter)
        buy_btn.bind("<Leave>", self.__on_leave)
        
    def __back_to_menu(self):
        self.__info_form_frame.destroy()
        self.__products_in_cart_frame.destroy()
        self.__button_frame.destroy()
        self.cart_frame.forget()
        #Re-create menu frame
        self.create_menu_frame()
        
################################ CART END HERE   #############################


################################ BILL START HERE   #############################
    def __create_bill_frame(self):
        #self.__info_form.buying()
        
        #Get customer's info from ClientInfo.py
        if self.__info_form.set_info() == True:
            #Hide cart frame
            self.cart_frame.forget()
            
            #Create bill frame
            self.bill_frame = Frame(self.__main_canvas.main_frame)
            self.bill_frame.pack(side=BOTTOM, fill=BOTH,
                                expand=True)
            
            inner_bill = Bill(self.__order.get_pro_list(), self.__info_form.get_info(), self.__order.get_price_list())
            
            inner_bill.create_bill(self.bill_frame).pack()
            
            bill_btn_frame = Frame(self.bill_frame)
            bill_btn_frame.pack()
            
            back_to_cart_btn = Button(bill_btn_frame, text="Chọn thêm sản phẩm", 
                                      width=20, command=lambda: self.__back_to_cart()
                                )
            back_to_cart_btn.pack(pady=5)
            back_to_cart_btn.bind("<Enter>", self.__on_enter)
            back_to_cart_btn.bind("<Leave>", self.__on_leave)
            
            
    def __back_to_cart(self):
        self.bill_frame.destroy()
        self.cart_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
################################ BILL END HERE   #############################


    def __on_enter(self, e):
        e.widget['background'] = '#ca3435'
        e.widget['foreground'] = 'white'

    def __on_leave(self, e):
        e.widget['background'] = 'SystemButtonFace'
        e.widget['foreground'] = 'black'



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
