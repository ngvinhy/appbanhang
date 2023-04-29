from tkinter.font import BOLD
from xulyanh import *
from tkinter import *
import os
import tkinter as tk
from tkinter import messagebox
from billap import Bill_App


def register():
    global register_screen
    global username
    global password
    global username_entry
    global password_entry
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.resizable(width=False, height=False)
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.resizable(width=False, height=False)
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    messagebox.showinfo("Account", "Registration Success")
    register_screen.destroy()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    login_success_screen.resizable(width=False, height=False)
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    password_not_recog_screen.resizable(width=False, height=False)
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    user_not_found_screen.resizable(width=False, height=False)
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("850x690")
    main_screen.title("Account Login")
    main_screen.resizable(width=False, height=False)
    Label(text="Select Your Choice", fg="white", bg="#252d35", width="300", height="2", font=("Comic Sans MS", 13, BOLD)).pack()
    login_frame = LabelFrame(main_screen, bd=2, relief="groove")
    login_frame.pack()
    image_cover = xuly_image("https://ik.imagekit.io/nhom2/Cover.png?updatedAt=1682768752412", 850, 640)
    img1 = tk.Label(login_frame, image=image_cover)
    img1.pack(side="top", fill=BOTH)

    Button(login_frame, text="Login", height="2", width="15", command=login, font=("Comic Sans MS", 10, BOLD)).place(x=360, y=260)
    Button(login_frame, text="Register", height="2", width="15", command=register, font=("Comic Sans MS", 10, BOLD)).place(x=360, y=320)

    main_screen.mainloop()


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
        file = open("Products.txt", "r", encoding="UTF-8")
        data = file.readlines()
        file.close()
        data = [i.strip("\n") for i in data]
        data = [i.split(",") for i in data]
        return data

    def append_data(self):
        file = open("Products.txt", "a", encoding="UTF-8")
        file.write("{},{},{},{},{}\n".format(self.name, self.price, self.image, self.description, self.type, self.code))
        file.close()


