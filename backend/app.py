import sqlite3
import time
from unicodedata import name
from flask import Flask, request, jsonify
from data_structure import Book
import orders

app = Flask(__name__)
book = Book()


@app.route("/user", methods=["GET"])
def read_users():
    con = sqlite3.connect("../users.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * from users"""
    entries = cur.execute(sqlite_select_query).fetchall()
    with app.app_context():
        return [
            {
                "user_id": t[0],
                "balance": t[1],
                "quantity": t[2],
            }
            for t in entries
        ]


@app.route("/price", methods=["GET"])
def read_price():
    list = [0] * 1000
    con = sqlite3.connect("../tradebook.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * from stock"""
    entries = cur.execute(sqlite_select_query)
    for entry in entries:
        t = entry[5]
        t = time.time() - t
        t = int(t // 600)
        list[t] = entry[4]
    with app.app_context():
        return list


@app.route("/tradebook", methods=["GET"])
def read_tradebook() -> list[int]:
    con = sqlite3.connect("../tradebook.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * from stock"""
    entries = cur.execute(sqlite_select_query).fetchall()
    with app.app_context():
        return [
            {
                "order_id": t[0],
                "buyer": t[1],
                "seller": t[2],
                "qunatity": t[3],
                "price": t[4],
            }
            for t in entries
        ]


@app.route("/order", methods=["POST"])
def place_order() -> list[int]:
    user_id, qty, price, bos, mol = (
        request.args["user_id"],
        request.args["qty"],
        request.args["price"],
        request.args["bos"],
        request.args["mol"],
    )
    if bos == 1:
        if mol == 1:
            orders.buy_market(book, user_id, qty)
        else:
            orders.buy_limit(book, user_id, qty, price)
    else:
        if mol:
            orders.sell_market(book, user_id, qty)
        else:
            orders.sell_limit(book, user_id, qty, price)
