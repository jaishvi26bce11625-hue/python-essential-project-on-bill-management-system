import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from customer import check
from products import items, price
from bill import calc, makebill
from database import save
from history import get
from analytics import get as stats


class App(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Bill Management System")
        self.geometry("850x650")

        self.data = []

        self.makegui()

    def makegui(self):

        tk.Label(
            self,
            text="Bill Management System",
            font=("Arial", 22, "bold")
        ).pack(pady=10)

        f1 = tk.Frame(self)
        f1.pack()

        tk.Label(
            f1,
            text="Customer Name"
        ).grid(row=0, column=0, padx=5)

        self.name = tk.Entry(f1, width=20)
        self.name.grid(row=0, column=1, padx=5)

        tk.Label(
            f1,
            text="Phone"
        ).grid(row=0, column=2, padx=5)

        self.phone = tk.Entry(f1, width=15)
        self.phone.grid(row=0, column=3, padx=5)

        f2 = tk.Frame(self)
        f2.pack(pady=15)

        tk.Label(
            f2,
            text="Product"
        ).grid(row=0, column=0, padx=5)

        self.item = ttk.Combobox(
            f2,
            values=items(),
            state="readonly",
            width=15
        )
        self.item.grid(row=0, column=1, padx=5)

        tk.Label(
            f2,
            text="Quantity"
        ).grid(row=0, column=2, padx=5)

        self.qty = tk.Entry(f2, width=10)
        self.qty.grid(row=0, column=3, padx=5)

        tk.Button(
            f2,
            text="Add Product",
            command=self.add
        ).grid(row=0, column=4, padx=10)

        self.list = tk.Listbox(
            self,
            width=80,
            height=8
        )
        self.list.pack(pady=10)

        f3 = tk.Frame(self)
        f3.pack()

        tk.Button(
            f3,
            text="Generate Bill",
            width=15,
            command=self.bill
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            f3,
            text="Clear",
            width=15,
            command=self.clear
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            f3,
            text="History",
            width=15,
            command=self.history
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            f3,
            text="Analytics",
            width=15,
            command=self.analytics
        ).grid(row=0, column=3, padx=5)

        self.text = tk.Text(
            self,
            width=80,
            height=15
        )
        self.text.pack(pady=10)

    def add(self):

        item = self.item.get()
        q = self.qty.get()

        if item == "":
            messagebox.showerror(
                "Error",
                "Select a product"
            )
            return

        if not q.isdigit():
            messagebox.showerror(
                "Error",
                "Enter a valid quantity"
            )
            return

        q = int(q)

        if q <= 0:
            messagebox.showerror(
                "Error",
                "Quantity must be greater than 0"
            )
            return

        p = price(item)
        total = p * q

        x = {
            "item": item,
            "qty": q,
            "price": p,
            "total": total
        }

        self.data.append(x)

        self.list.insert(
            tk.END,
            item + "   " +
            str(q) + "   " +
            str(p) + "   " +
            str(total)
        )

        self.item.set("")
        self.qty.delete(0, tk.END)

    def bill(self):

        name = self.name.get()
        phone = self.phone.get()

        ok, msg = check(name, phone)

        if not ok:
            messagebox.showerror(
                "Error",
                msg
            )
            return

        if len(self.data) == 0:
            messagebox.showerror(
                "Error",
                "Add at least one product"
            )
            return

        sub, gst, total = calc(self.data)

        date = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        text = makebill(
            name,
            phone,
            self.data,
            sub,
            gst,
            total,
            date
        )

        self.text.delete(
            "1.0",
            tk.END
        )

        self.text.insert(
            tk.END,
            text
        )

        save(
            name,
            phone,
            self.data,
            sub,
            gst,
            total,
            date
        )

        messagebox.showinfo(
            "Success",
            "Bill generated"
        )

    def clear(self):

        self.name.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.item.set("")
        self.qty.delete(0, tk.END)

        self.list.delete(
            0,
            tk.END
        )

        self.text.delete(
            "1.0",
            tk.END
        )

        self.data = []

    def history(self):

        data = get()

        win = tk.Toplevel(self)
        win.title("Bill History")
        win.geometry("650x400")

        text = tk.Text(
            win,
            width=75,
            height=20
        )
        text.pack(padx=10, pady=10)

        if len(data) == 0:

            text.insert(
                tk.END,
                "No bills found"
            )

            return

        for x in data:

            text.insert(
                tk.END,
                "Bill ID: " + str(x[0]) + "\n"
            )

            text.insert(
                tk.END,
                "Name: " + str(x[1]) + "\n"
            )

            text.insert(
                tk.END,
                "Phone: " + str(x[2]) + "\n"
            )

            text.insert(
                tk.END,
                "Total: Rs. " + str(x[3]) + "\n"
            )

            text.insert(
                tk.END,
                "Date: " + str(x[4]) + "\n"
            )

            text.insert(
                tk.END,
                "-----------------------------\n"
            )

    def analytics(self):

        bills, sales, item, qty = stats()

        msg = (
            "Total Bills: " + str(bills) + "\n"
            "Total Sales: Rs. " + str(round(sales, 2)) + "\n"
            "Top Product: " + item + "\n"
            "Quantity Sold: " + str(qty)
        )

        messagebox.showinfo(
            "Analytics",
            msg
        )