essential_spices = {'cardimom','ginger','cloves'}
optional_spices = {'cinnamon', 'ginger', 'black pepper'}

all_spices = essential_spices | optional_spices
print(f"All spices : {all_spices}")

common_spices = essential_spices & optional_spices 
print(f"Common spices : {common_spices}")

only_essential_spices = essential_spices - optional_spices 
print(f"Only Essential Spices : {only_essential_spices}")

