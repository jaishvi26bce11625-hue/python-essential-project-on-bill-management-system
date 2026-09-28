import sqlite3


def create():

    con = sqlite3.connect("bills.db")
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            sub REAL,
            gst REAL,
            total REAL,
            date TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS billitems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            billid INTEGER,
            item TEXT,
            qty INTEGER,
            price REAL,
            total REAL
        )
    """)

    con.commit()
    con.close()


def save(name, phone, data, sub, gst, total, date):

    con = sqlite3.connect("bills.db")
    cur = con.cursor()

    cur.execute("""
        INSERT INTO bills
        (name, phone, sub, gst, total, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, phone, sub, gst, total, date))

    billid = cur.lastrowid

    for x in data:

        cur.execute("""
            INSERT INTO billitems
            (billid, item, qty, price, total)
            VALUES (?, ?, ?, ?, ?)
        """, (
            billid,
            x["item"],
            x["qty"],
            x["price"],
            x["total"]
        ))

    con.commit()
    con.close()