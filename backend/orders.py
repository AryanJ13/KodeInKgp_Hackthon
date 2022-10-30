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
def buy_market(book: Book, buyer: int, quantity: int,price: int):
    if book.sellTree==None:
        book.insert(Order(generate_id(),True,price,quantity,buyer,time.time()))
    else:
        orders = book.buy(quantity)
        con = sqlite3.connect("tradebook.db")
        cur = con.cursor()
        for order in orders:
            data = (
                "("
                + str(generate_id())
                + ","
                + buyer.id
                + ","
                + order.placer.id
                + ","
                + order.quantity
                + ","
                + order.price
                + ","
                + order.time
                + ")"
            )
            sqlite_insert_query = (
                """INSERT INTO stock(id, buyer, seller, qty, price, time)
                                    VALUES """
                + data
            )
            cur.execute(sqlite_insert_query)

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


def sell_market(book: Book, seller: int, quantity: int,price: int):
    if book.buyTree==None:
        book.insert(Order(generate_id(),True,price,quantity,seller,time.time()))
    else:
        orders = book.sell(quantity)
        con = sqlite3.connect("tradebook.db")
        cur = con.cursor()
        for order in orders:
            data = (
                "("
                + str(generate_id())
                + ","
                + order.placer.id
                + ","
                + seller.id
                + ","
                + order.quantity
                + ","
                + order.price
                + ","
                + order.time
                + ")"
            )
            sqlite_insert_query = (
                """INSERT INTO stock(id, buyer, seller, qty, price, time)
                                    VALUES """
                + data
            )
            cur.execute(sqlite_insert_query)

def buy_limit(book: Book, buyer: int, quantity: int, price: int):
    randId = generate_id()
    if price <= book.lowestSell(book, book.sellTree):
        book.insert(Order(randId, True, price, quantity))
        with open("orders.txt", "a") as f:
            f.write("buy order matched\n")
            f.flush()
    else:
        buy_market(book, buyer, quantity)
        with open("orders.txt", "a") as f:
            f.write("buy order pushed to book\n")
            f.flush()


def sell_limit(book: Book, buyer: int, quantity: int, price: int):
    randId = generate_id()
    if price >= book.LargestBuy(book, book.buyTree):
        book.insert(Order(randId, False, price, quantity))
        with open("orders.txt", "a") as f:
            f.write("sell order matched\n")
            f.flush()
    else:
        sell_market(book, buyer, quantity)
        with open("orders.txt", "a") as f:
            f.write("sell order pushed to book\n")
            f.flush()


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_buy_limit(self):
        book = Book()
        # o1, o2, o3 = [
        #     Order(1, True, 110, 10, user, time.time()),
        #     Order(2, True, 120, 10, user, time.time()),
        #     Order(3, True, 110, 10, user, time.time()),
        # ]
        # l1, l2, l3 = [Limit(o1), Limit(o2), Limit(o3)]
        buy_limit(book, 1, 10, 100)
        buy_limit(book, 1, 10, 110)


if __name__ == "__main__":
    unittest.main()
