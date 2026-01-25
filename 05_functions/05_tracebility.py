# tracebility

def calculate_vat(price, vat_rate):
    return price + price*(vat_rate/100)


orders = [100, 150, 200]

for price in orders:
    final_price = calculate_vat(price, 18)
    print(f"Original Price : {price}, Price After Tax : {final_price}")