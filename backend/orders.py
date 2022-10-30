from random import randint
import sqlite3
import time
import unittest
import time
from data_structure import Book, Limit, Order
from user import User


def generate_id() -> int:
    return randint(1, 10_000_000)


# cmd = "CREATE TABLE stock(id, buyer, seller, qty, price, time)"
def buy_market(book: Book, buyer: int, quantity: int, price: int):
    if book.sellTree == None:
        book.insert(Order(generate_id(), True, price, quantity, buyer, time.time()))
    else:
        orders = book.buy(quantity)
        con = sqlite3.connect("../tradebook.db")
        cur = con.cursor()
        sqlite_insert_query = """INSERT INTO stock(id, buyer, seller, qty, price, time)
VALUES (?,?,?,?,?,?);"""
        for order in orders:
            data = (
                generate_id(),
                buyer,
                order.placer,
                order.quantity,
                order.price,
                order.time,
            )
            cur.execute(sqlite_insert_query, data)
        con.commit()

    # con = sqlite3.connect('orderbooks_buys.db')
    # cur = con.cursor()

    # sqlite_select_query = """SELECT 0 from stock"""
    # cur.execute(sqlite_select_query)
    # record = cur.fetchall()

    # #Placer Qty Price
    # change_qty(record[0], record[1])
    # change_balance(record[0], record[2])

    # data_tuple = (id, record[0], buye , record[1], record[2])
    # cursor.execute(sqlite_insert_query, data_tuple)
    # con.commit()
    pass


def sell_market(book: Book, seller: int, quantity: int, price: int):
    if book.buyTree == None:
        book.insert(Order(generate_id(), True, price, quantity, seller, time.time()))
    else:
        orders = book.sell(quantity)
        con = sqlite3.connect("../tradebook.db")
        cur = con.cursor()
        sqlite_insert_query = """INSERT INTO stock(id, buyer, seller, qty, price, time)
VALUES (?,?,?,?,?,?);"""
        for order in orders:
            data = (
                generate_id(),
                order.placer,
                seller,
                order.quantity,
                order.price,
                order.time,
            )
            cur.execute(sqlite_insert_query, data)
        con.commit()


def buy_limit(book: Book, buyer: int, quantity: int, price: int):
    randId = generate_id()
    if book.sellTree != None:
        book.get_lowestSell(book.buyTree)
    if book.sellTree == None or price < book.lowestSell.limitPrice:
        book.insert(Order(generate_id(), True, price, quantity, buyer, time.time()))
        with open("orders.log", "a") as f:
            f.write("limit buy order pushed to book\n")
            f.flush()
    else:
        buy_market(book, buyer, quantity, price)
        with open("orders.log", "a") as f:
            f.write("limit buy order matched\n")
            f.flush()


def sell_limit(book: Book, buyer: int, quantity: int, price: int):
    randId = generate_id()
    if book.buyTree != None:
        book.get_highestBuy(book.buyTree)
    if book.buyTree == None or price > book.highestBuy.limitPrice:
        book.insert(Order(randId, False, price, quantity, buyer, time.time()))
        with open("orders.log", "a") as f:
            f.write("limit sell order pushed to book\n")
            f.flush()
    else:
        sell_market(book, buyer, quantity, price)
        with open("orders.log", "a") as f:
            f.write("limit sell order matched\n")
            f.flush()


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_buy_limit(self):
        book = Book()
        buy_limit(book, 1, 10, 100)
        buy_limit(book, 1, 10, 110)


if __name__ == "__main__":
    unittest.main()
