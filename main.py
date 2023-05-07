import csv
from datetime import *
from tkinter.font import BOLD
import PIL
from xulyanh import *
from tkinter import *
import os
from tkinter import messagebox, ttk
from collections import Counter


class MainAccountScreen:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("850x690")
        self.root.title("TECH HUB SHOP")
        self.root.resizable(width=False, height=False)

        Label(text="Select Your Choice", fg="white", bg="#252d35", width="300", height="1", font=("Comic Sans MS", 13, "bold")).pack()

        login_frame = LabelFrame(self.root, bd=2, relief="groove")
        login_frame.pack()

        image_cover = xuly_image("https://ik.imagekit.io/nhom2/Cover.png?updatedAt=1682768752412", 850, 650)
        img1 = Label(login_frame, image=image_cover)
        img1.pack(side="top", fill=BOTH)

        Button(login_frame, text="Login", height="2", width="15", command=self.login, font=("Comic Sans MS", 10, "bold")).place(x=360, y=265)

        Button(login_frame, text="Register", height="2", width="15", command=self.register, font=("Comic Sans MS", 10, "bold")).place(x=360, y=320)

        Button(login_frame, text="Admin", height="1", width="7", command=self.admin_login, font=("Comic Sans MS", 10, "bold")).place(x=775, y=10)

        self.root.mainloop()

    def register(self):
        self.register_screen = Toplevel(self.root)
        self.register_screen.title("Register")
        self.register_screen.geometry("300x250")
        self.register_screen.resizable(width=False, height=False)
        self.username = StringVar()
        self.password = StringVar()
        Label(self.register_screen, text="Please enter details below").pack(pady=5)
        username_lable = Label(self.register_screen, text="Username")
        username_lable.pack(pady=5)
        username_entry = Entry(self.register_screen, textvariable=self.username)
        username_entry.pack(pady=5)
        password_lable = Label(self.register_screen, text="Password")
        password_lable.pack(pady=5)
        password_entry = Entry(self.register_screen, textvariable=self.password, show='*')
        password_entry.pack(pady=5)
        Button(self.register_screen, text="Register", width=10, height=1, command=self.register_user).pack(pady=5)

    def login(self):
        self.login_screen = Toplevel(self.root)
        self.login_screen.title("Login")
        self.login_screen.geometry("300x250")
        self.login_screen.resizable(width=False, height=False)
        Label(self.login_screen, text="Please enter details below to login").pack(pady=5)

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(self.login_screen, text="Username").pack(pady=5)
        self.username_login_entry = Entry(self.login_screen, textvariable=self.username_verify)
        self.username_login_entry.pack(pady=5)
        Label(self.login_screen, text="Password").pack(pady=5)
        self.password_login_entry = Entry(self.login_screen, textvariable=self.password_verify, show='*')
        self.password_login_entry.pack(pady=5)
        Button(self.login_screen, text="Login", width=10, height=1, command=self.login_verify).pack(pady=5)

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()

        file = open(username_info, "w")
        file.write(password_info)
        file.close()
        messagebox.showinfo("Account", "Registration Success!")
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
                messagebox.showinfo("Account", "Login Success!")
                self.root.destroy()
                main()
            else:
                self.password_not_recognised()
        else:
            self.user_not_found()

    def password_not_recognised(self):
        self.login_screen.destroy()
        self.login()
        Label(self.login_screen, text="Invalid Password!", fg="red").pack(pady=5)

    def user_not_found(self):
        self.login_screen.destroy()
        self.login()
        Label(self.login_screen, text="User Not Found!", fg="red").pack(pady=5)

    def admin_login(self):
        self.admin_login_screen = Toplevel(self.root)
        self.admin_login_screen.title("Admin Login")
        self.admin_login_screen.geometry("300x250")
        self.admin_login_screen.resizable(width=False, height=False)
        Label(self.admin_login_screen, text="Please enter details below to login").pack(pady=5)

        self.admin_username_verify = StringVar()
        self.admin_password_verify = StringVar()

        Label(self.admin_login_screen, text="Username").pack(pady=5)
        self.admin_username_login_entry = Entry(self.admin_login_screen, textvariable=self.admin_username_verify)
        self.admin_username_login_entry.pack(pady=5)
        Label(self.admin_login_screen, text="Password").pack(pady=5)
        self.admin_password_login_entry = Entry(self.admin_login_screen, textvariable=self.admin_password_verify, show='*')
        self.admin_password_login_entry.pack(pady=5)
        Button(self.admin_login_screen, text="Login", width=10, height=1, command=self.admin_login_verify).pack(pady=5)

    def admin_login_verify(self):
        username1 = self.admin_username_verify.get()
        password1 = self.admin_password_verify.get()
        self.admin_username_login_entry.delete(0, END)
        self.admin_password_login_entry.delete(0, END)
        if username1 == "admin":
            file = open("admin", "r")
            verify = file.read().splitlines()
            if password1 in verify:
                self.admin_login_screen.destroy()
                messagebox.showinfo("Account", "Login Success!")
                self.root.destroy()
                Admin()
            else:
                self.admin_password_not_recognised()
        else:
            self.admin_user_not_found()

    def admin_password_not_recognised(self):
        self.admin_login_screen.destroy()
        self.admin_login()
        Label(self.admin_login_screen, text="Invalid Password!", fg="red").pack(pady=5)

    def admin_user_not_found(self):
        self.admin_login_screen.destroy()
        self.admin_login()
        Label(self.admin_login_screen, text="User Not Found!", fg="red").pack(pady=5)


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


