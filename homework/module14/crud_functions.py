import sqlite3
from module_14_4 import  *


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

if __name__ == "__main__":

    initiate_db()
    # products = get_all_products()
    # for product in products:
    #     print(product[0], product[1], product[2], product[3])




