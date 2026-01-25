snack = input("Enter your choice of snack:").lower()

if snack == 'cookies' or snack == 'samosa':
    setback = 1
    print(f"Great choice!! We will have your order of {snack} ready in a few minutes.")
else:
    print("Sorry we only serve cookies and samosas")

# This shows that variable in python are function scoped. i.e if a variable is declared anywhere inside a
# funciton, it will live throughout the function.
print(f"Setcback : {setback}")