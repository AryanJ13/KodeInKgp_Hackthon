import sqlite3


con = sqlite3.connect("orderbooks.db")
cur = con.cursor()
columns = [str(v) for v in range(10)]
rows = "Price, "

