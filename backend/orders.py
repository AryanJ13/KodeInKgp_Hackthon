# Buy or Sell
import sqlite3

def buy_market(stock: str):
    con = sqlite3.connect("orderbooks_sells.db")
    cur = con.cursor()