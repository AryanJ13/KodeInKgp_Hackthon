import sqlite3



# Sr. No, Stock name, Placer, Buyer, Qty, Price
def tradebook():
    con = sqlite3.connect("tradebook.db")
    cur = con.cursor()

    cmd = "CREATE TABLE stock(id, buyer, seller, qty, price, time)"
    cur.execute(cmd)


def users():
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    cmd = "CREATE TABLE users(id, balance, qty)"
    cur.execute(cmd)
    for i in range(5):
        sqlite_insert_query = (
            """INSERT INTO users(id, balance, qty)
                                VALUES """
            + data
        )
        cur.execute(sqlite_insert_query)