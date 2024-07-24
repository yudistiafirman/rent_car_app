import re

def get_card_type(card_number):
    card_number = card_number.replace(" ", "")  # Remove any spaces
    
    if re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", card_number):
        return "Visa"
    elif re.match(r"^5[1-5][0-9]{14}$", card_number):
        return "MasterCard"
    else:
        return "Unknown"