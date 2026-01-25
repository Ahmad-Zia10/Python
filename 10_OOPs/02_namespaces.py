class Chai:
    origin = "India"


print(Chai.origin) # We can directly do this(instead of first creating an object) because in python class is also an object.
Chai.is_hot = True # We have added this property to the class Chai. Now every object of Chai will have this prop.

print(Chai.is_hot)

masala_chai = Chai()

print(f"Masala Chai : {masala_chai.is_hot}")
print(f"Masala Chai : {masala_chai.origin}")

masala_chai.type = "Masala"
print(f"Masala Chai object's attribute/variable 'type' has value : {masala_chai.type}")
# print("Class Chai does not have the property 'type' : ",Chai.type) #type object 'Chai' has no attribute 'type'