import sqlite3



# Sr. No, Stock name, Placer, Buyer, Qty, Price
def tradebook():
    con = sqlite3.connect("tradebook_buys.db")
    cur = con.cursor()

    cmd = "CREATE TABLE stock(id, placer, buyer, qty, price)"
    cur.execute(cmd)

    con = sqlite3.connect("tradebook_sells.db")
    cur = con.cursor()

    cmd = "CREATE TABLE stock(id, placer, seller, qty, price)"
    cur.execute(cmd)
