import sqlite3


def create_table():
    conn = sqlite3.connect("hashes.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (file TEXT, hash TEXT)")
    conn.commit()
    conn.close()


def insert_data(file, hash_value):
    conn = sqlite3.connect("hashes.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?)", (file, hash_value))
    conn.commit()
    conn.close()


def view_data():
    conn = sqlite3.connect("hashes.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows
