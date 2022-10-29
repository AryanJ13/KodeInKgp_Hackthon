import os
import sqlite3

from user import User


# Sr. No, Stock name, Placer, Buyer, Qty, Price
def tradebook():
    con = sqlite3.connect("tradebook.db")
    cur = con.cursor()

    cmd = "CREATE TABLE stock(id, buyer, seller, qty, price, time)"
    cur.execute(cmd)


def users():

    con = sqlite3.connect("users.db")
    cur = con.cursor()

    cmd = "CREATE TABLE users (id, balance, qty)"
    cur.execute(cmd)
    sqlite_insert_query = """INSERT INTO users (id, balance, qty)
VALUES (?,?,?);"""
    for i in range(5):
        user = User(i + 1)
        data = (user.id, user.balance, user.qty)
        cur.execute(sqlite_insert_query, data)
    con.commit()


if __name__ == "__main__":
    os.remove("users.db")
    os.remove("tradebook.db")
    users()
    tradebook()
