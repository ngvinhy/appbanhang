import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import sqlite3


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("CỬA HÀNG VUI VẺ")
        self.master.geometry("800x600")

        # Kết nối tới cơ sở dữ liệu
        self.conn = sqlite3.connect('products.db')

        # Lấy danh sách sản phẩm và giá cả từ cơ sở dữ liệu
        self.product_list = {}
        cursor = self.conn.execute("SELECT Name, Price FROM products")
        for row in cursor:
            self.product_list[row[0]] = row[1]

        # Tạo Combobox để chọn sản phẩm
        self.products_label = ttk.Label(self.master, text="Sản phẩm:")
        self.products_label.pack(pady=10)

        self.products = ttk.Combobox(self.master, values=list(self.product_list.keys()), state='readonly')
        self.products.pack()

        # Tạo Entry để nhập số lượng sản phẩm
        self.quantity_label = ttk.Label(self.master, text="Số lượng:")
        self.quantity_label.pack(pady=10)

        self.quantity = ttk.Entry(self.master)
        self.quantity.pack()

        # Tạo nút Thêm vào giỏ hàng
        self.add_to_cart_button = ttk.Button(self.master, text="Thêm vào giỏ hàng", command=self.add_to_cart)
        self.add_to_cart_button.pack(pady=10)

        # Hiển thị giỏ hàng và tổng số tiền
        self.cart_label = ttk.Label(self.master, text="Giỏ hàng:", font=("Arial", 14, "bold"))
        self.cart_label.pack(pady=10)

        self.cart_listbox = tk.Listbox(self.master, height=10, width=50, font=("Arial", 12))
        self.cart_listbox.pack()

        self.total_label = ttk.Label(self.master, text="Tổng số tiền: 0", font=("Arial", 14, "bold"))
        self.total_label.pack(pady=10)

        # Tạo nút Thanh toán
        self.pay_button = ttk.Button(self.master, text="Thanh toán", command=self.pay)
        self.pay_button.pack(pady=10)

    def add_to_cart(self):
        product = self.products.get()
        price = self.product_list[product]
        quantity = int(self.quantity.get())

        total = price * quantity

        self.cart_listbox.insert(tk.END, f"{product} ({quantity}): {total}")
        self.total_label.config(text=f"Tổng số tiền: {self.calculate_total()}")

    def calculate_total(self):
        total = 0
        for item in self.cart_listbox.get(0, tk.END):
            total += float(item.split(": ")[1])
        return total

    def pay(self):
        receipt = f"{'-'*30}\n{'BIÊN LAI THANH TOÁN':^30}\n{'-'*30}\n"
        for item in self.cart_listbox.get(0, tk.END):
            receipt += item + "\n"
        receipt += f"{'-'*30}\n{'Ngày: '}{datetime.now():%d-%m-%Y %H:%M:%S}"

        messagebox.showinfo("Thông tin thanh toán", receipt)

        # In biên lai thanh toán
        self.print_receipt(receipt)

    def print_receipt(self, receipt):
        # code in biên lai thanh toán
        pass


root = tk.Tk()
app = App(root)
root.mainloop()
