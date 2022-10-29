import sqlite3
import user

def buy_market(book: B, buye: str):
    # con = sqlite3.connect('orderbooks_buys.db')
    # cur = con.cursor()

    # sqlite_select_query = """SELECT 0 from stock"""
    # cur.execute(sqlite_select_query)
    # record = cur.fetchall()

    # #Placer Qty Price
    # change_qty(record[0], record[1])
    # change_balance(record[0], record[2])

    # con = sqlite3.connect('tradebook_buys.db')
    # sqlite_insert_query = """INSERT INTO stock (id, placer, buyer, qty, price)
    #                         VALUES
    #                         (?,?,?,?,?) """

    # data_tuple = (id, record[0], buye , record[1], record[2])
    # cursor.execute(sqlite_insert_query, data_tuple)  
    # con.commit()
    paas


def sell_market(stock :str):
    con = sqlite3.connect('orderbooks_sells.db')
    cur = con.cursor()


def buy_limit(book :B, buye :str, order : Order ):
    con = sqlite3.connect('orderbooks_buys.db')
    cur = con.cursor()

    sqlite_select_query = """SELECT 0 from stock"""
    cur.execute(sqlite_select_query)
    record = cur.fetchall()

    if()