from tkinter import *

from PIL import Image, ImageTk


class ClientInfo:

    def create_form(self, contain_frame):
        self.frame = Frame(contain_frame)
        # Lấy thông tin giao hàng
        Label(self.frame,
              text="Thông tin giao hàng",
              font=("default", 12, "bold"),
              anchor="w",
              width=50,).grid(
                  row=0, columnspan=2, pady=5)

        Label(self.frame,
              text="Tên khách hàng:",
              font=('default', 10, "bold"),
              anchor='w',
              justify="left",
              width=15).grid(
            row=1, column=0)
        customer_name = Entry(self.frame, width=40)
        customer_name.grid(row=1, column=1, pady=5, columnspan=3)

        Label(self.frame,
              text="Số điện thoại:",
              font=('default', 10, "bold"),
              anchor='w',
              width=15).grid(
            row=2, column=0)
        customer_phone = Entry(self.frame, width=40)
        customer_phone.grid(row=2, column=1, padx=5, pady=5, columnspan=3)
        if self.isNumber(customer_phone.get()) == False:
            customer_phone.insert(0, "Vui lòng nhập số điện thoại hợp lệ")

        Label(self.frame,
              text="Địa chỉ:",
              font=('default', 10, "bold"),
              anchor='w',
              width=15).grid(
            row=3, column=0)
        customer_address = Entry(self.frame, width=40)
        customer_address.grid(row=3, column=1, padx=5,
                              pady=5, ipady=30, columnspan=3)

        return self.frame

    def buying(self, customer_name, customer_phone, customer_address):
        print(customer_name)
        print(customer_phone)
        print(customer_address)

    def isNumber(self, input):
        try:
            int(input)
            return True
        except:
            return False
