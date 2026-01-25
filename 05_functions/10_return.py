def make_chai():
    # return "Heres your chai!!"
    print("Heres your Chai!!")

print(make_chai()) #prints None

def sold_cups():
    return 120

print(sold_cups())

def chai_status(cups_left):
    if cups_left == 0:
        return "We are out of Chai!!"
    return "Heres your Chai!!"#early return rxample
    print("Bla Bla Bla")

print(chai_status(0))
print(chai_status(5))

def report():
    return 100,120,10

# sold, left, _ = report() -- If I only want two value and dont really need the third, we can extract like this
sold, left, expired = report() 
print(f"Sold cups : {sold}, remianing cups : {left}")