masala_spices = ("Cardimom", "Cloves", "Cinnamon")
# (spice1, spice2) = masala_spices //Gives error : ValueError: too many values to unpack (expected 2, got 3)
# (spice1, spice2, spice3, spice4) = masala_spices //ValueError: not enough values to unpack (expected 4, got 3)
(spice1, spice2, spice3) = masala_spices 
 

print(f"Main masala spices : {spice1}, {spice2}, {spice3}")

ginger_ration, cardimom_ratio, clove_ratio = 2, 1, 3 #We can assign value to multiple variables. This infact is internally implementated using tuples

print(f"Ginger , cardimom and clove ratio : {ginger_ration} : {cardimom_ratio} : {clove_ratio}")

ginger_ration, cardimom_ratio = cardimom_ratio, ginger_ration #swap variable without using temp variable.  The references to the object that the variable points to is changed.The variables changed which objects they reference
print(f"Ginger , cardimom and clove ratio : {ginger_ration} : {cardimom_ratio} : {clove_ratio}")

# membership

print(f"Is the given word Cinnamon in tuple? {"cinnamon" in masala_spices}")

