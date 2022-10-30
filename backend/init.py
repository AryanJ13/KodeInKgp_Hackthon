import os
from random import randint
import sqlite3
import time
from data_structure import Order

from user import User


# Sr. No, Stock name, Placer, Buyer, Qty, Price
def tradebook():
    con = sqlite3.connect("tradebook.db")
    cur = con.cursor()

    cmd = "CREATE TABLE stock(id, buyer, seller, qty, price, time)"
    cur.execute(cmd)
    u = [User(1), User(2), User(3)]
    sqlite_insert_query = """INSERT INTO stock(id, buyer, seller, qty, price, time)
VALUES (?,?,?,?,?,?);"""
    # prices, qty, times, buyer = [], [], [], []
    for i in range(100):
        data = (
            i + 1,
            randint(0, 3),
            randint(0, 3),
            randint(0, 20),
            randint(100, 150),
            time.time() - 600 * i,
        )
        cur.execute(sqlite_insert_query, data)
    con.commit()


def users():

    con = sqlite3.connect("users.db")
    cur = con.cursor()

    cmd = "CREATE TABLE users (id, balance, qty)"
    cur.execute(cmd)
    sqlite_insert_query = """INSERT INTO users (id, balance, qty)
VALUES (?,?,?);"""
    for i in range(5):
        user = User(i + 1)
        user.change_balance(500)
        data = (user.id, user.balance, user.qty)
        cur.execute(sqlite_insert_query, data)
    con.commit()


if __name__ == "__main__":
    os.remove("users.db")
    os.remove("tradebook.db")
    users()
    tradebook()
