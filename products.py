products = {
    "Rice": 60,
    "Wheat": 50,
    "Milk": 30,
    "Bread": 40,
    "Biscuits": 20,
    "Juice": 50
}


def price(item):
    return products[item]


def items():
    return list(products.keys())