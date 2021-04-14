from functools import partial
from tkinter import *

from PIL import Image, ImageTk

from Helper import Helper


class Order:
    def __init__(self):
        self.pro_list = {
            "pro_id": [],
            "pro_name": [],
            "pro_size": [],
            "pro_quantity": [],
            "pro_status": []
        }
        self.size_list = []
        self.quantity_list = []

    def add_product(self, pro_id, pro_size):
        # If the product has not been in the cart then add it in dictionary
        # and set quantity = 1
        if not pro_id in self.pro_list["pro_id"]:
            self.pro_list["pro_id"].append(pro_id)
            self.pro_list["pro_size"].append(pro_size)

            pizzas = Helper("./dataPizza.xlsx").get_list_of_product()
            for pizza in pizzas:
                if pro_id == pizza.get_pro_id():
                    self.pro_list["pro_name"].append(pizza.get_name())
                    self.pro_list["pro_status"].append(pizza.get_status())
                    self.pro_list["pro_quantity"].append(1)
        # If the product is already in dictionary then + 1 its quantity
        else:
            for i in range(len(self.pro_list["pro_id"])):
                if pro_id == self.pro_list["pro_id"][i]:
                    self.pro_list["pro_quantity"][i] += 1

    def update_size(self, index, selection):
        self.pro_list["pro_size"][int(index)] = selection

    def update_quantity(self, sv):
        try:
            self.pro_list["pro_quantity"][self.textvariables.index(sv)] = sv.get()
        except:
            print("So luong khong hop le")


    def pro_info(self, bigger_frame):
        # Making a new frame for a single product in cart
        self.order_frame = Frame(bigger_frame)
        
        self.textvariables = []
        for index in range (len(self.pro_list["pro_id"])):
            sv = StringVar()
            self.textvariables.append(sv)

        for index in range(len(self.pro_list["pro_id"])):
            #  Displaying the product's buying information
            # Name
            Label(self.order_frame,
                  text=self.pro_list["pro_name"][index],
                  font=('default', 10, "bold"),
                  fg='#ca3435',
                  anchor="w",
                  width=50).grid(
                row=index*2, columnspan=3, pady=3)

            # Size
            Label(self.order_frame,
                  text="Kích cỡ:",
                  font=('default', 8, "bold"),
                  width=20).grid(
                row=index*2+1, column=0)
            size = StringVar(value=self.pro_list["pro_size"][index])
            size_opt = OptionMenu(
                self.order_frame, size, "s", "m", "l", command=partial(self.update_size, index))
            size_opt.grid(row=index*2+1, column=1, padx=2, ipadx=2, ipady=2)

            # Quantity
            Label(self.order_frame,
                  text="Số lượng:",
                  font=('default', 8, "bold"), justify="left").grid(
                row=index*2+1, column=2)
            quantity = Entry(self.order_frame, width=5, textvariable=self.textvariables[index])
            quantity.insert(0, self.pro_list["pro_quantity"][index])
            quantity.grid(row=index*2+1, column=3)
            if self.isNumber(quantity.get()) == True:
                print(self.textvariables[index])
                self.textvariables[index].trace_add("write", self.update_quantity(self.textvariables[index]))
            else:
                quantity.insert(0, "Vui lòng chọn số lượng")

            # Price (gọi hàm unit_price())
            self.product_price = self.unit_price(
                self.pro_list["pro_id"][index], self.pro_list["pro_size"][index])
            self.product_price *= int(self.pro_list["pro_quantity"][index])
            Label(self.order_frame,
                  font=('default', 10, "bold"),
                  fg="#1B8366",
                  text=f"{'{:,}'.format(self.product_price).replace(',', '.')} VNĐ").grid(row=index*2, column=4)

        return self.order_frame

    def unit_price(self, pro_id, pro_size):  # Calculate unit price of a product
        pizzas = Helper("./dataPizza.xlsx").get_list_of_product()
        size_price = 0
        for pizza in pizzas:
            if pro_id == pizza.get_pro_id():
                if pro_size == "s":
                    size_price = pizza.get_s()
                if pro_size == "m":
                    size_price = pizza.get_m()
                if pro_size == "l":
                    size_price = pizza.get_l()
        return size_price

    def isNumber(self, input):
        try:
            int(input)
            return True
        except:
            return False
