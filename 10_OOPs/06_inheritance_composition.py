class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):

    def add_spices(self):
        print("Adding cardamom, ginger, cloves")

class ChaiShop:
    chai_cls = BaseChai #Just a reference to base class

    def __init__(self):
        self.chai = self.chai_cls("regular") # now I am creating an object of class BaseChai and storing its reference in 'chai'
        print(f"chai is : {self.chai}")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop.")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai # We are overriding the property derived from base class ChaiShop, now this property references to class MasalaChai
    #So it calls ChaiShop.__init__(fancy): This runs the line :
    #self.chai = self.chai_cls("Regular")
    #self is now fancy.
    # Lookup of self.chai_cls:
    # on instance fancy → none 
    # on class FancyChaiShop → finds chai_cls = MasalaChai(this overrides the one from ChaiShop)


shop = ChaiShop()
fancy = FancyChaiShop() # NOTE : FancyChaiShop does not define its own __init__, so it inherits __init__ from ChaiShop.
print(f"Calling serve on shop : {shop.serve()}")
print(f"Calling serve on fancy : {fancy.serve()}")
# fancy.chai_cls.add_spices() #MasalaChai.add_spices() missing 1 required positional argument: 'self'
# fancy.chai.add_spices()