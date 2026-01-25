chai_menu = {"masala" : 30, "ginger": 40}

try:
    chai_menu["lemon"]
except KeyError:
    print("The chai type is not on our menu")

print("End line of code after handling error")