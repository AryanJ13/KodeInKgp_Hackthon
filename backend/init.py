import sqlite3


# Placer  Quantity    Price
# ~       ~           ~
# ~       ~           ~
# ~       ~           ~
def orderbooks():
    con = sqlite3.connect("orderbooks_buys.db")
    cur = con.cursor()

    cmd = "CREATE TABLE stock(placer, qty, price)"
    cur.execute(cmd)

    con = sqlite3.connect("orderbooks_sells.db")
    cur = con.cursor()
        
    cmd = "CREATE TABLE stock(placer, qty, price)"
    cur.execute(cmd)


# Sr. No, Stock name, Placer, Buyer, Qty, Price
def tradebook():
    con = sqlite3.connect("tradebook_buys.db")
    cur = con.cursor()

    cmd = "CREATE TABLE stock(id, placer, buyer, qty, price)"
    cur.execute(cmd)

    con = sqlite3.connect("tradebook_sells.db")
    cur = con.cursor()

    cmd = "CREATE TABLE stock(id, placer, buyer, qty, price)"
    cur.execute(cmd)
