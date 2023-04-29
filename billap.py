from tkinter import *
import random


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x730")
        self.root.resizable(width=False, height=False)
        self.root.title("Billing System - TECH HUB SHOP")
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        # For Generating Random Bill Numbers
        x = random.randint(10000, 99999)
        self.c_bill_no = StringVar()
        # Seting Value to variable
        self.c_bill_no.set(str(x))

        self.codeF001 = IntVar()
        self.codeF002 = IntVar()
        self.codeF003 = IntVar()
        self.codeF004 = IntVar()
        self.codeF005 = IntVar()
        self.codeB001 = IntVar()
        self.codeB002 = IntVar()
        self.codeB003 = IntVar()
        self.codeB004 = IntVar()
        self.codeB005 = IntVar()
        self.codeM001 = IntVar()
        self.codeM002 = IntVar()
        self.codeM003 = IntVar()
        self.codeM004 = IntVar()
        self.codeM005 = IntVar()
        self.total_face = StringVar()
        self.total_body = StringVar()
        self.total_other = StringVar()
        self.tax_face = StringVar()
        self.tax_body = StringVar()
        self.tax_other = StringVar()

        # ===================================
        bg_color = "pink"
        fg_color = "white"
        lbl_color = 'black'
        # Title of App
        title = Label(self.root, text="Billing System - TECH HUB SHOP", bd=12, relief=GROOVE, fg="Black", bg=bg_color,
                      font=("times new roman", 25, "bold"), pady=3).pack(fill=X)

        # ==========Customers Frame==========#
        F1 = LabelFrame(text="Customer Details", font=("times new roman", 12, "bold"), fg="Black", bg=bg_color,
                        relief=GROOVE, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        # ===============Customer Name===========#
        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="Black", font=("times new roman", 15, "bold")).grid(
            row=0, column=0, padx=10, pady=5)
        cname_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        # =================Customer Phone==============#
        cphon_lbl = Label(F1, text="Phone No", bg=bg_color, fg="Black", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20)
        cphon_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_phone)
        cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # ====================Customer Bill No==================#
        cbill_lbl = Label(F1, text="Bill No.", bg=bg_color, fg="Black", font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20)
        cbill_en = Entry(F1, bd=8, relief=GROOVE, textvariable=self.c_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # ==================Face Frame=====================#
        F2 = LabelFrame(self.root, text='FACE', bd=10, relief=GROOVE, bg=bg_color, fg="BLACK",
                        font=("times new roman", 13, "bold"))
        F2.place(x=5, y=180, width=325, height=380)

        # =======
        bath_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: F001")
        bath_lbl.grid(row=0, column=0, padx=10, pady=20)
        bath_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeF001)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        face_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: F002")
        face_lbl.grid(row=1, column=0, padx=10, pady=20)
        face_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeF002)
        face_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        wash_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: F003")
        wash_lbl.grid(row=2, column=0, padx=10, pady=20)
        wash_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeF003)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # =======
        hair_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: F004")
        hair_lbl.grid(row=3, column=0, padx=10, pady=20)
        hair_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeF004)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ==========
        lot_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: F005")
        lot_lbl.grid(row=4, column=0, padx=10, pady=20)
        lot_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeF005)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ===================================#
        F2 = LabelFrame(self.root, text='BODY', bd=10, relief=GROOVE, bg=bg_color, fg="BLACK",
                        font=("times new roman", 13, "bold"))
        F2.place(x=330, y=180, width=325, height=380)

        # ===========Frame Content
        rice_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: B001")
        rice_lbl.grid(row=0, column=0, padx=10, pady=20)
        rice_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeB001)
        rice_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        oil_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: B002")
        oil_lbl.grid(row=1, column=0, padx=10, pady=20)
        oil_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeB002)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        daal_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: B003")
        daal_lbl.grid(row=2, column=0, padx=10, pady=20)
        daal_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeB003)
        daal_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========
        wheat_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: B004")
        wheat_lbl.grid(row=3, column=0, padx=10, pady=20)
        wheat_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeB004)
        wheat_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============
        sugar_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: B005")
        sugar_lbl.grid(row=4, column=0, padx=10, pady=20)
        sugar_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeB005)
        sugar_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ==================Other=====================#

        F2 = LabelFrame(self.root, text='OTHERS', bd=10, relief=GROOVE, bg=bg_color, fg="BLACK",
                        font=("times new roman", 13, "bold"))
        F2.place(x=655, y=180, width=325, height=380)

        # ===========Frame Content
        maza_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: M001")
        maza_lbl.grid(row=0, column=0, padx=10, pady=20)
        maza_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeM001)
        maza_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        cock_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: M002")
        cock_lbl.grid(row=1, column=0, padx=10, pady=20)
        cock_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeM002)
        cock_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # =======
        frooti_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: M003")
        frooti_lbl.grid(row=2, column=0, padx=10, pady=20)
        frooti_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeM003)
        frooti_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ========
        cold_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: M004")
        cold_lbl.grid(row=3, column=0, padx=10, pady=20)
        cold_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeM004)
        cold_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ============
        bis_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Code: M005")
        bis_lbl.grid(row=4, column=0, padx=10, pady=20)
        bis_en = Entry(F2, bd=8, relief=GROOVE, textvariable=self.codeM005)
        bis_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ===================Bill Aera================#
        F3 = Label(self.root, bd=10, relief=GROOVE)
        F3.place(x=960, y=180, width=325, height=380)
        # ===========
        bill_title = Label(F3, text="Bill List", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        # ============
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ===========Buttons Frame=============#
        F4 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="Black",
                        font=("times new roman", 13, "bold"))
        F4.place(x=0, y=560, relwidth=1, height=160)

        # ===================
        cosm_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total - FACE")
        cosm_lbl.grid(row=0, column=0, padx=10, pady=0)
        cosm_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_face)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        # ===================
        gro_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total - BODY")
        gro_lbl.grid(row=1, column=0, padx=10, pady=5)
        gro_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_body)
        gro_en.grid(row=1, column=1, ipady=2, ipadx=5)

        # ================
        oth_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total - OTHERS")
        oth_lbl.grid(row=2, column=0, padx=10, pady=5)
        oth_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.total_other)
        oth_en.grid(row=2, column=1, ipady=2, ipadx=5)

        # ================
        cosmt_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="FACE - Tax")
        cosmt_lbl.grid(row=0, column=2, padx=30, pady=0)
        cosmt_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_face)
        cosmt_en.grid(row=0, column=3, ipady=2, ipadx=5)

        # =================
        grot_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="BODY - Tax")
        grot_lbl.grid(row=1, column=2, padx=30, pady=5)
        grot_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_body)
        grot_en.grid(row=1, column=3, ipady=2, ipadx=5)

        # ==================
        otht_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="OTHERS - Tax")
        otht_lbl.grid(row=2, column=2, padx=10, pady=5)
        otht_en = Entry(F4, bd=8, relief=GROOVE, textvariable=self.tax_other)
        otht_en.grid(row=2, column=3, ipady=2, ipadx=5)

        # ====================
        total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.total)
        total_btn.grid(row=1, column=4, ipadx=20, padx=30)

        # ========================
        genbill_btn = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=self.bill_area)
        genbill_btn.grid(row=1, column=5, ipadx=20)

        # ====================
        clear_btn = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                           command=self.clear)
        clear_btn.grid(row=1, column=6, ipadx=20, padx=30)

        # ======================
        exit_btn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=GROOVE,
                          command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=20)

    # Function to get total prices
    def total(self):
        # =================Total FACE Prices
        self.total_face_prices = (
                (self.codeF001.get() * 180000) +
                (self.codeF002.get() * 225000) +
                (self.codeF003.get() * 328000) +
                (self.codeF004.get() * 356000) +
                (self.codeF005.get() * 770000)
        )
        self.total_face.set(str(self.total_face_prices) + " VND")
        self.tax_face.set(str(round(self.total_face_prices * 0.05)) + " VND")
        # ====================Total BODY Prices
        self.total_body_prices = (
                (self.codeB001.get() * 235000) +
                (self.codeB002.get() * 245000) +
                (self.codeB003.get() * 399000) +
                (self.codeB004.get() * 146000) +
                (self.codeB005.get() * 92000)

        )
        self.total_body.set(str(self.total_body_prices) + " VND")
        self.tax_body.set(str(round(self.total_body_prices * 0.05)) + " VND")
        # ======================Total Other Prices
        self.total_other_prices = (
                (self.codeM001.get() * 320000) +
                (self.codeM002.get() * 360000) +
                (self.codeM003.get() * 275000) +
                (self.codeM004.get() * 175000) +
                (self.codeM005.get() * 700000)
        )
        self.total_other.set(str(self.total_other_prices) + " VND")
        self.tax_other.set(str(round(self.total_other_prices * 0.05)) + " VND")

    # Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "     Welcome To TECH HUB SHOP \n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty     Price")
        self.txt.insert(END, "\n===================================")

    # Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0', END)

    # Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.codeF001.get() != 0:
            self.txt.insert(END, f"\nCode: F001        {self.codeF001.get()}      {self.codeF001.get() * 180000}")
        if self.codeF002.get() != 0:
            self.txt.insert(END, f"\nCode: F002        {self.codeF002.get()}      {self.codeF002.get() * 225000}")
        if self.codeF003.get() != 0:
            self.txt.insert(END, f"\nCode: F003        {self.codeF003.get()}      {self.codeF003.get() * 328000}")
        if self.codeF004.get() != 0:
            self.txt.insert(END, f"\nCode: F004        {self.codeF004.get()}      {self.codeF004.get() * 256000}")
        if self.codeF005.get() != 0:
            self.txt.insert(END, f"\nCode: F005        {self.codeF005.get()}      {self.codeF005.get() * 770000}")
        if self.codeB001.get() != 0:
            self.txt.insert(END, f"\nCode: B001        {self.codeB001.get()}      {self.codeB001.get() * 235000}")
        if self.codeB002.get() != 0:
            self.txt.insert(END, f"\nCode: B002        {self.codeB002.get()}      {self.codeB002.get() * 245000}")
        if self.codeB003.get() != 0:
            self.txt.insert(END, f"\nCode: B003        {self.codeB003.get()}      {self.codeB003.get() * 399000}")
        if self.codeB004.get() != 0:
            self.txt.insert(END, f"\nCode: B004        {self.codeB004.get()}      {self.codeB004.get() * 146000}")
        if self.codeB005.get() != 0:
            self.txt.insert(END, f"\nCode: B005        {self.codeB005.get()}      {self.codeB005.get() * 92000}")
        if self.codeM001.get() != 0:
            self.txt.insert(END, f"\nCode: M001        {self.codeM001.get()}      {self.codeM001.get() * 320000}")
        if self.codeM002.get() != 0:
            self.txt.insert(END, f"\nCode: M002        {self.codeM002.get()}      {self.codeM002.get() * 360000}")
        if self.codeM003.get() != 0:
            self.txt.insert(END, f"\nCode: M003        {self.codeM003.get()}      {self.codeM003.get() * 275000}")
        if self.codeM004.get() != 0:
            self.txt.insert(END, f"\nCode: M004        {self.codeM004.get()}      {self.codeM004.get() * 175000}")
        if self.codeM005.get() != 0:
            self.txt.insert(END, f"\nCode: M005        {self.codeM005.get()}      {self.codeM005.get() * 700000}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n         Tax (5%) : {self.total_face_prices * 0.05 + self.total_body_prices * 0.05 + self.total_other_prices * 0.05} VND")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n            Total : {self.total_face_prices + self.total_body_prices + self.total_other_prices + self.total_face_prices * 0.05 + self.total_body_prices * 0.05 + self.total_other_prices * 0.05} VND")

    def exit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.mainloop()
