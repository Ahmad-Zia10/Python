class Laptop:
    RAM = "8 GB"
    type = "Business"

gaming_laptop = Laptop()
gaming_laptop.RAM = "16 GB"
gaming_laptop.GPU = "AMD Radeon"
print(f"Gaming laptop has RAM : {gaming_laptop.RAM}")
print(f"Laptop Class property 'RAM' has default value : {Laptop.RAM}")
print(f"Gaming Laptop Object has GPU : {gaming_laptop.GPU}")

del gaming_laptop.RAM
print(f"After deleting RAM property of object gaming_laptop : {gaming_laptop.RAM}") # Since the property RAM also exist in the class from which the gaming_laptop is derived, therefore it fallsback to that value of '8 GB'

del gaming_laptop.GPU
print(f"After deleting property of GPU from object gaming_laptop : {gaming_laptop.GPU}") #'Laptop' object has no attribute 'GPU'