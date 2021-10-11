import re


def convert_price(price):
    if price != 'NA':
        if bool(re.search('[a-zA-Z]', price)):
            return int(float(price.split()[0]) * 100000)
        return re.sub(r'[^\d.]', '', price)
    return price


def cleanup_record(row):
    brand = row[0]
    model = row[1].split()[0]
    engine = row[2].split()[0]
    price = convert_price(row[3])
    kilometers = row[4].split()[0]
    location = row[5]
    return [brand, model, engine, price, kilometers, location]


