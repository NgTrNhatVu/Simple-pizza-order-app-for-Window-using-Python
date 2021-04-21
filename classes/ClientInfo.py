from tkinter import *
import tkinter.messagebox

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
              anchor='nw',
              width=15, height=7).grid(
            row=3, column=0)
        self.__customer_address = Text(self.frame, width=30, height=5)
        self.__customer_address.grid(row=3, column=1, padx=5,
                              pady=5, ipady=5, columnspan=3)
        
        return self.frame
    
    def set_info(self):
        
        #Check if any infomation is missing, 
        # Address input uses Text widget that auto add \n at the end of it, so we check by its length from start to upmost end charater
        if self.__customer_name.get() == '' or self.__customer_phone.get() == '' or len(self.__customer_address.get("1.0", "end-1c")) == 0:
            tkinter.messagebox.showwarning("Dumb Pizza", "Xin vui lòng điền đủ thông tin nhận hàng")
            return False
        
        #Add infomation into _customer_info dictionary
        self.__customer_info["name"] = self.__customer_name.get()
        #Validate phone only include numbers
        try:
            temp = int(self.__customer_phone.get())
            self.__customer_info["phone"] = self.__customer_phone.get()
        except:
            tkinter.messagebox.showwarning("Dumb Pizza", "Số điện thoại không hợp lệ")
            return False
        
        self.__customer_info["address"] = self.__customer_address.get("1.0", "end")
        
        return True
