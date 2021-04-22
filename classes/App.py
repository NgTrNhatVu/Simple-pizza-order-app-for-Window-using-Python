from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

from Algorithms import Algorithm
from ACanvas import ACanvas
from ClientInfo import ClientInfo
from Bill import *
from Helper import Helper
from Order import Order
from OrderSuccess import OrderSuccess

# https://www.pizzaexpress.vn/


# Global list holds variables for radio buttons
# Bug fixed: radio buttons turn on when hover
radio_var = []


class App:
    def __init__(self, window, radio_var, pizza_list):
        self.__window = window
        self.__window.title("Dumb Pizza")
        self.__window.iconphoto(True, ImageTk.PhotoImage(file = "./img/icon.jpg"))
        self.__window.geometry("720x550")

        self.pizza_list = pizza_list

        # Initializing and temporary hidding all canvas
        self.__main_canvas = ACanvas(self.__window)
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
        self.menu_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

        Label(self.menu_frame, text="Dumb Pizza - Menu sản phẩm", 
                font = ('default', 14, "bold"), 
                fg = '#ca3435').grid(
                    row=0, column=0, padx=10, pady=5, columnspan=4
                )
        #======== To the cart
        Button(self.menu_frame, text="Giỏ hàng", 
               font = ('default', 8, "bold"),
               fg="white", bg="#ca3435", 
               highlightthickness = 0, bd = 0,
               command=self.__to_cart).grid(
            row=0, column=4, padx=10, pady=5, ipadx=10, ipady=5)
        
        #======= Sorting Algorithm
        Label(self.menu_frame, text="Sắp xếp theo: ", font=('default', 10, "bold")).grid(row=1, column=0, padx=10, pady=10)
        sort_choice = StringVar()
        OptionMenu(self.menu_frame, sort_choice, "Tìm theo giá tiền", "Tìm theo bảng chữ cái", 
                   command = self.__sorting).grid(
            row=1, column=1, padx=5, pady=10)
        
        #======= Searching Algorithm
        Label(self.menu_frame, text="Tìm kiếm", font=('default', 10, "bold")).grid(row=1, column=2, pady=10)
        self.find_by_name = Entry(self.menu_frame, width=12)
        self.find_by_name.grid(row=1, column=3, pady=10)
        self.find_by_name.bind("<Return>", self.__searching)
        
        #Reset pizza_list after it got changed due to __searching function
        reset_btn = Button(self.menu_frame, text="Quay lại", command=self.__reset_list)
        reset_btn.grid(row=1, column=4, padx=10, pady=10)
        reset_btn.bind("<Enter>", self.__on_enter)
        reset_btn.bind("<Leave>", self.__on_leave)
        
        # ============================ Displaying the MENU ============================
        # The menu table's headers
        Label(self.menu_frame, text="Tên sản phẩm", font=('default', 12, "bold"), fg='#ca3435').grid(
            row=2, column=0, padx=10, pady=10)
        Label(self.menu_frame, text="Size nhỏ", font=('default', 12, "bold"), fg='#ca3435').grid(
            row=2, column=1, padx=10, pady=10)
        Label(self.menu_frame, text="Size vừa", font=('default', 12, "bold"), fg='#ca3435').grid(
            row=2, column=2, padx=10, pady=10)
        Label(self.menu_frame, text="Size lớn", font=('default', 12, "bold"), fg='#ca3435').grid(
            row=2, column=3, padx=10, pady=10)

        # Tạo và thêm variables cho radio buttons vào list toàn cục đã tạo
        for i in range(len(self.pizza_list)):
            var = StringVar()
            # Phải có hàm set() để không bị lỗi
            # Không chọn gì thì sẽ hiển thị text này ở thông tin đơn hàng
            var.set("Chọn kích cỡ")
            radio_var.append(var)
            
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
            
    def __create_pro_row(self, a_pizza, radio_var, name, price_s, price_m, price_l, r):
    # This function create a row hold ONE product's information in the menu
        Label(self.menu_frame, text=name).grid(row=r, column=0, pady=5)

        #Radio options
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
            self.menu_frame, text="Thêm vào giỏ",
            command=lambda: self.create_cart_frame(product = a_pizza, size = radio_var.get())
        )
        buy_btn.grid(row=r, column=4, ipady=3, pady=3)
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
        
    def __reset_list(self):
        self.pizza_list = Helper("./dataPizza.xlsx").get_list_of_product()
        
        #Delete old menu order
        self.menu_frame.destroy()
        #Re-create menu with new list
        self.menu_frame = Frame(self.__main_canvas.main_frame)
        self.create_menu_frame()
        
    #Go to cart
    def __to_cart(self):
        self.create_cart_frame()
################################ MENU END HERE   #############################


