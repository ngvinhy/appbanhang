import csv
from datetime import *
from tkinter.font import BOLD
from xulyanh import *
from tkinter import *
import os
import tkinter as tk
from tkinter import messagebox
from collections import Counter


class MainAccountScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("850x690")
        self.root.title("TECH HUB SHOP")
        self.root.resizable(width=False, height=False)

        tk.Label(text="Select Your Choice", fg="white", bg="#252d35", width="300", height="1",
                 font=("Comic Sans MS", 13, "bold")).pack()

        login_frame = tk.LabelFrame(self.root, bd=2, relief="groove")
        login_frame.pack()

        image_cover = xuly_image("https://ik.imagekit.io/nhom2/Cover.png?updatedAt=1682768752412", 850, 650)
        img1 = tk.Label(login_frame, image=image_cover)
        img1.pack(side="top", fill=tk.BOTH)

        tk.Button(login_frame, text="Login", height="2", width="15", command=self.login,
                  font=("Comic Sans MS", 10, "bold")).place(x=360, y=265)

        tk.Button(login_frame, text="Register", height="2", width="15", command=self.register,
                  font=("Comic Sans MS", 10, "bold")).place(x=360, y=320)

        tk.Button(login_frame, text="Admin", height="1", width="7", command=self.admin,
                  font=("Comic Sans MS", 10, "bold")).place(x=775, y=10)

        self.root.mainloop()

    def register(self):
        self.register_screen = Toplevel(self.root)
        self.register_screen.title("Register")
        self.register_screen.geometry("300x250")
        self.register_screen.resizable(width=False, height=False)
        self.username = StringVar()
        self.password = StringVar()
        Label(self.register_screen, text="Please enter details below").pack()
        Label(self.register_screen, text="").pack()
        username_lable = Label(self.register_screen, text="Username")
        username_lable.pack()
        username_entry = Entry(self.register_screen, textvariable=self.username)
        username_entry.pack()
        password_lable = Label(self.register_screen, text="Password")
        password_lable.pack()
        password_entry = Entry(self.register_screen, textvariable=self.password, show='*')
        password_entry.pack()
        Label(self.register_screen, text="").pack()
        Button(self.register_screen, text="Register", width=10, height=1, command=self.register_user).pack()

    def login(self):
        self.login_screen = Toplevel(self.root)
        self.login_screen.title("Login")
        self.login_screen.geometry("300x250")
        self.login_screen.resizable(width=False, height=False)
        Label(self.login_screen, text="Please enter details below to login").pack()
        Label(self.login_screen, text="").pack()

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(self.login_screen, text="Username").pack()
        self.username_login_entry = Entry(self.login_screen, textvariable=self.username_verify)
        self.username_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Password").pack()
        self.password_login_entry = Entry(self.login_screen, textvariable=self.password_verify, show='*')
        self.password_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Button(self.login_screen, text="Login", width=10, height=1, command=self.login_verify).pack()

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()

        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        messagebox.showinfo("Account", "Registration Success")
        self.register_screen.destroy()

    def login_verify(self):
        username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_screen.destroy()
                messagebox.showinfo("Account", "Login Success")
                self.root.destroy()
                main()
            else:
                self.password_not_recognised()
        else:
            self.user_not_found()

    def password_not_recognised(self):
        password_not_recog_screen = Toplevel(self.login_screen)
        password_not_recog_screen.title("Account")
        password_not_recog_screen.geometry("150x100")
        password_not_recog_screen.resizable(width=False, height=False)
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        Button(password_not_recog_screen, text="OK", command=password_not_recog_screen.destroy).pack()

    def user_not_found(self):
        user_not_found_screen = Toplevel(self.login_screen)
        user_not_found_screen.title("Account")
        user_not_found_screen.geometry("150x100")
        user_not_found_screen.resizable(width=False, height=False)
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=user_not_found_screen.destroy).pack()

    def admin(self):
        self.root.destroy()
        Admin()


