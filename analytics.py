import sqlite3


def get():

    con = sqlite3.connect("bills.db")
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM bills")
    bills = cur.fetchone()[0]

    cur.execute("SELECT SUM(total) FROM bills")
    sales = cur.fetchone()[0]

    if sales is None:
        sales = 0

    cur.execute("""
        SELECT item, SUM(qty)
        FROM billitems
        GROUP BY item
        ORDER BY SUM(qty) DESC
        LIMIT 1
    """)

    x = cur.fetchone()

    if x is None:
        item = "None"
        qty = 0
    else:
        item = x[0]
        qty = x[1]

    con.close()

    return bills, sales, item, qty