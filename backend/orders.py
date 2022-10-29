from random import randint
import sqlite3
import user
from data_structure import Book,Order
def buy_market(book: Book, buyer: str, quantity: int):
    Book.buy(Book,quantity)

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
    pass


def sell_market(book: Book, stock :str,quantity: int):
    con = sqlite3.connect('orderbooks_sells.db')
    cur = con.cursor()
    book.sell(book,quantity)

def buy_limit(book :Book, buyer :str, order : Order ,quantity: int, price: int):
    con = sqlite3.connect('orderbooks_buys.db')
    cur = con.cursor()

    sqlite_select_query = """SELECT 0 from stock"""
    cur.execute(sqlite_select_query)
    record = cur.fetchall()

    randId=randint(1,1000000)
    if(price<book.lowestSell(book,book.sellTree)):
        book.insert(Order(randId,True,price,quantity))
    else:
        buy_market(book,buyer,quantity) 
def sell_limit(book :Book, buyer :str, order : Order ,quantity: int, price: int):
    con = sqlite3.connect('orderbooks_buys.db')
    cur = con.cursor()

    sqlite_select_query = """SELECT 0 from stock"""
    cur.execute(sqlite_select_query)
    record = cur.fetchall()

    randId=randint(1,1000000)
    if(price>book.LargestBuy(book,book.buyTree)):
        book.insert(Order(randId,True,price,quantity))
    else:
        sell_market(book,buyer,quantity) 
