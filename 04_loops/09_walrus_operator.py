value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not Divisble by 5")

# if remainder = value % 5:
#     print(f"Not Divisble by 5")
# if (remainder = value % 5):
#     print(f"Not Divisble by 5")
# BOth the syntaxes are not allowed

if (remainder := value % 5):
    print("Not divisble by 5")


available_sizes = ['small','large','medium']

if (requested_size := input("Enter Cup size : ")) in available_sizes:
    print(f"Serving {requested_size} Chai")
else:
    print(f"Requested Size {requested_size} not available")

flavors = ['Ginger', 'Masala', 'Lemon']

print("Avaliable Flavors : ",flavors)

while (flavor := input("Choose your flavor : ")) not in flavors:
    print(f"Requested flavor {flavor} is not avaiable")

print(f"You chose {flavor} chai!")
