sugar_amt = 2
print(f"Initial Sugar amount : {sugar_amt}")

sugar_amt = 12
# sugar_amt += 12 //Now sugar_amt points to a new memory location having 14 as value.
print(f"Sugar amount After addition of milk: {sugar_amt}")

print(f"Identity of sugar amount after milk addition : {id(14)}")
print(f"Identity of initial sugar amt : {id(2)}")


