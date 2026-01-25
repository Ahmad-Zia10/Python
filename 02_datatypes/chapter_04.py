# Boolean 

is_boiling = True
stir_count  = 5
total_actions = stir_count + is_boiling # called upcasting

print(f"Total Actions : {total_actions}")

milk_stock = 0 # false in boolean
print(f"Is milk present in inventory : {bool(milk_stock)}")

water_hot = True
tea_added = True

can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")