from tkinter import *

class Bill:
    __pro_list = {
        "pro_id": [], 
        "pro_name": [], 
        "pro_size": [], 
        "pro_quantity": [], 
        "pro_status": []
    }
    __customer_info = {
        "name": "", 
        "phone": "", 
        "address": ""
    }
    __total_price_list = []
    
    def __init__(self, pro_list, customer_info, total_price_list):
        self.__pro_list = pro_list
        self.__customer_info = customer_info
        self.__total_price_list = total_price_list
    
    def create_bill(self, contain_frame):
        #Creating a new Frame to hold Bill's information
        self.__main_frame = Frame(contain_frame)
        
        Label(self.__main_frame,
              text="Đơn hàng", font=('default', 12, 'bold'), fg='#ca3435').grid(
            row=0, column=0, columnspan=4, pady=3)
        
        #Display product infomation:
        for pro_index in range (0, len(self.__pro_list["pro_id"])):
            if int(self.__pro_list['pro_quantity'][pro_index]) > 0:
                #Product name
                name_label = Label(self.__main_frame,
                                text=self.__pro_list['pro_name'][pro_index],
                                font=('default', 10, 'bold'),
                                anchor="w", width = 40)
                name_label.grid(row = pro_index+1, column=0, padx=3, pady=3)
                #Product's size
                size_label = Label(self.__main_frame, text=f"Size: {self.__pro_list['pro_size'][pro_index].upper()}")
                size_label.grid(row=pro_index+1, column=1, padx=3, pady=3)
                #Product's quantity
                quantity_label = Label(self.__main_frame, text=f"SL: {self.__pro_list['pro_quantity'][pro_index]}")
                quantity_label.grid(row=pro_index+1, column=2, padx=3, pady=3)
                #Product's price
                size_label = Label(self.__main_frame, 
                                text=f"{'{:,}'.format(self.__total_price_list[pro_index]).replace(',', '.')} VNĐ",
                                fg = "#084f09")
                size_label.grid(row=pro_index+1, column=3, padx=3, pady=3)
        pro_index += 1
        
        #Total price
        total_price = 0
        for price in self.__total_price_list:
            total_price += price
        pro_index += 1
        Label(self.__main_frame, 
              text=f"Thành tiền: {'{:,}'.format(total_price).replace(',', '.')} VNĐ",
              font=('default', 10, 'bold'),
              fg = "#084f09").grid(
            row=pro_index, column=0, columnspan=4, pady=3)    
        
        #Customer information
        pro_index += 1
        Label(self.__main_frame,
              text="Thông tin giao hàng", font=('default', 12, 'bold'), fg='#ca3435').grid(
            row=pro_index, column=0, columnspan=4, pady=3)
              
        pro_index += 1
        customer_name_label = Label(self.__main_frame, text=f"Tên khách hàng: {self.__customer_info['name']}", wraplength=300)
        customer_name_label.grid(row=pro_index, column=0, columnspan=4, pady=3)
        
        pro_index += 1
        customer_phone_label = Label(self.__main_frame, text=f"Số điện thoại: {self.__customer_info['phone']}", wraplength=300)
        customer_phone_label.grid(row=pro_index, column=0, columnspan=4, pady=3)
        
        pro_index += 1
        customer_address_label = Label(self.__main_frame, text=f"Địa chỉ giao hàng: {self.__customer_info['address']}", wraplength=300)
        customer_address_label.grid(row=pro_index, column=0, columnspan=4, pady=3)
        
        return self.__main_frame