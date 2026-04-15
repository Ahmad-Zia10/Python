def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

menu = full_menu()
print(next(menu)) # Masala Chai
print(next(menu)) # Ginger Chai
print(next(menu)) # Matcha 
print(next(menu)) # Oolong

import sys

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
            print(f"Processing: {order}")
    except GeneratorExit:
        print("Generator closed by GC!")
    except Exception as e:
        print(f"Other exception: {e}")

# Test 1: Explicit close
stall = chai_stall()
next(stall)
print(stall.send("Masala Chai"))
stall.close()  # Explicit close
# Output: Generator closed by GC!

# Test 2: Let GC handle it
stall2 = chai_stall()
next(stall2)
print(stall2.send("Masala Chai"))
# When stall2 goes out of scope/del, GC will close it