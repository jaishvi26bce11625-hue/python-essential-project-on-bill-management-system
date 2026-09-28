def calc(data):

    sub = 0

    for x in data:
        sub = sub + x["total"]

    gst = sub * 5 / 100
    total = sub + gst

    return sub, gst, total


def makebill(name, phone, data, sub, gst, total, date):

    text = ""

    text = text + "       BILL MANAGEMENT SYSTEM\n"
    text = text + "--------------------------------\n"
    text = text + "Customer: " + name + "\n"
    text = text + "Phone: " + phone + "\n"
    text = text + "Date: " + date + "\n"
    text = text + "--------------------------------\n"

    for x in data:

        text = text + x["item"]
        text = text + "  "
        text = text + str(x["qty"])
        text = text + "  "
        text = text + str(x["price"])
        text = text + "  "
        text = text + str(x["total"])
        text = text + "\n"

    text = text + "--------------------------------\n"
    text = text + "Subtotal: " + str(round(sub, 2)) + "\n"
    text = text + "GST 5%: " + str(round(gst, 2)) + "\n"
    text = text + "Total: " + str(round(total, 2)) + "\n"
    text = text + "--------------------------------\n"
    text = text + "Thank You!"

    return text