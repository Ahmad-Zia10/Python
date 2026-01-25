class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai)) #<class 'type'>.This class is also an object, internally it is an object. In Python everything is an object.  

ginger_chai = Chai() #creating objects

print(type(ginger_chai))
print(type(ginger_chai) is Chai) #it checks whether this object is of class Chai
print(type(ginger_chai) is ChaiTime)