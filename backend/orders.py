from random import randint
import sqlite3
from user import User
from data_structure import Book, Order


def generate_id() -> int:
    return generate_id()


def buy_market(book: Book, buyer: User, quantity: int):
    orders = Book.buy(Book, quantity)
    con = sqlite3.connect("tradebook_buys.db")
    cur = con.cursor()
    for order in orders:
        data = (
            "("
            + str(generate_id())
            + ","
            + order.placer.id
            + ","
            + buyer.id
            + ","
            + order.quantity
            + ","
            + order.price
            + ")"
        )
        sqlite_insert_query = (
            """INSERT INTO stock (id, placer, buyer, qty, price)
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


def sell_market(book: Book, seller: User, quantity: int):
    orders = book.sell(book, quantity)
    con = sqlite3.connect("tradebook_buys.db")
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
            + ")"
        )
        sqlite_insert_query = (
            """INSERT INTO stock (id, placer, seller, qty, price)
                                VALUES """
            + data
        )
        cur.execute(sqlite_insert_query)


def buy_limit(book: Book, buyer: str, order: Order, quantity: int, price: int):
    randId = generate_id()
    if price < book.lowestSell(book, book.sellTree):
        book.insert(Order(randId, True, price, quantity))
    else:
        buy_market(book, buyer, quantity)


def sell_limit(book: Book, buyer: str, order: Order, quantity: int, price: int):
    randId = generate_id()
    if price > book.LargestBuy(book, book.buyTree):
        book.insert(Order(randId, False, price, quantity))
    else:
        sell_market(book, buyer, quantity)
