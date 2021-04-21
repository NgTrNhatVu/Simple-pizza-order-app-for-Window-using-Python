from tkinter import *


class ClientInfo:

    def __init__(self):
        self.__customer_info = {
            "name": "A", 
            "phone": "", 
            "address": ""
        }
    
    def get_info(self):
        return self.__customer_info
    
    def create_form(self, contain_frame):
        self.frame = Frame(contain_frame)
        # GET Customer information
        
        #NAME
        Label(self.frame,
              text="Thông tin giao hàng",
              font=("default", 10, "bold"),
              anchor="w",
              width=50,).grid(
                  row=0, columnspan=3, pady=5)

        Label(self.frame,
              text="Tên khách hàng:",
              font=('default', 8, "bold"),
              anchor='w',
              justify="left",
              width=15).grid(
            row=1, column=0)
        self.__customer_name = Entry(self.frame, width=40)
        self.__customer_name.grid(row=1, column=1, pady=5, columnspan=3)
        
        #PHONE NUMBER
        Label(self.frame,
              text="Số điện thoại:",
              font=('default', 8, "bold"),
              anchor='w',
              width=15).grid(
            row=2, column=0)
        self.__customer_phone = Entry(self.frame, width=40)
        self.__customer_phone.grid(row=2, column=1, padx=5, pady=5, columnspan=3)
        #customer_phone.bind("<FocusOut>", self.validate_phone(customer_phone))

        #ADDRESS
        Label(self.frame,
              text="Địa chỉ:",
              font=('default', 8, "bold"),
              anchor='w',
              width=15).grid(
            row=3, column=0)
        self.__customer_address = Entry(self.frame, width=40)
        self.__customer_address.grid(row=3, column=1, padx=5,
                              pady=5, ipady=30, columnspan=3)
        
        return self.frame
    
    def set_info(self):
        self.__customer_info["name"] = self.__customer_name.get()
        self.__customer_info["phone"] = self.__customer_phone.get()
        self.__customer_info["address"] = self.__customer_address.get()
    
    def validate_phone(self, phone_entry):
        try:
            self.__customer_info["phone"] = int(phone_entry.get())
            
        except:
            phone_entry.delete(0, END)
            phone_entry.insert(0, "Số điện thoại không hợp lệ")
