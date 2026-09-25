import uuid

def get_price(flight_type):

    prices = {
        "Economy": 25000,
        "Business": 35000,
        "FirstClass": 50000
    }

    return prices.get(flight_type)