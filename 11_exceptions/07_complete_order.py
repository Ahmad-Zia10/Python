class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala" : 30, "ginger" : 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("This Flavor is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be a number.")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups {flavor} chai: rupees {total}")
    except Exception as e: # we can all other exceptions with Exception class
        print("Error :", e)
    finally:
        print("Thank you for visiting Zia's!")

bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)