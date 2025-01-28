import sqlite3
from module_14_5 import  *


def initiate_db():
    connection = sqlite3.connect("telegram.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)",
                       (i, f"Продукт {i}", f"Описание {i}", f" {i * 100}"))
    connection.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        );
        ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("telegram.db")
    cursor = connection.cursor()
    # productsAll = cursor.execute("SELECT * FROM Products")
    cursor.execute("SELECT id, title, description, price FROM Products")
    productsAll = cursor.fetchall()
    connection.commit()
    connection.close()
    return productsAll

def add_user(username, email, age, balance=1000):
    connection = sqlite3.connect("telegram.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
        (username, email, age, balance))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("telegram.db")
    cursor = connection.cursor()
    count = cursor.execute('SELECT COUNT(*) from Users WHERE username = ?',
                   (username,)).fetchone()[0]
    connection.close()

    return True \
        if count \
        else False
    
if __name__ == "__main__":
    pass
    # initiate_db()
    # products = get_all_products()
    # for product in products:
    #     print(product[0], product[1], product[2], product[3])