class Mainmenu(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.products_frame = LabelFrame(self.master, bd=3, relief="raised", text="PRODUCTS",
                                         font=("Comic Sans MS", 16, BOLD), fg="white", bg="#252d35", labelanchor=N)
        self.button_frame = LabelFrame(self.master, bd=3, relief="raised", text="CATEGORY",
                                       font=("Comic Sans MS", 16, BOLD), fg="white", bg="#252d35", labelanchor=N)
        self.heading = LabelFrame(self.master, bd=3, relief="raised", bg="#080a0d")
        self.image_logo = xuly_image("https://ik.imagekit.io/nhom2/Logo.png?updatedAt=1682769745947", 100, 40)
        self.image_products = []
        self.lf_list = []
        self.pack()
        self.master.geometry("1180x740")
        self.master.title("TECH HUB SHOP")
        self.master.resizable(width=False, height=False)
        self.products = Product.get_data()
        self.cart_list = []
        self.create_widgets()
        self.quantity_entries = []

    def create_widgets(self):
        self.heading.place(x=0, y=0, width=1180, height=60)

        Label(self.heading, image=self.image_logo).grid(row=0, column=0, padx=10, pady=5)

        Label(self.heading, text="Empowering Your Tech Lifestyle", font=("Comic Sans MS", 16, BOLD), fg="white",
              bg="#080a0d").grid(row=0, column=2, padx=285, pady=5)

        Button(self.heading, text="Shopping Cart", font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="green", relief=SOLID, activebackground="green", activeforeground="#F6F5EC",
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
        self.image_products = []  # Xóa list hình ảnh cũ
        count = 0
        for product in self.products:
            if product[1] == phanloai:
                lf = LabelFrame(frame, bd=2, relief="solid", fg="white", bg="#252d35", text=product[3],
                                font=("Comic Sans MS", 12, "bold"), labelanchor=N)
                lf.grid(row=count // 3, column=count % 3, padx=10, pady=10)
                try:
                    self.image_products.append(xuly_image(product[5], 120, 100))
                except PIL.UnidentifiedImageError:
                    self.image_products.append(xuly_image("https://ik.imagekit.io/nhom2/404.png?updatedAt=1683199218403", 120, 100))
                label_image = Label(lf, image=self.image_products[count])
                label_image.grid(row=2, column=0, padx=85, pady=5)

                Label(lf, text="Brand: " + product[2], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=1, column=0, padx=85, pady=5)
                Label(lf, text=product[4], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=3, column=0, padx=85, pady=5)

                if int(product[6]) > 0:
                    Label(lf, text="Quantity: " + product[6], font=("Comic Sans MS", 12, "bold"), fg="white",
                          bg="#252d35").grid(row=4, column=0, padx=85, pady=5)
                    quantity_entry = ttk.Combobox(lf, values=list(range(1, int(product[6]) + 1)), state="readonly", font=("Comic Sans MS", 12, BOLD))
                    quantity_entry.configure(width=2, height=5)
                    quantity_entry.grid(row=5, column=0, padx=(65, 5), pady=5, sticky="w")
                    self.quantity_entries.append(quantity_entry)
                    Button(lf, command=lambda p=product, q=quantity_entry: self.update_quantity_temporary(p, q.get()),
                           text="Add to Cart", font=("Comic Sans MS", 12, "bold"), fg="white", bg="green", relief=SOLID,
                           activebackground="green", activeforeground="white").grid(row=5, column=0, padx=85, pady=5)
                else:
                    Button(lf, state=DISABLED, text="Sold Out", font=("Comic Sans MS", 12, "bold"),
                           relief=SOLID).grid(row=4, column=0, padx=85, pady=25)
                count += 1
            else:
                continue

        # Cập nhật thanh cuộn khi có thay đổi
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def update_quantity_temporary(self, product, quantity):  # Hiển thị số lượng tạm thời trên giao diện
        if quantity.strip() == "":
            self.cart_list.append(product)
            new_quantity = int(product[6]) - 1
        else:
            for i in range(int(quantity.strip())):
                self.cart_list.append(product)
            new_quantity = int(product[6]) - int(quantity.strip())
        product[6] = str("{:02d}".format(new_quantity))
        messagebox.showinfo("Success", "Product added to cart successfully!")
        self.ShowFrames(product[1])

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
        self.lf_list = []  # Xóa list label frames
        self.quantity_labels = {}  # Tạo từ điển chứa nhãn số lượng sản phẩm
        count = 0  # Khởi tạo biến đếm để định vị vị trí

        product_count = {}  # Tạo từ điển đếm số lượng sản phẩm cho từng mã code
        for item in self.cart_list:
            code = item[0]  # Mã code của sản phẩm
            product_count[code] = product_count.get(code, 0) + 1
        added_codes = []  # Danh sách mã code đã được xét
        for item in self.cart_list:
            code = item[0]  # Mã code của sản phẩm
            if code in added_codes:
                continue  # Bỏ qua nếu mã code đã được xét trước đó

            lf = LabelFrame(frame, bd=2, relief="solid", fg="white", bg="#252d35",
                            text=item[3], font=("Comic Sans MS", 12, BOLD), labelanchor=N)
            lf.grid(row=len(added_codes) // 3, column=len(added_codes) % 3, padx=10, pady=5)
            self.lf_list.append(lf)  # Thêm label frame vào list
            added_codes.append(code)  # Thêm mã code vào danh sách đã xét

            product_brand = item[2]
            product_image = item[5]
            product_price = item[4]
            try:
                self.image_products.append(xuly_image(product_image, 120, 100))
            except PIL.UnidentifiedImageError:
                self.image_products.append(xuly_image("https://ik.imagekit.io/nhom2/404.png?updatedAt=1683199218403", 120, 100))
            label_image = Label(lf, image=self.image_products[count])
            label_image.grid(row=2, column=0, padx=85, pady=5)
            Label(lf, text="Brand: " + product_brand, font=("Comic Sans MS", 12, "bold"), fg="white",
                  bg="#252d35").grid(row=1, column=0, padx=85, pady=5)
            Label(lf, text=product_price, font=("Comic Sans MS", 12, "bold"), fg="white",
                  bg="#252d35").grid(row=3, column=0, padx=85, pady=5)
            code = item[0]  # Mã code của sản phẩm
            quantity = product_count[code] if code in product_count else 1
            quantity_label = Label(lf, text="Quantity: {}".format(quantity), font=("Comic Sans MS", 12, "bold"),
                                   fg="white", bg="#252d35")
            quantity_label.grid(row=4, column=0, padx=85, pady=5)
            self.quantity_labels[lf] = quantity_label  # Thêm nhãn số lượng vào từ điển với key là label frame

            quantity_entry = ttk.Combobox(lf, values=list(range(1, int(quantity) + 1)), state="readonly",
                                          font=("Comic Sans MS", 12, BOLD))
            quantity_entry.configure(width=2, height=5)
            quantity_entry.grid(row=5, column=0, padx=(85, 5), pady=5, sticky="w")
            self.quantity_entries.append(quantity_entry)

            Button(lf, command=lambda p=item, q=quantity_entry, cart_item=lf: self.remove_item(p, q, cart_item),
                   text="Remove", font=("Comic Sans MS", 12, "bold"), fg="white", bg="red", activeforeground="white",
                   activebackground="red").grid(row=5, column=0, padx=85, pady=5)
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
                                command=self.show_delivery_info_window)
        payment_button.pack(side=RIGHT, padx=10, pady=5)

    def remove_item(self, item, quantity_entry, cart_item):
        quantity = quantity_entry.get()  # Lấy giá trị của quantity_entry
        if quantity.strip() == "":
            quantity = 1  # Mặc định xóa 1 sản phẩm nếu dữ liệu nhập vào là rỗng
        else:
            quantity = int(quantity)
        for i in range(quantity):
            self.cart_list.remove(item)
        for product in self.products:
            product[6] = str("{:02d}".format(int(item[6]) + int(quantity)))
        messagebox.showinfo("Success", "Products remove from cart successfully!")
        cart_item.destroy()
        self.show_cart()  # Load lại giao diện cart

    def tong(self):
        return sum([float(product[4].replace("₫", "").replace(".", "")) for product in self.cart_list])

    def show_delivery_info_window(self):
        self.delivery_window = Toplevel(self)
        self.delivery_window.title("Delivery Information")
        self.delivery_window.geometry("300x210")
        self.delivery_window.resizable(width=False, height=False)

        frame = Frame(self.delivery_window, bd=2, relief="solid")
        frame.pack(padx=10, pady=5)

        labels = ["Name:", "Phone:", "Email:", "Address:"]
        self.entries = []

        for i, label_text in enumerate(labels):
            label = Label(frame, text=label_text, font=("Comic Sans MS", 12, BOLD))
            entry = Entry(frame, bd=2, relief=SOLID)
            label.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        save_button = Button(self.delivery_window, bd=1, text="Save", bg="green", fg="white", activebackground="green",
                             activeforeground="white", font=("Comic Sans MS", 12, BOLD), command=self.show_order)
        save_button.pack(pady=5, padx=30)

    def show_order(self):
        if len(self.cart_list) != 0:
            self.bill_window = Toplevel(self.master)
            self.bill_window.title("Order")

            receipt_label = Label(self.bill_window, text="Order Confirmation", font=("Comic Sans MS", 15, BOLD))
            receipt_label.grid(row=0, column=0, columnspan=5, padx=10, pady=5)

            title_label = Label(self.bill_window, text="Products of Tech Hub Shop", font=("Comic Sans MS", 13, BOLD))
            title_label.grid(row=1, column=0, columnspan=5, padx=10, pady=3)

            current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
            time_label = Label(self.bill_window, text=current_time, font=("Comic Sans MS", 12, BOLD))
            time_label.grid(row=2, column=0, columnspan=5, padx=10, pady=5)

            line_label = Label(self.bill_window, text="-" * 80, font=("Comic Sans MS", 12, BOLD))
            line_label.grid(row=3, column=0, columnspan=5, padx=10, pady=5)

            headers = ["ID", "Product", "Quantity", "Price", "Total"]
            for col, header in enumerate(headers):
                header_label = Label(self.bill_window, text=header, font=("Comic Sans MS", 12, BOLD))
                header_label.grid(row=4, column=col, padx=10, pady=5)
            row = 5  # Khởi tạo biến chỉ thứ tự hàng
            total_amount = 0  # Khởi tạo biến tổng tiền
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
                    # Kiểm tra ID sản phẩm có trong list chưa
                    existing_index = next((i for i, code in enumerate(code_labels) if code['text'] == product_code), None)

                    if existing_index is not None:
                        # Nếu ID sản phẩm đã có thì cập nhật số lượng và tổng tiền của sản phẩm đó
                        existing_quantity = int(quantity_labels[existing_index]['text'])
                        new_quantity = existing_quantity + 1
                        quantity_labels[existing_index].configure(text=str(new_quantity))
                        total_price = int(product_price.replace("₫", "").replace(".", "").strip()) * new_quantity
                        total_labels[existing_index].configure(text="{:,.0f}₫".format(float(total_price)).replace(",", "."))
                    else:
                        # Nếu ID sản phẩm chưa có thì thêm vào list và tạo các Label mới
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
                        # Định dạng các chuỗi thể hiện giá tiền và tính tổng
                        product_price = product_price.replace("₫", "").replace(".", "").strip()
                        total_price = int(product_price) * 1
                        total_amount += total_price
                        total_label = Label(self.bill_window, text="{:,}₫".format(total_price).replace(",", "."),
                                            font=("Comic Sans MS", 12, BOLD))
                        total_label.grid(row=row, column=4, padx=10, pady=5)
                        total_labels.append(total_label)
                        row += 1  # Tăng biến thứ tự hàng nếu có thêm sản phẩm
            line_label = Label(self.bill_window, text="-" * 80, font=("Comic Sans MS", 12, BOLD))
            line_label.grid(row=row, column=0, columnspan=5, padx=10, pady=5)
            # Hiển thị tổng số tiền
            row += 1
            total_label = Label(self.bill_window, text="Total Amount: {:,.0f}₫".format(self.tong()).replace(".0", "").replace(",", "."),
                                font=("Comic Sans MS", 12, BOLD))
            total_label.grid(row=row, column=0, columnspan=2, padx=10, pady=10)

            confirm_button = Button(self.bill_window, text="Confirm", font=("Comic Sans MS", 12, BOLD), relief=SOLID,
                                    activeforeground="white", activebackground="green",
                                    command=lambda: self.confirm_order(*[en_try.get() for en_try in self.entries]))
            confirm_button.grid(row=row, column=4, sticky=E, padx=80, pady=5)

            cancel_button = Button(self.bill_window, text="Cancel", font=("Comic Sans MS", 12, BOLD), relief=SOLID,
                                   activeforeground="white", activebackground="red", command=self.bill_window.destroy)
            cancel_button.grid(row=row, column=4, sticky=E, padx=5, pady=5)
        else:
            messagebox.showinfo("Cart", "There are no products in the cart!")

    def confirm_order(self, name, phone, email, address):
        self.delivery_window.destroy()
        self.bill_window.destroy()
        self.show_bill(name, phone, email, address)

    def show_bill(self, name, phone, email, address):
        product_counts = Counter(product[0] for product in self.cart_list)
        receipt = f"{'-' * 50}\n{'PAYMENT RECEIPT':^50}\n{'Time: '}{datetime.now():%d-%m-%Y %H:%M:%S}\n{'-' * 50}"

        total_amount = 0  # Khởi tạo biến tổng số tiền
        unique_product_ids = set(product[0] for product in self.cart_list)  # Lấy ID sản phẩm

        receipt += f"\nCustomer Name: {name}\nPhone Number: {phone}\nEmail: {email}\nAddress: {address}\n{'-' * 30:^50}\n{'YOUR ORDER':^50}"

        row = 0
        for product_id in unique_product_ids:
            product_details = next((p for p in self.products if p[0] == product_id), None)
            if product_details:
                product_code = product_details[0]
                product_name = product_details[2] + " " + product_details[3]
                product_price = product_details[4]
                quantity = product_counts[product_id]
                total_price = float(product_price.replace("₫", "").replace(".", "")) * quantity
                total_amount += total_price  # Cập nhật tổng số tiền
                receipt += f"\nCode: {product_code}\nProduct: {product_name}\nQuantity: {quantity}\nPrice: {product_price}\n{'-' * 20}"
                row += 1

        receipt += "\nTotal: {:,.0f}₫".format(float(total_amount)).replace(",", ".")
        messagebox.showinfo("Order Confirmed!", receipt)
        self.cart_list.clear()

        # Ghi lại danh sách đã được cập nhật vào file CSV
        with open("Products.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(self.products)

        self.bill_window.destroy()
        self.show_cart()


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

        Label(self.heading, text="PRODUCTS MANAGEMENT", font=("Comic Sans MS", 16, BOLD), fg="white",
              bg="#080a0d").grid(row=0, column=2, padx=320, pady=5)

        Button(self.heading, text="Add Product", font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="green", relief=SOLID, activebackground="green", activeforeground="#F6F5EC",
               command=self.add_product).grid(row=0, column=3, padx=10, pady=5)

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
        count = 0
        for product in self.products:
            if product[1] == phanloai:
                lf = LabelFrame(frame, bd=2, relief="solid", fg="white", bg="#252d35", text=product[3],
                                font=("Comic Sans MS", 12, "bold"), labelanchor=N)
                lf.grid(row=count // 3, column=count % 3, padx=10, pady=10)
                try:
                    self.image_products.append(xuly_image(product[5], 120, 100))
                except PIL.UnidentifiedImageError:
                    self.image_products.append(xuly_image("https://ik.imagekit.io/nhom2/404.png?updatedAt=1683199218403", 120, 100))
                label_image = Label(lf, image=self.image_products[count])
                label_image.grid(row=2, column=0, padx=85, pady=5)

                Label(lf, text=product[2], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=1, column=0, padx=85, pady=5)
                Label(lf, text=product[4], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=3, column=0, padx=85, pady=5)
                Label(lf, text="Quantity: " + product[6], font=("Comic Sans MS", 12, "bold"), fg="white", bg="#252d35").grid(row=4, column=0, padx=85, pady=5)

                button_add = Button(lf, command=lambda p=product: self.change_info(p), text="Change Info",
                                    font=("Comic Sans MS", 12, "bold"), fg="white", bg="green", relief=SOLID,
                                    activebackground="green", activeforeground="white")
                button_add.grid(row=5, column=0, padx=85, pady=5)
                button_remove = Button(lf, command=lambda p=product: self.remove_product(p), text="Remove",
                                       font=("Comic Sans MS", 12, "bold"), fg="white", bg="red", relief=SOLID,
                                       activebackground="red", activeforeground="white")
                button_remove.grid(row=5, column=0, padx=(5, 10), pady=5, sticky="e")
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
        self.change_price_screen.geometry("250x160")
        self.change_price_screen.resizable(width=False, height=False)
        self.new_price = StringVar()
        Label(self.change_price_screen, text="New Price", font=("Comic Sans MS", 12, "bold")).pack(pady=5)
        self.new_price_entry = Entry(self.change_price_screen, textvariable=self.new_price, font=("Comic Sans MS", 12, "bold"))
        self.new_price_entry.pack()
        Button(self.change_price_screen, text="Confirm", font=("Comic Sans MS", 12, "bold"), relief=SOLID,
               activebackground="green", activeforeground="#F6F5EC", command=lambda: self.confirm_change_price(product_info, self.new_price.get())).pack(pady=10)

    def confirm_change_price(self, product_info, new_price):
        self.new_price_entry.delete(0, END)
        try:
            if float(new_price) < 0:
                self.change_price_screen.destroy()
                self.change_price(product_info)
                Label(self.change_price_screen, text="Invalid Price", font=("Comic Sans MS", 12, BOLD), fg="red").pack(pady=5)
            else:
                formatted_price = "{:,.0f}₫".format(float(new_price)).replace(",", ".")
                product_info[4] = formatted_price
                self.change_price_screen.destroy()
                self.change_info_screen.destroy()
                messagebox.showinfo("Success", "Your changes have been saved!")
                self.ShowFrames(product_info[1])
        except ValueError:
            self.change_price_screen.destroy()
            self.change_price(product_info)
            Label(self.change_price_screen, text="Invalid Price", font=("Comic Sans MS", 12, BOLD), fg="red").pack(pady=5)

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

    def change_quantity(self, product_info):
        self.change_quantity_screen = Toplevel(self.change_info_screen)
        self.change_quantity_screen.title("Quantity")
        self.change_quantity_screen.geometry("250x160")
        self.change_quantity_screen.resizable(width=False, height=False)
        self.new_quantity = StringVar()
        Label(self.change_quantity_screen, text="New Quantity", font=("Comic Sans MS", 12, "bold")).pack(pady=5)
        self.new_quantity_entry = Entry(self.change_quantity_screen, textvariable=self.new_quantity, font=("Comic Sans MS", 12, "bold"))
        self.new_quantity_entry.pack()
        Button(self.change_quantity_screen, text="Confirm", font=("Comic Sans MS", 12, "bold"), relief=SOLID,
               activebackground="green", activeforeground="#F6F5EC",
               command=lambda: self.confirm_change_quantity(product_info, self.new_quantity.get())).pack(pady=10)

    def confirm_change_quantity(self, product_info, new_quantity):
        self.new_quantity_entry.delete(0, END)
        try:
            if int(new_quantity) < 0:
                self.change_quantity_screen.destroy()
                self.change_quantity(product_info)
                Label(self.change_quantity_screen, text="Invalid Quantity", font=("Comic Sans MS", 12, BOLD), fg="red").pack(pady=5)
            else:
                product_info[6] = str("{:02d}".format(int(new_quantity)))
                self.change_quantity_screen.destroy()
                self.change_info_screen.destroy()
                messagebox.showinfo("Success", "Your changes have been saved!")
                self.ShowFrames(product_info[1])
        except ValueError:
            self.change_quantity_screen.destroy()
            self.change_quantity(product_info)
            Label(self.change_quantity_screen, text="Invalid Quantity", font=("Comic Sans MS", 12, BOLD), fg="red").pack(pady=5)
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

    def add_product(self):
        self.add_product_screen = Toplevel(self.root)
        self.add_product_screen.title("Delivery Information")
        self.add_product_screen.geometry("400x300")
        self.add_product_screen.resizable(width=False, height=False)

        frame = Frame(self.add_product_screen, bd=2, relief="solid")
        frame.pack(padx=10, pady=5)

        labels = ["Category:", "Brand:", "Name:", "Price:", "Image:", "Quantity:"]
        self.entries = []

        for i, label_text in enumerate(labels):
            label = Label(frame, text=label_text, font=("Comic Sans MS", 12, "bold"))
            label.grid(row=i, column=0, sticky="w", padx=5, pady=5)

            if label_text == "Category:":
                entry = ttk.Combobox(frame, values=["Laptop", "PC", "Apple", "Screen", "Keyboard", "Mouse", "Headphones",
                                                    "Accessories", "Others"], state="readonly", font=("Comic Sans MS", 12, BOLD))
                entry.configure(width=10, height=5)
            else:
                entry = Entry(frame, bd=2, relief=SOLID)

            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        save_button = Button(self.add_product_screen, bd=1, text="Save", bg="green", fg="white", activebackground="green",
                             activeforeground="white", font=("Comic Sans MS", 12, "bold"), command=self.save_product)
        save_button.pack(pady=5, padx=30)

    def save_product(self):
        if self.entries[0].get() or self.entries[1].get() or self.entries[2].get() or self.entries[3].get() or self.entries[4].get() or self.entries[5].get() == "":
            messagebox.showerror("Products", "Any information is not empty!")
        else:
            # Lấy giá trị đã nhập vào
            product_category = self.entries[0].get().strip()
            manufacturer = self.entries[1].get().strip()
            product_name = self.entries[2].get().strip()
            price = "{:,.0f}₫".format(float(self.entries[3].get().strip())).replace(",", ".")
            image = self.entries[4].get().strip()
            quantity = self.entries[5].get().strip()

            products = []
            for product in self.products:
                if product_category == product[1]:
                    products.append(product)
            product_id = [pr[0] for pr in products]
            if product_id:
                max_code = max([int(p[1:]) for p in product_id if p[1:].isdigit()])
                product_code = product_category[:1] + "{:02d}".format(max_code + 1)  # Định dạng số thành chuỗi nếu max_code = 3 thì product_code = 04
            else:
                product_code = product_category[:1] + "01"
            product_data = [product_code, product_category, manufacturer, product_name, price, image, quantity]
            # Thêm product_data vào file dữ liệu sản phẩm
            with open("Products.csv", "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(product_data)
            self.add_product_screen.destroy()
            messagebox.showinfo("Success", "Product added successfully!")
            self.root.destroy()
            Admin()

    def remove_product(self, product):
        self.remove_product_screen = Toplevel(self.root)
        self.remove_product_screen.title("Remove Product")
        self.remove_product_screen.geometry("235x150")
        self.remove_product_screen.resizable(width=False, height=False)
        Label(self.remove_product_screen, text="Are You Sure?", font=("Comic Sans MS", 12, "bold")).grid(row=0, column=0, padx=60, pady=10)
        Button(self.remove_product_screen, text="Confirm", font=("Comic Sans MS", 12, "bold"), relief=SOLID,
               activebackground="green", activeforeground="#F6F5EC",
               command=lambda: self.confirm_remove_product(product)).grid(row=1, column=0, padx=(10, 90), pady=5)
        Button(self.remove_product_screen, text="Cancel", font=("Comic Sans MS", 12, "bold"), relief=SOLID,
               activebackground="red", activeforeground="#F6F5EC",
               command=self.remove_product_screen.destroy).grid(row=1, column=0, padx=(90, 10), pady=5)

    def confirm_remove_product(self, product):
        # Đọc toàn bộ nội dung của file CSV vào một danh sách
        with open("Products.csv", "r", newline="", encoding="UTF-8") as file:
            reader = csv.reader(file)
            data = list(reader)
        # Tìm vị trí của sản phẩm cần thay đổi trong danh sách và thay đổi giá trị của nó
        for i, row in enumerate(data):
            if row[0] == product[0]:
                data.pop(i)
                break
        # Ghi lại danh sách đã được cập nhật vào file CSV
        with open("Products.csv", "w", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        self.remove_product_screen.destroy()
        messagebox.showinfo("Success", "Product removed successfully!")
        self.root.destroy()
        Admin()


def main():
    root = Tk()
    app = Mainmenu(master=root)
    app.mainloop()


if __name__ == "__main__":
    MainAccountScreen()
