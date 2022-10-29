import sqlite3
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
def read_price() -> list[int]:
    list = [0] * 1000
    con = sqlite3.connect("../tradebook.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * from stock"""
    entries = cur.execute(sqlite_select_query)
    for entry in entries:
        time = entry[5]
        time = time.time() - time
        time /= 600
        list[time] = entry[4]
    with app.app_context():
        return jsonify(list)