class Product:
    def __init__(self, code, name, price, image, description, type):
        self.name = name
        self.price = price
        self.image = image
        self.description = description
        self.type = type
        self.code = code

    @classmethod
    def get_data(cls):
        with open("Products.csv", "r", newline="", encoding="UTF-8") as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data

    def append_data(self):
        with open("Products.csv", "a", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.price, self.image, self.description, self.type, self.code])


class Mainmenu(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.products_frame = LabelFrame(self.master, bd=3, relief="raised", text="PRODUCTS",
                                         font=("Comic Sans MS", 16, BOLD), fg="white", bg="#252d35", labelanchor=N)
        self.button_frame = LabelFrame(self.master, bd=3, relief="raised", text="CATEGORY",
                                       font=("Comic Sans MS", 16, BOLD), fg="white", bg="#252d35", labelanchor=N)
        self.heading = LabelFrame(self.master, bd=3, relief="raised", bg="#080a0d")
        self.image_logo = xuly_image("https://ik.imagekit.io/nhom2/Logo.png?updatedAt=1682769745947", 100, 40)
        self.lf = []
        self.button_add = []
        self.lf1 = []
        self.image_products = []
        self.pack()
        self.master.geometry("1180x740")
        self.master.title("TECH HUB SHOP")
        self.master.resizable(width=False, height=False)
        self.products = Product.get_data()
        self.cart_list = []
        self.create_widgets()

    def create_widgets(self):
        self.heading.place(x=0, y=0, width=1180, height=60)

        Label(self.heading, image=self.image_logo).grid(row=0, column=0, padx=10, pady=5)

        Label(self.heading, text="Empowering Your Tech Lifestyle", font=("Comic Sans MS", 16, BOLD), fg="white",
              bg="#080a0d").grid(row=0, column=2, padx=285, pady=5)

        Button(self.heading, text="Shopping Cart", font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=SOLID, activebackground="#252d35", activeforeground="#F6F5EC",
               command=self.show_cart).grid(row=0, column=3, padx=10, pady=5)

        self.button_frame.place(x=0, y=60, width=130, height=680)
        self.products_frame.place(x=130, y=60, width=1050, height=680)

        Button(self.button_frame, text="Laptop", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Laptop")).grid(row=0, column=0, padx=10)

        Button(self.button_frame, text="PC", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("PC")).grid(row=1, column=0, padx=10)

        Button(self.button_frame, text="Apple", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Apple")).grid(row=2, column=0, padx=10)

        Button(self.button_frame, text="Screen", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Screen")).grid(row=3, column=0, padx=10)

        Button(self.button_frame, text="Keyboard", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Keyboard")).grid(row=4, column=0, padx=10)

        Button(self.button_frame, text="Mouse", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Mouse")).grid(row=5, column=0, padx=10)

        Button(self.button_frame, text="Headphones", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Headphones")).grid(row=6, column=0, padx=10)

        Button(self.button_frame, text="Accessories", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Accessories")).grid(row=7, column=0, padx=10)

        Button(self.button_frame, text="Others", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Others")).grid(row=8, column=0, padx=10)

    def buy_product(self, product):
        self.cart_list.append(product)

    def HideAllFrame(self):
        for widget in self.products_frame.winfo_children():
            widget.destroy()

    def ShowFrames(self, phanloai):
        self.HideAllFrame()

        # Tạo khung Canvas để chứa các sản phẩm
        canvas = Canvas(self.products_frame, bg="#252d35")
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Tạo thanh cuộn dọc
        scrollbar = Scrollbar(self.products_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Thiết lập khung Canvas để sử dụng thanh cuộn
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Tạo khung con trong Canvas để chứa sản phẩm
        frame = Frame(canvas, bg="#252d35")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        self.image_products = []
        self.button_add = []  # Khởi tạo danh sách mới cho button_add
        count = 0
        for product in self.products:
            if product[1] == phanloai:
                lf = LabelFrame(frame, bd=2, relief="solid", fg="white", bg="#252d35", text=product[3],
                                font=("Comic Sans MS", 12, "bold"), labelanchor=N)
                lf.grid(row=count // 3, column=count % 3, padx=10, pady=10)

                self.image_products.append(xuly_image(product[5], 120, 100))
                label_image = Label(lf, image=self.image_products[count])
                label_image.grid(row=2, column=0, padx=85, pady=5)

                Label(lf, text=product[2], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=1, column=0, padx=85, pady=5)
                Label(lf, text=product[4], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=3, column=0, padx=85, pady=5)

                button_add = Button(lf, command=lambda p=product: self.buy_product(p), text="Add to Cart",
                                    font=("Comic Sans MS", 12, "bold"), fg="white", bg="green", relief=SOLID,
                                    activebackground="green", activeforeground="white")
                button_add.grid(row=4, column=0, padx=85, pady=5)
                self.button_add.append(button_add)
                count += 1
            else:
                continue

        # Cập nhật thanh cuộn khi có thay đổi
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def show_cart(self):
        self.HideAllFrame()

        # Tạo frame chứa sản phẩm
        products_frame = Frame(self.products_frame, bg="#252d35")
        products_frame.pack(side=TOP, fill=BOTH, expand=True)

        # Tạo frame chứa tổng và nút thanh toán
        total_frame = Frame(self.products_frame, bg="#252d35", bd=2, relief="raised")
        total_frame.pack(side=BOTTOM, fill=X)

        # Tạo khung Canvas để chứa các sản phẩm
        canvas = Canvas(products_frame, bg="#252d35")
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Tạo thanh cuộn dọc
        scrollbar = Scrollbar(products_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Thiết lập khung Canvas để sử dụng thanh cuộn
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Tạo khung con trong Canvas để chứa sản phẩm
        frame = Frame(canvas, bg="#252d35")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        self.image_products = []  # Xóa list hình ảnh sản phẩm
        self.lf1 = []  # Xóa list label frames
        count = 0  # Khởi tạo biến đếm để định vị vị trí

        for i in range(len(self.cart_list)):
            lf = LabelFrame(frame, bd=2, relief="solid", fg="white", bg="#252d35",
                            text=self.cart_list[i][3], font=("Comic Sans MS", 12, BOLD), labelanchor=N)
            lf.grid(row=count // 3, column=count % 3, padx=10, pady=5)
            self.lf1.append(lf)  # Thêm label frame vào list
            product_name = self.cart_list[i][2]
            product_image = self.cart_list[i][5]
            product_price = self.cart_list[i][4]
            self.image_products.append(xuly_image(product_image, 120, 100))
            label_image = Label(lf, image=self.image_products[count])
            label_image.grid(row=2, column=0, padx=85, pady=5)
            Label(lf, text=product_name, font=("Comic Sans MS", 12, "bold"), fg="white",
                  bg="#252d35").grid(row=1, column=0, padx=85, pady=5)
            Label(lf, text=product_price, font=("Comic Sans MS", 12, "bold"), fg="white",
                  bg="#252d35").grid(row=3, column=0, padx=85, pady=5)
            Button(lf, command=lambda idx=i: self.remove_item(idx), text="Remove",
                   font=("Comic Sans MS", 12, "bold"), fg="white", bg="red",
                   activebackground="red", activeforeground="white").grid(row=4, column=0, padx=85, pady=5)
            count += 1  # Tăng biến đếm

        # Cập nhật thanh cuộn khi có thay đổi
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        self.total_label = Label(total_frame, text="Total: 0₫", font=("Comic Sans MS", 12, BOLD), fg="#F6F5EC",
                                 bg="#252d35")
        self.total_label.pack(side=LEFT, padx=10, pady=5)
        self.total_label.config(text="Total: {:,.0f}₫".format(self.tong()).replace(".0", "").replace(",", "."))

        payment_button = Button(total_frame, text="Payment", font=("Comic Sans MS", 12, BOLD), fg="#F6F5EC",
                                bg="green", relief=SOLID, activebackground="green", activeforeground="#F6F5EC",
                                command=self.show_order)
        payment_button.pack(side=RIGHT, padx=10, pady=5)

    def remove_item(self, idx):
        if 0 <= idx < len(self.cart_list):
            self.lf1[idx].destroy()
            del self.lf1[idx]  # Xóa label frame khỏi list
            self.cart_list.pop(idx)
        self.show_cart()  # Load lại giao diện cart

    def tong(self):
        return sum([float(product[4].replace("₫", "").replace(".", "")) for product in self.cart_list])

    def show_bill(self):
        product_counts = Counter(product[0] for product in self.cart_list)
        receipt = f"{'-' * 50}\n{'PAYMENT RECEIPT':^50}\n{'Time: '}{datetime.now():%d-%m-%Y %H:%M:%S}\n{'-' * 50}"
        total_amount = 0  # Initialize the total amount variable

        unique_product_ids = set(product[0] for product in self.cart_list)  # Get unique product IDs

        row = 0
        for product_id in unique_product_ids:
            product_details = next((p for p in self.products if p[0] == product_id), None)
            if product_details:
                product_code = product_details[0]
                product_name = product_details[2] + " " + product_details[3]
                product_price = product_details[4]
                quantity = product_counts[product_id]
                total_price = float(product_price.replace("₫", "").replace(".", "")) * quantity
                total_amount += total_price  # Update the total amount
                receipt += f"\nCode: {product_code}\nProduct: {product_name}\nQuantity: {quantity}\nPrice: {product_price}\n{'-' * 20}"
                row += 1

        receipt += "\nTotal: {:,.0f}₫".format(float(total_amount)).replace(",", ".")
        messagebox.showinfo("Order Confirmed", receipt)
        self.cart_list.clear()
        self.bill_window.destroy()
        self.show_cart()

    def show_order(self):
        if len(self.cart_list) != 0:
            self.bill_window = Toplevel(self.master)
            self.bill_window.title("Order")
            # Add label for "Payment Receipt"
            receipt_label = Label(self.bill_window, text="Order Confirmation", font=("Comic Sans MS", 15, BOLD))
            receipt_label.grid(row=0, column=0, columnspan=5, padx=10, pady=5)
            # Add label for "Tech Hub"
            title_label = Label(self.bill_window, text="Products of Tech Hub Shop", font=("Comic Sans MS", 13, BOLD))
            title_label.grid(row=1, column=0, columnspan=5, padx=10, pady=3)
            # Add label for current date and time
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
            time_label = Label(self.bill_window, text=current_time, font=("Comic Sans MS", 12, BOLD))
            time_label.grid(row=2, column=0, columnspan=5, padx=10, pady=5)
            # Add dashed line separator
            line_label = Label(self.bill_window, text="-" * 80, font=("Comic Sans MS", 12, BOLD))
            line_label.grid(row=3, column=0, columnspan=5, padx=10, pady=5)
            # Create the table headers
            headers = ["Code", "Product", "Quantity", "Price", "Total"]
            for col, header in enumerate(headers):
                header_label = Label(self.bill_window, text=header, font=("Comic Sans MS", 12, BOLD))
                header_label.grid(row=4, column=col, padx=10, pady=5)
            # Create the bill details
            row = 5  # Initialize the row variable
            total_amount = 0  # Initialize the total amount variable
            # Create lists to store the labels
            code_labels = []
            name_labels = []
            quantity_labels = []
            price_labels = []
            total_labels = []
            for product in self.cart_list:
                product_id = product[0]
                product_details = next((p for p in self.products if p[0] == product_id), None)
                if product_details:
                    product_code = product_details[0]
                    product_name = product_details[2] + " " + product_details[3]
                    product_price = product_details[4]
                    # Check if the code already exists in the labels
                    existing_index = next((i for i, code in enumerate(code_labels) if code['text'] == product_code), None)

                    if existing_index is not None:
                        # If the code already exists, update the quantity and total
                        existing_quantity = int(quantity_labels[existing_index]['text'])
                        new_quantity = existing_quantity + 1
                        quantity_labels[existing_index].configure(text=str(new_quantity))
                        total_price = int(product_price.replace("₫", "").replace(".", "").strip()) * new_quantity
                        total_labels[existing_index].configure(text="{:,.0f}₫".format(float(total_price)).replace(",", "."))
                    else:
                        # If the code doesn't exist, add new labels
                        code_label = Label(self.bill_window, text=product_code, font=("Comic Sans MS", 12, BOLD))
                        code_label.grid(row=row, column=0, padx=10, pady=5)
                        code_labels.append(code_label)

                        name_label = Label(self.bill_window, text=product_name, font=("Comic Sans MS", 12, BOLD))
                        name_label.grid(row=row, column=1, padx=10, pady=5)
                        name_labels.append(name_label)

                        quantity_label = Label(self.bill_window, text="1", font=("Comic Sans MS", 12, BOLD))
                        quantity_label.grid(row=row, column=2, padx=10, pady=5)
                        quantity_labels.append(quantity_label)

                        price_label = Label(self.bill_window, text=product_price, font=("Comic Sans MS", 12, BOLD))
                        price_label.grid(row=row, column=3, padx=10, pady=5)
                        price_labels.append(price_label)
                        # Process the product price and calculate the total
                        product_price = product_price.replace("₫", "").replace(".", "").strip()
                        total_price = int(product_price) * 1
                        total_amount += total_price
                        total_label = Label(self.bill_window, text="{:,}₫".format(total_price).replace(",", "."),
                                            font=("Comic Sans MS", 12, BOLD))
                        total_label.grid(row=row, column=4, padx=10, pady=5)
                        total_labels.append(total_label)
                        row += 1  # Increment the row variable
            # Add dashed line separator
            line_label = Label(self.bill_window, text="-" * 80, font=("Comic Sans MS", 12, BOLD))
            line_label.grid(row=row, column=0, columnspan=5, padx=10, pady=5)
            # Display the total amount
            row += 1  # Increment the row variable
            total_label = Label(self.bill_window, text="Total Amount: {:,.0f}₫".format(self.tong()).replace(".0", "").replace(",", "."),
                                font=("Comic Sans MS", 12, BOLD))
            total_label.grid(row=row, column=0, columnspan=2, padx=10, pady=10)
            # Add Confirm button
            confirm_button = Button(self.bill_window, text="Confirm", font=("Comic Sans MS", 12, BOLD), relief=SOLID,
                                    activeforeground="white", activebackground="green", command=self.show_bill)
            confirm_button.grid(row=row, column=4, sticky=E, padx=80, pady=5)
            # Add Cancel button
            cancel_button = Button(self.bill_window, text="Cancel", font=("Comic Sans MS", 12, BOLD), relief=SOLID,
                                   activeforeground="white", activebackground="red", command=self.bill_window.destroy)
            cancel_button.grid(row=row, column=4, sticky=E, padx=5, pady=5)
        else:
            messagebox.showinfo("Cart", "There are no products in the cart")


class Admin:
    def __init__(self):
        self.root = Tk()
        self.products_frame = LabelFrame(self.root, bd=3, relief="raised", text="PRODUCTS",
                                         font=("Comic Sans MS", 16, BOLD), fg="white", bg="#252d35", labelanchor=N)
        self.button_frame = LabelFrame(self.root, bd=3, relief="raised", text="CATEGORY",
                                       font=("Comic Sans MS", 16, BOLD), fg="white", bg="#252d35", labelanchor=N)
        self.heading = LabelFrame(self.root, bd=3, relief="raised", bg="#080a0d")
        self.image_logo = xuly_image("https://ik.imagekit.io/nhom2/Logo.png?updatedAt=1682769745947", 100, 40)
        self.lf = []
        self.lf1 = []
        self.image_products = []
        self.root.geometry("1180x740")
        self.root.title("Products Management")
        self.root.resizable(width=False, height=False)
        self.products = Product.get_data()
        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        self.heading.place(x=0, y=0, width=1180, height=60)

        Label(self.heading, image=self.image_logo).grid(row=0, column=0, padx=10, pady=5)

        Label(self.heading, text="Products Management", font=("Comic Sans MS", 16, BOLD), fg="white",
              bg="#080a0d").grid(row=0, column=2, padx=375, pady=5)

        self.button_frame.place(x=0, y=60, width=130, height=680)
        self.products_frame.place(x=130, y=60, width=1050, height=680)

        Button(self.button_frame, text="Laptop", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Laptop")).grid(row=0, column=0, padx=10)

        Button(self.button_frame, text="PC", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("PC")).grid(row=1, column=0, padx=10)

        Button(self.button_frame, text="Apple", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Apple")).grid(row=2, column=0, padx=10)

        Button(self.button_frame, text="Screen", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Screen")).grid(row=3, column=0, padx=10)

        Button(self.button_frame, text="Keyboard", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Keyboard")).grid(row=4, column=0, padx=10)

        Button(self.button_frame, text="Mouse", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Mouse")).grid(row=5, column=0, padx=10)

        Button(self.button_frame, text="Headphones", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Headphones")).grid(row=6, column=0, padx=10)

        Button(self.button_frame, text="Accessories", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Accessories")).grid(row=7, column=0, padx=10)

        Button(self.button_frame, text="Others", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#252d35", relief=FLAT, activebackground="#252d35", activeforeground="#F6F5EC",
               command=lambda: self.ShowFrames("Others")).grid(row=8, column=0, padx=10)

    def HideAllFrame(self):
        for widget in self.products_frame.winfo_children():
            widget.destroy()

    def ShowFrames(self, phanloai):
        self.HideAllFrame()

        # Tạo khung Canvas để chứa các sản phẩm
        canvas = Canvas(self.products_frame, bg="#252d35")
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Tạo thanh cuộn dọc
        scrollbar = Scrollbar(self.products_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Thiết lập khung Canvas để sử dụng thanh cuộn
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Tạo khung con trong Canvas để chứa sản phẩm
        frame = Frame(canvas, bg="#252d35")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        self.image_products = []
        self.button_add = []  # Khởi tạo danh sách mới cho button_add
        count = 0
        for product in self.products:
            if product[1] == phanloai:
                lf = LabelFrame(frame, bd=2, relief="solid", fg="white", bg="#252d35", text=product[3],
                                font=("Comic Sans MS", 12, "bold"), labelanchor=N)
                lf.grid(row=count // 3, column=count % 3, padx=10, pady=10)

                self.image_products.append(xuly_image(product[5], 120, 100))
                label_image = Label(lf, image=self.image_products[count])
                label_image.grid(row=2, column=0, padx=85, pady=5)

                Label(lf, text=product[2], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=1, column=0, padx=85, pady=5)
                Label(lf, text=product[4], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=3, column=0, padx=85, pady=5)
                Label(lf, text="Quantity: " + product[6], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=4, column=0, padx=85, pady=5)

                button_add = Button(lf, command=lambda p=product: self.change_info(p), text="Change Info",
                                    font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35", relief=SOLID,
                                    activebackground="green", activeforeground="white")
                button_add.grid(row=5, column=0, padx=85, pady=5)
                self.button_add.append(button_add)
                count += 1
            else:
                continue

        # Cập nhật thanh cuộn khi có thay đổi
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def change_info(self, product):
        self.change_info_screen = Toplevel(self.root)
        self.change_info_screen.title("Product Information")
        self.change_info_screen.geometry("300x200")
        self.change_info_screen.resizable(width=False, height=False)
        Label(self.change_info_screen, text="ID: " + product[0], font=("Comic Sans MS", 12, "bold")).pack()
        Label(self.change_info_screen, text=product[2] + " " + product[3], font=("Comic Sans MS", 12, "bold")).pack(pady=5)

        self.info_frame = Frame(self.change_info_screen)
        self.info_frame.pack(pady=10)

        Label(self.info_frame, text="Price: " + product[4], pady=10, font=("Comic Sans MS", 12, "bold")).grid(row=0, column=0, padx=10)
        Label(self.info_frame, text="Quantity: " + product[6], pady=10, font=("Comic Sans MS", 12, "bold")).grid(row=1, column=0, padx=10)
        Button(self.info_frame, text="Change", font=("Comic Sans MS", 12, "bold"), relief=SOLID,
               activebackground="green", activeforeground="#F6F5EC", command=lambda: self.change_price(product)).grid(row=0, column=1, padx=10)
        Button(self.info_frame, text="Change", font=("Comic Sans MS", 12, "bold"), relief=SOLID,
               activebackground="green", activeforeground="#F6F5EC", command=lambda: self.change_quantity(product)).grid(row=1, column=1, padx=10)

    def change_price(self, product_info):
        self.change_price_screen = Toplevel(self.change_info_screen)
        self.change_price_screen.title("Price")
        self.change_price_screen.geometry("250x150")
        self.change_price_screen.resizable(width=False, height=False)
        self.new_price = StringVar()
        Label(self.change_price_screen, text="New Price", font=("Comic Sans MS", 12, "bold")).pack(pady=5)
        self.new_price_entry = Entry(self.change_price_screen, textvariable=self.new_price)
        self.new_price_entry.pack()
        Button(self.change_price_screen, text="Confirm", font=("Comic Sans MS", 12, "bold"), relief=SOLID,
               activebackground="green", activeforeground="#F6F5EC", command=lambda: self.confirm_change_price(product_info, self.new_price.get())).pack(pady=10)

    def confirm_change_price(self, product_info, new_price):
        formatted_price = "{:,.0f}₫".format(float(new_price)).replace(",", ".")
        product_info[4] = formatted_price

        # Đọc toàn bộ nội dung của file CSV vào một danh sách
        with open("Products.csv", "r", newline="", encoding="UTF-8") as file:
            reader = csv.reader(file)
            data = list(reader)

        # Tìm vị trí của sản phẩm cần thay đổi trong danh sách và thay đổi giá trị của nó
        for i, row in enumerate(data):
            if row[0] == product_info[0]:
                data[i] = product_info
                break

        # Ghi lại danh sách đã được cập nhật vào file CSV
        with open("Products.csv", "w", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        self.change_price_screen.destroy()
        self.change_info_screen.destroy()
        self.change_info(product_info)
        self.ShowFrames(product_info[1])

    def change_quantity(self, product_info):
        self.change_quantity_screen = Toplevel(self.change_info_screen)
        self.change_quantity_screen.title("Quantity")
        self.change_quantity_screen.geometry("250x150")
        self.change_quantity_screen.resizable(width=False, height=False)
        self.new_quantity = StringVar()
        Label(self.change_quantity_screen, text="New Quantity", font=("Comic Sans MS", 12, "bold")).pack(pady=5)
        self.new_quantity_entry = Entry(self.change_quantity_screen, textvariable=self.new_quantity)
        self.new_quantity_entry.pack()
        Button(self.change_quantity_screen, text="Confirm", font=("Comic Sans MS", 12, "bold"), relief=SOLID,
               activebackground="green", activeforeground="#F6F5EC",
               command=lambda: self.confirm_change_quantity(product_info, self.new_quantity.get())).pack(pady=10)

    def confirm_change_quantity(self, product_info, new_quantity):
        product_info[6] = new_quantity

        # Đọc toàn bộ nội dung của file CSV vào một danh sách
        with open("Products.csv", "r", newline="", encoding="UTF-8") as file:
            reader = csv.reader(file)
            data = list(reader)

        # Tìm vị trí của sản phẩm cần thay đổi trong danh sách và thay đổi giá trị của nó
        for i, row in enumerate(data):
            if row[0] == product_info[0]:
                data[i] = product_info
                break

        # Ghi lại danh sách đã được cập nhật vào file CSV
        with open("Products.csv", "w", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        self.change_quantity_screen.destroy()
        self.change_info_screen.destroy()
        self.change_info(product_info)
        self.ShowFrames(product_info[1])


def main():
    root = Tk()
    app = Mainmenu(master=root)
    app.mainloop()


if __name__ == "__main__":
    MainAccountScreen()
