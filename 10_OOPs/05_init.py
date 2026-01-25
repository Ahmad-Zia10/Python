class ChaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size
    
    def summary(self):
        return f"{self.size} cup of {self.type}."

order_1 = ChaiOrder("Masala Chai", "Small")
print(order_1.summary())

order_2 = ChaiOrder("Ginger Chai", "Large")
print(order_2.summary())