################################ CART START HERE   #############################
    def create_cart_frame(self, **kwargs):
        # Changing title
        self.__window.title("Dumb Pizza - Đặt hàng")
        # Hidding canvas 1, which displays menu
        self.menu_frame.forget()
        # Displaying cart frame
        self.cart_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
        
       
        #If there is any argument for product parse in
        try:
            self.__order.add_product(kwargs['product'].get_pro_id(), kwargs['size'])

            # Creating a frame hold product's information
            self.__products_in_cart_frame = self.__order.pro_info(self.cart_frame)
            self.__products_in_cart_frame.pack(side=TOP)
        #If not (user press "cart" button)
        except:
            #If cart is empty => Print "Cart is empty"
            if not self.__order.get_pro_list()["pro_id"]:
                self.__products_in_cart_frame = Label(self.cart_frame, 
                                                    text="Giỏ hàng trống",
                                                    font=("default", 10, "bold"),
                                                    fg = '#ca3435')
                self.__products_in_cart_frame.pack(side=TOP, pady=10)
            #If cart is not empty => create and pck self.cart_frame
            else:
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
        # Buy button
        buy_btn = Button(
            self.__button_frame, text="Mua ngay", width=20,
            command=lambda: self.__create_bill_frame()
        )
        buy_btn.grid(row=0, column=2, padx=3)
        buy_btn.bind("<Enter>", self.__on_enter_green)
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
    def __create_bill_frame(self, **kwargs):
        #self.__info_form.buying()
        
        #Get customer's info from ClientInfo.py
        if self.__info_form.set_info() == True:
            #Hide cart frame
            self.cart_frame.forget()
            
            #Create bill frame
            self.bill_frame = Frame(self.__main_canvas.main_frame)
            self.bill_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
            
            inner_bill = Bill(self.__order.get_pro_list(), self.__info_form.get_info(), self.__order.get_price_list())
            
            inner_bill.create_bill(self.bill_frame).pack()
            
            bill_btn_frame = Frame(self.bill_frame)
            bill_btn_frame.pack()
            try:
                if kwargs['isReadOnly'] == True:
                    print ("True")
                    #Delete success frame
                    self.__success_frame.destroy()
                    #Repack banner
                    self.__main_canvas.banner.pack(side=TOP, fill=BOTH, expand=True, anchor=CENTER)
                    
                    back_to_menu_btn = Button(
                        bill_btn_frame, text="Tiếp tục mua sắm", width=20,
                        command=lambda: self.__re_shopping()
                    )
                    back_to_menu_btn.grid(row=0, column=0, padx=5, pady=5)
                    back_to_menu_btn.bind("<Enter>", self.__on_enter_green)
                    back_to_menu_btn.bind("<Leave>", self.__on_leave)
            except:
                back_to_cart_btn = Button(bill_btn_frame, text="Quay lại giỏ hàng", 
                                        width=20, command=self.__back_to_cart
                                    )
                back_to_cart_btn.grid(row=0, column=0, padx=5, pady=5)
                back_to_cart_btn.bind("<Enter>", self.__on_enter)
                back_to_cart_btn.bind("<Leave>", self.__on_leave)
                
                confirm_buy_btn = Button(bill_btn_frame, text="Xác nhận mua",
                                        width=20, command=self.__create_success_frame)
                confirm_buy_btn.grid(row=0, column=1, padx=5, pady=5)
                confirm_buy_btn.bind("<Enter>", self.__on_enter_green)
                confirm_buy_btn.bind("<Leave>", self.__on_leave)
            
    def __back_to_cart(self):
        self.bill_frame.destroy()
        self.cart_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
        
################################ BILL END HERE   #############################

################################    SUCCESS ##################################
    def __create_success_frame(self):
        #Delete bill frame
        self.bill_frame.destroy()
        #Hide banner
        self.__main_canvas.banner.forget()
        
        self.__success_frame = Frame(self.__main_canvas.main_frame)
        self.__success_frame.pack(side=BOTTOM, fill=BOTH, expand=True)
        
        OrderSuccess().create_frame(self.__success_frame)
        
        success_btn = Frame(self.__success_frame)
        success_btn.pack()
        
        back_to_menu_btn = Button(
            success_btn, text="Tiếp tục mua sắm", width=20,
            bg='#ca3435', fg="white",
            command=lambda: self.__re_shopping()
        )
        back_to_menu_btn.grid(row=0, column=0, padx=5, pady=5)
        
        check_bill_btn = Button(
            success_btn, text="Xem đơn hàng", width=20,
            bg='#ca3435', fg="white",
            command=lambda: self.__create_bill_frame(isReadOnly=True)
        )
        check_bill_btn.grid(row=0, column=1, padx=5, pady=5)
        
    def __re_shopping(self):
        try:
            #Delete success frame
            self.__success_frame.destroy()
            #Repack banner
            self.__main_canvas.banner.pack(side=TOP, fill=BOTH, expand=True, anchor=CENTER)
        except:
            print()
        #Call menu
        self.create_menu_frame()
    

######################### OTHER FUNCTIONS    ################################
    def __on_enter(self, e):
        e.widget['background'] = '#ca3435'
        e.widget['foreground'] = 'white'

    def __on_leave(self, e):
        e.widget['background'] = 'SystemButtonFace'
        e.widget['foreground'] = 'black'
        
    def __on_enter_green(self, e):
        e.widget['background'] = '#016612'
        e.widget['foreground'] = 'white'

    
    
if __name__ == "__main__":
    window = Tk()
    # Creating a list of objects that hold all product objects
    pizzas = Helper("./dataPizza.xlsx").get_list_of_product()
    app = App(window, radio_var, pizzas)

    window.mainloop()
