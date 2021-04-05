from tkinter import *
class Info_form:
    def __init__(self):
        # Lấy thông tin khách hàng
        Label(self.order_frame, text="Tên khách hàng:",font=('default', 10, "bold")).grid(row=5, column=0)
        customer_name = Entry(self.order_frame, width=40)
        customer_name.grid(row=5, column=1, padx=10, pady=5)
        
        Label(self.order_frame, text="Số điện thoại:", font=('default', 10, "bold")).grid(row=6, column=0)
        customer_phone = Entry(self.order_frame, width=40)
        customer_phone.grid(row=6, column=1, padx=10, pady=5)
        if self.isNumber(customer_phone.get()) == False:
            customer_phone.insert(0, "Vui lòng nhập số điện thoại hợp lệ")
        
        Label(self.order_frame, text="Địa chỉ:", font=('default', 10, "bold")).grid(row=7, column=0)
        customer_address = Entry(self.order_frame, width=40)
        customer_address.grid(row=7, column=1, padx=10, pady=5)