from tkinter import *

from PIL import Image, ImageTk

class Order:
    def __init__(self, window, pro_id, pro_name, pro_type, pro_size, pro_status):
        self.window = window
        self.pro_id = pro_id
        self.pro_name = pro_name
        self.pro_size = pro_size
        self.pro_status = pro_status
        
    def cart(self, window, bigger_frame):
        window.title("Dumb Pizza - Đặt hàng")
        # Tạo một frame mới hiển thị chi tiết đơn hàng
        self.order_frame = Frame(bigger_frame)
        
        return self.pro_detail()
       
    
    def pro_detail(self):
        # Hiển thị chi tiết sản phẩm
        Label(self.order_frame, text = self.pro_name, font=('default', 18, "bold"), fg = '#ca3435', anchor="e").grid(
            row=1, columnspan=4)
        
        Label(self.order_frame, text="Kích cỡ:", font=('default', 10, "bold"), width = 10).grid(row=2, column=0, padx=10, pady=5)
        size = StringVar(value= self.pro_size)
        size_opt = OptionMenu(self.order_frame, size, "s", "m", "l")
        size_opt.grid(row=2, column=1)
        
        Label(self.order_frame, text="Số lượng:", font=('default', 10, "bold")).grid(row=3, column=0)
        quantity = Entry(self.order_frame, width=5)
        quantity.insert(0, '1')
        quantity.grid(row=3, column=1)
        if self.isNumber(quantity.get()) == False:
            quantity.insert(0, "Vui lòng chọn số lượng")
        
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
        
        #trả về frame chứa thông tin sản phẩm và form lấy thông tin khách hàng
        return self.order_frame
    
    def isNumber(self, input):
        try:
            int(input)
            return True
        except:
            return False