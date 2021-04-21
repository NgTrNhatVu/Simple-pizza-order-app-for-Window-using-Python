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
        for pro_index in range (1, len(self.__pro_list["pro_id"])):
            #Product name
            name_label = Label(self.__main_frame,
                               text=self.__pro_list['pro_name'][pro_index],
                               font=('default', 10, 'bold'))
            name_label.grid(row = pro_index, column=0, pady=3)
            #Product's size
            size_label = Label(self.__main_frame, text=f"Size: {self.__pro_list['pro_size'][pro_index]}")
            size_label.grid(row=pro_index, column=1, pady=3)
             #Product's quantity
            quantity_label = Label(self.__main_frame, text=f"SL: {self.__pro_list['pro_quantity'][pro_index]}")
            quantity_label.grid(row=pro_index, column=2, pady=3)
            #Product's price
            size_label = Label(self.__main_frame, 
                               text=f"{'{:,}'.format(self.__total_price_list[pro_index]).replace(',', '.')} VNĐ",
                               fg = "#1B8366")
            size_label.grid(row=pro_index, column=3, pady=3)
        
        #Total price
        total_price = 0
        for price in self.__total_price_list:
            total_price += price
        pro_index += 1
        Label(self.__main_frame, 
              text=f"Thành tiền: {'{:,}'.format(total_price).replace(',', '.')} VNĐ",
              font=('default', 10, 'bold'),
              fg = "#1B8366").grid(
            row=pro_index, column=0, columnspan=4, pady=3)    
        
        #BILL information
        pro_index += 1
        Label(self.__main_frame,
              text="Thông tin giao hàng", font=('default', 12, 'bold'), fg='#ca3435').grid(
            row=pro_index, column=0, columnspan=4, pady=3)
              
        pro_index += 1
        customer_name_label = Label(self.__main_frame, text=f"Tên khách hàng: {self.__customer_info['name']}")
        customer_name_label.grid(row=pro_index, column=0, columnspan=4, pady=3)
        
        pro_index += 1
        customer_phone_label = Label(self.__main_frame, text=f"Số điện thoại: {self.__customer_info['phone']}")
        customer_phone_label.grid(row=pro_index, column=0, columnspan=4, pady=3)
        
        pro_index += 1
        customer_address_label = Label(self.__main_frame, text=f"Địa chỉ giao hàng: {self.__customer_info['address']}")
        customer_address_label.grid(row=pro_index, column=0, columnspan=4, pady=3)
        
        return self.__main_frame