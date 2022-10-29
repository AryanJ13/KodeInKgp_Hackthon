import sqlite3
from flask import Flask, request, jsonify
from user import User

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user", methods=["POST"])
def read_users() -> list[User]:
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    sqlite_select_query = """SELECT * from users"""
    cur.execute(sqlite_select_query)
    with app.app_context():
        return jsonify(cur.fetchall())

# @app.route("/user", methods=["POST"])
# def read_users() -> list[int]:

