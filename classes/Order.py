from functools import partial
from tkinter import *

from PIL import Image, ImageTk

from Helper import Helper
import tkinter.messagebox


class Order:
    def __init__(self):
        self.__pro_list = {
            "pro_id": [], 
            "pro_name": [], 
            "pro_size": [], 
            "pro_quantity": [], 
            "pro_status": []
        }

    def get_pro_list(self):
        return self.__pro_list
    
    def get_price_list(self):
        return self.__total_price_list
    
    def add_product(self, pro_id, pro_size):
        # If the product and size is ALREADY IN dictionary then + 1 its quantity
        isExist = False
        for index in range (len(self.__pro_list["pro_id"])):
            if(pro_id == self.__pro_list["pro_id"][index] and pro_size == self.__pro_list["pro_size"][index]):
                self.__pro_list["pro_quantity"][i] += 1
                isExist = True
                
        # If the product has NOT been in the cart then add it in dictionary
        if isExist == False:
            #Adding id and size to pro_list
            self.__pro_list["pro_id"].append(pro_id)
            self.__pro_list["pro_size"].append(pro_size)

            pizzas = Helper("./dataPizza.xlsx").get_list_of_product()
            for pizza in pizzas:
                if pro_id == pizza.get_pro_id():
                    # Checking in Excel file to get pizza's name and status
                    self.__pro_list["pro_name"].append(pizza.get_name())
                    self.__pro_list["pro_status"].append(pizza.get_status())
                    # and set quantity = 1
                    self.__pro_list["pro_quantity"].append(1)

    def pro_info(self, bigger_frame):
        # Making a new frame for a single product in cart
        self.__order_frame = Frame(bigger_frame)
        
        #StringVar list used for quantity Entries
        self.__quantity_string_var_list = []
        #List used for storing price's Label on top right corner of each product
        self.__price_label_list = []
        #List used for storing price from every product's section in cart
        self.__total_price_list = []
        
        #Adding StringVar variable for __quantity_string_var_list list
        for i in range (len(self.__pro_list["pro_id"])):
            sv = StringVar()
            self.__quantity_string_var_list.append(sv)
        Label(self.__order_frame, 
                  text = "Dumb Pizza - Giỏ hàng", 
                  font = ('default', 14, "bold"), 
                  fg = '#ca3435').grid(
                      row = 0, columnspan = 3, pady = 3)
        #  Displaying ONE row of the product's buying information
        for index in range(len(self.__pro_list["pro_id"])):
            # ======== NAME
            Label(self.__order_frame, 
                  text = self.__pro_list["pro_name"][index], 
                  font = ('default', 10, "bold"), 
                  fg = '#ca3435', 
                  anchor = "w", 
                  width = 50).grid(
                row = index + index + 1, columnspan = 3, pady = 3)
                  
             # ===== PRICE PER PRODUCT'S SECTION
            #product_price = unit price * quantity
            product_price = self.__unit_price(
                self.__pro_list["pro_id"][index], self.__pro_list["pro_size"][index])
            product_price *= int(self.__pro_list["pro_quantity"][index])
            #Displaying and formatting product_price
            price_label = Label(self.__order_frame, 
                  font = ('default', 10, "bold"), 
                  fg = "#084f09", 
                  text = f"{'{:,}'.format(product_price).replace(',', '.')} VNĐ")
            price_label.grid(row = index + index + 1, column = 4)
            self.__price_label_list.append(price_label)
            self.__total_price_list.append(product_price)
            
            # ======== SIZE
            Label(self.__order_frame,
                  text = "Kích cỡ:",
                  font = ('default', 8, "bold"),
                  width = 20).grid(
                row = index + index + 2, column = 0)
            size = StringVar(value = self.__pro_list["pro_size"][index])
            # Choose size, callback __update_size function when user change to other sizes
            size_opt = OptionMenu(
                self.__order_frame, size, "s", "m", "l", command = partial(self.__update_size, index))
            size_opt.grid(row = index + index + 2, column = 1, padx = 2, ipadx = 2, ipady = 2)

            # ====== QUANTITY
            Label(self.__order_frame, 
                  text = "Số lượng:", 
                  font = ('default', 8, "bold"), justify = "left").grid(
                row = index + index + 2, column = 2)
            quantity = Entry(self.__order_frame, width = 5, textvariable = self.__quantity_string_var_list[index])
            quantity.insert(0, self.__pro_list["pro_quantity"][index])
            quantity.grid(row = index + index + 2, column = 3)
            #If user changes the quantity, callback __update_quantity
            self.__quantity_string_var_list[index].trace("w", lambda name, index, mode, sv = self.__quantity_string_var_list[index]: self.__update_quantity(sv))


            
        #Calculate every price in cart
        total_price = 0
        for price in self.__total_price_list:
            total_price += int(price)
        #===== TOTAL PRICE
        self.total_price_label = Label(self.__order_frame, 
                  font = ('default', 12, "bold"), 
                  fg = "#084f09",
                    text=f"Thành tiền: {'{:,}'.format(total_price).replace(',', '.')} VNĐ"
            )
        #Display total price at the end of the cart
        self.total_price_label.grid(row=len(self.__pro_list["pro_id"])*2 + 1, column=0, columnspan=4, pady=5)
        
        return self.__order_frame

    def __unit_price(self, pro_id, pro_size):  # Calculate unit price of a product
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

    def __update_size(self, index, selection):
        
        try:
            self.__pro_list["pro_size"][int(index)] = selection
            #Call update price function
            self.__update_price(int(index))
        except:
            print("Could not update size")

    def __update_quantity(self, sv):
        try:
            if sv.get() == '':
                self.__pro_list["pro_quantity"][self.__quantity_string_var_list.index(sv)] = 0
            else:
                self.__pro_list["pro_quantity"][self.__quantity_string_var_list.index(sv)] = int(sv.get())
            #Call update price function
        except:
            tkinter.messagebox.showwarning("Dumb Pizza", "Số lượng sản phẩm không hợp lệ")
            sv.set(0)
            self.__pro_list["pro_quantity"][self.__quantity_string_var_list.index(sv)] = 0
        self.__update_price(self.__quantity_string_var_list.index(sv))

    def __update_price(self, index):
        try:
            #Update price on top of every product in cart
            product_price = self.__unit_price(
                    self.__pro_list["pro_id"][index], self.__pro_list["pro_size"][index])
            product_price *= int(self.__pro_list["pro_quantity"][index])
            self.__price_label_list[int(index)].configure(text=f"{'{:,}'.format(product_price).replace(',', '.')} VNĐ")
            
            #Update price list for calculate total price
            self.__total_price_list[index] = product_price
            #Re-calculate total price and update total price's label
            total_price = 0
            for i in self.__total_price_list:
                total_price += i
            self.total_price_label.configure(text=f"Thành tiền: {'{:,}'.format(total_price).replace(',', '.')} VNĐ")
        except:
            print("Could not calculate money")