from tkinter.font import BOLD, ITALIC
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
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter details below", bg="pink").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="pink", command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
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

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


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
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("850x690")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="pink", width="300", height="2", font=("Calibri", 13)).pack()
    login_frame = LabelFrame(main_screen, bd=2, relief="groove", bg="light yellow")
    login_frame.pack()
    image_logo = xuly_image("https://ik.imagekit.io/nhom2/Logo/techhub.png?updatedAt=1679738096844", 850, 690)
    img1 = tk.Label(login_frame, image=image_logo)
    img1.pack(side="top", fill=BOTH)

    Button(login_frame, text="Login", height="2", width="30", command=login).place(x=335, y=225)

    Button(login_frame, text="Register", height="2", width="30", command=register).place(x=335, y=275)

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
        self.lf = []
        self.button_add = []
        self.lf1 = []
        self.image_products = []
        self.pack()
        self.master.geometry("1360x1000")
        self.master.title("Fat Cat Ruru")
        self.products = Product.get_data()
        self.cart_list = []
        self.create_widgets()

    def create_widgets(self):
        self.heading = LabelFrame(self.master, bd=2, relief="groove", bg="light yellow")
        self.heading.place(x=0, y=0, width=1380, height=55)
        self.image_logo = xuly_image("https://ik.imagekit.io/nhom2/Logo/techhub.png?updatedAt=1679738096844", 70, 50)
        self.label_logo = Label(self.heading, image=self.image_logo)
        self.label_logo.grid(row=0, column=0)
        self.heading_label = Label(self.heading, text="Fat Cat Clinic", font="arial 20 bold italic", bg="light pink",
                                   fg="blue").grid(row=0, column=1)
        self.tagline = Label(self.heading, text="At your service!", font=("Trebuchet MS Bold", 16, ITALIC, BOLD),
                             fg="white", bg="pink").grid(row=0, column=2, padx=280)
        self.products_frame = LabelFrame(self.master, bd=2, relief="groove", text="Products", font="arial 16 bold",
                                         fg="dark blue")
        self.products_frame.place(x=310, y=60, width=1040, height=950)
        self.button_frame = LabelFrame(self.master, bd=2, relief="groove", text="Buttons", font="arial 16 bold",
                                       fg="dark blue")
        self.button_frame.place(x=0, y=60, width=310, height=950)
        self.paymentt = Button(self.heading, text="Payment", font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID,
                               command=self.payment).grid(row=0, column=3, padx=200)
        self.label_page = Label(self.master, text="Page", font="arial 12 bold", fg="blue", bg="light green").place(x=10,
                                                                                                                   y=950)
        self.entry_page_var = StringVar()
        self.entry_page = Entry(self.master, textvariable=self.entry_page_var, width=5, font="arial 12 bold", fg="blue",
                                bg="light green").place(x=80, y=950)
        self.button_face = Button(self.button_frame, text="Face", pady=10, font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID,
                                  command=lambda: self.ShowFrames("face", self.entry_page_var.get())).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=3)
        self.button_body = Button(self.button_frame, text="Body", pady=10, font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID,
                                  command=lambda: self.ShowFrames("body", self.entry_page_var.get())).grid(row=1,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=3)
        self.button_srm = Button(self.button_frame, text="Cleanser", pady=10, font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID,
                                 command=lambda: self.ShowFrames("Cleanser", self.entry_page_var.get())).grid(row=2,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=3)
        self.button_toner = Button(self.button_frame, text="Toner", pady=10, font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID,
                                   command=lambda: self.ShowFrames("Toner", self.entry_page_var.get())).grid(row=3,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=3)
        self.button_serum = Button(self.button_frame, text="Serum", pady=10, font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID,
                                   command=lambda: self.ShowFrames("Serum", self.entry_page_var.get())).grid(row=4,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=3)
        self.button_duongtrang = Button(self.button_frame, text="Whitening", pady=10, font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID,
                                        command=lambda: self.ShowFrames("Whitening", self.entry_page_var.get())).grid(
            row=5, column=0, padx=10, pady=3)
        self.button_duongam = Button(self.button_frame, text="Body lotion", pady=10, font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID,
                                     command=lambda: self.ShowFrames("Lotion", self.entry_page_var.get())).grid(row=6,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=3)
        self.button_taytebaochet = Button(self.button_frame, text="Body Scrub", pady=10, font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID,
                                          command=lambda: self.ShowFrames("Exfoliate", self.entry_page_var.get())).grid(
            row=7, column=0, padx=10, pady=3)
        self.makeup = Button(self.button_frame, text="Others", pady=10, font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC",
                             bg="#765341", relief=SOLID,
                             command=lambda: self.ShowFrames("Others", self.entry_page_var.get())).grid(row=8,
                                                                                                        column=0,
                                                                                                        padx=10, pady=3)
        self.button_showcart = Button(self.button_frame, text="Show Cart", pady=10, font=("Comic Sans MS", 12, "bold"),
                                      fg="#F6F5EC", bg="#765341", relief=SOLID, command=self.show_cart).grid(row=9,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=3)

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

    def ShowFrames(self, type, page):
        try:
            page = int(page)
        except:
            page = 0
        self.HideAllFrame()
        count = 0
        self.image_products = []
        a = page * 8
        for i in range(len(self.products)):
            try:
                if self.products[i][4] == type:
                    self.lf.append(LabelFrame(self.products_frame, bd=2, relief="groove", text=self.products[i][0],
                                              bg="light yellow"))
                    self.image_products.append(xuly_image(self.products[i][2], 70, 50))
                    label_image = Label(self.lf[count], image=self.image_products[count])
                    Label(self.lf[count], text=self.products[i][1], font=("Comic Sans MS", 12, "bold"),
                          fg="blue").grid(row=2, column=0, padx=10)
                    Label(self.lf[count], text=self.products[i][3], font=("Comic Sans MS", 12, "bold"),
                          fg="blue").grid(row=3, column=0, padx=10)
                    self.button_add.append(
                        Button(self.lf[count], command=lambda: self.buy_product(self.products[i]),
                               text="Add to Cart", font=("Comic Sans MS", 12, "bold"), fg="#F6F5EC", bg="#765341", relief=SOLID,))
                    if count >= a:
                        self.lf[count].grid(row=(count - a) // 4, column=(count - a) % 4, padx=10, pady=1)
                        label_image.grid(row=1, column=0, padx=10)
                        self.button_add[count].grid(row=4, column=0, padx=10)
                    if count >= a + 7:
                        return
                    count += 1
            except:
                continue

    def show_cart(self):
        self.HideAllFrame()
        for i in range(len(self.cart_list)):
            self.lf1.append(LabelFrame(self.products_frame, bd=2, relief="groove", bg="light yellow"))
            self.lf1[i].grid(row=i // 4, column=i % 4, padx=10, pady=1)
            Label(self.lf1[i], text=self.cart_list[i][1], font="arial 12 bold", fg="blue").grid(
                row=1, column=0, padx=10)
            self.image_products.append(xuly_image(self.cart_list[i][2], 70, 50))
            label_image = Label(self.lf1[i], image=self.image_products[i])
            label_image.grid(row=2, column=0, padx=10)
            Label(self.lf1[i], text=self.cart_list[i][3], font="arial 12 bold", fg="blue").grid(
                row=3, column=0, padx=10)
            Button(self.lf1[i], command=lambda: (self.lf1[i].destroy(), self.cart_list.pop(i)), text="Remove",
                   font="arial 12 bold", fg="blue", bg="light green").grid(row=4, column=0, padx=10)


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
