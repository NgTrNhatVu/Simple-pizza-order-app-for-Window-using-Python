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

        # Hiển thị chi tiết sản phẩm
        Label(self.order_frame,
              text=self.pro_name,
              font=('default', 12, "bold"),
              fg='#ca3435',
              anchor="w",
              width=50).grid(
            row=1, columnspan=4, pady=5)

        Label(self.order_frame,
              text="Kích cỡ:",
              font=('default', 10, "bold"),
              width=20,
              anchor='c').grid(
                  row=2, column=0, pady=5)
        size = StringVar(value=self.pro_size)
        size_opt = OptionMenu(self.order_frame, size, "s", "m", "l")
        size_opt.grid(row=2, column=1, padx=2, ipadx=2, ipady=2)

        Label(self.order_frame,
              text="Số lượng:",
              font=('default', 10, "bold"),justify="left").grid(
                  row=2, column=2)
        quantity = Entry(self.order_frame, width=5)
        quantity.insert(0, '1')
        quantity.grid(row=2, column=3)
        if self.isNumber(quantity.get()) == False:
            quantity.insert(0, "Vui lòng chọn số lượng")

        # trả về frame chứa thông tin sản phẩm và form lấy thông tin khách hàng
        return self.order_frame

    def isNumber(self, input):
        try:
            int(input)
            return True
        except:
            return False
