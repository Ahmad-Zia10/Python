class TeaLeaf:

    def __init__(self, age):
        self._age = age #In Python, there is no public or private - instead you name your private elements giving it a prefix of a single underscore (i.e. self._bar instead of self.bar),
    
    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <=age<= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2)
print(leaf._age) # we can access this private varaible but it is understood that we must not do so unless absolutely necessary
print(leaf.age) # calls the getter method
leaf.age = 4 # calls the setter method
print(leaf.age) # calls the getter method 
        
