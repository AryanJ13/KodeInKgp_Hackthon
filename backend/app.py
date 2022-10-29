import sqlite3
import time
from unicodedata import name
from flask import Flask, request, jsonify
from user import User

app = Flask(__name__)


@app.route("/user", methods=["GET"])
def read_users():
    con = sqlite3.connect("../users.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * from users"""
    cur.execute(sqlite_select_query)
    with app.app_context():
        return jsonify(cur.fetchall())


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


if __name__ == "__main__":
    read_price()
