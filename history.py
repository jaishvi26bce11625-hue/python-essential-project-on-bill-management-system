import sqlite3


def get():

    con = sqlite3.connect("bills.db")
    cur = con.cursor()

    cur.execute("""
        SELECT id, name, phone, total, date
        FROM bills
        ORDER BY id DESC
    """)

    data = cur.fetchall()

    con.close()

    return data