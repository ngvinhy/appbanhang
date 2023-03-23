import sqlite3

# Kết nối tới cơ sở dữ liệu
conn = sqlite3.connect('products.db')
c = conn.cursor()

# Tạo bảng sản phẩm
c.execute('''CREATE TABLE IF NOT EXISTS products
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  Name TEXT NOT NULL,
                  Price REAL NOT NULL)''')

with open("product_image.jpg", "rb") as f:
    img_data = f.read()

# Thêm sản phẩm vào bảng
c.execute("INSERT INTO products (Name, Price) VALUES ('Laptop', 15000000)")
c.execute("INSERT INTO products (Name, Price) VALUES ('Điện thoại', 5000000)")
c.execute("INSERT INTO products (Name, Price) VALUES ('Màn hình', 3000000)")
c.execute("INSERT INTO products (Name, Price) VALUES ('Tai nghe', 1000000)")

# Lưu các thay đổi vào cơ sở dữ liệu
conn.commit()

# Đóng kết nối tới cơ sở dữ liệu
conn.close()
