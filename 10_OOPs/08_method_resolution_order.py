class A:
    label = "A : Tea available"

class B(A):
    label = "B : Ginger Tea is available"

class C(A):
    label = "C : Masala Tea is available"

class D(B, C):
    pass # this class does not have any property. It inherits the properties from class B, C, A. 

chai = D()
print(f"MRO of Object D : {D.mro()}")
print(chai.label)

# (MRO) in Python defines the sequence in which Python searches for methods and attributes in a class hierarchy,
# especially in scenarios involving multiple inheritance. 