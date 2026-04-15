def process_order(item, quantity):
    try:
        price = {"masala":20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry we dont have this type of tea on our menu.")
    except TypeError:
        print("Quantity must be a number")
    
process_order("ginger", 20)
process_order("masala", 10) # if we pass "masala", "two" : we get "total cost is twotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwo" because of operator overloading.