class Mainmenu(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.products_frame = LabelFrame(self.master, bd=3, relief="groove", text="Products", font="arial 16 bold", fg="dark blue", labelanchor=N)
        self.button_frame = LabelFrame(self.master, bd=3, relief="groove", text="Menu", font="arial 16 bold", fg="dark blue", labelanchor=N)
        self.heading = LabelFrame(self.master, bd=3, relief="groove", bg="#080a0d")
        self.image_logo = xuly_image("https://ik.imagekit.io/nhom2/Logo.png?updatedAt=1682769745947", 100, 40)
        self.entry_page_var = StringVar()
        self.lf = []
        self.button_add = []
        self.lf1 = []
        self.image_products = []
        self.pack()
        self.master.geometry("1361x791")
        self.master.title("TECH HUB SHOP")
        self.master.resizable(width=False, height=False)
        self.products = Product.get_data()
        self.cart_list = []
        self.create_widgets()

    def create_widgets(self):
        self.heading.place(x=1, y=0, width=1360, height=60)

        Label(self.heading, image=self.image_logo).grid(row=0, column=0, padx=10, pady=5)

        Label(self.heading, text="Empowering Your Tech Lifestyle", font=("Comic Sans MS", 16, BOLD), fg="white", bg="#080a0d").grid(row=0, column=2, padx=400, pady=5)
        Button(self.heading, text="Payment", font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC", bg="#765341", relief=SOLID, command=self.payment).grid(row=0, column=3, padx=10, pady=5)

        self.button_frame.place(x=1, y=60, width=130, height=730)
        self.products_frame.place(x=131, y=60, width=1230, height=730)

        Label(self.master, text="Page", font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC", bg="#765341", relief=SOLID).place(x=10, y=740)
        Entry(self.master, textvariable=self.entry_page_var, width=5, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC", bg="#765341", relief=SOLID).place(x=70, y=740)

        Button(self.button_frame, text="Laptop", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#765341", relief=SOLID, command=lambda: self.ShowFrames("face")).grid(row=0, column=0, padx=10,
                                                                                         pady=3)

        Button(self.button_frame, text="PC", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC", bg="#765341",
               relief=SOLID, command=lambda: self.ShowFrames("body")).grid(row=1, column=0, padx=10, pady=3)

        Button(self.button_frame, text="Apple", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC", bg="#765341",
               relief=SOLID, command=lambda: self.ShowFrames("Cleanser")).grid(row=2, column=0, padx=10, pady=3)

        Button(self.button_frame, text="Screen", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#765341", relief=SOLID, command=lambda: self.ShowFrames("Toner")).grid(row=3, column=0, padx=10,
                                                                                          pady=3)

        Button(self.button_frame, text="Keyboard", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#765341", relief=SOLID, command=lambda: self.ShowFrames("Serum")).grid(row=4, column=0, padx=10,
                                                                                          pady=3)

        Button(self.button_frame, text="Mouse", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC", bg="#765341",
               relief=SOLID, command=lambda: self.ShowFrames("Whitening")).grid(row=5, column=0, padx=10, pady=3)

        Button(self.button_frame, text="Headphones", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#765341", relief=SOLID, command=lambda: self.ShowFrames("Lotion")).grid(row=6, column=0, padx=10,
                                                                                           pady=3)

        Button(self.button_frame, text="Accessories", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#765341", relief=SOLID, command=lambda: self.ShowFrames("Exfoliate")).grid(row=7, column=0, padx=10,
                                                                                              pady=3)

        Button(self.button_frame, text="Others", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#765341", relief=SOLID, command=lambda: self.ShowFrames("Others")).grid(row=8, column=0, padx=10,
                                                                                           pady=3)

        Button(self.button_frame, text="Show Cart", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
               bg="#765341", relief=SOLID, command=self.show_cart).grid(row=9, column=0, padx=10, pady=3)

    def payment(self):
        self.cart_list = []
        self.show_cart()
        messagebox.showinfo("Payment", "Thank you for shopping with us")
        self.master.destroy()
        root = Tk()
        bill = Bill_App(root)
        bill.mainloop()

    def buy_product(self, product):
        self.cart_list.append(product)

    def HideAllFrame(self):
        for widget in self.products_frame.winfo_children():
            widget.destroy()

    def ShowFrames(self, phanloai):
        self.HideAllFrame()
        self.image_products = []
        self.button_add = []  # Khởi tạo danh sách mới cho button_add
        count = 0
        for i in range(len(self.products)):
            try:
                if self.products[i][4] == phanloai:
                    lf = LabelFrame(self.products_frame, bd=2, relief="groove", text=self.products[i][0])
                    self.image_products.append(xuly_image(self.products[i][2], 70, 50))
                    label_image = Label(lf, image=self.image_products[count])
                    Label(lf, text=self.products[i][1], font=("Comic Sans MS", 12, "bold"), fg="blue").grid(row=1,
                                                                                                            column=0,
                                                                                                            padx=10)
                    Label(lf, text=self.products[i][3], font=("Comic Sans MS", 12, "bold"), fg="blue").grid(row=3,
                                                                                                            column=0,
                                                                                                            padx=10)
                    self.button_add.append(
                        Button(lf, command=lambda idx=count: self.buy_product(self.products[idx]), text="Add to Cart",
                               font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC", bg="#765341", relief=SOLID))
                    lf.grid(row=count // 4, column=count % 4, padx=10, pady=1)
                    label_image.grid(row=2, column=0, padx=10)
                    self.button_add[count].grid(row=4, column=0, padx=10)
                    count += 1
            except:
                continue

    def show_cart(self):
        self.HideAllFrame()
        for i in range(len(self.cart_list)):
            lf = LabelFrame(self.products_frame, bd=2, relief="groove")
            lf.grid(row=i // 4, column=i % 4, padx=10, pady=1)
            self.lf1.append(lf)  # Append the label frame to the list

            Label(lf, text=self.cart_list[i][1], font="arial 12 bold", fg="blue").grid(row=1, column=0, padx=10)
            self.image_products.append(xuly_image(self.cart_list[i][2], 70, 50))
            label_image = Label(lf, image=self.image_products[i])
            label_image.grid(row=2, column=0, padx=10)
            Label(lf, text=self.cart_list[i][3], font="arial 12 bold", fg="blue").grid(row=3, column=0, padx=10)
            Button(lf, command=lambda idx=i: self.remove_item(idx), text="Remove", font="arial 12 bold",
                   fg="blue", bg="light green").grid(row=4, column=0, padx=10)

    def remove_item(self, idx):
        if -1 <= idx < len(self.cart_list):
            self.lf1[idx].destroy()
            del self.lf1[idx]  # Remove the label frame from the list
            self.cart_list.pop(idx)


def delete_login_success():
    login_success_screen.destroy()
    main_screen.destroy()
    main()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def main():
    root = Tk()
    app = Mainmenu(master=root)
    app.mainloop()


main_account_screen()
