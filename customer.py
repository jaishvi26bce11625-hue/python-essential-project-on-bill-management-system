def check(name, phone):

    if name == "":
        return False, "Enter customer name"

    if phone == "":
        return False, "Enter phone number"

    if not phone.isdigit():
        return False, "Phone number must contain numbers only"

    if len(phone) != 10:
        return False, "Phone number must be 10 digits"

    return True, ""