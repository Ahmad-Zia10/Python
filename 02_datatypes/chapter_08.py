ingredients = ["water", "milk", "oolong"]
ingredients.append("sugar")
print(f"Ingredients of chai are :{ingredients}")

ingredients.remove("water")
print(f"New ingredients : {ingredients}")

spice_options = ["ginger", "pineapple", "chia seeds"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai Ingredients : {chai_ingredients}")

chai_ingredients.insert(2,"black tea leaves")
print(f"Chai Ingredients : {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Popped element : {last_added}")

chai_ingredients.reverse()
print(f"Reversed List : {chai_ingredients}")

chai_ingredients.sort()
print(f"Sorted list : {chai_ingredients}")

milk_cups = [1,2,3]

print(f"Max item : {max(milk_cups)}")

print(f"Minimum Item in List : {min(milk_cups)}")



# bytes array.

raw_data = bytearray(b"Cardimom")
raw_data.remove(ord('a'))
print(f"Bytes : {raw_data}")