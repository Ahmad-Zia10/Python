chai_order = dict(type='Masala Chai', size='Large', sugar=2)
print(f"Chai Order : {chai_order}")

chai_recipe = {} #declaring an empty dictionary
chai_recipe['base'] = 'black tea'
chai_recipe['liquid'] = 'milk'

print(f"Recipe base : {chai_recipe['base']}")
print(f"Recipe : {chai_recipe}")

del chai_recipe['liquid']

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}") #Order details (items): dict_items([('type', 'Ginger Chai'), ('size', 'Medium'), ('sugar', 1)]) The answer is an array and each item is a tuple.

last_element = chai_order.popitem()
print(f"LAst item  : {last_element}")

# chai_order.update(dict(cardamom="crushed")) - This is also correct.
chai_order.update([('cardamom', 'crushed')])
print(f"UPdated chai_order : {chai_order}")

customer_note = chai_order.get("customer_note", "NO Note")
print(f"customer_note is: {customer_note}")